#!/usr/bin/python

import argparse
from pandocfilters import toJSONFilter, Str, Link, walk, stringify
import commands as c
import json
from classes import *


parser = argparse.ArgumentParser(description='Relativize absolute URLs.')
parser.add_argument(
    "origin",
    nargs = 1,
    help = 'file in the site directory from which to link'
)
args = parser.parse_args()

link_from = Filepath(args.origin[0])

def relativize_urls_filter(key, value, format, meta):
    if key == 'Link':
        # Here value[0] is the text that appears for the link, but it is
        # a list of thing wrapped around Str, so to get the actual
        # string one must do stringify(value[0]), then put it back in a
        # Str and then back in a list; value[1] is the link URL, which
        # is a list with two elements: the first element is the string
        # of the URL, and the second is the mouse-over text.
        if value[1][0].startswith("/"):
            fp = Filepath(value[1][0][1:]) # remove "/"
            actual_link = fp.relative_to(link_from).path
            if not actual_link.startswith("../"):
                actual_link = "./" + actual_link
            return Link(value[0], [actual_link, value[1][1]])

def relativize_urls(json_lst, link_from):
    return walk(json_lst, relativize_urls_filter, "", "")

if __name__ == "__main__":
    toJSONFilter(relativize_urls_filter)
    #lst = json.loads(c.run_command("pandoc -f markdown -t json pages/index.md"))
    #print lst
    #print json.dumps(walk(lst, relativize_urls, "", ""), separators=(',',': '), indent=2)
