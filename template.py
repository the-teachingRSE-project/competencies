"""
Customize the default pandoc template used to generate PDF files.
"""

import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="pandoc template file")
args = parser.parse_args()

def substitute(content, old_text, new_text):
    assert old_text in content
    assert content.count(old_text) == 1
    return content.replace(old_text, new_text)

with open(args.file) as f:
    content = f.read()

# generate XMP data and make document PDF-A compliant
content = re.sub("\n *pdfcreator=\{[^\{\}]+\},?", "\n$if(pdfa-true)$\n$else$\g<0>\n$endif$\n", content)
content = substitute(content, r"\begin{document}", r"""
$if(pdfa-true)$
\begin{filecontents*}{\jobname.xmpdata}
\Author{$for(authorxmp)$$authorxmp$$sep$\sep $endfor$}
$if(title-meta)$
\Title{$title-meta$}
$endif$
$if(lang)$
\Language{$lang$}
$else$
\Language{English}
$endif$
$if(subject)$
\Subject{$subject$}
$endif$
$if(keywords)$
\Keywords{$for(keywords)$$keywords$$sep$\sep $endfor$}
$endif$
$if(datexmp)$
\Date{$datexmp$}
$endif$
\PublicationType{journal}
\end{filecontents*}

% PDF/A compliance with pdfx, must be loaded last (loads hyperref and xcolor)
\usepackage[a-3u]{pdfx}
$endif$

\begin{document}""")

# include packages that must be included before hyperref
content = substitute(content,
r"""\IfFileExists{bookmark.sty}{\usepackage{bookmark}}{\usepackage{hyperref}}""",
r"""\usepackage[bottom]{footmisc}
\IfFileExists{bookmark.sty}{\usepackage{bookmark}}{\usepackage{hyperref}}""")

# generate the abstract and keywords list
content = substitute(content, r"""$if(abstract)$
\begin{abstract}
$abstract$
\end{abstract}
$endif$""",
r"""$if(abstract)$
\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}
$elseif(keywords)$
\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}
$endif$
$if(abstract)$
\textbf{Abstract}: {$abstract$}
$endif$

$if(keywords)$
\textbf{Keywords}: {$for(keywords)$$keywords$$sep$, $endfor$}
$endif$
$if(abstract)$
\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}
$elseif(keywords)$
\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}
$endif$"""
)

content = substitute(content,
r"\printbibliography$if(biblio-title)$[title=$biblio-title$]$endif$",
r"\printbibliography[heading=bibintoc$if(biblio-title)$,title=$biblio-title$$endif$]"
)

content = substitute(content,
r"""
\tableofcontents
""",
r"""
$if(toc-baselinestretch)$\renewcommand{\baselinestretch}{$toc-baselinestretch$}\normalsize$endif$
\tableofcontents
$if(toc-baselinestretch)$\renewcommand{\baselinestretch}{1.0}\normalsize$endif$
"""
)

with open(args.file, "w") as f:
    f.write(content)
