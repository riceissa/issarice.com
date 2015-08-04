#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Issa Rice

# This is free and unencumbered software released into the public
# domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

from pandocfilters import toJSONFilter, stringify, Link
from slugify import slugify_unicode
import commands as c

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
        [txt, [url, attr]] = value
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
            url = slugify_unicode(stringify(txt), to_lower=True)
            url = "./" + url
        return Link(txt, [url, attr])

if __name__ == '__main__':
    toJSONFilter(url_filter)
