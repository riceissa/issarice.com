# Source for issarice.com

This repository hosts the files needed to compile my website,
<http://issarice.com>.  The website is compiled from a set of (mainly) markdown
files using Pandoc and a Makefile. Assuming one has the prerequisites to
compile the site (Pandoc 1.17 with the Python
[pandocfilters](https://github.com/jgm/pandocfilters) and GNU Make) just do:

```bash
# cd to the repo directory
make fullsite
```

This will generate all resulting files under `_site`, which can
eventually be served on the site with:

```bash
rsync -r --delete _site/ destination_directory/
```

Note that in the interest of [Cool URIs], the compiled files have no
file extensions (which would usually be `.html`).  Therefore simply
opening the files in your browser may not work as expected.  (Firefox
and Chrome can figure out that the file is still an HTML, but for
instance Elinks seems to have trouble—though on Elinks specifically you
can hit `\` to force it to render as HTML.)

[Cool URIs]: http://www.w3.org/TR/cooluris/
