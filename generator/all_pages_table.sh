#!/bin/bash

cat << EOF
---
title: All pages
created: 2017-11-11
---

This is a list of pages on this site ordered by the "last substantive revision"
date.

|Title|Last substantive revision|Last modified|
|------------------------------------------------|--------------|--------------|
EOF

{
git ls-tree -r --name-only HEAD | grep -e '^wiki/' | \
    parallel --tag git log -1 --format="%ai" -- | while read line; do
        lastmodified=`echo "$line" | sed -n 's/[^\t]\+\t\([^ ]\+\) .*/\1/p'`
        filename=`echo "$line" | sed -n 's/\([^\t]\+\)\t.*/\1/p'`
        base=$(basename $filename .md)
        title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
        date=`grep -m 1 -e '^date: ' $filename | sed -n 's/^date: \(.*\)/\1/p'`
        echo -e "$date\t$lastmodified\t$title\t$base"
    done
} | sort -r | \
    sed -n 's/\([^\t]*\)\t\([^\t]\+\)\t\([^\t]\+\)\t\([^\t]\+\)/|[\3](\4)|\1|\2|/p'
