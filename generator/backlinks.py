#!/usr/bin/env python3

import subprocess
import os
import shutil
import json
import sys

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

print("Generating link graph...", file=sys.stderr)
# if os.path.isfile("link-graph.json"):
#     os.remove("link-graph.json")
with open("link-graph.json", "w") as lg:
    lg.write("{\n")
directory = os.listdir("wiki")
for i, filename in enumerate(directory):
    if filename.endswith(".md"):
        fileroot = filename[:-len(".md")]
        # final_dest = "_site/" + slugify(fileroot)
        filepath = "wiki/" + filename
        print("Processing", filepath, "for link graph...", file=sys.stderr)
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
            postfix = "" if i == len(directory) - 1 else ","
            p2 = subprocess.run(["wikilinks.py", "--save-links"],
                                input=p.stdout, check=True,
                                capture_output=True)
            with open("link-graph.json", "a") as lg:
                escaped_fileroot = fileroot.replace('"', '\\"')
                lg.write(f'    "{escaped_fileroot}": {p2.stdout.decode("utf-8").strip()}{postfix}\n')
        except subprocess.CalledProcessError as e:
            print("Error running wikilinks.py:",
                  "error code:", e.returncode,
                  "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
            sys.exit()
with open("link-graph.json", "a") as lg:
    lg.write("}\n")

# TODO: might need to think about capitalization (esp of first letter of page)
with open("link-graph.json", "r") as lg, open("backlinks.json", "w") as b:
    link_graph = json.load(lg)
    backlinks = {}
    for x in link_graph:
        for y in link_graph[x]:
            if y in backlinks:
                if x not in backlinks[y]:
                    backlinks[y].append(x)
            else:
                backlinks[y] = []
    json.dump(backlinks, b, indent=4)

shutil.rmtree("backlink_fragments")
os.makedirs("backlink_fragments", exist_ok=True)
for x in backlinks:
    with open("backlink_fragments/" + x + ".html", "w") as f:
        f.write("<h2>Backlinks</h2>\n")
        f.write("<ul>\n")
        for y in backlinks[x]:
            f.write(f'<li><a href="{slugify(y)}">{y}</a></li>\n')
        f.write("</ul>\n")

