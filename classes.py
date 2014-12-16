#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

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

def split_path(path):
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
