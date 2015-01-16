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
import metadata as meta
import commands as c
from tag_ontology import *

def to_unicode(string):
    '''
    Convert a string, bool, or unicode to a unicode object.
    '''
    if isinstance(string, str):
        return string.decode('utf-8')
    if isinstance(string, bool):
        if string:
            return "True".decode('utf-8')
        else:
            return "False".decode('utf-8')
    if isinstance(string, unicode):
        return string
    if isinstance(string, type(None)):
        return "".decode('utf-8')
    else:
        raise TypeError("to_unicode cannot convert something that isn't a string, unicode, or bool; type was {t}".format(t=type(string)))

def to_string(unic):
    '''
    Convert a string, bool, or unicode to a string.
    '''
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
        raise TypeError("to_string cannot convert something that isn't a string, unicode, or bool")

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

class Metadata(object):
    '''
    Represents the metadata of a file.
    '''
    def __init__(self, **kwargs):
        seen = {
            "title": False,
            "authors": False,
            "math": False,
            "tags": False,
            "license": False,
        }
        for k in kwargs.keys():
            seen[to_string(k)] = False
        if "title" in kwargs.keys():
            self.title = to_unicode(kwargs['title'])
            seen['title'] = True
        if "authors" in kwargs.keys():
            self.authors = [to_unicode(author) for author in kwargs['authors']]
            seen['authors'] = True
        if "math" in kwargs.keys():
            if type(kwargs['math']) is bool:
                if kwargs['math']:
                    self.math = "True"
                else:
                    self.math = "False"
            else:
                self.math = kwargs['math']
            self.math = to_unicode(self.math)
            seen['math'] = True
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
                # set default license to CC-BY
                self.license = to_unicode("CC-BY")
            seen['license'] = True
        if "tags" in kwargs.keys():
            self.tags = [to_unicode(tag) for tag in kwargs['tags']]
            seen['tags'] = True
        for key in kwargs:
            if not seen[key]:
                self.__setattr__(key, to_unicode(kwargs[key]))

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
            print metadata
            self.metadata = Metadata(yaml.load(metadata))

    def load(self):
        '''
        Load both raw and metadata
        '''
        output = c.run_command("pandoc --smart -f markdown -t json {page}".format(page=self.origin.path))
        self.json = meta.organize_tags(
            json.loads(output),
            tag_synonyms,
            tag_implications
        )
        self.metadata = Metadata(**meta.get_metadata_dict(self.json))
        #page.metadata.update_with(meta.get_metadata_dict(page.json))

    def base(self):
        return self.origin.route_with(set_extension("")).route_with(drop_one_parent_dir_route).path

    def __repr__(self):
        return "Page('{}')".format(self.origin.path)

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
