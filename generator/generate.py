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

class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def filename(self):
        return self.filepath.split("/")[-1]

    def fileroot(self):
        return ".".join(self.filename().split(".")[:-1])

    def is_markdown(self):
        return self.filepath.endswith(".md")

    def destination(self):
        if self.filepath.startswith("wiki/"):
            if self.is_markdown():
                return File("_site/" + slugify(self.fileroot()))
            else:
                return File("_site/" + self.filename())
        else:
            raise ValueError(f"This file ({self.filepath}) is not in the wiki/ directory, so it doesn't have a destination!")

    def __repr__(self):
        return f"File(filepath={self.filepath})"

    def __hash__(self):
        return hash(self.filepath)

    def __eq__(self, other):
        return self.filepath == other.filepath

def main():
    os.makedirs("_site", exist_ok=True)

    # First, we scan the wiki/ directory to look for new files and files that
    # have changed. If it's a markdown file, we keep track of it in
    # content_changed in order to process later. If it's any other file, we
    # just need to copy it to its destination.
    content_changed = []
    for filename in os.listdir("wiki"):
        file = File("wiki/" + filename)
        destination = file.destination()
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
    backlinks_changed = []

    link_graph = {}
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

def outgoing_wikilinks(file):
    try:
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

def construct_backlinks_graph(link_graph):
    # TODO: might need to think about capitalization (esp of first letter of page)
    backlinks = {}
    for x in link_graph:
        for y in link_graph[x]:
            if y in backlinks:
                if x not in backlinks[y]:
                    backlinks[y].append(x)
            else:
                backlinks[y] = [x]
    return backlinks

def generate_backlink_fragment(file, backlinks):
    os.makedirs("backlink_fragments", exist_ok=True)
    with open("backlink_fragments/" + file.fileroot() + ".html", "w") as f:
        f.write("<h2>Backlinks</h2>\n")
        f.write("<ul>\n")
        for y in backlinks[file]:
            f.write(f'<li><a href="{slugify(y.filename())}">{y.filename()}</a></li>\n')
        f.write("</ul>\n")

def write_link_graph(link_graph, write_to_file):
    # A link_graph is a dict from File to [File].
    d = {}
    for key in link_graph:
        d[key.filepath] = [x.filepath for x in link_graph[key]]
    with open(write_to_file.filepath, "w") as f:
        print(f"Saving new link graph to {write_to_file.filepath}...", end="", file=sys.stderr)
        json.dump(d, f, indent=4)
        print("done.", file=sys.stderr)

def load_link_graph(read_from_file):
    link_graph = {}
    with open (read_from_file.filepath, "r") as f:
        d = json.load(f)
        for key in d:
            link_graph[File(key)] = [File(x) for x in d[key]]
        return link_graph

def slugify(s):
    '''
    "Slugify" the string s as follows: keep only the characters that are
    alphabetic or numerical, and group them together; all other characters are
    replaced by "-" and squeezed together.
    '''
    s = s.lower()
    s = "".join(c if (c.isalpha() or c.isdigit()) else "-" for c in s)
    s = "-".join(filter(bool, s.split("-")))
    return s


def process_filepath(file):
    # TODO: probably switch to using --filter instead of pipes.
    # actually, maybe this isn't possible since --filter
    # doesn't seem to allow sending flags/arguments to the
    # executable (it just tries to run the whole string as
    # the executable).
    # -implicit_header_references is necessary when using wikilinks: if the
    # about page has a section called "Contact" as well as a wiklink
    # [[contact]], then the Pandoc Markdown reader will interpret that as a
    # link to the contact section, and you will end up with
    # "[[contact](#contact)]" instead of "[contact](contact)".
    # try:
    #     p = subprocess.run([
    #         "pandoc", "-f", "markdown+smart-implicit_header_references",
    #         "-t", "json", filepath
    #     ], check=True, capture_output=True)
    # except subprocess.CalledProcessError as e:
    #     print("Error running pandoc (markdown to json):",
    #           "error code:", e.returncode,
    #           "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
    #     sys.exit()

    # try:
    #     # https://github.com/riceissa/pandoc-wikilinks-filter/blob/main/wikilinks.py
    #     p2 = subprocess.run(["wikilinks.py"],
    #                         input=p.stdout, check=True,
    #                         capture_output=True)
    # except subprocess.CalledProcessError as e:
    #     print("Error running wikilinks.py:",
    #           "error code:", e.returncode,
    #           "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
    #     sys.exit()

    if not os.path.isfile(file.filepath):
        print(f"The file {file.filepath} does not exit; skipping.")
        return None

    try:
        p_last_mod = subprocess.run([
            "git", "log", "-1",
            '--format=%ad',  # TODO: i think i can just use %as or %cs
            '--date=format:%Y-%m-%d',
            "--", file.filepath
        ], check=True, capture_output=True)
        last_mod = p_last_mod.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        print("Error running git log command:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

    # print(subprocess.list2cmdline(p_last_mod.args))
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
        print("This page may contain math, so running mjpage...", file=sys.stderr, end='')
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
        print("No math so just renaming page.", file=sys.stderr)
        os.rename(temp_dest.filepath, final_dest.filepath)

if __name__ == "__main__":
    main()
