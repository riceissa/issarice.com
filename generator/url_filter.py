#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Issa Rice
# License: CC0

from pandocfilters import toJSONFilter, stringify, Link

def slug(s):
    '''
    "Slugify" the string s as follows: keep only the characters that are
    alphabetic or numerical, and group them together; all other characters are
    replaced by "-" and squeezed together.
    '''
    s = s.lower()
    s = "".join(c if (c.isalpha() or c.isdigit()) else "-" for c in s)
    s = "-".join(filter(bool, s.split("-")))
    return s

def url_filter(key, value, format_, meta):
    '''
    Filter special links.  If a link is of the form '!STRING', use the
    bang-expression to search DuckDuckGo.  So for instance (with markdown)
    '[Fishmans](!w)' would search Wikipedia for "Fishmans".  If a link
    is empty, like '[About me]()', then automatically link to the
    slug-form of the text; in this case, the link would be transformed
    to '[About me](./about-me)' (or whatever equivalent in the output
    format).
    '''
    if key == 'Link':
        attr, txt, urllst = value
        url = urllst[0]
        # For debugging
        #with open('log.txt', 'w') as f:
        #    f.write(str(value) + "\n")
        #    f.write("txt: " + str(txt) + "\n")
        #    f.write("url: " + str(url) + "\n")
        #    f.write("attr: " + str(attr) + "\n")
        if url == "!w":
            url = "https://en.wikipedia.org/wiki/" + stringify(txt)
        elif url.startswith("!w%20"):
            url = "https://en.wikipedia.org/wiki/" + url[len("!w%20"):]
        elif url == "!wja":
            url = "https://ja.wikipedia.org/wiki/" + stringify(txt)
        elif url.startswith("!wja%20"):
            url = "https://ja.wikipedia.org/wiki/" + url[len("!wja%20"):]
        elif url.startswith("!"):
            url = "http://duckduckgo.com/?q=" + url + " " + stringify(txt)
        elif url == '':
            # So we want to internally link txt
            url = slug(stringify(txt))
            url = "./" + url
        urllst = [url, urllst[1]]
        return Link(attr, txt, urllst)
        #return Link(txt, [url, attr]) # old return, used for pandoc <=1.5

if __name__ == '__main__':
    toJSONFilter(url_filter)
