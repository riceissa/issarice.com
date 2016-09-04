#!/bin/bash

cat << EOF
This is a list of pages on this site that have a "last substantive revision"
date, ordered by the date of last modification. Note that insubstantial are not
taken into account here; to see a more volatile list, see [List of all pages on
this site](_all).

EOF

grep -m 1 -e '^date: ' wiki/* | \
    sed -n 's/\([^:]\+\):date: \(.*\)/\2 \1/p' | \
    sort -r | \
    while read line; do
        # echo $line | filename=`sed -n 's/[^ ] \(.*\)/\1/p'`
        filename=`echo $line | sed -n 's/[^ ]\+ \(.*\)/\1/p'`
        # echo $filename
        title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
        base=$(basename $filename .md)
        date=`echo $line | sed -n 's/\([^ ]\+\) \(.*\)/\1/p'`

        # Write the actual markdown bullet
        echo "- [$title]($base), $date"
    done
