---
title: rsync
author: Issa Rice
created: 2015-02-04
date: 2015-02-28
status: notes
belief: possible
---

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
