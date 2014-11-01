---
title: About the site
description: site info, tools used to build the site
tags: site-info, general
creation-date: 2014-09-14
last-major-revision-date: 2014-09-14
license: CC0
...

## Philosophy

This site is my attempt to execute gwern's idea of [Long Content](http://www.gwern.net/About#long-content).
Inspired by [Vipul Naik](http://vipulnaik.com), I am also experimenting with the [tree structure](http://riceissa.com/content-creation-the-organization-and-dissemination-of-knowledge#the-tree-structure-of-a-website) of this site.


## Colophon

For the sake of transparency, we list below the tools used to run this site.

Most pages are written using [Vim](http://www.vim.org/) using the [Pandoc markdown syntax](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).
The source markdown file for each page can be accessed by clicking “page source” at the top of that page.
The markdown files are then compiled to HTML using [Hakyll](http://jaspervdj.be/hakyll/)[^hak], a static site generator[^ssglist] written in Haskell.

The CSS for this site is compressed by Hakyll, but the uncompressed version is available [here](https://github.com/riceissa/riceissa.com/blob/master/css/minimal.css); it uses [Ethan Schoonover](http://ethanschoonover.com/)’s light [solarized theme](http://ethanschoonover.com/solarized), as well as taking hints from various places like [Gwern’s site](http://www.gwern.net/About#tools) and GitHub’s documentation pages.

All of the source files necessary to build this site are hosted on GitHub.
You can visit the repository [here](https://github.com/riceissa/riceissa.com) or by clicking “website source” at the top of any page.

The actual site is served via [Linode](https://www.linode.com/), using Apache 2 on a 64-bit Debian 7 (Wheezy) machine.
I currently use the [Linode 1GB \$10 per month plan](https://www.linode.com/pricing).

I have registered the domains [riceissa.com](http://riceissa.com) and [issarice.com](http://issarice.com) through [Hover](https://www.hover.com/).

[^hak]: I should eventually write out the details of this, and explain what goes into the `site.hs` file.

[^ssglist]: A list of all static site generators can be found [here](http://staticsitegenerators.net/).

## Getting updates

Since the site's source code is hosted on GitHub, one can simply use GitHub's RSS for the master branch, available [here](https://github.com/riceissa/riceissa.com/commits/master.atom).
I tend to prefer incremental updates instead of massive updates, so most of the changes in there will be very insignificant (and probably not worth your time).
When I feel a page is "good enough", I will probably place a link to it on the front page, along with a possible status update on Facebook.
