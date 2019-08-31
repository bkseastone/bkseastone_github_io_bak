SHELL = /bin/bash
FLAG = --standalone --toc --toc-depth=2 --mathjax --metadata last_modified="`date +%FT%TZ`"
SRC = src
DST = html
CSS = style.css
TEMPLATE = template.yaml
MD = $(notdir $(wildcard $(SRC)/*.md))
HTML = $(patsubst %.md, %.html, $(MD))

all: $(HTML) 
%.html: $(SRC)/%.md $(TEMPLATE) $(CSS)
	@echo Converting $< to $@
	@pandoc $(TEMPLATE) $< -f markdown --css $(CSS) -t html $(FLAG) -o $(DST)/$@
clean:
	rm $(HTML)
