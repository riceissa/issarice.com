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

[cool]: http://www.w3.org/TR/cooluris/
[pf]: https://github.com/jgm/pandocfilters
