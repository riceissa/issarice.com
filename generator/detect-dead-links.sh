#!/bin/bash

cat /dev/stdin | \
    while read url; do
        # Old way:
        # Keep following the URL with curl (-L). If the end result is a 200 OK
        # status code, then we are good to go; otherwise print the URL so we
        # know what to fix on the site.
        # if ! (curl -L -s --head "$url" | grep -e '^HTTP\/' | tail -1 | grep -q '200'); then

        # New way: use curl's --fail flag to actually download the document and
        # see if it works. This way works on some sites like Quora that always
        # return a 403 for header requests.
        if ! (curl -L --fail --silent -A 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0' -o /dev/null "$url"); then
            echo $url
        fi
    done
