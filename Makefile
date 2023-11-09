.DEFAULT_GOAL := all

MAKE_PDFA := true

ifeq ($(MAKE_PDFA),true)
  template_opts=--with-pdfx
  xelatex_opts=-shell-escape
else
  template_opts=
  xelatex_opts=
endif

objects := intro.pdf competencies.pdf institutionalised_education.pdf survey.pdf call_to_action.pdf

all: $(objects)

%.pdf: %.md bibliography.bib contributors.yml preamble.sty template.tex
	@mkdir -p build
	@rm -f build/pdfa.xmpi build/creationdate.lua build/creationdate.timestamp
	cp --update preamble.sty build/
	cp --update bibliography.bib build/
	python3 filter.py --input="$<" --output="build/$<" --contributors="contributors.yml"
	pandoc \
	    --standalone \
	    --number-sections \
	    --filter pandoc-xnos \
	    --bibliography=bibliography.bib \
	    --biblatex \
	    --toc \
	    --template="template.tex" \
	    -M date="`date "+%B %e, %Y"`" \
	    -M datexmp="`date "+%F"`" \
	    -V hyperrefoptions=pdfa \
	    -V colorlinks=true \
	    -V papersize=a4 \
	    -M mainfont="Linux Libertine O" \
	    -M sansfont="Linux Biolinum O" \
	    -M monofont="Linux Libertine Mono O" \
	    -o "build/${@:.pdf=}.tex" \
	    "build/$<"
	latexmk \
	    -e '$$'"hash_calc_ignore_pattern{'timestamp'} = '^';" \
	    -xelatex -bibtex -halt-on-error $(xelatex_opts) \
	    -jobname="${@:.pdf=}" -cd "build/${@:.pdf=}.tex"
	@mv "build/${@}" ${@}

template.tex: template.py
	pandoc --print-default-template=latex > "${@}"
	python3 "${<}" $(template_opts) "${@}"

clean:
	rm -f $(objects)
