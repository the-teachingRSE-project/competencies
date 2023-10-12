---
title: "Teaching and Learning Research Software Engineering"
geometry: margin=2.5cm
author:
  - Heidi Seibold
  - Florian Goth
  - Jan Linxweiler
  - Jan Philipp Thiele
  - Jeremy Cohen
  - Renato Alves
  - Samantha Wittke
  - Jean-Noël Grad
  - Fredo Erxleben
  - Magnus Hagdorn
  - Harald von Waldow
  - Moritz Schwarzmeier
  - Matthias Braun
output:
  pdf_document:
    citation_package: biblatex
    toc: true
    number_sections: true
bibliography: bibliography.bib
---

**Abstract**:
Being an outcome of a community workshop held in Paderborn, Germany in February 2023 this paper tries 
for the first time(FIXME: ? true?) to define which competencies are required to participate in modern digital sciences.
Some of these competencies are required in more depth, therefore, giving rise to the trade of the RSE:
scientific personnel that specializes in writing research software that facilitates work in all stages of the research cycle.
Due to their generality, these competencies are often shared between RSE specializations,
and we believe they are also relevant for domains outside of the RSE community.

But knowing a set of competencies is not enough, therefore we discuss explicitly how to make people aware that these skills are
required and how these are taught(FIXME: Do we want to add this pedagogical dimension?).
In order to also facilitate structural change in the German research institution landscape
we will discuss the organizations and structures that support this change and educate new RSEs.
The discussion in this paper is meant to be general. Therefore, we will discuss domain specific applications in an appendix.

---

**Keywords**: research software engineering, training, learning, competencies

## Introduction
- background
    - RSEs have been around for a long time but the name is new.
    - RSEs have a specialist skill set that brings together technical and research knowledge.
    - Skills development traditionally provided largely through peer learning, self learning, introductory training courses not targeted specifically at RSEs, ...
    - Requirements for RSE skills growing rapidly across all domains.
- past attempts, other initiatives
- contributions

Computers and software have played a key role in the research lifecycle for many
decades. Traditionally, they were specialist tools used only in a small number
of fields and the Computer Scientists who maintained and programmed them needed
extensive technical training over several years to gain the necessary skills and
expertise. Fast forward 50-60 years and software and computation are all around
us, underpinning our everyday lives. This shift is also true within research.

With the ability to capture and process ever more data, undertake larger scale,
higher resolution simulations and, increasingly, leverage new self-adapting
approaches through Machine Learning, computers and software are now vital
elements of the research process across almost all domains. However, this shift
means that basic research software skills are now required by researchers of all 
career levels across a vast array of research fields where these were not
previously required. Researchers often lack the skills to write and use software
for their research and even to effectively request help from and interact with
more experienced staff at their institutions. There still exists a gap in
academic education, as many curricula do not sufficiently prepare their students
in that regard. This situation is exemplified by the extracurricular MIT class
"The Missing Semester of Your CS Education" [@MIT], which aims to convey computing
ecosystem literacy even to students of Computer Science at MIT.

The need to access both research data and software has been formalised with the
FAIR principles: software and data need to be easily findable by both people and
machines, and they also need to be accessible, interoperable and reusable. More
recently the FAIR principles have been extended specifically to research
software [@FAIR4RS].

The people who focus on writing research software are now known as Research
Software Engineers (RSEs) - a term that was coined a little over 10 years ago
[@Hettrick2016]. RSEs may work within one of the many Research Software
Engineering teams that have been set up at universities and research
organisations over the last decade, or they may be embedded within a research
team. They may have a job title that officially recognises them as an RSE, or
they may have a standard research or technical job title such as Research
Assistant, Research Fellow or Software Engineer. Regardless of their job title,
RSEs share a set of core skills that are required to write software, understand
the research environment and ensure that they produce sustainable, maintainable
code that supports reproducible research outputs. They are the ones who
implement the FAIR principles that make digital research output more valuable.
In order to do so they draw upon skills from traditional software engineering,
established research culture and a commitment to being part of a team.

Developing and maintaining these skills is time-consuming and often challenging.
Part of the challenge is that there is not a standard pathway to becoming an RSE
and, partly as a result of this, there is something of an ad hoc approach to
training within the community. We also see increasing amounts of basic-level
training materials that are great to put researchers or technical professionals
on a path towards gaining significant RSE expertise, but the trail often ends as
developing RSEs want to progress to intermediate and advanced level material. In
particular, recent technology developments are ensuring that there is a growing
need for specialist expertise, for example in areas such as making efficient use
of high-performance computing infrastructure. This is an area where there is a
skills shortage and a shortage of training materials.

In this paper, we look at the challenge of understanding the core competencies
that underpin Research Software Engineering and the way that these competencies
may be combined to help support a more coordinated approach to future RSE skills
development. The paper builds on a workshop session held as part of the German
Research Software Engineering Conference (deRSE23), held in Paderborn, Germany
in February 2023.

_[Information on key contributions to add]_

'Related work and activities' gives a brief overview of other initiatives in the area of digital skills for researchers.
The content is twofold. Firstly, we consider other initiatives trying to identify relevant skills for and pathways to becoming an expert in their specific but related area, 
e.g. high performance computing. Secondly, we look at groups and organisations that compose specific training material that can be 
used for teaching RSE skills.

'Challenges' discusses the challenges in the current academic training and research landscape when it comes to 
students and researchers learning the necessary skills to write FAIR software in their specific domain.

In 'Results' we describe the main results of the workshop, namely the set of relevant skills as well as 
the levels of expertise needed in these skills for students and researchers at different career levels.
Furthermore, we look at different RSE specializations which may additionally need skills not relevant 
to RSEs of different specialisations.
The skills themselves belong to one of the three main categories needed to perform RSE tasks. 
Those are the 'R', i.e. an understanding of how research is performed, 
the 'SE', i.e. writing and maintaining reusable software, as well as team skills.

'Organizational Infrastructures' focuses on changes that are required to at best support
the training of new RSEs.

FIXME (finalization): Exchange chapter titles by numbers?


### Some Definitions
A few definitions are in order.
First, as software, we define source code, documentation, tests
and all other artefacts that are created by humans during the development process
that are necessary to understand its purpose.

We define research to encompass all domains of research.
Since we expect a sizeable portion of readers from Germany we
quickly want to address a common false friend.
The German term 'Wissenschaft' encompasses all domains of publicly funded
research, while the English term 'science' is generally limited to natural sciences.
Therefore, we will use 'research' to encompass all domains therefore gives the employability of RSEs.
Of course 'research' as well as 'Forschung' is not limited to public funding
but also part of industrial and other private companies.
We surmise that the same software engineering and team skills will be needed there,
but we limit our considerations to the views of public research.

This enables us to define Research Software in this paper to include source code files,
algorithms, scripts, computational workflows and executables that were created
during the research process or for a research purpose.
This definition is broader than in [@FAIR4RS] and is the outcome of a recent
discussion in [@Gruenpeter2021].

Using this, Research Software Engineers are now people who 
create or improve research software and/or the structures that the software interacts with
in the computational ecosystem of a research domain.
They are highly skilled team members who can also conduct their own research as part of their role.

### Intended Target Audience
While this paper is based on discussions held during a workshop at the deRSE23
conference we believe that the competencies formulated here have a far-reaching
impact beyond the domain of RSE into adjacent fields of science. The most
obvious users come from computer science, are HPC programmers with a background
in physical sciences, or manage research data. Graduates from traditional STEM
sciences with a focus on software or some library or IT staff will also find 
this paper interesting. However, these days most research involves some amount 
of data management, processing and visualisation and the role of RSEs is also
becoming increasingly important in medical domains and the digital humanities. 
Access to central compute resources ranging from small departmental sizes to 
national facilities is becoming readily available. Additionally, pressure is 
growing from funding bodies to prioritise projects that generate archived, 
annotated, re-usable and potentially remotely executable data. These resources 
and requirements fall within the skill set of RSEs. They become a vital link to
cross-pollinate computational skills and infrastructure know-how between domain
scientists. Funders and research managers will find the discussion in this paper
valuable in order to observe how software development in academia will be
institutionalised. Finally, the strong emphasis on team skills allows RSEs to be
very employable in industrial workplaces.

### National Context

Having been developed at a workshop in Paderborn in Germany, naturally a part
of the discussion in this paper focuses on the German academic landscape.
So, although there are Germany-specific traits found in this document
we are nevertheless dealing with the education of humans to become RSEs -
A topic that is of major relevance also in an international context.


## Values

The activities of an RSE are guided by ethical values.
A general list of applicable values is given in the Software Engineering Code of Ethics [@Gotterbarn1999].
Central to that code is the RSE's obligation to act in the public interest.
Further values loosely based on that code include the obligations

+ to take great care to develop software that adheres to current best practices,
+ to judge independently and maintain professional integrity,
+ to treat colleagues and collaborators with respect and work towards a fair and inclusive environment, and
+ to promote these values whenever possible and make sure that they are passed on to new practitioners.

RSEs often assume a multifaceted role at the junction of research, software engineering and data management.
They work with a varying and diverse set of colleagues that might include other developers,
support unit staff and academics of different fields and all career stages.
This situation yields a specific set of challenges RSEs should be aware of
to consciously make ethically sound judgment calls.
We list some example areas that could be addressed in RSE courses or workshops.

### Personal data

Independent from the encoding into the respective national law in an RSE's jurisdiction,
the right to information privacy is internationally recognized as a fundamental human right,
e.g. in the European Convention on Human Rights [@CouncilOfEuropeProtocol1988], [@Hirvela2022].
RSEs need to be aware of this topic's importance
and deal with tensions that might arise with researchers' desire for frictionless sharing of data.
Handling personal data also has ramifications for information security considerations during the software development process.
Data protection is a difficult subject and RSEs should notice when they need to consult external expertise for example when dealing with
special topics such as cryptography or re-identification attacks (e.g. [@Sweeney2002]).

### Mentoring and diversity

RSEs are often experienced professionals who instruct and work closely with early career researchers.
Similarly to academic supervisors, they bear a certain responsibility to guide and advise younger colleagues
with respect to career development and the achievement of academic goals.
Software engineering is still strongly dominated by white males [@StackOverflow2022].
In their work RSEs might frequently find themselves in a position
to encourage, mentor and empower people who gravitate towards software-related occupations.
In this capacity, they should be aware of the diversity problem and help to mediate it
whenever they have the chance to do so.

### The scientific community

Through writing research software, RSEs have a pivotal position in the process of scientific production.
Their choices might determine whether the respective research is reproducible or not,
whether the results can be re-used, whether future research can build on existing tools or has to start from scratch.
Builders of larger research-infrastructure projects determine to some extent
the possibilities and limitations of future research
and therefore need to be aware of concepts such as Open Science, path dependence and vendor lock-in.

### Emerging challenges

RSEs often operate at the cutting edge of technological development
and therefore might have to deal with technologies of which the dangers and drawbacks are still poorly understood.
A current example is the rush for the application of Large Language Models (LLMs),
where RSEs working in these fields should stay up-to-date and be able to help researchers to assess topics
such as training-data bias, LLM "hallucinations" or malicious use.

### Number of required RSE graduates
In order to set up the argument for dedicated RSE education we need at least a ballpark estimate of the number of required graduates.
We start from the number of researchers in Germany. The OECD Data [@OECD2023] reports a number of 667,394 researchers in 2019.
In public research alone we have better numbers and 71,733 researchers were recorded in 2020.
Taking a rough estimate of requiring around one RSE per 10 researchers (FIXME!! Number anecdotal!!)(A number that has been put forward in another workshop
in Paderborn) brings us to a need of around 6.000 RSEs in Germany. Assuming an equal distribution with regard to age
and an average time in the RSE workforce of 40 years, yields an average need of around 150 RSEs per year.
If we assume that half of the workforce is made up by researchers coming from domain specific graduation programs and the other half are properly minted
RSE graduates this suggests that there is a requirement for around four dedicated RSE education places each producing graduating classes of around 20 persons each year.
This calculation assumes that RSEs remain within the research community and do not move into industry with their highly transferable skillset.
While this calculation is only supposed to give a rough ballpark estimate, we note that Germany has 319 places of higher education [@destatis2023].
Having only three RSEs at each site already gives a requirement of 1000 persons.

## Identifying skills and pathways

The development of a standardized list of RSE competencies could help develop
metrics to measure an individual's progression in specific RSE skill sets,
e.g. using the Software Sustainability Institute's RSE Competencies
Toolkit [@RSECompetenciesToolkit2023].

Special interest groups have in the past outlined the core competencies
of various RSE disciplines, such as HPC-RSE [@HPCCFCompetencies; @Kunkel2020a]
(see Appendix: [HPC skills and certification]),
bioinformatics-RSE [@Tractenberg2019; @Mulder2018; @WilsonSayres2018; @Welch2014]
(see Appendix: [Bioinformatics skills and certification])
clinical informatics-RSE [@Davies2022; @Davies2020; @Gardner2009; @Brouat2022],
librarian/RDM-RSE [@Federer2020; @Demchenko2021; @Scholtens2019],
community manager-RSE [@Woodley2021], and generalist RSE [@usRSESkills].
However, the present document is, to our knowledge, the first attempt
at defining the skills of a generalist RSE at different levels of seniority.


FIXME:

- [@Cosden2022b]
- skill gaps:
   - bioinformatics: clear need for more graduate programs [@Attwood2017; @Isik2023]
   - information and communications technology [@AllDigital2022]
   - librarian [@Zignani2020]
   - basic digital skills [@DigitalSkillsGap2023]
   - software verification/testing (fig. 1 in [@Hannay2009])
- software evaluation criteria [@Jackson2011a; @ChueHong2014]
