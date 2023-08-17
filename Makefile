.DEFAULT_GOAL := all

all: call_to_action.pdf competencies.pdf institutionalized_education.pdf intro.pdf survey.pdf

%.pdf: %.md bibliography.bib
	pandoc -V papersize:a4 -s --bibliography=bibliography.bib --biblatex -M date="`date "+%B %e, %Y"`" -V colorlinks=true --toc -o "${@:.pdf=}.tex" "$<"
	latexmk -xelatex -bibtex -jobname="${@:.pdf=}" "${@:.pdf=}.tex"

clean:
	latexmk -c -bibtex -jobname=call_to_action
	latexmk -c -bibtex -jobname=competencies
	latexmk -c -bibtex -jobname=institutionalized_education
	latexmk -c -bibtex -jobname=intro
	latexmk -c -bibtex -jobname=survey
