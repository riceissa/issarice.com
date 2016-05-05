#!/bin/bash

# TODO: this is a hack
# All the sed, cut, and tr filters make me uncomfortable since they depend on
# certain bytes being in the right place (although my source files currently
# adhere to this restriction).  However, I still prefer this to the old
# solution of bringing in dependencies like PyYaml, parsing the whole header,
# and then generating date-dependent pages using that.

echo "This is a list of all pages on this site, ordered by the date of last modification. Note that even insubstantial edits are taken into account when calculating the last modification date, so the ordering differs from the ordering obtained when sorting by the date when the last substantial edit was made on each page."
echo ""
{
    git ls-tree -r --name-only HEAD | while read filename; do
        if [[ $filename == wiki/* ]] ;
        then
            title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
            echo "$(git log -1 --format="%ai" -- $filename) - [$title]($(basename $filename .md))"
        fi
    done
} | sort -r | cut -d " " -f 4-
