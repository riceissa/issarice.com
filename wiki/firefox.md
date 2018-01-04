---
title: Firefox
author: Issa Rice
created: 2015-08-18
date: 2017-12-05
---

As of March 2017, Firefox is the main web browser I use.
I find it slower than Google Chrome (which I use for
[Facebook](facebook), Gmail, and /g/), but find its address bar and some
plugins more useful.

# Extensions

- Decentraleyes
- HTTPS Everywhere
- Privacy Badger
- uBlock Origin
- uMatrix (I removed the 1st-party allow rules so that it behaves more like NoScript. On Chrome I have 1st-party enabled by default.)
- Web Developer (for viewing the generated HTML source)
- Zotero Connector

Due to the Firefox 57 upgrade, several of the plugins I used to use were marked as "Legacy" and are not usable.
In particular, NoScript was at first unavailable, then available under
the new extensions system in a new form. I didn't like the new
interface so I switched to uMatrix.

# Bookmarklets

Here are the bookmarklets I use:

-   "IA" (Internet Archive)

    ```
    javascript:void(window.open('https://web.archive.org/save/'+location.href))
    ```

-   archive.is

    ```
    javascript:void(open('https://archive.is/?run=1&url='+encodeURIComponent(document.location)))
    ```

-   "DOM" (dump the DOM in a new tab)

    ```
    javascript:(function(){var%20a=document.createElement("p");var%20b=document.createTextNode(document.documentElement.innerHTML.toString());a.appendChild(b);var%20c=window.open();c.document.body.appendChild(a)})();
    ```

-   [Citewebgen](https://github.com/riceissa/citewebgen/)

-   "Cite md" (the [Markdown version](https://github.com/riceissa/citewebgen/blob/master/markdown-part.js) of Citewebgen)

# Keyword search

I have several custom keyword searches on Firefox. Following DuckDuckGo's idea
of "bang expressions", I prefix each keyword with `!`.

- `!g`: google search
- `!w`: English Wikipedia
- `!yt`: YouTube (actually sound doesn't work on Firefox now ever since they
  dropped ALSA support, so I don't use this much now)
- `!d`: The Free Dictionary
- `!ia`: Internet Archive
- `!ias`: save with internet archive
- `!gooj`: yahoo jisho (japanese dictionary)

Note that for the internet archive keyword searches, use `%S` rather than `%s`
for the search string placeholder. The latter URL-encodes the search string
while the former doesn't.

# Settings

In `about:config`:

- Set `network.IDN_show_punycode` to `true`

# See also

* [Software]() for more about the software I use
