"""
Customize the default pandoc template used to generate PDF files.
"""

import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="pandoc template file")
parser.add_argument("--with-pdfx", action="store_true", help="use pdfx")
args = parser.parse_args()

def substitute(content, old_text, new_text):
    assert old_text in content
    assert content.count(old_text) == 1
    return content.replace(old_text, new_text)

with open(args.file) as f:
    content = f.read()

# generate XMP data and make document PDF-A compliant
if args.with_pdfx:
    content = re.sub("\n *pdfcreator=\{[^\{\}]+\},?", "\n", content)
    content = substitute(content, r"\begin{document}", r"""
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

\begin{document}""")

with open(args.file, "w") as f:
    f.write(content)
