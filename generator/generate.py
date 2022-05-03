#!/usr/bin/env python3

import os
import subprocess
import sys

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

for filename in os.listdir("wiki"):
    if filename.endswith(".md") and filename.startswith("about"):
        print("Processing", filename, file=sys.stderr)
        fileroot = filename[:-len(".md")]
        # TODO: probably switch to using --filter instead of pipes.
        # actually, maybe this isn't possible since --filter
        # doesn't seem to allow sending flags/arguments to the
        # executable (it just tries to run the whole string as
        # the executable).
        p = subprocess.run(["pandoc", "-f", "markdown+smart", "-t", "json", "wiki/" + filename], check=True, capture_output=True)
        p2 = subprocess.run(["/home/issa/projects/pandoc-wikilinks-filter/wikilinks.py", "--base-url", "https://issarice.com/"], input=p.stdout, check=True, capture_output=True)
        p3 = subprocess.run(["pandoc", "-f", "json", "-t", "html", "-o", "_site/" + slugify(fileroot)], input=p2.stdout)
