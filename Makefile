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
	# various patches to the generated file
	@sed -i '/\\author{}/d' "build/${@:.pdf=}.tex"
	@sed -ri 's/(\\label\{[a-zA-Z0-9_:-]+\})\}\1/\1}/' "build/${@:.pdf=}.tex"
	# try to gain some space on the first page to avoid keywords appearing alone on the second page
	if [ "${@:.pdf=}" = competencies ]; then \
		sed -ri 's/^\\maketitle$$/\\maketitle\n\\vspace{-1em}/' "build/${@:.pdf=}.tex"; \
		python3 -c "import re,pathlib;p=pathlib.Path('build/${@:.pdf=}.tex');p.write_text(re.sub('.begin.center..rule.0.5.linewidth.+(?=\\n\\n.newpage)','',p.read_text(),flags=re.M))"; \
	fi
	# build glossary auxiliary files
	if grep -q "\\makeglossaries" "${<}"; then \
		cd build; \
		pdflatex -shell-escape --jobname="${@:.pdf=}" "${@:.pdf=}.tex"; \
		makeglossaries "${@:.pdf=}"; \
	fi
	latexmk \
	    -pdflatex -shell-escape -bibtex -halt-on-error -Werror \
	    -jobname="${@:.pdf=}" -cd "build/${@:.pdf=}.tex"
	@mv "build/${@}" "${@}"

build/template.tex: template.py
	@mkdir -p build
	pandoc --print-default-template=latex > "${@}"
	python3 "${<}" "${@}"

patch_pandocxnos:
	./patch_pandocxnos.sh

clean:
	rm -f $(objects)
