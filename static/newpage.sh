#!/bin/bash

# See http://stackoverflow.com/a/246128/3422337
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sitedir="${scriptdir}/.."

echo -n "Title: "

read title

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
    echo "---" >> $pagepath
    echo "title: $title" >> $pagepath
    echo "#description: " >> $pagepath
    echo "author: Issa Rice" >> $pagepath
    echo "creation-date: `date +'%Y-%m-%d'`" >> $pagepath
    echo "last-major-revision-date: `date +'%Y-%m-%d'`" >> $pagepath
    echo "language: English" >> $pagepath
    echo '# accepts "notes", "draft", "in progress", or "mostly finished"' >> $pagepath
    echo "status: notes" >> $pagepath
    echo '# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"' >> $pagepath
    echo "belief: possible" >> $pagepath
    echo '# accepts "CC0", "CC-BY", or "CC-BY-SA"' >> $pagepath
    echo "license: CC-BY" >> $pagepath
    echo "tags: untagged" >> $pagepath
    echo "#aliases: " >> $pagepath
    echo -e "---\n\n" >> $pagepath
    # open with vim on the last line new a new tab on an existing session (if possible)
    gvim --remote-tab-silent +"call GoToLastLine()" $pagepath
fi
