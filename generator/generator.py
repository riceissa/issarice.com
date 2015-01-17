#!/usr/bin/python
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

import commands as c
import metadata as meta
from classes import *
from tag_ontology import *

def clean():
    print("Removing {d}".format(d=SITE_DIR))
    c.run_command("rm -rf {d}".format(d=SITE_DIR))

def compile_scss():
    if not os.path.exists(SITE_DIR + "_css/"):
        os.makedirs(SITE_DIR + "_css/")
    compiled = c.run_command("sass --style compressed css/minimal.scss")
    with open(SITE_DIR + "_css/minimal.css", 'w') as f:
        f.write(compiled)

def copy_files(pattern, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for f in glob.glob(pattern):
        print("Copying {f} to {to}".format(f=f, to=destination))
        c.run_command("cp {f} {to}".format(f=f, to=destination))

# Make page for each page

def create_pages():
    global all_tags
    global page_data
    for page_path in pages_lst:
        create_page(page_path)

def pandoc_compile(json_lst):
    return to_unicode(
        c.run_command(
            "pandoc -f json -t html --toc --toc-depth=4 --template=templates/toc.html --smart --mathjax --base-header-level=2 --filter generator/url_filter.py",
            pipe_in=json.dumps(json_lst, separators=(',',':'))
        )
    )

def create_page(path):
    '''
    Compile a single file from markdown to HTML.
    '''
    global all_tags
    global page_data
    page = Page(path)
    print("Processing " + str(page.origin))
    page.load()
    all_tags.extend(page.metadata.tags)
    body = pandoc_compile(page.json)
    #inter = page.origin.route_with(set_extension("")).route_with(drop_one_parent_dir_route).path
    inter = page.base()
    write_to = page.origin.route_with(my_route)

    env = Environment(loader=FileSystemLoader('.'))
    skeleton = env.get_template('templates/skeleton.html')
    final = skeleton.render(
        body = body,
        # In templates, we use page.field to access metadata fields
        page = page.metadata,
        tags = sorted(
            [
                {
                    'name': tag,
                    'path': to_unicode(Filepath(to_string(tag))\
                        .route_with(to_dir(TAGS_DIR)).path),
                }
                for tag in page.metadata.tags
            ],
            key = lambda t: t['name'],
        ),
        # Calculate where the css file will be located relative to the
        # current file's (eventual) location
        css = Filepath("_css/minimal.css").relative_to(Filepath(inter)).path,
        source = to_unicode(page.origin.path),
        path = "./",
    )
    #page_data.append((page.metadata.title, inter, page.metadata.tags)) # to be used later
    # Keep a cumulative list of pages for later use
    page_data.append(page)

    if not os.path.exists(SITE_DIR):
        os.makedirs(SITE_DIR)

    with open(write_to.path, 'w') as f:
        f.write(to_string(final))

def create_tag_page():
    global page_data
    global all_tags
    for tag in all_tags:
        print("Processing tag page for " + tag)
        pages = []
        for page in page_data:
            if tag in page.metadata.tags:
                pages.append({'title': to_unicode(page.metadata.title), 'url': to_unicode("../" + page.base())})
        pages = sorted(pages, key=lambda t: t['title'])
        write_to = Filepath(SITE_DIR + TAGS_DIR + to_string(tag))
        ctx = Metadata(
            title = "Tag: " + tag,
            license = "cc0",
        )
        env = Environment(loader=FileSystemLoader('.'))
        page_list = env.get_template('templates/page-list.html')
        body = to_unicode(page_list.render(pages=pages))
        skeleton = env.get_template('templates/skeleton.html')
        final = skeleton.render(
            body = body,
            page = ctx,
            css = Filepath("_css/minimal.css").relative_to(Filepath(TAGS_DIR + to_string(tag))).path,
            path = "../",
        )
        if not os.path.exists(SITE_DIR + TAGS_DIR):
            os.makedirs(SITE_DIR + TAGS_DIR)
        with open(write_to.path, 'w') as f:
            f.write(to_string(final))

# Make page with all tags
def create_page_with_all_tags():
    global all_tags
    print("Creating page with all the tags")
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    pages = [{'title': to_unicode(tag), 'url': to_unicode(tag)} for tag in all_tags]
    pages = sorted(pages, key=lambda t: t['title'])
    body = to_unicode(page_list.render(pages=pages))
    skeleton = env.get_template('templates/skeleton.html')
    ctx = Metadata(
        title = "All tags",
        css = Filepath("_css/minimal.css").relative_to(Filepath(TAGS_DIR + "index")).path,
        license = "cc0",
    )
    final = skeleton.render(page=ctx, body=body, css=ctx.css, path="../")
    if not os.path.exists(SITE_DIR + TAGS_DIR):
        os.makedirs(SITE_DIR + TAGS_DIR)
    with open(SITE_DIR + TAGS_DIR + "index", 'w') as f:
        f.write(to_string(final))

# Make page with all pages
def create_page_with_all_pages():
    global page_data
    print("Creating page with all the pages")
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    pages = [
        {
            'title': to_unicode(page.metadata.title),
            'url': to_unicode(page.base())
        } for page in page_data
    ]
    pages = sorted(pages, key=lambda t: t['title'])
    body = page_list.render(pages=pages)
    skeleton = env.get_template('templates/skeleton.html')
    ctx = Metadata(
        title = "All pages on the site",
        css = Filepath("_css/minimal.css").relative_to(Filepath("all")).path,
        license = "cc0",
    )
    final = skeleton.render(page=ctx, body=body, css=ctx.css, path="./")
    if not os.path.exists(SITE_DIR):
        os.makedirs(SITE_DIR)
    with open(SITE_DIR + "_all", 'w') as f:
        f.write(to_string(final))

def create_sitemap():
    global page_data
    global all_tags
    print("Generating sitemap")

    env = Environment(loader=FileSystemLoader('.'))
    sitemap_list = env.get_template('templates/sitemap-list.xml')
    page_data = sorted(page_data, key=lambda t: t.metadata.title)
    body = u""
    for page in page_data:
        body += to_unicode(sitemap_list.render(slug=to_unicode(page.base())))
    for t in all_tags:
        body += to_unicode(sitemap_list.render(slug="_tags/" + t))
    sitemap = env.get_template('templates/sitemap.xml')
    final = sitemap.render(body=body)

    with open(SITE_DIR + "sitemap.xml", "w") as f:
        f.write(to_string(final))

def create_rss():
    global page_data
    print("Generating RSS feed")
    env = Environment(loader=FileSystemLoader('.'))
    feed_template = env.get_template('templates/rss.xml')
    page_data = sorted(page_data, key=lambda t: t.revision_date(string=False), reverse=True)
    pages = [
        {
            'title': page.metadata.title + " ({})".format(page.revision_date(string=False).strftime("%Y-%m-%d").strip()),
            'description': page.metadata.description if hasattr(page.metadata, 'description') else "",
            'slug': to_unicode(page.base()),
            'hashval': hashlib.sha1(to_string(page.metadata.title) + "|" + page.revision_date()).hexdigest(),
            'date': page.revision_date(),
        }
        for page in page_data
    ]
    final = feed_template.render(pages=pages, now=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"))

    with open(SITE_DIR + "feed.xml", "w") as f:
        f.write(to_string(final))

if __name__ == '__main__':
    import argparse
    SITE_DIR = "_site/"
    # relative to SITE_DIR
    TAGS_DIR = "_tags/"
    all_tags = [] # cumulative list of all tags
    page_data = [] # stores all pages

    parser = argparse.ArgumentParser(description='generate a site or just a few files')
    parser.add_argument(
        "--files",
        "--file",
        "-f",
        nargs = '+',
        metavar = 'FILE',
        help = 'the locations of files to compile; accepts patterns'
    )
    args = parser.parse_args()
    if args.files is not None:
        for p in args.files:
            create_page(p)
    else:
        clean()
        pages_pat = "wiki/a*.md"
        pages_lst = [Filepath(i) for i in glob.glob(pages_pat)]
        compile_scss()
        copy_files("images/*", SITE_DIR)
        copy_files("static/*", SITE_DIR + "_static/")
        create_pages()
        all_tags = list(set(all_tags))
        create_tag_page()
        create_page_with_all_tags()
        create_page_with_all_pages()
        create_sitemap()
        create_rss()
