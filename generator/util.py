#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2015, Issa Rice
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

import subprocess
import shlex
from slugify import slugify_unicode
import os

def run_command(command, pipe_in=''):
    '''
    Run command and return its output by optionally piping in pipe_in.
    Same as
        command < pipe_in.txt
    where pipe_in.txt contains pipe_in.  If no pipe_in is
    specified, or pipe_in is '', then just run the command
    and return its output.
    '''
    if pipe_in == '':
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()
        if stderr not in ["None", "", None]:
            print("On the command")
            print("    {command}".format(command=command))
            print("there was an error:")
            print(stderr)
        return stdout
    else:
        # See http://stackoverflow.com/a/165662/3422337
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate(input=pipe_in)
        if stderr not in ["None", "", None]:
            print("On the command")
            print("    {command}".format(command=command))
            print("with the input")
            for line in pipe_in.split("\n"):
                print("    " + line)
            print("there was an error:")
            print(stderr)
        return stdout

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
