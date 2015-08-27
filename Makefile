OUTDIR = _site
MD_PAGES = $(wildcard wiki/*.md)
HTML_PAGES = $(patsubst wiki/%.md,_site/%,$(MD_PAGES))
CSS = $(OUTDIR)/minimal.css $(OUTDIR)/common.css $(OUTDIR)/standard.css $(OUTDIR)/solarized_light.css $(OUTDIR)/solarized_dark.css

#all:
#	./generator/generator.py --commit_ps

#all: _site/index

all: $(HTML_PAGES) $(CSS)

#about-me: wiki/about-me.md
#	./generator/generator.py --commit_ps --file "$<"

_site/%: wiki/%.md
	./generator/generator.py --commit_ps --file "$<"

$(OUTDIR)/minimal.css: css/minimal.scss
	sass --style compressed "$<" > "$@"
$(OUTDIR)/common.css: css/common.scss
	sass --style compressed "$<" > "$@"
$(OUTDIR)/standard.css: css/standard.scss
	sass --style compressed "$<" > "$@"
$(OUTDIR)/solarized_light.css: css/solarized_light.scss
	sass --style compressed "$<" > "$@"
$(OUTDIR)/solarized_dark.css: css/solarized_dark.scss
	sass --style compressed "$<" > "$@"

clean:
	rm -rf _site
