#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import json
from collections import OrderedDict
from jinja2 import Template, Environment, FileSystemLoader
import os

import commands as c
import metadata as meta
from tag_ontology import *

def to_unicode(string):
    if isinstance(string, str):
        return string.decode('utf-8')
    if isinstance(string, bool):
        if string:
            return "True".decode('utf-8')
        else:
            return "False".decode('utf-8')
    if isinstance(string, unicode):
        return string
    else:
        return "".decode("utf-8")

def to_string(unic):
    if isinstance(unic, unicode):
        return unic.encode('utf-8')
    if isinstance(unic, bool):
        if unic:
            return "True"
        else:
            return "False"
    if isinstance(unic, str):
        return unic
    else:
        return ""

pages_pat = "pages/*.md"
pages_lst = glob.glob(pages_pat)

all_tags = []
page_data = []
for page in pages_lst:
    #print "on page " + page
    output = c.run_command("pandoc -f markdown -t json {page}".format(page=page))
    json_lst = json.loads(output)
    file_dict = meta.organize_tags(json_lst, tag_synonyms, tag_implications)
    tags_lst = meta.get_tags(file_dict['json'])
    tags_lst = [to_unicode(i) for i in tags_lst]
    all_tags.extend(tags_lst)
    json_str = json.dumps(file_dict['json'], separators=(',',':'))
    body = c.run_command("pandoc -f json -t html --toc --template=templates/toc.html --mathjax --base-header-level=2", pipe_in=json_str).decode('utf-8')
    title = to_unicode(meta.get_metadata_field(json_lst, "title"))
    math = to_unicode(meta.get_metadata_field(json_lst, "math"))
    license = to_unicode(meta.get_metadata_field(json_lst, "license"))

    env = Environment(loader=FileSystemLoader('.'))
    skeleton = env.get_template('templates/skeleton.html')
    tags = []
    for tag in tags_lst:
        tags.append({'name': to_unicode(tag), 'path': to_unicode("tags/" + tag)})
    tags = sorted(tags, key=lambda t: t['name'])
    final = skeleton.render(body=body, title=title, license=license, math=math, tags=tags)
    inter = os.path.split(os.path.splitext(page)[0])[1]
    write_to = "_site/" + inter
    page_data.append((title, inter, tags_lst))

    with open(write_to, 'w') as f:
        f.write(to_string(final))

all_tags = list(set(all_tags))

for tag in all_tags:
    pages = []
    for page_tuple in page_data:
        if tag in page_tuple[2]:
            pages.append({'title': to_unicode(page_tuple[0]), 'url': to_unicode("../" + page_tuple[1])})
    pages = sorted(pages, key=lambda t: t['title'])
    write_to = "_site/tags/" + to_string(tag)
    env = Environment(loader=FileSystemLoader('.'))
    page_list = env.get_template('templates/page-list.html')
    body = to_unicode(page_list.render(pages=pages))
    skeleton = env.get_template('templates/skeleton.html')
    final = skeleton.render(body=body, title=to_unicode("Tag page for " + tag))

    with open(write_to, 'w') as f:
        f.write(to_string(final))

# Make page with all tags
env = Environment(loader=FileSystemLoader('.'))
page_list = env.get_template('templates/page-list.html')
pages = [{'title': to_unicode(tag), 'url': to_unicode(tag)} for tag in all_tags]
pages = sorted(pages, key=lambda t: t['title'])
body = to_unicode(page_list.render(pages=pages))
skeleton = env.get_template('templates/skeleton.html')
final = skeleton.render(title=to_unicode("All tags"), body=body)
with open("_site/tags/index", 'w') as f:
    f.write(to_string(final))

# Make page with all pages
env = Environment(loader=FileSystemLoader('.'))
page_list = env.get_template('templates/page-list.html')
pages = [{'title': to_unicode(page_tup[0]), 'url': to_unicode(page_tup[1])} for page_tup in page_data]
pages = sorted(pages, key=lambda t: t['title'])
body = page_list.render(pages=pages)
skeleton = env.get_template('templates/skeleton.html')
final = skeleton.render(title=to_unicode("All pages on the site"), body=body)
with open("_site/all", 'w') as f:
    f.write(to_string(final))
