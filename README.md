# The teachingRSE project: "Teaching and Learning Research Software Engineering" [![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)

It started all at a workshop at deRSE23 in Paderborn where the community came together to discuss what to teach to future RSEs
and in which institutions to bring up the next generation of RSEs.

As we discovered, the scope of this task is so big that 
we had to split the paper in different subpapers highlighting different aspects

Get the latest version of the respective PDF files here:

* "Foundational competencies and responsibilities of an RSE" ([competencies.pdf](https://github.com/CaptainSifff/paper_teaching-learning-RSE/blob/build/competencies.pdf))
* "Institutionalized Organisation of RSE Education" ([institutionalised_education.pdf](https://github.com/CaptainSifff/paper_teaching-learning-RSE/blob/build/institutionalised_education.pdf))
* A separate web project on surveying and curating existing resources, the [learn-and-teach project](https://github.com/DE-RSE/learn-and-teach)  [website](https://de-rse.org/learn-and-teach/)
* "A Survey of Initiatives Providing Educative Material in the RSE Space" ([survey.pdf](https://github.com/CaptainSifff/paper_teaching-learning-RSE/blob/build/survey.pdf))
* "Educating RSEs in Germany - What Needs to Be Done" ([call_to_action.pdf](https://github.com/CaptainSifff/paper_teaching-learning-RSE/blob/build/call_to_action.pdf))

## How to contribute - Some of our rules

This paper is intended as a collaborative effort and we are looking for input from you.

**We follow GitLab/GitHub flow**

**Please utilise semantic line breaks!**

**We use British English**

**We have regular meetings, out meeting notes can be found here: https://pad.gwdg.de/s/pVBQ3Sh7Z#**

**If you want to get notified of our calls, and participate in the discussion by E-Mail, we have a Mailing-List: https://lists.uni-wuerzburg.de/mailman/listinfo/teachingrse**

- competencies.md will be published on arxiv. LaTeX tags/code is fine in here.
- survey.md will move to a website, hence this file has to be Markdown
- We utilise tags to categorise issues and PRs to the respective paper.

You can contribute in various ways:

1. Propose content/text via pull request
1. Improve existing content via pull request
1. Review or comment on pull requests of others

To build the PDF files, we recommend a full TeXlive installation.
You will also need to install a few Python packages:

```sh
python3 -m pip install -r requirements.txt
```

### How to create a pull request

- Fork this repository
- Create your changes in your fork
- Go to the [pull requests](https://github.com/CaptainSifff/paper_teaching-learning-RSE/pulls) page of this repository and push `new pull request`
- You can add DRAFT, or WIP to indicate work-in-progress PRs.
- Add a short description

The community will review your pull request and may ask you for additional changes.
If you have any questions, please don't hesitate to ask (we are trying to be as
helpful as possible).

#### How to review existing pull requests

- Go to the [pull requests](https://github.com/CaptainSifff/paper_teaching-learning-RSE/pulls) page of this repository
- Click on any of the open pull requests
- Leave comments under `Conversation` or do a full review under `Files changed`

#### How to get credit

If you've contributed to this paper in any way, please add your name to
[contributors.yml](contributors.yml) using the template at the bottom
of the file. Make sure the name provided in the "author:" field matches
exactly with the name in the Markdown preamble author list.

## Publication
We currently have split the topic of teaching RSEs in Germany across four papers.
We aim for a publication of most of these papers.
All people that have participated in discussions with us,
e.g. at deRSE23 or undeRSE23 are at least eligible for contributor status.
If you have participated regularly at our weekly working meetings you are eligible for
authorship.

The first paper,
_Foundational Competencies and Responsibilities of a Research Software Engineer_,
is now available as a pre-print: https://arxiv.org/abs/2311.11457
Feedback is welcome as an issue on this repository.

## License

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

Each file in this repository is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

When re-using material from this repository, please attribute it with the information given in the file [attribution.md](attribution.md).
