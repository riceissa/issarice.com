#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2014, Issa Rice
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import glob
import json
from jinja2 import Template, Environment, FileSystemLoader
import os
from datetime import datetime
import hashlib
import shutil
import time

from classes import *
from tag_ontology import *
from config import *

def clean():
    print("Removing {d}".format(d=SITE_DIRECTORY), file=sys.stderr)
    run_command("rm -rf {d}".format(d=SITE_DIRECTORY))

def compile_scss(stylesheet_basename):
    if not os.path.exists(SITE_DIRECTORY + SITE_CSS_DIRECTORY):
        os.makedirs(SITE_DIRECTORY + SITE_CSS_DIRECTORY)
    command = "sass --style compressed " + PRE_CSS_DIRECTORY +\
        stylesheet_basename + ".scss"
    compiled = run_command(command)
    with open(SITE_DIRECTORY + SITE_CSS_DIRECTORY + stylesheet_basename +
        ".css", "w", encoding="utf-8") as f:
        f.write(compiled)

def copy_files(pattern, destination):
    '''
    Copy files matching a pattern to a destination directory.
    '''
    if not os.path.exists(destination):
        os.makedirs(destination)
    for f in glob.iglob(pattern):
        if os.path.isfile(f):
            print("Copying {f} to {to}".format(f=f, to=destination), file=sys.stderr)
            shutil.copy2(f, destination)

def build_data(list_filepath):
    '''
    Take a list of Filepaths and return a tuple of two lists: the first
    is a list of all pages corresponding to the filepaths, and the
    second is a list of all tags that are in those pages.
    '''
    list_page = []
    list_tag = []
    for filepath in list_filepath:
        page = Page(filepath)
        page.load_metadata()
        # just ignore Japanese pages ... for now
        if page.metadata['language'].lower() not in ["ja", "japanese",
            "にほんご", "日本語"]:
            list_page.append(page)
            list_tag.extend(page.metadata["tags"])
    list_tag = list(set(list_tag))
    return (list_page, list_tag)

def create_pages(list_page):
    '''
    Take a list of pages and yield new pages with the compiled data.
    '''
    for page in list_page:
        print("Processing " + str(page.origin), file=sys.stderr)
        write_to = page.origin.route_with(my_route).path
        final = page.compiled(tags_dir=SITE_TAGS_DIRECTORY, commit_ps=args.commit_ps)
        yield Page(data=final, destination=write_to)

def create_single_page(filepath):
    '''
    For use when one only wants to partially compile.
    '''
    page = Page(origin=filepath)
    print("Processing " + str(page.origin), file=sys.stderr)
    page.destination = page.origin.route_with(my_route).path
    page.load_metadata()
    page.data = page.compiled(tags_dir=SITE_TAGS_DIRECTORY, commit_ps=args.commit_ps)
    return page

def create_tag_pages(list_page, list_tag):
    for tag in list_tag:
        print("Processing tag page for " + tag, file=sys.stderr)
        pages = []
        for page in list_page:
            if tag in page.metadata["tags"]:
                pages.append({
                    'title': page.metadata['title'],
                    'url': "../" + page.base(),
                })
        pages = sorted(pages, key=lambda t: t['title'].lower())
        write_to = Filepath(SITE_DIRECTORY + SITE_TAGS_DIRECTORY +
            slug(tag)).path
        metadata = {
            "title": "Tag: " + tag,
            "license": "CC0",
        }
        env = Environment(loader=FileSystemLoader('.'))
        page_list = env.get_template('templates/page-list.html')
        body = page_list.render(pages=pages)
        skeleton = env.get_template('templates/skeleton.html')
        final = skeleton.render(body=body, page=metadata, path="../")
        page = Page(metadata=metadata, data=final, destination=write_to)
        yield page

def create_page_with_all_tags(list_tag):
    '''
    Take a list of tags and return a page that lists all the tags.
    '''
    print("Creating page with all the tags", file=sys.stderr)
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    pages = [{'title': tag, 'url': slug(tag)} for tag in list_tag]
    pages = sorted(pages, key=lambda t: t['title'].lower())
    body = page_list.render(pages=pages)
    skeleton = env.get_template('templates/skeleton.html')
    metadata = {
        "title": "All tags",
        "license": "CC0",
    }
    final = skeleton.render(page=metadata, body=body, path="../")
    return Page(data=final,
        destination=SITE_DIRECTORY + SITE_TAGS_DIRECTORY + "index")

# Make page with all pages
def create_page_with_all_pages(list_page):
    print("Creating page with all the pages", file=sys.stderr)
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    pages = [
        {
            'title': page.metadata['title'],
            'url': page.base(),
        } for page in list_page
    ]
    pages = sorted(pages, key=lambda t: t['title'])
    body = page_list.render(pages=pages)
    skeleton = env.get_template('templates/skeleton.html')
    metadata = {
        "title": "All pages on the site",
        "license": "CC0",
    }
    final = skeleton.render(page=metadata, body=body, path="./")
    return Page(data=final, destination=SITE_DIRECTORY + "_all")

def create_sitemap(list_page=[], list_tag=[]):
    '''
    Take a list of pages and a list of tags.  Return a page object for
    the sitemap.
    '''
    print("Generating sitemap", file=sys.stderr)
    env = Environment(loader=FileSystemLoader('.'))
    sitemap_list = env.get_template('templates/sitemap-list.xml')
    list_page = sorted(list_page, key=lambda t: t.metadata['title'])
    body = ""
    for page in list_page:
        body += sitemap_list.render(slug=page.base())
    for t in list_tag:
        body += sitemap_list.render(slug="_tags/" + slug(t))
    sitemap = env.get_template('templates/sitemap.xml')
    final = sitemap.render(body=body)
    return Page(data=final, destination=SITE_DIRECTORY + "sitemap.xml")

def create_rss(list_page, loc=RSS_FEED_LOCATION):
    print("Generating RSS feed", file=sys.stderr)
    env = Environment(loader=FileSystemLoader('.'))
    feed_template = env.get_template('templates/rss.xml')
    list_page = sorted([i for i in list_page if i.revision_date()],
        key=lambda t: t.revision_date(), reverse=True)
    pages = []
    for page in list_page:
        hashstr = page.metadata["title"] + "|" + page.revision_date(fmt="%Y-%m-%d")
        hashval = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()
        metadata = {
            "title": page.metadata["title"] + " ({})".format(
                page.revision_date().strftime(
                "%Y-%m-%d").strip()),
            "feed_description": page.metadata["feed_description"] if
                "feed_description" in page.metadata else "",
            "slug": page.base(),
            "hashval": hashval,
            "date": page.revision_date(fmt="rfc822"),
        }
        pages.append(metadata)
    final = feed_template.render(pages=pages, now=get_date(datetime.now(), fmt="rfc822"))
    return Page(data=final, destination=SITE_DIRECTORY + loc)

def create_atom(list_page):
    print("Generating Atom feed", file=sys.stderr)
    env = Environment(loader=FileSystemLoader("."))
    feed_template = env.get_template("templates/atom.xml")
    list_page = sorted([i for i in list_page if i.revision_date()],
        key=lambda t: t.revision_date(), reverse=True)
    for page in list_page:
        hashstr = page.metadata["title"] + "|" + page.revision_date(fmt="%Y-%m-%d")
        hashval = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()
        extra = {
            "title": "{title} ({date})".format(title=page.metadata["title"], date=page.revision_date().strftime("%Y-%m-%d").strip()),
            "slug": page.base(),
            "hashval": hashval,
            "date": page.revision_date("rfc3339"),
        }
        if "_extra" in page.metadata:
            print("The '_extra' metadata field is reserved; overwriting", file=sys.stderr)
        page.metadata["_extra"] = extra
    final = feed_template.render(pages=[p.metadata for p in list_page],
        now=get_date(datetime.now(), fmt="rfc3339"))
    return Page(data=final, destination=SITE_DIRECTORY + "atom.xml")

def create_aliases(list_page):
    '''
    Take a list of pages and yield alias pages for them.
    '''
    for page in list_page:
        if "aliases" in page.metadata:
            for alias in page.metadata["aliases"]:
                print("Creating alias: " + alias, file=sys.stderr)
                write_to = Filepath(alias).route_with(site_dir_route).path
                env = Environment(loader=FileSystemLoader('.'))
                skeleton = env.get_template('templates/redirect.html')
                final = skeleton.render(title=page.metadata["title"],
                    location=page.base())
                yield Page(data=final, destination=write_to)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='generate a site or just a few files')
    parser.add_argument("--files", "--file", "-f", nargs='+',
        metavar='FILE',
        help='the locations of files to compile; accepts patterns'
    )
    parser.add_argument("--commit_ps", action="store_true",
        help="commit page source; use the current commit's page source link instead of linking to the latest one")
    args = parser.parse_args()
    if args.commit_ps:
        args.commit_ps = run_command("git rev-parse --verify HEAD").strip()
    if args.files is not None:
        for p in args.files:
            create_single_page(p).write()
    else:
        # So build the whole site
        clean()
        pages_pat = PRE_PAGES_DIRECTORY + PRE_PAGES_GLOB
        list_filepath = [Filepath(i) for i in glob.glob(pages_pat)]
        list_page, list_tag = build_data(list_filepath)
        compile_scss("common")
        compile_scss("minimal")
        compile_scss("standard")
        compile_scss("solarized_light")
        compile_scss("solarized_dark")
        copy_files(PRE_IMAGES_DIRECTORY + "*", SITE_DIRECTORY)
        copy_files(PRE_STATIC_DIRECTORY + "*",
            SITE_DIRECTORY + SITE_STATIC_DIRECTORY)
        for page in create_pages(list_page):
            page.write()
        for page in create_tag_pages(list_page, list_tag):
            page.write()
        create_page_with_all_tags(list_tag).write()
        create_page_with_all_pages(list_page).write()
        for page in create_aliases(list_page):
            page.write()
        create_sitemap(list_page, list_tag).write()
        create_rss(list_page).write()
        # For backwards-compatibility
        create_rss(list_page, "feed.xml").write()
        create_atom(list_page).write()
