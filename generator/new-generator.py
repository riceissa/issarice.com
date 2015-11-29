#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob
import argparse
import yaml
from yaml import SafeLoader, BaseLoader
import os
import datetime

import templates

def main():
    parser = argparse.ArgumentParser(
            description="Generate Atom and RSS feeds, sitemap, " +
            "and page index for a static site")
    parser.add_argument("--source", "-s", metavar="FILE", nargs="+",
            help="source files")
    parser.add_argument("--destination", "--dest", "-d", default="./",
            help="destination directory")
    parser.add_argument("--atom", "-A", default="",
            help="destination of Atom feed relative to destination directory")
    parser.add_argument("--rss", "-R", default="",
            help="destination of RSS feed relative to destination directory")
    parser.add_argument("--sitemap", "-S", default="",
            help="destination of sitemap relative to destination directory")
    parser.add_argument("--index", "-I", default="",
            help=("destination of index of pages relative " +
            "to destination directory"))
    args = parser.parse_args()
    print(args.source)

    pages = [Page(i) for i in args.source]
    dest = args.destination
    dest += "/" if not dest[-1] == "/" else ""
    process_pages(pages, atom=dest+args.atom, rss=dest+args.rss,
            sitemap=dest+args.sitemap, index=dest+args.index)

class Page(object):
    """
    Store page metadata.
    """
    def __init__(self, origin, metadata={}):
        self.origin = origin
        with open(origin, "r") as f:
            s = ""
            line = f.readline()
            if line == '---\n':
                line = f.readline()
                while line not in ['---\n', '...\n', '']:
                    s += line
                    line = f.readline()
        self.metadata = yaml.load(s, Loader=BaseLoader)
        self.metadata.update(metadata)

    def slug(self):
        return os.path.splitext(self.origin.split("/")[-1])[0]

def process_pages(pages, atom=False, rss=False, sitemap=False, index=False):
    if atom:
        for p in pages:
            date = p.metadata["date"]
            title = p.metadata["title"] + " ({} update)".format(date)
            dt = datetime.strptime(p.metadata["date"], "%Y-%m-%d").strftime("%Y-%m-%dT%H:%M:%SZ")
            inner_list = templates.atom_list.format(title=title, date=date,
                    dt=dt)
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        s = templates.atom_template.format(now=now, inner_list=inner_list)
    if rss:
        for p in pages:
            pass
    if sitemap:
        s = ('<?xml version="1.0" encoding="UTF-8"?>\n' +
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in pages:
            s += "<url>\n"
            s += "  <loc>http://issarice.com/{}</loc>\n".format(p.slug())
            s += "  <changefreq>weekly</changefreq>\n"
            s += "</url>\n"
        s += "</urlset>\n"
        with open(sitemap, "w") as f:
            f.write(s)
    if index:
        for p in pages:
            pass

def slug(s):
    """
    Return the slug value of a string.
    """
    result = ""
    prev_hyph = True
    for c in s.lower():
        if c.isalpha() or c.isdigit():
                result += c
                prev_hyph = False
        else:
            if not prev_hyph:
                result += "-"
            prev_hyph = True
    if result and result[-1] == "-":
        result = result[:-1]
    return result

if __name__ == "__main__":
    main()
