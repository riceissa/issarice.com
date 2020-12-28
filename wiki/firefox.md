---
title: Firefox
author: Issa Rice
created: 2015-08-18
date: 2019-02-10
---

As of February 2019, Firefox is the main web browser I use.
I find it slower than Google Chrome (which I use for
[Facebook](facebook), Messenger, Gmail, and YouTube),
but find its address bar more useful.

# Extensions

- Citewebgen (this is a rough draft addon I made for myself, to avoid
  the [bookmarklet blocking](https://github.com/riceissa/citewebgen#caveats) on some sites)
- Decentraleyes
- Don't track me Google (this removes link conversion on google search result pages, so that right-clicking on a search result will give the actual URL, rather than google's obfuscated URL)
- Make Medium Readable Again
- Nitter Redirect
- Read Aloud: A Text to Speech Voice Reader
- Save To The Wayback Machine
- SingleFile
- Tampermonkey
- uBlacklist: custom domain blacklist for Google search results
- uBlock Origin
- uMatrix
- Web Developer (for viewing the generated HTML source)
- Zotero Connector (I don't actually use this nowadays...)

Due to the Firefox 57 upgrade, several of the plugins I used to use were marked as "Legacy" and are not usable.
In particular, NoScript was at first unavailable, then available under
the new extensions system in a new form. I didn't like the new
interface so I switched to uMatrix.

# Keyword search

I have several [custom keyword searches](https://www-archive.mozilla.org/docs/end-user/keywords.html "'How Cool are Custom Keywords?' by Asa Dotzler") on Firefox. Following DuckDuckGo's idea
of "bang expressions", I prefix each keyword with `!` (even though I don't use DuckDuckGo).

- `!g`: google search, `https://www.google.com/search?q=%s`
- `!w`: English Wikipedia, `https://en.wikipedia.org/w/index.php?search=%s&title=Special%3ASearch`
- `!d`: The Free Dictionary
- `!ia`: Internet Archive, `https://web.archive.org/web/*/%S`
- `!ias`: save with internet archive, `https://web.archive.org/save/%S`
- `!gooj`: goo jisho (Japanese dictionary), `https://dictionary.goo.ne.jp/freewordsearcher.html?MT=%s&mode=0&kind=all`

Note that for the Internet Archive keyword searches, use `%S` rather than `%s`
for the search string placeholder. The latter URL-encodes the search string
while the former doesn't.

I used to use bookmarklets, but have since switched to using an addon
(for citation generation) and keyword searches (for accessing
websites).

# Settings

In `about:config`:

- Set `network.IDN_show_punycode` to `true`

# See also

* [Software]() for more about the software I use
