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

import subprocess
import shlex

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

def write_to_filepath(contents, filepath):
    with open(filepath, 'w') as f:
        f.write(contents)

