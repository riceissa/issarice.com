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

from classes import *
from tag_ontology import *

def clean():
    print("Removing {d}".format(d=SITE_DIRECTORY))
    run_command("rm -rf {d}".format(d=SITE_DIRECTORY))

def compile_scss():
    if not os.path.exists(SITE_DIRECTORY + SITE_CSS_DIRECTORY):
        os.makedirs(SITE_DIRECTORY + SITE_CSS_DIRECTORY)
    command = "sass --style compressed " + PRE_CSS_DIRECTORY + "minimal.scss"
    compiled = run_command(command)
    with open(SITE_DIRECTORY + SITE_CSS_DIRECTORY +
        "minimal.css", 'w') as f:
        f.write(compiled)

def copy_files(pattern, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for f in glob.glob(pattern):
        print("Copying {f} to {to}".format(f=f, to=destination))
        run_command("cp {f} {to}".format(f=f, to=destination))

def create_pages(list_page):
    for page in list_page:
        print("Processing " + str(page.origin))
        write_to = page.origin.route_with(my_route)
        final = page.compiled(tags_dir=SITE_TAGS_DIRECTORY)
        if not os.path.exists(SITE_DIRECTORY):
            os.makedirs(SITE_DIRECTORY)
        with open(write_to.path, 'w') as f:
            f.write(to_string(final))

def build_data(list_filepath):
    list_page = []
    list_tag = []
    for filepath in list_filepath:
        page = Page(filepath)
        page.load_metadata()
        list_page.append(page)
        list_tag.extend(page.metadata.tags)
    list_tag = list(set(list_tag))
    return (list_page, list_tag)

def create_single_page(filepath):
    '''
    For use when one only wants to partially compile.
    '''
    page = Page(filepath)
    print("Processing " + str(page.origin))
    page.load_metadata()
    write_to = page.origin.route_with(my_route)
    final = page.compiled(tags_dir=SITE_TAGS_DIRECTORY)
    if not os.path.exists(SITE_DIRECTORY):
        os.makedirs(SITE_DIRECTORY)
    with open(write_to.path, 'w') as f:
        f.write(to_string(final))

def create_tag_page(list_page, list_tag):
    for tag in list_tag:
        print("Processing tag page for " + tag)
        pages = []
        for page in list_page:
            if tag in page.metadata.tags:
                pages.append({'title': to_unicode(page.metadata.title), 'url': to_unicode("../" + page.base())})
        pages = sorted(pages, key=lambda t: t['title'].lower())
        write_to = Filepath(SITE_DIRECTORY + SITE_TAGS_DIRECTORY +
            to_string(slug(tag)))
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
            css = Filepath(SITE_CSS_DIRECTORY +
                "minimal.css").relative_to(Filepath(SITE_TAGS_DIRECTORY +
                to_string(tag))).path,
            path = "../",
        )
        if not os.path.exists(SITE_DIRECTORY + SITE_TAGS_DIRECTORY):
            os.makedirs(SITE_DIRECTORY + SITE_TAGS_DIRECTORY)
        with open(write_to.path, 'w') as f:
            f.write(to_string(final))

# Make page with all tags
def create_page_with_all_tags(list_tag):
    print("Creating page with all the tags")
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    pages = [{'title': to_unicode(tag), 'url': to_unicode(slug(tag))} for tag in list_tag]
    pages = sorted(pages, key=lambda t: t['title'].lower())
    body = to_unicode(page_list.render(pages=pages))
    skeleton = env.get_template('templates/skeleton.html')
    ctx = Metadata(
        title = "All tags",
        css = Filepath(SITE_CSS_DIRECTORY +
            "minimal.css").relative_to(Filepath(SITE_TAGS_DIRECTORY +
            "index")).path,
        license = "cc0",
    )
    final = skeleton.render(page=ctx, body=body, css=ctx.css, path="../")
    if not os.path.exists(SITE_DIRECTORY + SITE_TAGS_DIRECTORY):
        os.makedirs(SITE_DIRECTORY + SITE_TAGS_DIRECTORY)
    with open(SITE_DIRECTORY + SITE_TAGS_DIRECTORY + "index", 'w') as f:
        f.write(to_string(final))

# Make page with all pages
def create_page_with_all_pages(list_page):
    print("Creating page with all the pages")
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    pages = [
        {
            'title': to_unicode(page.metadata.title),
            'url': to_unicode(page.base())
        } for page in list_page
    ]
    pages = sorted(pages, key=lambda t: t['title'])
    body = page_list.render(pages=pages)
    skeleton = env.get_template('templates/skeleton.html')
    ctx = Metadata(
        title = "All pages on the site",
        css = Filepath(SITE_CSS_DIRECTORY +
            "minimal.css").relative_to(Filepath("all")).path,
        license = "cc0",
    )
    final = skeleton.render(page=ctx, body=body, css=ctx.css, path="./")
    if not os.path.exists(SITE_DIRECTORY):
        os.makedirs(SITE_DIRECTORY)
    with open(SITE_DIRECTORY + "_all", 'w') as f:
        f.write(to_string(final))

def create_sitemap(list_page, list_tag):
    print("Generating sitemap")

    env = Environment(loader=FileSystemLoader('.'))
    sitemap_list = env.get_template('templates/sitemap-list.xml')
    list_page = sorted(list_page, key=lambda t: t.metadata.title)
    body = u""
    for page in list_page:
        body += to_unicode(sitemap_list.render(slug=to_unicode(page.base())))
    for t in list_tag:
        body += to_unicode(sitemap_list.render(slug="_tags/" + t))
    sitemap = env.get_template('templates/sitemap.xml')
    final = sitemap.render(body=body)

    with open(SITE_DIRECTORY + "sitemap.xml", "w") as f:
        f.write(to_string(final))

def create_rss(list_page):
    print("Generating RSS feed")
    env = Environment(loader=FileSystemLoader('.'))
    feed_template = env.get_template('templates/rss.xml')
    list_page = sorted(list_page, key=lambda t: t.revision_date(string=False), reverse=True)
    pages = [
        {
            'title': page.metadata.title + " ({})".format(page.revision_date(string=False).strftime("%Y-%m-%d").strip()),
            'description': page.metadata.description if hasattr(page.metadata, 'description') else "",
            'slug': to_unicode(page.base()),
            'hashval': hashlib.sha1(to_string(page.metadata.title) + "|" + page.revision_date()).hexdigest(),
            'date': page.revision_date(),
        }
        for page in list_page
    ]
    final = feed_template.render(pages=pages, now=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"))

    with open(SITE_DIRECTORY + "feed.xml", "w") as f:
        f.write(to_string(final))

def create_aliases(list_page):
    for page in list_page:
        try:
            aliases = [slug(i) for i in page.metadata.aliases]
            for alias in aliases:
                print("Creating alias: " + alias)
                write_to = Filepath(alias).route_with(site_dir_route).path
                env = Environment(loader=FileSystemLoader('.'))
                skeleton = env.get_template('templates/redirect.html')
                final = skeleton.render(
                    title = to_unicode(page.metadata.title),
                    location = to_unicode(page.base()),
                )
                if not os.path.exists(write_to):
                    with open(write_to, 'w') as f:
                        f.write(to_string(final))
        except AttributeError:
            pass

if __name__ == '__main__':
    from config import *
    import argparse
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
        # So build the whole site
        clean()
        pages_pat = PRE_PAGES_DIRECTORY + "*.md"
        list_filepath = [Filepath(i) for i in glob.glob(pages_pat)]
        list_page, list_tag = build_data(list_filepath)
        compile_scss()
        copy_files(PRE_IMAGES_DIRECTORY + "*", SITE_DIRECTORY)
        copy_files(PRE_STATIC_DIRECTORY + "*", SITE_DIRECTORY + SITE_STATIC_DIRECTORY)
        create_pages(list_page)
        create_tag_page(list_page, list_tag)
        create_page_with_all_tags(list_tag)
        create_page_with_all_pages(list_page)
        create_aliases(list_page)
        create_sitemap(list_page, list_tag)
        create_rss(list_page)
