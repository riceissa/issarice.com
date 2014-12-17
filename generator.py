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
from collections import OrderedDict
from jinja2 import Template, Environment, FileSystemLoader
import os

import commands as c
import metadata as meta
from classes import *
from tag_ontology import *

pages_pat = "pages/*.md"
pages_lst = [Filepath(i) for i in glob.glob(pages_pat)]

# Copy css
with open('css/minimal.css', 'r') as i, open('_site/css/minimal.css', 'w') as o:
    x = i.read()
    o.write(x)

all_tags = []
page_data = []

# Make page for each page
for page in pages_lst:
    print("Processing " + str(page))
    output = c.run_command("pandoc -f markdown -t json {page}".format(page=str(page)))
    json_lst = json.loads(output)
    file_dict = meta.organize_tags(json_lst, tag_synonyms, tag_implications)
    tags_lst = meta.get_tags(file_dict['json'])
    all_tags.extend(tags_lst)
    json_str = json.dumps(file_dict['json'], separators=(',',':'))
    body = to_unicode(c.run_command("pandoc -f json -t html --toc --template=templates/toc.html --mathjax --base-header-level=2", pipe_in=json_str))

    inter = page.route_with(set_extension("")).route_with(drop_one_parent_dir_route).path
    write_to = page.route_with(my_route)

    ctx = Metadata(
        title = meta.get_metadata_field(json_lst, "title"),
        math = meta.get_metadata_field(json_lst, "math"),
        license = meta.get_metadata_field(json_lst, "license"),
        tags = tags_lst,
        css = Filepath("css/minimal.css").relative_to(Filepath(inter)).path,
        source = page.path,
    )

    env = Environment(loader=FileSystemLoader('.'))
    skeleton = env.get_template('templates/skeleton.html')
    tags = []
    for tag in ctx.tags:
        tags.append({'name': tag, 'path': to_unicode(Filepath(to_string(tag)).route_with(to_dir("tags/")).path)})
    tags = sorted(tags, key=lambda t: t['name'])
    final = skeleton.render(body=body, page=ctx, tags=tags, css=ctx.css)
    page_data.append((ctx.title, inter, tags_lst))

    with open(write_to.path, 'w') as f:
        f.write(to_string(final))

all_tags = list(set(all_tags))

for tag in all_tags:
    print("Processing tag page for " + tag)
    pages = []
    for page_tuple in page_data:
        if tag in page_tuple[2]:
            pages.append({'title': to_unicode(page_tuple[0]), 'url': to_unicode("../" + page_tuple[1])})
    pages = sorted(pages, key=lambda t: t['title'])
    write_to = Filepath("_site/tags/" + to_string(tag))
    ctx = Metadata(
        title = "Tag: " + tag,
        css = Filepath("css/minimal.css").relative_to(Filepath("tags/" + to_string(tag))).path,
        license = "cc0",
    )
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    body = to_unicode(page_list.render(pages=pages))
    skeleton = env.get_template('templates/skeleton.html')
    final = skeleton.render(body=body, page=ctx, css=ctx.css)

    with open(write_to.path, 'w') as f:
        f.write(to_string(final))

# Make page with all tags
print("Creating page with all the tags")
env = Environment(loader=FileSystemLoader('.'))
page_list = env.get_template('templates/page-list.html')
pages = [{'title': to_unicode(tag), 'url': to_unicode(tag)} for tag in all_tags]
pages = sorted(pages, key=lambda t: t['title'])
body = to_unicode(page_list.render(pages=pages))
skeleton = env.get_template('templates/skeleton.html')
ctx = Metadata(
    title = "All tags",
    css = Filepath("css/minimal.css").relative_to(Filepath("tags/index")).path,
    license = "cc0",
)
final = skeleton.render(page=ctx, body=body, css=ctx.css)
with open("_site/tags/index", 'w') as f:
    f.write(to_string(final))

# Make page with all pages
print("Creating page with all the pages")
env = Environment(loader=FileSystemLoader('.'))
page_list = env.get_template('templates/page-list.html')
pages = [{'title': to_unicode(page_tup[0]), 'url': to_unicode(page_tup[1])} for page_tup in page_data]
pages = sorted(pages, key=lambda t: t['title'])
body = page_list.render(pages=pages)
skeleton = env.get_template('templates/skeleton.html')
ctx = Metadata(
    title = "All pages on the site",
    css = Filepath("css/minimal.css").relative_to(Filepath("all")).path,
    license = "cc0",
)
final = skeleton.render(page=ctx, body=body, css=ctx.css)
with open("_site/all", 'w') as f:
    f.write(to_string(final))
