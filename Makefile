OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,$(OUTDIR)/%,$(MD_PAGES))
IMAGES = $(wildcard images/*)
IMAGES_DEST = $(patsubst images/%,$(OUTDIR)/%,$(IMAGES))

.PHONY: pages
pages: $(HTML_PAGES) $(IMAGES_DEST)

.PHONY: fullsite
fullsite: pages $(OUTDIR)/sitemap.xml $(OUTDIR)/_all $(OUTDIR)/_all_date

$(OUTDIR)/_all: $(MD_PAGES) generator/all_pages.sh | $(OUTDIR)
	./generator/all_pages.sh | \
	pandoc -f markdown -t html5 --smart \
		--base-header-level=2 --template=templates/default.html5 \
		-M title:"List of all pages on this site" \
		-o "$@"

$(OUTDIR)/_all_date: $(MD_PAGES) generator/all_date_pages.sh | $(OUTDIR)
	bash ./generator/all_date_pages.sh | \
		pandoc -f markdown -t html5 --smart \
		--base-header-level=2 --template=templates/default.html5 \
		-M title:"List of pages sorted by date of last substantive revision" \
		-o "$@"

$(OUTDIR)/sitemap.xml: $(MD_PAGES) generator/sitemap.sh | $(OUTDIR)
	./generator/sitemap.sh

$(OUTDIR):
	mkdir -p $(OUTDIR)

$(OUTDIR)/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc -f markdown -t html5 --smart --toc --toc-depth=4 --mathjax \
		--base-header-level=2 --template=templates/default.html5 \
		--filter generator/url_filter.py \
		-M sourcefilename:"$<" \
		-o "$@" "$<"

$(OUTDIR)/%: images/% | $(OUTDIR)
	cp "$<" "$@"

$(OUTDIR)/%: static/% | $(OUTDIR)
	cp "$<" "$@"

.PHONY: clean
clean:
	rm -rf $(OUTDIR)
