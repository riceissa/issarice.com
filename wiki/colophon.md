---
title: Colophon
#description: 
#feed_description: 
author: Issa Rice
creation_date: 2015-08-31
last_major_revision_date: 2015-08-31
language: English
# Possible values are "notes", "draft", "in progress", and
# "mostly finished"
status: notes
# Possible values are "certain", "highly likely", "likely", "possible",
# "unlikely", "highly unlikely", "remote", "impossible", "fiction", and
# "emotional"
#belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC0
tags: site-info
#aliases: 
---

Here are the tools used to build and run this site.

Most pages are written using [Vim](http://www.vim.org/) using the [Pandoc markdown syntax](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).
For each page that was manually written, the source markdown file can be accessed by clicking “page source” at the top of that page.
The markdown files are then compiled to HTML using a static site generator I wrote, which is stored in [`generator.py`](https://github.com/riceissa/issarice.com/blob/master/generator/generator.py) in the repository[^ssglist].

The [style sheet for this site](https://github.com/riceissa/issarice.com/blob/master/css/solarized_light.scss) is written in [SASS](http://sass-lang.com/) and compiled to CSS.
It uses the [Solarized](http://ethanschoonover.com/solarized) light theme by [Ethan Schoonover](http://ethanschoonover.com/) for body text, background, and colors.
Other aspects of the style sheet are inspired by [gitit](http://gitit.johnmacfarlane.net/), [Gwern’s site](http://www.gwern.net/About#tools) and GitHub’s (old) documentation pages.

All of the source files necessary to build this site are hosted on GitHub.
You can [visit the repository](https://github.com/riceissa/riceissa.com) by clicking “website source” at the top of any page.
I also have a [mirror on BitBucket](https://bitbucket.org/riceissa/issarice.com/).

The actual site is served via [Linode](https://www.linode.com/), using Nginx on a 64-bit Debian 8 (Jessie) machine.
I currently use the [Linode 1GB \$10 per month plan](https://www.linode.com/pricing).

I have registered the domains [issarice.com](http://issarice.com) and [riceissa.com](http://riceissa.com) through [Hover](https://www.hover.com/).

[^ssglist]: Although the static site generator I wrote is freely licensed, I don't recommend that others use it (at least for now); it is somewhat of a hack that I put together to get some features I wanted working (but found lacking in other static site generators).
Instead, one can find a list of many static site generators [here](http://staticsitegenerators.net/).
