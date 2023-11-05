.DEFAULT_GOAL := all

objects := intro.pdf competencies.pdf institutionalised_education.pdf survey.pdf call_to_action.pdf

all: $(objects)

%.pdf: %.md bibliography.bib contributors.yml preamble.sty
	@mkdir -p build
	cp --update preamble.sty build/bookmark.sty
	python3 filter.py --input="$<" --output="build/$<" --contributors="contributors.yml"
	pandoc -V papersize:a4 -s -N --filter pandoc-xnos --bibliography=bibliography.bib --biblatex -M date="`date "+%B %e, %Y"`" -V colorlinks=true --toc -o "build/${@:.pdf=}.tex" "build/$<"
	sed -i 's|\\addbibresource{bibliography.bib}|\\addbibresource{../bibliography.bib}|' "build/${@:.pdf=}.tex"
	latexmk -xelatex -bibtex -halt-on-error -jobname="${@:.pdf=}" -cd "build/${@:.pdf=}.tex"
	@mv "build/${@}" ${@}

clean:
	rm -f $(objects)
