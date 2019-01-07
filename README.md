# Source for issarice.com

This repository hosts the files needed to compile my website,
<https://issarice.com>.  The website is compiled from a set of (mainly)
markdown files using Pandoc and a Makefile. Assuming one has the prerequisites
to compile the site (see [build requirements](#build-requirements) below) just
do from the shell:

    make fullsite

This will generate all resulting files under `_site`, which can be browsed
locally or be served elsewhere with:

    rsync -r --delete _site/ destination_directory/

In the interest of [Cool URIs][cool], the compiled files have no file
extensions (which would usually be `.html`).  Therefore locally opening the files
in your browser may not work as expected.

Since the Markdown files in this repository use Pandoc's
Markdown, they do not render correctly on GitHub.
Any MediaWiki files in this repository will render incorrectly on GitHub as
well, because they use special templates that are only available on some
MediaWiki installations (such as the English Wikipedia).

## Build requirements

The following are the requirements to build the site:

- Pandoc ≥2.0
- GNU Make
- GNU Parallel (for `generator/all_pages_table.sh`)
- MySQL/MariaDB (for `work.py`)
- Python 3 (for `generator/account_names.py` and `generator/work.py`)
  - `mysql.connector` library (for `generator/work.py`)
- Bash (for some of the shell scripts in `generator/`)
- Some common command-line utilities like cat, sed, and so on (used in the
  shell scripts)
- mathjax-node-page (trying this out as a replacement for client-side MathJax rendering)

I have only ever tried building the site on Debian-based GNU/Linux systems, but since most of the site is just Markdown files it shouldn't be *too* hard to make the site build on other systems.

## Detecting broken links

Broken link detection is accomplished by two scripts:

- `generator/list_links.lua`, which finds all the links on the site
- `generator/detect-dead-links.sh`, which goes through the links and determines
  whether each is dead or not

Doing the following will work:

```bash
# Get all links
rm -f links.txt && \
    for filename in wiki/*; do
        pandoc -f markdown+smart -t html5 --mathjax "$filename" \
        --lua-filter generator/url_filter.lua \
        --lua-filter generator/list_links.lua \
        -o /dev/null >> links.txt
    done

# Go through the links and get the dead ones
cat links.txt | ./generator/detect-dead-links.sh > temp

sort -u temp > dead.txt && rm temp
```

## License

The content in this repository is variously licensed.

The vast majority of the files in `wiki/`, the main content directory, is
licensed under the [CC0 1.0 Universal Public Domain Dedication][cc0].
For all files in `wiki/`, if the YAML header does not have a `license` field,
it is CC0; otherwise whatever is in the `license` field gives the license.
When compiling the website, Pandoc uses `templates/default.html5` to perform
exactly this logic, so it might be easier to look at the bottom of the compiled
page.

For files in `external/` (which I use as a place to store contributions to
external sites), the license depends on whether I am the sole contributor.
If I am the sole contributor, it is CC0.
Otherwise, the license is whatever that is used on the destination site.
For instance, most of the files in `external/en.wikipedia.org/` are licensed
under the Creative Commons Attribution-ShareAlike License because that is what
the English Wikipedia uses and I often incorporate edits from others when
writing Wikipedia pages.

For files in `templates/`, everything except `default.html5` is CC0.
The file `default.html5` inherits from the [Pandoc template][pd_html5] (dual
licensed GPL v2 or higher or BSD 3-clause); the BSD 3-clause license is
reproduced below.

For `css/`, `solarized_light.css`, is MIT licensed because it uses
Solarized colors. The other files are CC0.

All the files in `images/` except `identification-photo.jpg` are CC0.
For the exception, I don't remember if the photographer has allowed me to
license it freely.

Everything in `generator/` is CC0. Since these are scripts that allow comments,
there should be a license line near the top of each.

Everything in `static/` except `anchor.min.js`, `jquery-latest.min.js`,
`jquery.tablesorter.js`, and `theme.default.css` is CC0. The exceptions are
variously licensed; you can look at the file for the license. For
`theme.default.css`, see my [tablesorter bare bones theme](https://github.com/riceissa/tablesorter-bare-bones-theme)
repository.

Everything in `data/` is CC0.

The files `.gitignore`, `Makefile`, `TODO.txt`, `page_reqs.txt`, as well as
this README file are CC0.

If the license of a particular file is unclear, please ask me.

```
This applies to templates/default.html5.

Copyright (c) 2014, John MacFarlane

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

    * Neither the name of John MacFarlane nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

[cc0]: https://creativecommons.org/publicdomain/zero/1.0/
[cool]: http://www.w3.org/TR/cooluris/
[pd_html5]: https://github.com/jgm/pandoc-templates/blob/master/default.html5
