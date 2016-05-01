#!/bin/bash

git ls-tree -r --name-only HEAD | while read filename; do
    if [[ $filename == wiki/* ]] ;
    then
        title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
        echo "$(git log -1 --format="%ai" -- $filename) - [$title]($(basename $filename .md))"
    fi
done | sort -r | cut -d " " -f 4-
