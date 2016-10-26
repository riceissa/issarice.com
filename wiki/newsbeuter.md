---
title: Newsbeuter
author: Issa Rice
date: 2016-10-26
---

I use [Newsbeuter][official] to read RSS and Atom feeds.

    browser firefox
    auto-reload yes
    suppress-first-reload yes
    #max-items 20

    bind-key ^R reload-all

    # use J and K for inter-feed navigation and j and k for smaller
    # movements
    unbind-key J
    unbind-key K
    bind-key J next-feed
    bind-key K prev-feed

    unbind-key j
    unbind-key k
    bind-key j down "all"
    bind-key k up "all"

    # quitting is like moving left and viewing items is like moving right
    unbind-key l
    bind-key l open
    unbind-key h
    bind-key h quit

    # modified from the default given at
    # http://newsbeuter.org/doc/newsbeuter.html#_configuring_colors
    color background          default   default
    color listnormal          default   default
    color listfocus           default   white
    color listnormal_unread   default   default
    color listfocus_unread    default   white
    color info                default   white
    color article             default   default

[official]: http://newsbeuter.org/ "Newsbeuter: The Mutt of RSS Feed Readers"
