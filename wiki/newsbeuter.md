---
title: Newsbeuter
author: Issa Rice
date: 2016-10-26
---

I use [Newsbeuter][official] to read RSS and Atom feeds.
On a server, I have a cronjob that runs `newsbeuter -x reload`.
This is useful for archiving some sites that I don't regularly want to read.
On my local machine, I have a [smaller list of
URLs](https://issarice.com/urls.txt) that I regularly check.

My [dotfiles
repository](https://github.com/riceissa/dotfiles/blob/master/.newsbeuter/config)
contains my `~/.newsbeuter/config`.

[official]: http://newsbeuter.org/ "Newsbeuter: The Mutt of RSS Feed Readers"
