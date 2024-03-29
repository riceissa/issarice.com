#!/bin/bash
# License: CC0

# TODO: this is a hack
# All the sed, cut, and tr filters make me uncomfortable since they depend on
# certain bytes being in the right place (although my source files currently
# adhere to this restriction).  However, I still prefer this to the old
# solution of bringing in dependencies like PyYaml, parsing the whole header,
# and then generating date-dependent pages using that.

cat << EOF
---
title: All pages
created: 2017-11-11
bigtable: true
---

This is a list of all pages on this site ordered by the "last substantive
revision" date. The "last modified" date comes from version control
([Git](git)) and takes into account even insubstantial edits.

# Table

|Title|Last substantive revision|Last modified|Created|Belief|Completion status|
|------------------------------------------------|--------------|--------------|--------------|--------------|--------------|
EOF

# All the "git log" commands for each file are the bottleneck of computation,
# so that is the process we want to parallelize with GNU parallel.

{
git ls-tree -r --name-only HEAD | grep -e '^wiki/.*md' | \
    parallel --tag git log -1 --format="%ai" -- | while read line; do
        lastmodified=`echo "$line" | sed -n 's/[^\t]\+\t\([^ ]\+\) .*/\1/p'`
        filename=`echo "$line" | sed -n 's/\([^\t]\+\)\t.*/\1/p'`
        base=$(basename "$filename" .md)
        # title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
        title="$base"
        slug=`echo "$base" | slug`
        date=`grep -m 1 -e '^date: ' "$filename" | sed -n 's/^date: \(.*\)/\1/p'`
        created=`grep -m 1 -e '^created: ' "$filename" | sed -n 's/^created: \(.*\)/\1/p'`
        belief=`grep -m 1 -e '^belief: ' "$filename" | sed -n 's/^belief: \(.*\)/\1/p'`
        compstatus=`grep -m 1 -e '^status: ' "$filename" | sed -n 's/^status: \(.*\)/\1/p'`
        echo -e "$date\t$lastmodified\t$title\t$slug\t$created\t$belief\t$compstatus"
    done
} | sort -r | \
    sed -n 's/\([^\t]*\)\t\([^\t]\+\)\t\([^\t]\+\)\t\([^\t]\+\)\t\([^\t]*\)\t\([^\t]*\)\t\([^\t]*\)/|[\3](\4)|\1|\2|\5|\6|\7|/p'

cat <<EOF

# See also

- [Gwern.net metadata table](gwern-net-metadata-table)
EOF
