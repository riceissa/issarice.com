OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,$(OUTDIR)/%,$(MD_PAGES))
IMAGES = $(wildcard images/*)
IMAGES_DEST = $(patsubst images/%,$(OUTDIR)/%,$(IMAGES))

.PHONY: pages
pages: $(HTML_PAGES) $(OUTDIR)/sitemap.xml $(IMAGES_DEST)

$(OUTDIR)/sitemap.xml: $(MD_PAGES) generator/sitemap.sh | $(OUTDIR)
	sh generator/sitemap.sh

$(OUTDIR):
	mkdir -p $(OUTDIR)

$(OUTDIR)/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc -f markdown -t html5 --smart --toc --toc-depth=4 --mathjax \
		--base-header-level=2 --template=templates/default.html5 \
		--filter generator/url_filter.py -o \
		"$@" "$<"

$(OUTDIR)/%: images/% | $(OUTDIR)
	cp "$<" "$@"

.PHONY: clean
clean:
	rm -rf $(OUTDIR)
