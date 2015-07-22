#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from tld import get_tld
from bs4 import BeautifulSoup

def main():
    #url = "http://gwern.net/Spaced repetition"
    #url = "http://gwern.net/Spaced%20repetition"
    #url = "http://issarice.com/anecdote-story"
    #url = "http://quora.com"
    #url = "https://stackoverflow.com/questions/1695183/how-to-percent-encode-url-parameters-in-python"
    url = "http://issarice.com/favicon.ico"
    response = requests.get(url, stream=True)
    url = response.url

    # <title> is probably in the first around 10MB
    doc = response.iter_content(chunk_size=10000)
    print(get_markdown_link(get_link_text(url, response.headers["content-type"], data=next(doc)), url), end="")

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
        soup = BeautifulSoup(data, 'html.parser')
        try:
            if soup.title.string:
                result = soup.title.string
            else:
                result = "Page on " + tld
        except AttributeError:
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
