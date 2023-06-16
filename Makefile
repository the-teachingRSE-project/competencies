.DEFAULT_GOAL := output.pdf

output.pdf: paper_teaching-learning-RSE.md bibliography.bib
	pandoc -s --bibliography=bibliography.bib --biblatex -V colorlinks=true -o "${@:.pdf=}.tex" "$<"
	latexmk -xelatex -bibtex -jobname="${@:.pdf=}" "${@:.pdf=}.tex"

clean:
	latexmk -c -bibtex -jobname=output
