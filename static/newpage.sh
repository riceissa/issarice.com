#!/bin/bash

# this dir must have a slash at the end
sitedir="/home/issa/projects/riceissa.com/"

echo -n "Title: "

read title

slug="$(echo -n "${title}" | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)"
pagename="$slug.md"
pagepath="${sitedir}pages/$slug.md"

if [ -f $pagepath ];
then
    echo "File $pagename exists.  Opening..."
    vim $pagepath
else
    echo "Creating $pagepath"
    echo "---" >> $pagepath
    echo "title: $title" >> $pagepath
    echo "description: " >> $pagepath
    echo "author: Issa Rice" >> $pagepath
    echo "creation-date: `date +'%Y-%m-%d'`" >> $pagepath
    echo "last-major-revision-date: `date +'%Y-%m-%d'`" >> $pagepath
    echo "language: English" >> $pagepath
    # accepted: "draft", "public"
    echo "status: draft" >> $pagepath
    # accepted: "CC BY", "CC0"
    echo "license: CC BY" >> $pagepath
    echo "tags: untagged" >> $pagepath
    echo -e "...\n\n" >> $pagepath
    # open with vim on the last line
    vim + $pagepath
fi
