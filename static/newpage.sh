#!/bin/bash

# this dir must have a slash at the end
sitedir="/home/issa/projects/riceissa.com/"

echo -n "Title: "

read title

slug="$(echo -n "${title}" | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)"

pagename="${sitedir}pages/$slug.md"

if [ -f $pagename ];
then
    echo "File $slug.md exists"
else
    echo "Creating $pagename"
    echo "---" >> $pagename
    echo "title: $title" >> $pagename
    echo "description: " >> $pagename
    echo "author: Issa Rice" >> $pagename
    echo "creation-date: `date +'%Y-%m-%d'`" >> $pagename
    echo "last-major-revision-date: `date +'%Y-%m-%d'`" >> $pagename
    echo "language: English" >> $pagename
    # accepted: "draft", "public"
    echo "status: draft" >> $pagename
    # accepted: "CC BY", "CC0"
    echo "license: CC BY" >> $pagename
    echo "tags: untagged" >> $pagename
    echo -e "...\n\n" >> $pagename
    # open with vim on the last line
    vim + $pagename
fi
