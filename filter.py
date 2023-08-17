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
args = parser.parse_args()


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


def process_markdown(metadata, body, contributors):
    authors = []
    affiliations = {}
    acknowledgements = []
    # parse metadata
    for key in metadata["author"]:
        author_metadata = contributors[key]
        author = key
        if "orcid" in author_metadata:
            author += rf" \orcidlinksimple{{{author_metadata['orcid']}}}"
        for affiliation in author_metadata.get("affiliations", []):
            if affiliation not in affiliations:
                affiliations[affiliation] = f"[^affiliation{len(affiliations) + 1}]"
            author += f"{affiliations[affiliation]}"
        authors.append(author)
        if "acknowledgements" in author_metadata:
            acknowledgements.append(author_metadata["acknowledgements"])
    # update Markdown metadata
    metadata["author"] = authors
    # rewrite Markdown file
    markdown = []
    markdown.append("---")
    markdown.append(yaml.dump(metadata, allow_unicode=True))
    markdown.append("---")
    markdown.append(body)
    markdown.append("## Acknowledgements")
    markdown += acknowledgements
    markdown += [f"{v}: {k}" for k, v in affiliations.items()]
    return "\n".join(markdown)


if __name__ == "__main__":
    with open(args.contributors) as f:
        contributors = get_contributors_metadata(f.read())
    with open(args.input) as f:
        metadata, body = get_manuscript_metadata(f.read())
    for key in metadata["author"]:
        assert key in contributors, f"author '{key}' {debuginfo} in {args.input} not found in {args.contributors}"
    markdown = process_markdown(metadata, body, contributors)
    if args.output:
        with open(args.output, "w") as f:
            f.write(markdown)
    else:
        print(markdown)
