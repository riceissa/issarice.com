---
title: Colophon
author: Issa Rice
creation_date: 2015-08-31
date: 2015-08-31
---

Here are the tools used to build and run this site.

Most pages are written using [Vim](http://www.vim.org/) using the [Pandoc markdown syntax](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown).
The markdown files are then compiled to HTML using Pandoc and a Makefile.

The [style sheet for this site](https://github.com/riceissa/issarice.com/blob/master/css/solarized_light.css) uses the [Solarized](http://ethanschoonover.com/solarized) light theme by [Ethan Schoonover](http://ethanschoonover.com/) for some of the body text,[^bodytext] background, and colors.
Other aspects of the style sheet are inspired by [gitit](http://gitit.johnmacfarlane.net/), [Gwern’s site](http://www.gwern.net/About#tools) and GitHub’s (old) documentation pages.

All of the source files necessary to build this site are hosted on GitHub.
You can [visit the repository](https://github.com/riceissa/riceissa.com) on GitHub.
I also have a [mirror on BitBucket](https://bitbucket.org/riceissa/issarice.com/) (which is often behind, and should not be relied on).

The actual site is served via [Linode](https://www.linode.com/), using Nginx on a 64-bit Debian 8 (Jessie) machine.
I currently use the [Linode 1GB \$10 per month plan](https://www.linode.com/pricing).

I have registered the domains [issarice.com](http://issarice.com) and [riceissa.com](http://riceissa.com) through [Hover](https://www.hover.com/).

[^bodytext]: The main body text color was made darker due to a request made by a friend.
