#!/usr/bin/env python3

import os
import subprocess
import sys
import datetime
import shlex
import shutil
import shutil
import json
import urllib.parse
from __future__ import annotations

'''
I didn't want to write my own static site generator, but... Obsidian wikilinks
require files to be named exactly as they appear in the wikilink (minus the .md
extension), which means I have to deal with filenames containing spaces (and
potentially other special characters like apostrophe). Unfortunately, GNU Make
does not work with filenames that contain spaces, so I can no longer use Make
to do the site generation.

This script takes no arguments because the idea is that it should be smart
enough to figure out which files need to be regenerated, and just do the right
thing.
'''

ALL_PAGES_BEFORE = """---
title: All pages
created: 2017-11-11
bigtable: true
---

This is a list of all pages on this site ordered by the "last substantive
revision" date. The "last modified" date comes from version control
([Git](git)) and takes into account even insubstantial edits.

# Table

|Title|Last substantive revision|Last modified|Created|Belief|Completion status|
|------------------------------------------------|--------------|--------------|--------------|--------------|--------------|
"""

ALL_PAGES_AFTER = """
# See also

- [Gwern.net metadata table](gwern-net-metadata-table)
"""

class File:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def filename(self) -> str:
        return self.filepath.split("/")[-1]

    def fileroot(self) -> str:
        return ".".join(self.filename().split(".")[:-1])

    def is_markdown(self) -> bool:
        return self.filepath.endswith(".md")

    def destination(self) -> File:
        if self.filepath.startswith("wiki/"):
            if self.is_markdown():
                return File("_site/" + slugify(self.fileroot()))
            else:
                return File("_site/" + self.filename())
        else:
            raise ValueError(f"This file ({self.filepath}) is not in the wiki/ directory, so it doesn't have a destination!")

    def __repr__(self) -> str:
        return f"File(filepath={self.filepath})"

    def __hash__(self) -> int:
        return hash(self.filepath)

    def __eq__(self, other) -> bool:
        return self.filepath == other.filepath

def main() -> None:
    os.makedirs("_site", exist_ok=True)

    # First, we scan the wiki/ directory to look for new files and files that
    # have changed. If it's a markdown file, we keep track of it in
    # content_changed in order to process later. If it's any other file, we
    # just need to copy it to its destination.
    content_changed: list[File] = []
    filename: str
    for filename in os.listdir("wiki"):
        file: File = File("wiki/" + filename)
        destination: File = file.destination()
        if (not os.path.isfile(destination.filepath) or
                os.path.getmtime(file.filepath) > os.path.getmtime(destination.filepath)):
            if file.is_markdown():
                print(f"Processing {file.filepath}...", file=sys.stderr)
                content_changed.append(file)
            else:
                # Just copy the file if it's not markdown.
                print(f"Copying {file.filepath} to {destination.filepath}...", file=sys.stderr)
                shutil.copyfile(file.filepath, destination.filepath)

    # Besides the markdown files whose content changed, we also need to
    # regenerate markdown files whose backlinks have changed. In other words,
    # these are the files for which other files changed such that the backlinks
    # section now needs to be updated.
    backlinks_changed: list[File] = []

    link_graph: dict[File, list[File]] = {}
    link_graph_has_changed = False
    if os.path.isfile("link-graph.json"):
        link_graph = load_link_graph(File("link-graph.json"))
    for file in content_changed:
        print(f"Updating links for {file.filepath}...", end="", file=sys.stderr)
        outgoing = outgoing_wikilinks(file)

        # For each file that changed, compare the existing link graph
        # to the set of current links we've detected in the file. Any
        # differences (in either direction) mean that backlinks need to
        # be updated. Also, if the file doesn't even exist in the link
        # graph, then all the pages it links to must be updated.
        if file in link_graph:
            for linked_to in outgoing.symmetric_difference(set(link_graph[file])):
                backlinks_changed.append(linked_to)
        else:
            for linked_to in outgoing:
                backlinks_changed.append(linked_to)

        # Once we're done comparing against the old link graph, make
        # sure to update the link graph to the current links.
        assert all(x.filepath != "wiki/.md" for x in outgoing), f"DEBUG: {outgoing}"
        link_graph[file] = list(outgoing)
        link_graph_has_changed = True
        print("done.", file=sys.stderr)

    if link_graph_has_changed:
        print("Saving new link graph...", end="", file=sys.stderr)
        write_link_graph(link_graph, File("link-graph.json"))
        print("done.", file=sys.stderr)

        backlinks = construct_backlinks_graph(link_graph)
        print("Saving new backlinks graph...", end="", file=sys.stderr)
        write_link_graph(backlinks, File("backlinks.json"))
        print("done.", file=sys.stderr)

        for file in backlinks_changed:
            print(f"Generating new backlink fragment for {file.filepath}...", end="", file=sys.stderr)
            generate_backlink_fragment(file, backlinks)
            print("done.", file=sys.stderr)

    # Now that the backlinks graph has been regenerated, we can finally
    # generate the page HTMLs.
    for file in content_changed:
        process_filepath(file)
    for file in backlinks_changed:
        process_filepath(file)

    if not content_changed:
        print("Nothing to do because no files have changed.", file=sys.stderr)

    # TODO: old comment from the old shell script, generator/all_pages_table.sh.
    # All the "git log" commands for each file are the bottleneck of computation,
    # so that is the process we want to parallelize with GNU parallel.
    # UPDATE: actually it looks like the slow part is reading each file and reading
    # the metadata off of it.

    # Now we update all-pages.json to reflect the lastest metadata of the
    # pages, and then regenerate that page.
    if content_changed:
        print("Generating new all-pages file...", end="", file=sys.stderr)
        all_pages = {}
        if os.path.isfile("all-pages.json"):
            all_pages = load_all_pages(File("all-pages.json"))
        for file in content_changed:
            metadata = read_metadata(file)
            all_pages[file] = metadata
        write_all_pages(all_pages, File("all-pages.json"))
        generate_all_pages_page(all_pages)
        print("done.", file=sys.stderr)

def read_metadata(file: File) -> dict[str, str]:
    # TODO: this is a hack
    # All the .startswith() calls make me uncomfortable since they depend on
    # certain bytes being in the right place (although my source files currently
    # adhere to this restriction).  However, I still prefer this to the old
    # solution of bringing in dependencies like PyYaml, parsing the whole header,
    # and then generating date-dependent pages using that.
    result: dict[str, str] = {}
    print(f"Opening {file.filepath} to read metadata...", file=sys.stderr)
    with open(file.filepath, "r") as f:
        first_line: str = next(f).strip()
        if first_line != "---":
            return result
        for line in f:
            if line.strip() == "---" or line.strip() == "...":
                break
            # print(f"Seeing line: {line}", file=sys.stderr)
            if line.startswith("title: "):
                title_part = line[len("title: "):].strip()
                # TODO: some titles have quotes surrounding them because YAML
                # requires escaping. Maybe it really just need a library to parse
                # YAML...
                if title_part[0] == '"' or title_part[0] == '"':
                    title_part = title_part[1:-1]
                result["title"] = title_part
            if line.startswith("author: "):
                result["author"] = line[len("author: "):].strip()
            if line.startswith("created: "):
                result["created"] = line[len("created: "):].strip()
            if line.startswith("date: "):
                result["date"] = line[len("date: "):].strip()
            if line.startswith("belief: "):
                result["belief"] = line[len("belief: "):].strip()
            if line.startswith("status: "):
                result["status"] = line[len("status: "):].strip()
    return result

def load_all_pages(read_from_file: File) -> dict[File, dict[str, str]]:
    all_pages: dict[File, dict[str, str]] = {}
    with open(read_from_file.filepath, "r") as f:
        d: dict[str, dict[str, str]] = json.load(f)
        for key in d:
            all_pages[File(key)] = d[key]
    return all_pages

def write_all_pages(all_pages: dict[File, dict[str, str]], write_to_file: File) -> None:
    d: dict[str, dict[str, str]] = {}
    for key in all_pages:
        d[key.filepath] = all_pages[key]
    with open(write_to_file.filepath, "w") as f:
        json.dump(d, f, indent=4)

def generate_all_pages_page(all_pages: dict[File, dict[str, str]]) -> None:
    pages = sorted(all_pages.keys(), key=lambda x: all_pages[x].get("date", "2000-01-01"), reverse=True)
    source = ALL_PAGES_BEFORE
    for page in pages:
        title = all_pages[page].get('title')
        url = slugify(page.fileroot())
        last_substantive_revision = all_pages[page].get('date') or ""
        last_modified = last_modified_in_git(page)
        created = all_pages[page].get('created') or ""
        belief = all_pages[page].get('belief') or ""
        status = all_pages[page].get('status') or ""
        source += f"[{title}]({url})|{last_substantive_revision}|{last_modified}|{created}|{belief}|{status}|\n"
        # f.write(str(all_pages[page]) + "\n")
    source += ALL_PAGES_AFTER

    try:
        p = subprocess.run([
            "pandoc", "-f", "markdown+smart", "-t", "html",
            "--shift-heading-level-by", "1",
            "--template", "templates/default.html5",
            "--toc", "-M", "toc-title:Contents",
            "-M", "today:" + datetime.date.today().strftime("%Y-%m-%d"),
            "-M", "lang:en", "-o", "_site/all-pages"
        ], input=source.encode('utf-8'), check=True)
    except subprocess.CalledProcessError as e:
        print("Error while trying to find last modification date inside last_modified_in_git:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()


def last_modified_in_git(file: File) -> str:
    try:
        p = subprocess.run([
            "git", "log", "-1", "--format=%as", file.filepath
        ], check=True, capture_output=True)
        output = p.stdout.decode("utf-8").strip()
        return output
    except subprocess.CalledProcessError as e:
        print("Error while trying to find last modification date inside last_modified_in_git:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()


def outgoing_wikilinks(file: File) -> set[File]:
    try:
        # -implicit_header_references is necessary when using wikilinks: if the
        # about page has a section called "Contact" as well as a wiklink
        # [[contact]], then the Pandoc Markdown reader will interpret that as a
        # link to the contact section, and you will end up with
        # "[[contact](#contact)]" instead of "[contact](contact)".
        p = subprocess.run([
            "pandoc", "-f", "markdown+smart-implicit_header_references+wikilinks_title_after_pipe",
            "-t", "native", "-o", "/dev/null", "--lua-filter", "generator/print_wikilinks.lua", file.filepath
        ], check=True, capture_output=True)
        output = p.stdout.decode("utf-8").strip()
        if not output:
            return set()
        links = output.split("\n")
        return set([File("wiki/" + x + ".md") for x in links])
    except subprocess.CalledProcessError as e:
        print("Error running pandoc inside outgoing_wikilinks:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

def construct_backlinks_graph(link_graph: dict[File, list[File]]) -> dict[File, list[File]]:
    # TODO: might need to think about capitalization (esp of first letter of page)
    backlinks: dict[File, list[File]] = {}
    x : File
    for x in link_graph:
        y: File
        for y in link_graph[x]:
            if y in backlinks:
                if x not in backlinks[y]:
                    backlinks[y].append(x)
            else:
                backlinks[y] = [x]
    return backlinks

def generate_backlink_fragment(file: File, backlinks: dict[File, list[File]]) -> None:
    os.makedirs("backlink_fragments", exist_ok=True)
    with open("backlink_fragments/" + file.fileroot() + ".html", "w") as f:
        f.write("<h2>Backlinks</h2>\n")
        f.write("<ul>\n")
        for y in backlinks[file]:
            f.write(f'<li><a href="{slugify(y.filename())}">{y.filename()}</a></li>\n')
        f.write("</ul>\n")

def write_link_graph(link_graph: dict[File, list[File]], write_to_file: File) -> None:
    d = {}
    for key in link_graph:
        d[key.filepath] = [x.filepath for x in link_graph[key]]
    with open(write_to_file.filepath, "w") as f:
        print(f"Saving new link graph to {write_to_file.filepath}...", end="", file=sys.stderr)
        json.dump(d, f, indent=4)
        print("done.", file=sys.stderr)

def load_link_graph(read_from_file: File) -> dict[File, list[File]]:
    link_graph: dict[File, list[File]] = {}
    with open (read_from_file.filepath, "r") as f:
        d = json.load(f)
        for key in d:
            link_graph[File(key)] = [File(x) for x in d[key]]
        return link_graph

def slugify(s: str) -> str:
    '''
    "Slugify" the string s as follows: keep only the characters that are
    alphabetic or numerical, and group them together; all other characters are
    replaced by "-" and squeezed together.
    '''
    s = s.lower()
    s = "".join(c if (c.isalpha() or c.isdigit()) else "-" for c in s)
    s = "-".join(filter(bool, s.split("-")))
    return s


def process_filepath(file: File) -> None:

    if not os.path.isfile(file.filepath):
        print(f"The file {file.filepath} does not exist; skipping.")
        return None

    last_mod = last_modified_in_git(file)

    final_dest = File("_site/" + slugify(file.fileroot()))
    temp_dest = File(final_dest.filepath + ".tempmjpage.html")
    try:
        pandoc_args = [
            "pandoc", "-f", "markdown+smart+wikilinks_title_after_pipe-implicit_header_references", "-t", "html5",
            "--shift-heading-level-by", "1",
            "--template", "templates/default.html5",
            "-M", "toc-title:Contents",
            "-M", "today:" + datetime.date.today().strftime("%Y-%m-%d"),
            "-M", "lang:en",
            "--toc", "--toc-depth", "4",
            "--mathjax",
            "--lua-filter", "generator/url_filter.lua",
            "--lua-filter", "generator/blockquote_sig.lua",
            # TODO: make sure this gives correct filepath
            # "-M", "sourcefilename:" + shlex.quote(filepath),
            "-M", "sourcefilename:" + urllib.parse.quote(file.filepath),
            "-M", "lastmodified:" + last_mod,
        ]
        if os.path.isfile("backlink_fragments/" + file.fileroot() + ".html"):
            pandoc_args.extend([
                "--include-after-body", "backlink_fragments/" + file.fileroot() + ".html",
            ])
        pandoc_args.extend(["-o", temp_dest.filepath])
        pandoc_args.extend([file.filepath])
        p3 = subprocess.run(pandoc_args, check=True)
        # print(subprocess.list2cmdline(p3.args))
    except subprocess.CalledProcessError as e:
        print("Error running pandoc (json to html5):",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

    possibly_has_math = False
    with open(temp_dest.filepath, "r") as f:
        for line in f:
            if "\\(" in line or "\\[" in line:
                possibly_has_math = True
    if possibly_has_math:
        print(f"This page ({file.filepath}) may contain math, so running mjpage...", file=sys.stderr, end='')
        try:
            with open(temp_dest.filepath, "r") as f1, open(final_dest.filepath, "w") as f2:
                p_mjpage = subprocess.run([
                    "mjpage", "--output", "CommonHTML"
                ], stdin=f1, stdout=f2, check=True)
            print('done.', file=sys.stderr)
            os.remove(temp_dest.filepath)
        except subprocess.CalledProcessError as e:
            print("Error running mjpage:",
                  "error code:", e.returncode,
                  "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
            sys.exit()
    else:
        print(f"No math in {file.filepath} so just renaming page.", file=sys.stderr)
        os.rename(temp_dest.filepath, final_dest.filepath)

if __name__ == "__main__":
    main()
