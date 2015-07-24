---
title: Useful shell commands
#rss_description: 
author: Issa Rice
creation-date: 2015-07-11
last-major-revision-date: 2015-07-11
language: English
# Possible values are "notes", "draft", "in progress", and
# "mostly finished"
status: notes
# Possible values are "certain", "highly likely", "likely", "possible",
# "unlikely", "highly unlikely", "remote", "impossible", "fiction", and
# "emotional"
#belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: vim, bash, linux, command line
#aliases: 
---

Open all pages in `wiki/` containing `uw course review`:

``` {.bash}
vim --remote-tab-silent `grep "uw course review" wiki/* -l | tr '\n' ' '`
```
