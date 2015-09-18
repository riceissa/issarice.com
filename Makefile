OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,_site/%,$(MD_PAGES))
CSS = $(OUTDIR)/_css/solarized_light.css
CSSDIR = _site/_css

# Make only regular pages
pages: $(HTML_PAGES) $(CSS) $(CSSDIR)

# Make the full site, including pages, images, static content, tags
# pages, feeds, and sitemap
fullsite:
	./generator/generator.py --commit_ps

$(CSSDIR):
	mkdir -p $(CSSDIR)

_site/%: wiki/%.md
	./generator/generator.py --commit_ps --file "$<"

$(OUTDIR)/_css/solarized_light.css: css/solarized_light.scss css/_colors.scss | $(CSSDIR)
	sass --style compressed "$<" > "$@"

clean:
	rm -rf _site

# These are things that aren't implemented yet, and I'm not sure I would implement them
#tags:
#	# some specialized script here that just generates tags

#feeds:
#	# feed generation scripts
