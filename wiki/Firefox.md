---
title: Firefox
author: Issa Rice
created: 2015-08-18
date: 2022-05-10
---

As of May 2022, Firefox is the main web browser I use.
I find it slower than [[Chrome|Google Chrome]] (which I use for
[Facebook](facebook), Messenger, Gmail, and YouTube),
but find its address bar more useful.

# Extensions

Starting in 2021, I decided to reduce the number of extensions I use after
learning more about how little auditing goes on for browser extensions and
case-studies like The Great Suspender (where the original author sold it to
some sketchy people who then put in spyware, or something like that).

- ClearURLs
- uBlock Origin
- F.B Purity

(Above list is up-to-date as of 2023-07-26.)

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

* [[software I use]] for more about the software I use
