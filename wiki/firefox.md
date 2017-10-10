---
title: Firefox
author: Issa Rice
created: 2015-08-18
date: 2017-03-10
---

As of March 2017, Firefox is the main web browser I use.
I find it slower than Google Chrome (which I use for
[Facebook](facebook), Gmail, and /g/), but find its address bar and some
plugins more useful.

# Extensions

- Decentraleyes
- DOM Inspector
- HTTPS Everywhere
- It's All Text!
- NoScript
- Privacy Badger
- ScrapBook X
- uBlock Origin
- Ubuntu Modifications (came with Ubuntu)
- VimFx
- Web Developer (for viewing the generated HTML source)
- Zotero

Due to a recent Firefox upgrade, many of the plugins are now marked as
"Legacy".

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

-   "Cite md" (the [Markdown version of Citewebgen](https://github.com/riceissa/citewebgen/blob/master/citewebgen.js))

# Settings

In `about:config`:

- Set `network.IDN_show_punycode` to `true`

# See also

* [Software]() for more about the software I use
