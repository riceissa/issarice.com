OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,$(OUTDIR)/%,$(MD_PAGES))
IMAGES = $(wildcard images/*)
IMAGES_DEST = $(patsubst images/%,$(OUTDIR)/%,$(IMAGES))
STATIC_FILES = $(wildcard static/*)
STATIC_DEST = $(patsubst static/%,$(OUTDIR)/%,$(STATIC_FILES))
SERVER_DEST = carbon:/var/www/issarice.com/public_html
PANDOC_FLAGS = -f markdown+smart -t html5 --shift-heading-level-by=2 --template=templates/default.html5 --include-in-header css/solarized_light.css -M today:$(shell date -Idate | tr -d '\n')

.PHONY: pages
pages: $(HTML_PAGES) $(IMAGES_DEST) $(STATIC_DEST) $(OUTDIR)/work $(OUTDIR)/account-names $(OUTDIR)/portfolio

.PHONY: fullsite
fullsite: $(OUTDIR)/atom.xml $(OUTDIR)/all-pages $(OUTDIR)/sitemap.xml pages

.PHONY: sync
sync:
	rsync --delete --exclude=_archive/ -r $(OUTDIR)/ $(SERVER_DEST)

.PHONY: push
push:
	git push origin master
	git push bitbucket master
	git push gitlab master

.PHONY: deploy
deploy:
	$(MAKE) fullsite
	$(MAKE) sync
	$(MAKE) push

.PHONY: fast_deploy
fast_deploy:
	$(MAKE) pages
	$(MAKE) sync
	$(MAKE) push

.PHONY: deploy_archive
deploy_archive:
	$(MAKE) clean
	$(MAKE) deploy
	$(eval hash := $(shell git rev-parse --verify HEAD))
	rsync -r $(OUTDIR)/ \
		$(SERVER_DEST)/_archive/$(shell date -Idate)-$(hash)

$(OUTDIR)/all-pages: $(MD_PAGES) generator/all_pages_table.sh | $(OUTDIR)
	./generator/all_pages_table.sh | \
		pandoc $(PANDOC_FLAGS) \
		--toc -o "$@"

$(OUTDIR)/sitemap.xml: $(MD_PAGES) generator/sitemap.sh | $(OUTDIR)
	./generator/sitemap.sh

$(OUTDIR)/atom.xml: $(MD_PAGES) generator/atom.sh | $(OUTDIR)
	./generator/atom.sh > "$@"

$(OUTDIR)/portfolio: html/portfolio.html | $(OUTDIR)
	cp html/portfolio.html "$@"

$(OUTDIR):
	mkdir -p $(OUTDIR)

# The one-liner with mjpage below is horrible but the idea is simple. If the
# page coming out of Pandoc has either \( or \[ in it, then there is a
# possibility that there is math on that page (because these are used as
# opening delimiters for MathJax); so run mjpage on that page to process the
# math. Otherwise, there is no chance for math to be on the page, so just copy
# whatever we got from Pandoc to the final destination.

$(OUTDIR)/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc $(PANDOC_FLAGS) --toc --toc-depth=4 --mathjax \
		--lua-filter generator/url_filter.lua \
		-M sourcefilename:"$<" \
		-M lastmodified:$(shell git log -1 --format="%ad" --date=format:"%Y-%m-%d" -- "$<" | tr -d '\n') \
		-o "$@.tempmjpage.html" "$<"
	if (grep -q -F '\(' "$@.tempmjpage.html" || grep -q -F '\[' "$@.tempmjpage.html"); then (echo "Has math so running mjpage..."; mjpage --output CommonHTML < "$@.tempmjpage.html" > "$@"); else (echo "No math so just copying page"; cp "$@.tempmjpage.html" "$@"); fi
	rm "$@.tempmjpage.html"

$(OUTDIR)/%: images/% | $(OUTDIR)
	cp "$<" "$@"

$(OUTDIR)/%: static/% | $(OUTDIR)
	cp "$<" "$@"

$(OUTDIR)/work: $(OUTDIR)/theme.default.css $(OUTDIR)/jquery.tablesorter.js $(OUTDIR)/jquery-latest.min.js generator/work.py | $(OUTDIR)
	./generator/work.py > "$@"

$(OUTDIR)/account-names: $(OUTDIR)/theme.default.css $(OUTDIR)/jquery.tablesorter.js $(OUTDIR)/jquery-latest.min.js generator/account_names.py data/online-presence.csv | $(OUTDIR)
	./generator/account_names.py > "$@"

.PHONY: clean
clean:
	rm -rf $(OUTDIR)
