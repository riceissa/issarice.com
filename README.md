# riceissa.com

This repository hosts the files needed to compile my website, <http://riceissa.com>.
The website is compiled using a custom static site generator stored in `generator.py`.
Assuming one has the prerequisites to compile the site (Python, Jinja2, pandocfilers), just do:

~~~~bash
mkdir _site
mkdir _site/tags
python generator.py
~~~~

This will generate all HTML files under `_site`, which are eventually served on the site.
Note that in the interest of [Cool URIs](http://www.w3.org/TR/cooluris/), the compiled files have no file extensions (which would usually be `.html`).
Therefore simply opening the files in your browser may not work as expected.
