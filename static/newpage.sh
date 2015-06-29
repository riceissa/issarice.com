#!/bin/bash

# See http://stackoverflow.com/a/246128/3422337
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sitedir="${scriptdir}/.."

echo "Enter title for entry.  Leave blank to use current date and time."
echo -n "Title: "

read title

isStatusUpdate=false
if [ "$title" == '' ]; then
    title=`date +"%F, %I:%M %p"`
    isStatusUpdate=true
fi

# You must have slug.py in the same directory as this script
slug="$(echo -n "${title}" | python ${scriptdir}/slug.py)"
pagename="$slug.md"
pagepath="${sitedir}/wiki/$slug.md"

if [ -f $pagepath ];
then
    echo "File $pagename exists.  Opening..."
    gvim --remote-tab-silent $pagepath
else
    echo "Creating $pagepath"
    cat <<EOF > $pagepath
---
title: $title
#rss-description: 
author: Issa Rice
creation-date: `date +'%Y-%m-%d'`
last-major-revision-date: `date +'%Y-%m-%d'`
language: English
# accepts "draft" or "finished"
status: draft
# accepts "log"
#belief: log
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
EOF
    if [ "$isStatusUpdate" = true ]; then
        echo "tags: status update" >> $pagepath
    else
        echo "tags: untagged" >> $pagepath
    fi
    cat <<EOF >> $pagepath
#aliases: 
---


EOF
    # open with vim on the last line (if there is no existing session)
    # or in a new tab on an existing session (if possible)
    # Note that this requires GoToLastLine to be defined in .vimrc
    gvim --remote-tab-silent +"call GoToLastLine()" $pagepath
fi
