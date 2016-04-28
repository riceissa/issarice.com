OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,_site/%,$(MD_PAGES))

# Make only regular pages
pages: $(HTML_PAGES) cpimages

cpimages:
	cp images/* $(OUTDIR)

$(OUTDIR):
	mkdir -p $(OUTDIR)

_site/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc -f markdown -t html5 --smart --toc --toc-depth=4 --mathjax --base-header-level=2 --template=templates/default.html5 --filter generator/url_filter.py -o "$@" "$<"

clean:
	rm -rf _site
