#!/usr/bin/python3
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

import argparse
import sys
import requests
import urllib3
from tld import get_tld
from bs4 import BeautifulSoup

def main():
    # See https://blog.quora.com/Launched-Customizable-Links for Quora's launch post
    parser = argparse.ArgumentParser(description="Get the linked title of URLs (similar to Quora and Facebook)")
    parser.add_argument("url", type=str, help="the URL")
    args = parser.parse_args()
    url = args.url
    attempt_1 = try_url(url)
    if attempt_1["exit"]:
        print(attempt_1["text"], end="")
    else:
        attempt_2 = try_url("http://" + url)
        if attempt_2["exit"]:
            print(attempt_2["text"], end="")
        else:
            print(attempt_1["text"], end="")

def try_url(url):
    '''
    Return (Str, True) if succeeded; (Str, False) otherwise.
    '''
    result = {}
    try:
        response = requests.get(url, stream=True)
        url = response.url
        if  "text/html" in response.headers["content-type"]:
            # <title> is probably in the first around 10MB
            doc = response.iter_content(chunk_size=10000)
            data = next(doc)
            result["text"] = get_markdown_link(get_link_text(url, response.headers["content-type"], data=data), url)
        else:
            result["text"] = get_markdown_link(get_link_text(url, response.headers["content-type"]), url)
        result["exit"] = True
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema, urllib3.exceptions.LocationParseError):
        result["text"] = "[{url}]({url})".format(url=url)
        result["exit"] = False
    return result

def get_link_text(url, mime_type, data=None):
    '''
    Take URL, MIME type, and optional data to produce the link text.
    '''
    tld = get_tld(url)
    result = "File on " + tld
    if mime_type.startswith("image"):
        result = "Image on " + tld
    elif mime_type == "application/pdf":
        result = "PDF on " + tld
    elif "text/html" in mime_type:
        try:
            soup = BeautifulSoup(data, 'html.parser')
            if soup.title.string:
                result = soup.title.string
            else:
                result = "Page on " + tld
        except:
            result = "Page on " + tld
    if len(result) > 255:
        result = result[:253] + " …"

    return result

def get_markdown_link(link_text, url):
    return "[{link_text}]({url})".format(link_text=escape_special_chars(link_text), url=url)

def escape_special_chars(string):
    '''
    Escape special characters for Pandoc markdown.
    '''
    # From http://pandoc.org/README.html#backslash-escapes
    special_chars = "\\`*_{}[]()>#+-.!"
    result = ""
    for c in string:
        if c in special_chars:
            result += "\\" + c
        else:
            result += c
    return result

if __name__ == "__main__":
    main()
