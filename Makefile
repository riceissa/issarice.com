OUTDIR = _site
IMAGES = $(wildcard images/*)
IMAGES_DEST = $(patsubst images/%,$(OUTDIR)/%,$(IMAGES))
STATIC_FILES = $(wildcard static/*)
STATIC_DEST = $(patsubst static/%,$(OUTDIR)/%,$(STATIC_FILES))
SERVER_DEST = carbon:/var/www/issarice.com/public_html
PANDOC_FLAGS = -f markdown+smart -t html5 --shift-heading-level-by=1 --template=templates/default.html5 -M toc-title:"Contents" -M today:$(shell date -Idate | tr -d '\n') -M lang:"en"

.PHONY: quick
quick:
	./generator/generate.py

.PHONY: pages
pages: wiki_pages non_wiki_pages

.PHONY: non_wiki_pages
non_wiki_pages: $(IMAGES_DEST) $(STATIC_DEST) $(OUTDIR)/work $(OUTDIR)/account-names $(OUTDIR)/portfolio

.PHONY: wiki_pages
wiki_pages:
	./generator/generate.py

.PHONY: fullsite
fullsite: meta_pages pages

.PHONY: meta_pages
meta_pages: $(OUTDIR)/atom.xml $(OUTDIR)/all-pages $(OUTDIR)/sitemap.xml

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

$(OUTDIR)/all-pages: generator/all_pages_table.sh | $(OUTDIR)
	./generator/all_pages_table.sh | \
		pandoc $(PANDOC_FLAGS) \
		--toc -o "$@"

$(OUTDIR)/sitemap.xml: generator/sitemap.sh | $(OUTDIR)
	./generator/sitemap.sh

$(OUTDIR)/atom.xml: generator/atom.sh | $(OUTDIR)
	./generator/feed.py > "$@"

$(OUTDIR)/portfolio: html/portfolio.html | $(OUTDIR)
	cp html/portfolio.html "$@"

$(OUTDIR):
	mkdir -p $(OUTDIR)

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
	rm -rf backlink_fragments
	rm -f link-graph.json backlinks.json
