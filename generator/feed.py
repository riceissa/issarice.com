#!/usr/bin/env python3

import datetime
import subprocess
import os
import sys

# Generates atom.xml and rss.xml

def slugify(s):
    '''
    "Slugify" the string s as follows: keep only the characters that are
    alphabetic or numerical, and group them together; all other characters are
    replaced by "-" and squeezed together.
    '''
    s = s.lower()
    s = "".join(c if (c.isalpha() or c.isdigit()) else "-" for c in s)
    s = "-".join(filter(bool, s.split("-")))
    return s




print("""<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet href="/feed.xsl" type="text/xsl"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title type="text">issarice.com</title>
  <updated>{}</updated>
  <author>
    <name>Issa Rice</name>
  </author>
  <id>https://issarice.com/</id>
  <link href="https://issarice.com/atom.xml" rel="self" type="application/atom+xml" />
  <link rel="alternate" type="application/rss+xml" hreflang="en" href="http://issarice.com/rss.xml" />
  <generator uri="https://github.com/riceissa/issarice.com/blob/master/generator/feed.py">atom.sh</generator>
""".format(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "+00:00"))

pages = []

for filename in os.listdir("wiki"):
    if filename.endswith(".md"):
        filepath = "wiki/" + filename
        date = None
        title = None
        # slug = slugify(filename)
        with open(filepath, "r") as f:
            yaml_opened = False
            for linenum, line in enumerate(f):
                if line.startswith("---") and len(set(line.strip())) == 1:
                    if linenum == 0:
                        # We see a yaml divider on the first line of the file,
                        # so consider the yaml block opened.
                        yaml_opened = True
                    else:
                        # This means we're seeing something that looks like a
                        # yaml divider, and it's not the start of the file. So
                        # either it's the "closing" divider, or else it's some
                        # random markdown horizontal rule. In either case, the
                        # yaml block (which should be at the start of the file)
                        # has ended, so we want to stop looking at this file.
                        break
                elif linenum > 0 and not yaml_opened:
                    # We didn't encounter a yaml starting divider on the first
                    # line, so assume there is no yaml block in this file.
                    break
                elif yaml_opened and line.startswith("title:"):
                    title = line[len("title:"):].strip().replace('"', '')
                elif yaml_opened and line.startswith("date:"):
                    date = line[len("date:"):].strip()
        if date:
            if not title:
                title = filename[:-len(".md")]
            pages.append({
                "title": title,
                "date": date,
                "filepath": filepath,
            })

pages = sorted(pages, key=lambda x: x['date'], reverse=True)[:30]
for page in pages:
    try:
        p = subprocess.run([
            "pandoc", "-f", "markdown+smart-implicit_header_references", "-t", "html5",
            "--toc", "--toc-depth", "4", "--shift-heading-level-by", "1",
            "--lua-filter", "generator/url_filter.lua",
            "--filter", "generator/wikilinks.sh",
            page['filepath'],
        ], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Error running pandoc:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()
    print(f"""  <entry>
    <title>{page['title']} ({page['date']})</title>
    <link href="https://issarice.com/{slugify(page['title'])}"/>
    <id>tag:issarice.com,{page['date']}:/{slugify(page['title'])}</id>
    <updated>{page['date']}T00:00:00+00:00</updated>
    <content type="html"><![CDATA[
        {p.stdout.decode("utf-8")}
    ]]></content>
  </entry>""")
print("</feed>")
