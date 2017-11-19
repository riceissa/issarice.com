#!/bin/bash

cat /dev/stdin | \
    while read url; do
        # If URL is local, it is a relative link within my site
        if ! (echo "$url" | grep -E -q -e "^https?://"); then
            url="https://issarice.com/$url"
        fi
        # Keep following the URL with curl (-L). If the end result is a 200 OK
        # status code, then we are good to go; otherwise print the URL so we
        # know what to fix on the site.
        if ! (curl -L -s --head "$url" | grep -e '^HTTP\/' | tail -1 | grep -q '200'); then
            echo $url
        fi
    done
