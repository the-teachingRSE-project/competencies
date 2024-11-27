.DEFAULT_GOAL := all

MAKE_PDFA := true

objects := competencies.pdf summarised_competencies.pdf

all: $(objects)

%.pdf: %.md bibliography/bibliography.bib contributors.yml preamble.sty build/template.tex glossary.tex filter.py Makefile
	@mkdir -p build
	@mkdir -p build/svg-inkscape
	@rm -f build/pdfa.xmpi
	cp --update preamble.sty build/
	cp --update bibliography/bibliography.bib build/
	cp --update glossary.tex build/
	python3 filter.py --input="${<}" --output="build/${<}" --contributors="contributors.yml"
	pandoc \
	    --standalone \
	    --number-sections \
	    --filter pandoc-xnos \
	    --bibliography=bibliography.bib \
	    --biblatex \
	    --toc \
	    --template="build/template.tex" \
	    -f markdown-latex_macros \
	    -M pdfa-$(MAKE_PDFA)=1 \
	    -M date="`date "+%F"`" \
	    -M datexmp="`date "+%F"`" \
	    -M linkcolor=darkgray \
	    -V hyperrefoptions=pdfa \
	    -V colorlinks=true \
	    -V papersize=a4 \
	    -o "build/${@:.pdf=}.tex" \
	    "build/$<"
	@sed -i '/\\author{}/d' "build/${@:.pdf=}.tex"
	@sed -ri 's/(\\label\{[a-zA-Z0-9_:-]+\})\}\1/\1}/' "build/${@:.pdf=}.tex"
	if grep -q "\\makeglossaries" "${<}"; then \
		cd build; \
		pdflatex -shell-escape --jobname="${@:.pdf=}" "${@:.pdf=}.tex"; \
		makeglossaries "${@:.pdf=}"; \
	fi
	latexmk \
	    -pdflatex -shell-escape -bibtex -halt-on-error \
	    -jobname="${@:.pdf=}" -cd "build/${@:.pdf=}.tex"
	@mv "build/${@}" "${@}"

build/template.tex: template.py
	@mkdir -p build
	pandoc --print-default-template=latex > "${@}"
	python3 "${<}" "${@}"

clean:
	rm -f $(objects)
