.DEFAULT_GOAL := output.pdf

output.pdf: paper_teaching-learning-RSE.md bibliography.bib
	pandoc -V papersize:a4 -s --bibliography=bibliography.bib --biblatex -M date="`date "+%B %e, %Y"`" --toc -o "${@:.pdf=}.tex" "$<"
	latexmk -xelatex -bibtex -jobname="${@:.pdf=}" "${@:.pdf=}.tex"

clean:
	latexmk -c -bibtex -jobname=output
