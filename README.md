# Source for issarice.com

This repository hosts the files needed to compile my website,
<https://issarice.com>.  The website is compiled from a set of (mainly) markdown
files using Pandoc and a Makefile. Assuming one has the prerequisites to compile
the site (Pandoc ≥1.17.1 with [pandocfilters][pf] ≥1.4.0 and GNU Make)
just do from the shell:

    make fullsite

This will generate all resulting files under `_site`, which can be browsed
locally or be served elsewhere with:

    rsync -r --delete _site/ destination_directory/

Note that in the interest of [Cool URIs][cool], the compiled files have no file
extensions (which would usually be `.html`).  Therefore locally opening the files
in your browser may not work as expected.

Note also that since the Markdown files in this repository use Pandoc's
Markdown, they do not render correctly on GitHub.
Any MediaWiki files in this repository will render incorrectly on GitHub as
well, because they use special templates that are only available on some
MediaWiki installations (such as the English Wikipedia).

## License

The content in this repository is variously licensed.

The vast majority of the files in `wiki/`, the main content directory, is
licensed under the [CC0 1.0 Universal Public Domain Dedication][cc0].
For all files in `wiki/`, if the YAML header does not have a `license` field,
it is CC0; otherwise whatever is in the `license` field gives the license.
When compiling the website, Pandoc uses `templates/default.html5` to do exactly
this logic, so it might be easier to look at the bottom of the compiled page.

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

The sole file in `css/`, `solarized_light.css`, uses the MIT license, which is
reproduced in the file.
If you want a more permissive CSS file without Solarized, see my
[document-templates][dt] repository (in particular, `default.css`).

All the files in `images/` except `identification-photo.jpg` are CC0.
For the exception, I don't remember if the photographer has allowed me to
license it freely.

Everything in `generator/` and `static/` is CC0.
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
[dt]: https://github.com/riceissa/document-templates
[pd_html5]: https://github.com/jgm/pandoc-templates/blob/master/default.html5
[pf]: https://github.com/jgm/pandocfilters
