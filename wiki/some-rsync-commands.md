---
title: Some rsync commands
description: 
author: Issa Rice
creation-date: 2014-12-08
last-major-revision-date: 2014-12-08
language: English
status: draft
license: CC BY
tags: untagged
---

For syncing a PDF to my site; use with `uppdf FILENAME`:

    uppdf() {
        rsync --ignore-existing -vv $1 issa@carbon:/var/www/exp/public_html/pdf/
    }
