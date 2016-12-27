---
title: rsync
author: Issa Rice
created: 2015-02-04
date: 2015-02-28
status: notes
belief: possible
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
