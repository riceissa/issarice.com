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

from pandocfilters import toJSONFilter, stringify, Link
import commands as c

def url_filter(key, value, format_, meta):
    '''
    If a link is of the form "!STRING", use the !-expression to search
    DuckDuckGo.  So for instance [Fishmans](!w) would search Wikipedia
    for "Fishmans".
    '''
    if key == 'Link':
        [txt, [url, attr]] = value
        if url.startswith("!"):
            url = "http://duckduckgo.com/?q=" + url + " " + stringify(txt)
            return Link(txt, [url, attr])
        if url == '':
            # So we want to internally link txt
            url = c.run_command("sed -e 's/[^[:alnum:]]/-/g'", pipe_in=stringify(txt))
            url = c.run_command("tr -s '-'", pipe_in = url)
            url = c.run_command("tr A-Z a-z", pipe_in=url)
            url = c.run_command("sed -e 's/^\-//'", pipe_in=url)
            url = c.run_command("sed -e 's/\-$//'", pipe_in=url)
            url = "./" + url
            return Link(txt, [url, attr])

if __name__ == '__main__':
    toJSONFilter(url_filter)
