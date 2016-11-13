# Source for issarice.com

This repository hosts the files needed to compile my website,
<https://issarice.com>.  The website is compiled from a set of (mainly) markdown
files using Pandoc and a Makefile. Assuming one has the prerequisites to compile
the site (Pandoc ≥1.17.1 with [pandocfilters][pf] ≥1.4.0 and GNU Make)
just do from the shell:

    # cd to the repo directory
    make fullsite

This will generate all resulting files under `_site`, which can be browsed
locally or be served on the site with:

    rsync -r --delete _site/ destination_directory/

Note that in the interest of [Cool URIs][cool], the compiled files have no file
extensions (which would usually be `.html`).  Therefore simply opening the files
in your browser may not work as expected.  (Firefox and Chrome can figure out
that the file is still an HTML, but for instance Elinks seems to have
trouble—though on Elinks specifically you can hit `\` to force it to render as
HTML.)

Note also that since the Markdown files in this repository use Pandoc's
Markdown, they do not render correctly on GitHub.
Any MediaWiki files in this repository will render incorrectly on GitHub as
well, because they use special templates that are only available on some
MediaWiki installations (such as the English Wikipedia).

[cool]: http://www.w3.org/TR/cooluris/
[pf]: https://github.com/jgm/pandocfilters
