---
title: Useful shell commands
author: Issa Rice
created: 2015-07-11
date: 2015-07-11
status: notes
---

Open all pages in `wiki/` containing `uw course review`:

``` {.bash}
vim --remote-tab-silent `grep "uw course review" wiki/* -l | tr '\n' ' '`
```
