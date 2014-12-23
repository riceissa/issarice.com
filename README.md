# Source for issarice.com

This repository hosts the files needed to compile my website,
<http://issarice.com>.  The website is compiled from a set of (mainly)
markdown files using a custom static site generator stored in
`generator.py` (which needs access to `classes.py`, `commands.py`,
`metadata.py`, and `tag_ontology.py`).  Assuming one has the
prerequisites to compile the site (Python,
[Jinja2](http://jinja.pocoo.org/),
[pandocfilers](https://github.com/jgm/pandocfilters/)), just
do:

~~~~bash
# cd to the repo directory
python generator.py
~~~~

This will generate all resulting files under `_site`, which are eventually
served on the site with:

```bash
rsync -r --delete _site/ destination_directory/
```

If you only want to compile some of the pages, you can use the `--files` or `-f` flag; for instance, if you only want to compile the pages that contain "at-the-university" in the filename (characteristic of my course review pages, which have the form "subject-number-at-the-university-of-washington.md"), you can do:

```bash
python generator.py --files pages/*at-the-university*
```

(Though keep in mind that this will do nothing about CSS, so this option is generally only useful when one is working on a subset of the pages and wants to view changes on them quickly.)

Note that in the interest of
[Cool URIs](http://www.w3.org/TR/cooluris/), the compiled files have no
file extensions (which would usually be `.html`).  Therefore simply
opening the files in your browser may not work as expected.
