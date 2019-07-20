SHELL = /bin/bash
CSS = ../style.css
FLAG = --standalone --toc --toc-depth=2 --mathjax --metadata last_modified="`date +%FT%TZ`"
SRC = src
OUT = html
TEMPLATE = template.yaml
MD = $(notdir $(wildcard $(SRC)/*.md))
HTML = $(patsubst %.md, %.html, $(MD))

all: $(HTML)
%.html: $(SRC)/%.md $(TEMPLATE) $(CSS)
	@echo Converting $< to $(OUT)/$@
	@pandoc $(TEMPLATE) $< -f markdown --css $(CSS) -t html $(FLAG) -o $(OUT)/$@

clean:
	rm $(HTML)
