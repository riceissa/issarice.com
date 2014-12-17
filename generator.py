#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        css = Filepath("css/minimal.css").relative_to(write_to).path
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
    ctx = Metadata(
        title = "Tag: " + tag,
    )
    write_to = "_site/tags/" + to_string(tag)
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    body = to_unicode(page_list.render(pages=pages))
    skeleton = env.get_template('templates/skeleton.html')
    final = skeleton.render(body=body, page=ctx)

    with open(write_to, 'w') as f:
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
)
final = skeleton.render(page=ctx, body=body)
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
)
final = skeleton.render(page=ctx, body=body)
with open("_site/all", 'w') as f:
    f.write(to_string(final))
