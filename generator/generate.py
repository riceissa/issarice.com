#!/usr/bin/env python3

import os
import subprocess
import sys

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
    if filename.endswith(".md") and filename.startswith("Q"):
        print("Processing", filename, file=sys.stderr)
        fileroot = filename[:-len(".md")]
        p = subprocess.run(["pandoc", "-f", "markdown+smart", "-t", "json", "wiki/" + filename], check=True, capture_output=True)
        p2 = subprocess.run(["/home/issa/projects/pandoc-wikilinks-filter/wikilinks.py", "--base-url", "https://issarice.com/"], input=p.stdout, check=True, capture_output=True)
        p3 = subprocess.run(["pandoc", "-f", "json", "-t", "html", "-o", "_site/" + slugify(fileroot)], input=p2.stdout)
