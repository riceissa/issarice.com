---
title: rsync
#description: 
author: Issa Rice
created: 2015-02-04
date: 2015-02-28
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: linux
aliases: some-rsync-commands
---

For deploying my site:

```bash
# run from the root of the git repository
alias deploy='git push origin master && git push bitbucket master && time python3 generator/generator.py && rsync -e ssh -r --delete _site/ server:destination/'
```


For syncing a PDF to my site; use with `uppdf FILENAME`:

```bash
uppdf() {
    rsync --ignore-existing -vv $1 server:destination/
}
```

Backup Linode:

```bash
rsync -avz server:/var/www/ var/
```
