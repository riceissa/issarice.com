---
title: About the site
description: site info, tools used to build the site
tags: site-info, general
creation-date: 2014-09-14
last-major-revision-date: 2015-01-14
license: CC0
aliases: about-this-site, site
---

*This page is about this site; for information about myself, see [About me]().*

# Philosophy

This site is my attempt to realize gwern's idea of [Long Content]().[^pess]
In particular, I strive to make all the pages' source human-readable (by writing pages in [Pandoc](http://johnmacfarlane.net/pandoc/) markdown), version-controlled (with git), and freely-licensed (all pages are at least CC-BY, with some in the public domain[^copy]; the [software used to make this site](#colophon) is all free software).
I also like to [release early, release often](https://en.wikipedia.org/wiki/Release_early,_release_often); I actually don't deploy the site as often, but I try to commit to the git repository often---so my site is the result of many incremental updates.

[^pess]: Of course, more pessimistically, [one could quote Scott Alexander](https://web.archive.org/web/20130118212124/http://raikoth.net/) about the reason many people have personal websites:

    > You know how if you're under the age of thirty you have to have a personal webpage with your name, your photo, your resume, and then a link to your blog or something like that?

[^copy]: So content will be copied, making the data safe.

Inspired by [Vipul Naik](http://vipulnaik.com), I am also experimenting with the [tree structure](./using-a-tree-structure-for-websites) of this site.


# Colophon

Here are the tools used to build and run this site.

Most pages are written using [Vim](http://www.vim.org/) using the [Pandoc markdown syntax](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).
For each page that was manually written, the source markdown file can be accessed by clicking “page source” at the top of that page.
The markdown files are then compiled to HTML using a static site generator I wrote, which is stored in [`generator.py`](https://github.com/riceissa/riceissa.com/blob/master/generator.py) in the repository[^ssglist].

The [style sheet for this site](https://github.com/riceissa/issarice.com/blob/master/css/minimal.scss) is written using [SASS](http://sass-lang.com/), then is compiled to CSS.
It uses [Ethan Schoonover](http://ethanschoonover.com/)’s light [solarized theme](http://ethanschoonover.com/solarized) as well as small ideas from various places like [Gwern’s site](http://www.gwern.net/About#tools) and GitHub’s (old) documentation pages.

All of the source files necessary to build this site are hosted on GitHub.
You can [visit the repository](https://github.com/riceissa/riceissa.com) by clicking “website source” at the top of any page.
I also have a [mirror on BitBucket](https://bitbucket.org/riceissa/issarice.com/).

The actual site is served via [Linode](https://www.linode.com/), using Apache 2 on a 64-bit Debian 7 (Wheezy) machine.
I currently use the [Linode 1GB \$10 per month plan](https://www.linode.com/pricing).

I have registered the domains [issarice.com](http://issarice.com) and [riceissa.com](http://riceissa.com) through [Hover](https://www.hover.com/).

[^ssglist]: Although the static site generator I wrote is freely licensed, I don't recommend that others use it (at least for now); it is somewhat of a hack that I put together to get some features I wanted working (but found lacking in other static site generators).
Instead, one can find a list of many static site generators [here](http://staticsitegenerators.net/).

# Getting updates

I have an [RSS feed](http://issarice.com/feed.xml) for this site.
For more ways to get updates, see [Feed]().
