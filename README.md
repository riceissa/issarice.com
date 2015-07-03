# Source for issarice.com

This repository hosts the files needed to compile my website,
<http://issarice.com>.  The website is compiled from a set of (mainly)
markdown files using a custom static site generator stored in the
directory `generator` (`generator.py` is the main file).  Assuming one
has the prerequisites to compile the site (Python 3.3, Pandoc 1.13,
[SASS], [Jinja2], [pandocfilers], [awesome-slugify], [PyYAML]; oddly I
have to install the Python packages for both Python 2 and Python 3),
just do:

```bash
# cd to the repo directory
python3 generator/generator.py --commit_ps
```

[SASS]: http://sass-lang.com/
[Jinja2]: http://jinja.pocoo.org/
[pandocfilers]: https://github.com/jgm/pandocfilters/
[awesome-slugify]: https://github.com/dimka665/awesome-slugify
[PyYAML]: http://pyyaml.org/wiki/PyYAML

(If you get `Python.h: No such file or directory compilation terminated`
when installing awesome-slugify, you might need to install `python-dev`
or `python3-dev`; see [the relevant StackOverflow answer][so a] for more.)

[so a]: http://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory

This will generate all resulting files under `_site`, which can
eventually be served on the site with:

```bash
rsync -r --delete _site/ destination_directory/
```

If you only want to compile some of the pages, you can use the `--files`
or `-f` flag; for instance, if you only want to compile the index page,
you can do:

```bash
python3 generator.py --files wiki/index.md
```

(Though keep in mind that this will do nothing about the CSS, sitemap,
RSS feed, or alias pages, so this option is generally only useful when
one is working on a subset of the pages and wants to view changes on
them quickly.  For instance, I have

```vim
:!python3 generator/generator.py --files %<CR><CR>
```

bound to a key in Vim so I can edit and preview
quickly.)

Note that in the interest of [Cool URIs], the compiled files have no
file extensions (which would usually be `.html`).  Therefore simply
opening the files in your browser may not work as expected.  (Firefox
and Chrome can figure out that the file is still an HTML, but for
instance Elinks seems to have trouble—though on Elinks specifically you
can hit `\` to force it to render as HTML.)

[Cool URIs]: http://www.w3.org/TR/cooluris/
