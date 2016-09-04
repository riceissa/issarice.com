#!/bin/bash
# grep -m 1 -e '^date: ' wiki/*
# grep -m 1 -e '^date: ' wiki/* | sed -n 's/\([^:]\+\):date: \(.*\)/\2 \1/p'
# grep -m 1 -e '^date: ' wiki/* | sed -n 's/\([^:]\+\):date: \(.*\)/\2 \1/p' | sort -r
grep -m 1 -e '^date: ' wiki/* | \
    sed -n 's/\([^:]\+\):date: \(.*\)/\2 \1/p' | \
    sort -r | \
    while read line; do
        # echo $line | filename=`sed -n 's/[^ ] \(.*\)/\1/p'`
        filename=`echo $line | sed -n 's/[^ ]\+ \(.*\)/\1/p'`
        # echo $filename
        title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
        echo -n '- ['
        echo -n $title
        # echo $title
        echo $line | sed -n 's/\([^ ]\+\) \(.*\)/](\2), \1/p'
    done
