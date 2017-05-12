#!/bin/sh

cat <<EOF > _site/sitemap.xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
EOF

for file in wiki/*
    do cat <<EOF  >> _site/sitemap.xml
<url>
  <loc>https://issarice.com/$(basename $file .md)</loc>
  <changefreq>weekly</changefreq>
</url>
EOF
done

echo '</urlset>' >> _site/sitemap.xml
