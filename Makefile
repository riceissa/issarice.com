OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,_site/%,$(MD_PAGES))
CSS = $(OUTDIR)/_css/solarized_light.css
CSSDIR = _site/_css

# Make only regular pages
pages: $(HTML_PAGES) $(CSS) $(CSSDIR) cpimages

cpimages:
	cp images/* $(OUTDIR)

$(CSSDIR):
	mkdir -p $(CSSDIR)

$(OUTDIR):
	mkdir -p $(OUTDIR)

_site/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc -f markdown -t html5 --smart --toc --toc-depth=4 --mathjax --base-header-level=2 --template=templates/default.html5 --filter generator/url_filter.py -o "$@" "$<"

$(OUTDIR)/_css/solarized_light.css: css/solarized_light.css | $(CSSDIR)
	cp "$<" "$@"

clean:
	rm -rf _site

# These are things that aren't implemented yet, and I'm not sure I would implement them
#tags:
#	# some specialized script here that just generates tags

#feeds:
#	# feed generation scripts
