#!/bin/bash
# License: CC0

cat << EOF
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title type="text">issarice.com</title>
  <updated>$(date -Iseconds)</updated>
  <author>
    <name>Issa Rice</name>
  </author>
  <id>https://issarice.com/</id>
  <link href="https://issarice.com/atom.xml" rel="self" type="application/atom+xml" />
  <link rel="alternate" type="application/rss+xml" hreflang="en" href="http://issarice.com/rss.xml" />
  <generator uri="https://github.com/riceissa/issarice.com/blob/master/generator/atom.sh">atom.sh</generator>
EOF

grep -m 1 -e '^date: ' wiki/* | \
    sed -n 's/\([^:]\+\):date: \(.*\)/\2 \1/p' | \
    sort -r | \
    sed 30q | \
    while read line; do
        # echo $line | filename=`sed -n 's/[^ ] \(.*\)/\1/p'`
        filename=`echo $line | sed -n 's/[^ ]\+ \(.*\)/\1/p'`
        # echo $filename
        title=`sed -n '2{p;q}' $filename | cut -c 8- | tr -d '"'`
        base=$(basename $filename .md)
        date=`echo $line | sed -n 's/\([^ ]\+\) \(.*\)/\1/p'`
        echo "  <entry>"
        echo "    <title>$title ($date)</title>"
        echo '    <link href="https://issarice.com/'"$base"'"/>'
        echo "    <id>tag:issarice.com,$date:/$base</id>"
        echo "    <updated>$date""T00:00:00$(date +'%:z')</updated>"
        echo '    <content type="html"><![CDATA['
        pandoc -f markdown+smart -t html5 --toc --toc-depth=4 --shift-heading-level-by=1 --lua-filter generator/url_filter.lua $filename
        echo "    ]]></content>"
        echo "  </entry>"

        # Write the actual markdown bullet
        # echo "- [$title]($base), $date"
    done
echo "</feed>"
