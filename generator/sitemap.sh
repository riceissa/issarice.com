#!/bin/sh
# License: CC0

cat <<EOF > _site/sitemap.xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
EOF

# Download the slug command from https://github.com/riceissa/dotfiles/blob/master/.local/bin/slug

for file in wiki/*md
    do cat <<EOF  >> _site/sitemap.xml
<url>
  <loc>https://issarice.com/$(basename "$file" .md | slug)</loc>
  <changefreq>weekly</changefreq>
</url>
EOF
done

# These are the pages that are not wiki pages, so add them to the sitemap
# manually.
for path in all-pages work account-names portfolio
do
    cat <<EOF >> _site/sitemap.xml
<url>
  <loc>https://issarice.com/$path</loc>
  <changefreq>weekly</changefreq>
</url>
EOF
done

echo '</urlset>' >> _site/sitemap.xml
