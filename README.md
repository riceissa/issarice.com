# riceissa.com

This repository hosts the files needed to compile my website,
<http://riceissa.com>.  The website is compiled from a set of (mainly)
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

Note that in the interest of
[Cool URIs](http://www.w3.org/TR/cooluris/), the compiled files have no
file extensions (which would usually be `.html`).  Therefore simply
opening the files in your browser may not work as expected.
