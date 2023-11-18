"""
Edit a Markdown file based on an external metadata file.
Replace each author in the YAML header file by a LaTeX string
with full author information (name, affiliation(s), ORCID iD).
Add funding acknowledgements at the bottom of the manuscript.
"""

import yaml
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--input", type=str, required=True,
                    help="input Markdown file")
parser.add_argument("--output", type=str, required=False,
                    help="output Markdown file")
parser.add_argument("--contributors", type=str, required=False,
                    default="contributors.yml",
                    help="contributors YAML file")


def get_contributors_metadata(content):
    entries = yaml.safe_load(content)["authors"]
    dictionary = {entry["author"]: entry for entry in entries}
    assert len(entries) == len(dictionary), "duplicate keys found in YAML file"
    return dictionary


def get_manuscript_metadata(markdown):
    markdown = markdown.lstrip()
    assert markdown.startswith("---")
    markdown = markdown.split("\n", 1)[1]
    markdown = markdown.lstrip()
    metadata, body = markdown.split("\n---", 1)
    body = body.split("\n", 1)[1]
    return yaml.safe_load(metadata), body


def get_author_thanks(metadata):
    retval = {}
    for line in metadata["author"]:
        author, *thanks = [x.strip() for x in line.split("|")]
        retval[author] = thanks
    return retval


def process_markdown(metadata, body, contributors):
    authors_tex = []
    authors_xmp = []
    affiliations = {}
    acknowledgements = ["# Acknowledgements {- #sec:acknowledgements}"]
    bookkeeping_initials = {}
    author_thanks = get_author_thanks(metadata)
    # parse metadata
    for fullname, annotations in author_thanks.items():
        author_metadata = contributors[fullname]
        authors_xmp.append(fullname)
        author_tex = fullname
        if "orcid" in author_metadata:
            author_tex += f"\\texorpdfstring{{\\thinspace\\orcidlink{{{author_metadata['orcid']}}}}}{{}}"
        author_affil = []
        if annotations:
            author_affil.append("")
            for thanks in annotations:
                author_tex += f"\\texorpdfstring{{\\thanks{{{thanks}}}}}{{}}"
        for affiliation in author_metadata.get("affiliations", []):
            if affiliation not in affiliations:
                affiliations[affiliation] = f"{len(affiliations) + 1}"
            author_affil.append(affiliations[affiliation])
        authors_tex.append(f"\\author[{','.join(author_affil)}]{{{author_tex}}}")
        initials = author_metadata["initials"]
        assert initials not in bookkeeping_initials, f"initials '{initials}' collide with '{fullname}' and '{bookkeeping_initials[initials]}'"
        bookkeeping_initials[initials] = fullname
        if "acknowledgements" in author_metadata:
            message = author_metadata["acknowledgements"]
            assert initials in message, f"'{initials}' doesn't appear in the acknowledgements of '{fullname}'"
            acknowledgements.append(message)
    affiliations_tex = [f"\\affil[{key}]{{{affil}}}" for affil, key in affiliations.items()]
    # update Markdown metadata
    del metadata["author"]
    metadata["authorxmp"] = authors_xmp
    metadata["header-includes"].extend(authors_tex)
    metadata["header-includes"].extend(affiliations_tex)
    # rewrite Markdown file
    markdown = []
    markdown.append("---")
    markdown.append(yaml.dump(metadata, allow_unicode=True))
    markdown.append("---")
    token_appendix = "\n\\appendix\n"
    if token_appendix in body:
        body = body.replace(token_appendix, "\n\n" + "\n".join(acknowledgements) + "\n\n" + token_appendix, 1)
        markdown.append(body)
    else:
        markdown.append(body)
        markdown.append("")
        markdown.extend(acknowledgements)
    return "\n".join(markdown)


if __name__ == "__main__":
    args = parser.parse_args()
    with open(args.contributors) as f:
        contributors = get_contributors_metadata(f.read())
    with open(args.input) as f:
        metadata, body = get_manuscript_metadata(f.read())
    for key in get_author_thanks(metadata).keys():
        assert key in contributors, f"author '{key}' in {args.input} not found in {args.contributors}"
    markdown = process_markdown(metadata, body, contributors)
    if args.output:
        with open(args.output, "w") as f:
            f.write(markdown)
    else:
        print(markdown)
