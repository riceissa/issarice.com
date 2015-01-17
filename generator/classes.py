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

import os
import json
from datetime import datetime
import yaml
from yaml import SafeLoader, BaseLoader
from slugify import slugify_unicode
import commands as c
from tag_ontology import *

def to_unicode(string):
    '''
    Convert a string, bool, int, float, or unicode to a unicode object.
    '''
    if isinstance(string, unicode):
        return string
    if type(string) in [bool, float, int, str]:
        return str(string).decode('utf-8')
    if isinstance(string, type(None)):
        return "".decode('utf-8')
    else:
        raise TypeError("to_unicode cannot convert something ({s}) that isn't a string, unicode, or bool; type was {t}".format(s=string, t=type(string)))

def to_string(unic):
    '''
    Convert a string, bool, or unicode to a string.
    '''
    if isinstance(unic, unicode):
        return unic.encode('utf-8')
    if type(unic) in [str, int, float, bool]:
        return str(unic)
    else:
        raise TypeError("to_string cannot convert something that isn't a string, unicode, or bool")

def parse_as_list(x, delimiter=','):
    '''
    Take a list or string of comma-delimited items, and return a cleaned
    list.
    '''
    if type(x) in [str, unicode]:
        return [to_unicode(i.strip(" ")) for i in x.split(delimiter)
            if i != '']
    elif type(x) is list:
        return [to_unicode(i) for i in x]
    else:
        return []

def slug(s):
    return slugify_unicode(s, to_lower=True)

def split_path(path):
    '''
    Take a path(str) and return a list where each element is one
    directory.
    '''
    # See http://stackoverflow.com/a/15050936/3422337
    a, b = os.path.split(path)
    return (split_path(a) if len(a) and len(b) else []) + [b]

class AbsolutePathException(Exception):
    pass

class DirectoryException(Exception):
    pass

class Filepath(object):
    '''
    Represents a single filepath of a file relative to the current
    directory.
    '''
    def __init__(self, path):
        path = path.strip()
        if path[0] in ["/", "~"]:
            raise AbsolutePathException(
                "path is absolute; must be relative"
            )
        elif path[-1] in ["/"] or os.path.isdir(path):
            raise DirectoryException(
                "path is a directory; must be a file"
            )
        self.path = path

    def __str__(self):
        return self.path

    def filename(self):
        '''
        >>> Filepath("pages/programming/hello.md")
        'hello.md'
        '''
        return os.path.split(self.path)[1]

    def directory(self):
        '''
        >>> Filepath("pages/programming/hello.md").directory()
        'pages/programming/'
        '''
        return os.path.split(self.path)[0] + "/"

    def path_lst(self):
        '''
        >>> Filepath("pages/programming/hello.md").path_lst()
        ['pages', 'programming', 'hello.md']
        '''
        return split_path(self.path)

    def route_with(self, route):
        return route(self)

    def relative_to(self, other):
        '''
        >>> fp1 = Filepath("tags/python")
        >>> fp2 = Filepath("pages/programming/hello.md")
        >>> print(fp1.relative_to(fp2))
        ../../tags/python
        '''
        path1 = os.path.normpath(self.path)
        path2 = os.path.normpath(other.path)
        depth = len(Filepath(path2).path_lst()) - 1
        return Filepath("../" * depth + path1)

    def to_item(self):
        with open(self.path, 'r') as f:
            return Item(self, f.read())

class Route(object):
    '''
    Represents a route (Filepath -> Filepath)
    '''
    def __init__(self, route):
        self.route = route

    def __call__(self, filepath):
        if type(filepath) is not Filepath:
            raise TypeError("input is not a filepath")
        result = self.route(filepath)
        if type(result) is not Filepath:
            raise TypeError(
                "output is not a filepath;\
                this route object is an invalid route"
            )
        return result

class Tag(object):
    '''
    Represents a tag
    '''
    def __init__(self, name, pages=[]):
        self.name = name
        self.pages = pages

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return (slug(self.name) == slug(other.name))

class TagList(object):
    def __init__(self, data=[]):
        self.data = data

    def __repr__(self):
        return self.data.__repr__()

    def standardize_using(self, tag_synonyms):
        '''
        Take a dictionary of tag synonyms  and update the TagList
        instance's list of tags according to the synonyms.  For
        instance, if tag_synonyms contains the line
            "university-of-washington": ["uw", "uwashington"],
        and if tags contains "uw" or "uwashington", then this will be
        replaced by "university-of-washington".
        '''
        result = []
        for tag in self.data:
            canonical = []
            for key, value in tag_synonyms.items():
                slug_value = [slug(i) for i in value]
                if slug(tag) == slug(key) or slug(tag) in slug_value:
                    print slug(tag)
                    canonical.append(key)
            if not canonical:
                # So could not find a match in tag_synonyms
                canonical = [tag]
            result.extend(canonical)
        self.data = result

    def imply_using(self, tag_implications):
        '''
        Take an OrderedDict of tag implications and  update the TagList
        instance's list of tags with the implications applied.  Apply
        this after standardizing tags.
        '''
        for key in tag_implications:
            if key.lower() in self.data or key in self.data:
                self.data.extend(tag_implications.get(key))
        self.data = list(set(self.data))

    def organize_using(self, tag_synonyms, tag_implications):
        self.standardize_using(tag_synonyms)
        self.imply_using(tag_implications)

class Metadata(object):
    '''
    Represents the metadata of a file.
    '''
    def __init__(self, **kwargs):
        for key in kwargs:
            if type(kwargs[key]) in [str, bool, unicode]:
                self.__setattr__(key, to_unicode(kwargs[key]))
            else:
                self.__setattr__(key, kwargs[key])
        if "title" in kwargs.keys():
            self.title = to_unicode(kwargs['title'])
        if "authors" in kwargs.keys():
            self.authors = parse_as_list(kwargs['authors'])
        if "math" in kwargs.keys():
            if type(kwargs['math']) is bool:
                if kwargs['math']:
                    self.math = "True"
                else:
                    self.math = "False"
            else:
                self.math = kwargs['math']
            self.math = to_unicode(self.math)
        if "license" in kwargs.keys():
            license = kwargs['license']
            # clean up license string
            for char in ' -':
                license = license.replace(char, '')
            license = license.upper()
            if license in ["CC0", "PUBLICDOMAIN", "PD"]:
                self.license = to_unicode("CC0")
            elif license.upper() in ["CCBY", "BY", "ATTRIBUTION"]:
                self.license = to_unicode("CC-BY")
            elif license.upper() in ["CCBYSA", "CCSA", "SHAREALIKE"]:
                self.license = to_unicode("CC-BY-SA")
            else:
                # set default license to unknown (i.e., copyrighted)
                self.license = to_unicode("UNKNOWN")
        if "tags" in kwargs.keys():
            tag_list = TagList(parse_as_list(kwargs['tags']))
            tag_list.organize_using(TAG_SYNONYMS, TAG_IMPLICATIONS)
            self.tags = tag_list.data

    def __str__(self):
        return str(self.__dict__)

    def update_with(self, other):
        if type(other) is Metadata:
            self.__init__(**other.__dict__)
        elif type(other) is dict:
            self.__init__(**other)
        else:
            raise TypeError("you must update_with another metadata object or a dict")

    def __call__(self, **kwargs):
        self.__init__(**kwargs)
        #for key in kwargs:
            #print "setting {key} to {val}".format(key=key, val=kwargs[key])
            #if key == "tags":
                #self.__setattr__(key, kwargs[key])
            #else:
                #self.__setattr__(key, to_unicode(kwargs[key]))

default_metadata = Metadata(title="", tags=["untagged"], math="False", authors=[], license="CC-BY")

class Page(object):
    '''
    Represents a typical page (i.e. those that are read from a file and
    are to be converted); special pages like the page with all the tags
    will not be an object of this class.
    '''
    def __init__(self, origin, json=[], metadata=Metadata()):
        if type(origin) is Filepath:
            self.origin = origin
        else:
            self.origin = Filepath(origin)
        self.json = json
        self.metadata = metadata

    def load_metadata(self):
        with open(self.origin.path, 'r') as f:
            metadata = ""
            first = f.readline()
            if first == '---\n':
                then = f.readline()
                while then not in ['---\n', '...\n', '']:
                    metadata += then
                    then = f.readline()
            self.metadata = Metadata(**yaml.load(metadata,
                Loader=BaseLoader))

    def compiled(self):
        '''
        Compile page and return the string of the output.
        '''
        ast = json.loads(c.run_command("pandoc --smart -f markdown -t json {page}".format(page=self.origin.path)))
        return to_unicode(
            c.run_command(
                "pandoc -f json -t html --toc --toc-depth=4 --template=templates/toc.html --smart --mathjax --base-header-level=2 --filter generator/url_filter.py",
                pipe_in=json.dumps(ast, separators=(',',':'))
            )
        )

    def base(self):
        return self.origin.route_with(set_extension("")).route_with(drop_one_parent_dir_route).path

    def __repr__(self):
        return "Page({})".format(self.origin.path.__repr__())

    def revision_date(self, string=True):
        try:
            rev_date = self.metadata.__getattribute__(
                'last-major-revision-date'
            )
        except AttributeError:
            rev_date = ''
        rev_date = to_string(rev_date) # sanitize
        if rev_date != '':
            date_obj = datetime.strptime(rev_date, '%Y-%m-%d')
            if string:
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S %z").strip()
            else:
                return date_obj
        else:
            date_obj = datetime.strptime("2010-01-01", '%Y-%m-%d')
            if string:
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S %z").strip()
            else:
                return date_obj

@Route
def drop_one_parent_dir_route(filepath):
    return Filepath('/'.join([i for i in split_path(filepath.path)[1:]]))

def to_dir(dirname):
    '''
    dirname(str) -> (Filepath -> Filepath)
    '''
    @Route
    def f(filepath):
        return Filepath(dirname + filepath.path)
    return f

def set_extension(extension):
    '''
    Extension(str) -> Filepath -> Filepath
    '''
    @Route
    def f(filepath):
        '''
        Filepath -> Filepath
        '''
        return Filepath(os.path.splitext(filepath.path)[0] + extension)
    return f

site_dir = "_site/"
site_dir_route = to_dir(site_dir)

@Route
def my_route(filepath):
    return filepath.route_with(set_extension("")).route_with(drop_one_parent_dir_route).route_with(site_dir_route)

