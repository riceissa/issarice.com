OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,_site/%,$(MD_PAGES))

.PHONY: pages
pages: $(HTML_PAGES) cpimages _site/sitemap.xml

.PHONY: cpimages
cpimages:
	cp images/* $(OUTDIR)

_site/sitemap.xml: $(MD_PAGES) generator/sitemap.sh
	sh generator/sitemap.sh

$(OUTDIR):
	mkdir -p $(OUTDIR)

_site/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc -f markdown -t html5 --smart --toc --toc-depth=4 --mathjax \
		--base-header-level=2 --template=templates/default.html5 \
		--filter generator/url_filter.py -o \
		"$@" "$<"

.PHONY: clean
clean:
	rm -rf _site
