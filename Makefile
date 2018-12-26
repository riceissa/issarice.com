OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,$(OUTDIR)/%,$(MD_PAGES))
IMAGES = $(wildcard images/*)
IMAGES_DEST = $(patsubst images/%,$(OUTDIR)/%,$(IMAGES))
STATIC_FILES = $(wildcard static/*)
STATIC_DEST = $(patsubst static/%,$(OUTDIR)/%,$(STATIC_FILES))
SERVER_DEST = carbon:/var/www/issarice.com/public_html
PANDOC_FLAGS = -f markdown+smart -t html5 --base-header-level=2 --template=templates/default.html5 --include-in-header css/solarized_light.css -M today:$(shell date -Idate | tr -d '\n')

.PHONY: pages
pages: $(HTML_PAGES) $(IMAGES_DEST) $(STATIC_DEST) $(OUTDIR)/work $(OUTDIR)/account-names

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

$(OUTDIR):
	mkdir -p $(OUTDIR)

$(OUTDIR)/%: wiki/%.md templates/default.html5 | $(OUTDIR)
	pandoc $(PANDOC_FLAGS) --toc --toc-depth=4 --mathjax \
		--lua-filter generator/url_filter.lua \
		-M sourcefilename:"$<" \
		-M lastmodified:$(shell git log -1 --format="%ad" --date=format:"%Y-%m-%d" -- "$<" | tr -d '\n') \
		-o "$@.tempmjpage.html" "$<"
	mjpage --output CommonHTML < "$@.tempmjpage.html" > "$@"
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
