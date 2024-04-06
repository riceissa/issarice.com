#!/usr/bin/env python3

import os
import subprocess
import sys
import datetime
import shlex
import shutil
import argparse
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
'''

def main():
    # TODO: I'm thinking now that this script shouldn't take any arguments. It
    # should be pretty obvious which files need to be regenerated, so just
    # regenerate those. So argparse stuff can all be deleted.

    os.makedirs("_site", exist_ok=True)

    content_changed = []
    for filename in os.listdir("wiki"):
        if filename.endswith(".md"):
            fileroot = filename[:-len(".md")]
            final_dest = "_site/" + slugify(fileroot)
            filepath = "wiki/" + filename
            if (not os.path.isfile(final_dest) or
                    os.path.getmtime(filepath) > os.path.getmtime(final_dest)):
                print(f"Processing {filepath}...", file=sys.stderr)
                content_changed.append(filepath)
        else:
            # Just copy the file if it's not markdown
            # TODO: right now we copy these every single time, but it should be
            # checked whether the destination timestamp is old/whether the file
            # exists, and only copy if needed.
            filepath = "wiki/" + filename
            dest = "_site/" + filename
            print(f"Copying {filepath} to {dest}...", file=sys.stderr)
            shutil.copyfile(filepath, dest)

    # These are the files that we need to regenerate, not because their content
    # changed, but because other files changed such that the backlinks section
    # now needs to be updated.
    backlinks_changed = []

    link_graph = {}
    if os.path.isfile("link-graph.json"):
        with open("link-graph.json", "r") as lg:
            link_graph = json.load(lg)
            for filepath in content_changed:
                outgoing = outgoing_wikilinks(filepath)
                fileroot = filename[:-len(".md")]
                # For each file that changed, compare the existing link graph
                # to the set of current links we've detected in the file. Any
                # differences (in either direction) mean that backlinks need to
                # be updated. Also, if the file doesn't even exist in the link
                # graph, then all the pages it links to must be updated.
                if fileroot in link_graph:
                    for linked_to_root in outgoing.symmetric_difference(set(link_graph[fileroot])):
                        backlinks_changed.append(linked_to_root)
                else:
                    for linked_to_root in outgoing:
                        backlinks_changed.append(linked_to_root)
                # Once we're done comparing against the old link graph, make
                # sure to update the link graph to the current links.
                link_graph[fileroot] = list(outgoing)
    else:
        for filepath in content_changed:
            outgoing = outgoing_wikilinks(filepath)
            for linked_to_root in outgoing:
                backlinks_changed.append(linked_to_root)
            link_graph[fileroot] = list(outgoing)

    with open("link-graph.json", "w") as lg:
        json.dump(link_graph, lg, indent=4)

    with open("backlinks.json", "w") as b:
        backlinks = construct_backlinks_graph(link_graph)
        json.dump(backlinks, b, indent=4)

    for fileroot in backlinks_changed:
        generate_backlink_fragment(fileroot)

    # Now that the backlinks graph has been regenerated, we can finally
    # generate the page HTMLs.
    for filepath in content_changed:
        process_filepath(filepath)
    for fileroot in backlinks_changed:
        filepath = fileroot + ".md"
        process_filepath(filepath)

def outgoing_wikilinks(filepath):
    try:
        p = subprocess.run([
            "pandoc", "-f", "markdown+smart-implicit_header_references+wikilinks_title_after_pipe",
            "-t", "native", "-o", "/dev/null", "--lua-filter", "generator/print_wikilinks.lua", filepath
        ], check=True, capture_output=True)
        output = p.stdout.decode("utf-8")
        return set(output.strip().split("\n"))
    except subprocess.CalledProcessError as e:
        print("Error running pandoc inside outgoing_wikilinks:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

def construct_backlinks_graph(link_graph):
    backlinks = {}
    for x in link_graph:
        for y in link_graph[x]:
            if y in backlinks:
                if x not in backlinks[y]:
                    backlinks[y].append(x)
            else:
                backlinks[y] = [x]
    return backlinks

def generate_backlink_fragment(fileroot, backlinks):
    os.makedirs("backlink_fragments", exist_ok=True)
    with open("backlink_fragments/" + fileroot + ".html", "w") as f:
        f.write("<h2>Backlinks</h2>\n")
        f.write("<ul>\n")
        for y in backlinks[fileroot]:
            f.write(f'<li><a href="{slugify(y)}">{y}</a></li>\n')
        f.write("</ul>\n")

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


def process_filepath(filepath):
    filename = filepath.split('/')[-1]
    fileroot = filename[:-len(".md")]
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

    try:
        p_last_mod = subprocess.run([
            "git", "log", "-1",
            '--format=%ad',  # TODO: i think i can just use %as or %cs
            '--date=format:%Y-%m-%d',
            "--", filepath
        ], check=True, capture_output=True)
        last_mod = p_last_mod.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        print("Error running git log command:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

    # print(subprocess.list2cmdline(p_last_mod.args))
    final_dest = "_site/" + slugify(fileroot)
    temp_dest = final_dest + ".tempmjpage.html"
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
            "-M", "sourcefilename:" + urllib.parse.quote(filepath),
            "-M", "lastmodified:" + last_mod,
        ]
        if os.path.isfile("backlink_fragments/" + fileroot + ".html"):
            pandoc_args.extend([
                "--include-after-body", "backlink_fragments/" + fileroot + ".html",
            ])
        pandoc_args.extend(["-o", temp_dest])
        pandoc_args.extend([filepath])
        p3 = subprocess.run(pandoc_args, check=True)
        # print(subprocess.list2cmdline(p3.args))
    except subprocess.CalledProcessError as e:
        print("Error running pandoc (json to html5):",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

    possibly_has_math = False
    with open(temp_dest, "r") as f:
        for line in f:
            if "\\(" in line or "\\[" in line:
                possibly_has_math = True
    if possibly_has_math:
        print("This page may contain math, so running mjpage...", file=sys.stderr, end='')
        try:
            with open(temp_dest, "r") as f1, open(final_dest, "w") as f2:
                p_mjpage = subprocess.run([
                    "mjpage", "--output", "CommonHTML"
                ], stdin=f1, stdout=f2, check=True)
            print('done.', file=sys.stderr)
            os.remove(temp_dest)
        except subprocess.CalledProcessError as e:
            print("Error running mjpage:",
                  "error code:", e.returncode,
                  "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
            sys.exit()
    else:
        print("No math so just renaming page.", file=sys.stderr)
        os.rename(temp_dest, final_dest)

if __name__ == "__main__":
    main()
