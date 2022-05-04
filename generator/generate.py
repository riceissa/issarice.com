#!/usr/bin/env python3

import os
import subprocess
import sys
import datetime
import shlex
import argparse

'''
Obsidian wikilinks require filenames to be named exactly as it appears
in the wikilink, which means I have to deal with filenames containing
spaces. Unfortunately, GNU Make does not work with filenames that
contain spaces, so I can no longer use Make to do the site generation.
'''

# eventually, add argparse so that i can compile a single markdown file at a time

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

os.makedirs("_site", exist_ok=True)

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
    try:
        p = subprocess.run([
            "pandoc", "-f", "markdown+smart-implicit_header_references",
            "-t", "json", filepath
        ], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Error running pandoc (markdown to json):",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

    try:
        # https://github.com/riceissa/pandoc-wikilinks-filter/blob/main/wikilinks.py
        p2 = subprocess.run(["wikilinks.py"],
                            input=p.stdout, check=True,
                            capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Error running wikilinks.py:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

    try:
        p_last_mod = subprocess.run([
            "git", "log", "-1",
            '--format=%ad',
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
        p3 = subprocess.run([
            "pandoc", "-f", "json", "-t", "html5",
            "--shift-heading-level-by", "1",
            "--template", "templates/default.html5",
            "-M", "toc-title:Contents",
            "-M", "today:" + datetime.date.today().strftime("%Y-%m-%d"),
            "-M", "lang:en",
            "--toc", "--toc-depth", "4",
            "--mathjax",
            "--lua-filter", "generator/url_filter.lua",
            "-M", "sourcefilename:" + shlex.quote(filepath),
            "-M", "lastmodified:" + last_mod,
            "-o", temp_dest
        ], input=p2.stdout, check=True)
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

parser = argparse.ArgumentParser()
parser.add_argument("filepaths", nargs="*")
args = parser.parse_args()

if args.filepaths:
    for filepath in args.filepaths:
        print("Processing", filepath, file=sys.stderr)
        process_filepath(filepath)
else:
    for filename in os.listdir("wiki"):
        if filename.endswith(".md") and filename.startswith("betting"):
            filepath = "wiki/" + filename
            print("Processing", filepath, file=sys.stderr)
            process_filepath(filepath)
