.DEFAULT_GOAL := all

objects := intro.pdf competencies.pdf institutionalised_education.pdf survey.pdf call_to_action.pdf

all: $(objects)

%.pdf: %.md bibliography.bib contributors.yml preamble.sty
	@mkdir -p build
	cp --update preamble.sty build/bookmark.sty
	cp --update bibliography.bib build/bibliography.bib
	python3 filter.py --input="$<" --output="build/$<" --contributors="contributors.yml"
	pandoc \
	    --standalone \
	    --number-sections \
	    --filter pandoc-xnos \
	    --bibliography=bibliography.bib \
	    --biblatex \
	    --toc \
	    -M date="`date "+%B %e, %Y"`" \
	    -V colorlinks=true \
	    -V papersize=a4 \
	    -o "build/${@:.pdf=}.tex" \
	    "build/$<"
	latexmk \
	    -xelatex -bibtex -halt-on-error \
	    -jobname="${@:.pdf=}" -cd "build/${@:.pdf=}.tex"
	@mv "build/${@}" ${@}

clean:
	rm -f $(objects)
