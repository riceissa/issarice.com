#!/bin/bash

# See http://stackoverflow.com/a/246128/3422337
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sitedir="${scriptdir}/.."

echo "Enter URL for article."
echo -n "URL: "

read url

# See http://unix.stackexchange.com/a/103253

text=`wget -qO- "$url" | gawk -v IGNORECASE=1 -v RS='</title' 'RT{gsub(/.*<title[^>]*>/,"");print;exit}'`

pagepath="${sitedir}/wiki/articles-read.md"

if [ -f $pagepath ];
then
    echo "File $pagename exists.  Opening..."
    cat <<EOF >> $pagepath
---

[$text]($url)


EOF
    gvim --remote-tab-silent +"call GoToLastLine()" $pagepath
else
    echo "Creating $pagepath"
    cat <<EOF > $pagepath
---
title: Articles read
#rss-description: 
author: Issa Rice
creation-date: `date +'%Y-%m-%d'`
last-major-revision-date: `date +'%Y-%m-%d'`
language: English
# Possible values are "notes", "draft", "in progress", and
# "mostly finished"
#status: notes
# Possible values are "certain", "highly likely", "likely", "possible",
# "unlikely", "highly unlikely", "remote", "impossible", "fiction", and
# "emotional"
#belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: news, articles, links
#aliases: 
---

[$text]($url)


EOF
    # open with vim on the last line (if there is no existing session)
    # or in a new tab on an existing session (if possible)
    # Note that this requires GoToLastLine to be defined in .vimrc
    gvim --remote-tab-silent +"call GoToLastLine()" $pagepath
fi
