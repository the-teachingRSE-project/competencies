---
title: "Foundational Competencies and Responsibilities of a Research Software Engineer"
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
  - Simon Christ
output:
  pdf_document:
    citation_package: biblatex
    toc: true
    number_sections: true
secnumdepth: 3
bibliography: bibliography.bib
header-includes:
    - \input{preamble.sty}
    - \usepackage{pdflscape}
    - \usepackage{multirow}
    - \usepackage{array}
    - \usepackage{longtable}
    - \newcommand{\blandscape}{\begin{landscape}}
    - \newcommand{\elandscape}{\end{landscape}}
xnos-cleveref: True
xnos-capitalise: True
keywords:
  - research software engineering
  - training
  - learning
  - competencies
abstract: "
The term Research Software Engineer, or RSE,
emerged a little over 10 years ago as a way to represent
individuals working in the research community but focusing on software development.
The term has been widely adopted and there are a number of high-level definitions of what an RSE is.
However, the roles of RSEs vary depending on the institutional context they work in.
At the one end of the spectrum, RSE roles may look similar to a traditional research role.
At the other extreme, they resemble that of a software engineer in industry.
Most RSE roles inhabit the space between these two extremes. Therefore, providing a straightforward,
comprehensive definition of what an RSE does
and what experience, skills and competencies are required to become one is challenging.
In this paper we define the broad notion of what an RSE is, explore the different types of work they undertake, and
define a list of fundamental competencies as well as values that define the general profile of an RSE.
On this basis, we elaborate on the progression of these skills along different
dimensions, looking at specific types of RSE roles and giving examples of future specialisations.
An Appendix details how existing curricula fit into this framework.
"
---

# Introduction {#sec:introduction}

Computers and software have played a key role in the research life-cycle for many
decades, while they are now vital elements of the research process across almost all domains.
They enable researchers to collect and process ever increasing amounts of data,
simulate a wide range of physical phenomena across previously unexplored scales of the universe,
and discover previously inconceivably complex structures in nature and societies via Machine Learning.
This prevalence of computations in research means that basic
software skills are now required by researchers at all
career levels, and in fields significantly beyond the previously expected.
Research software is now used and developed not only in
science, technology, engineering and mathematics (STEM) domains,
but also in medicine and in digital humanities.

Researchers often lack the skills to use specialised software
for their research, let alone write it [@NamingPain]. If they come from a non-technical domain, they may
also struggle to know what to ask when trying to request help from and interact with
more experienced staff at their institutions. A gap still exists in
academic education, as many curricula do not sufficiently prepare their students
in this regard. This situation is exemplified by the extracurricular MIT class
"The Missing Semester of Your CS Education" [@MIT], which aims to convey computing
ecosystem literacy even to students of Computer Science at MIT.

Researchers investing increasing amounts of their time developing their software engineering
skills to support their research work can find themselves with little time to do the research
itself.
This, in turn, presents career development challenges since the experience required to gain
and progress in research and academic roles is traditionally assessed through metrics that
do not directly include software outputs.
A recent shift towards the establishment of the distinct role of a
_"Research Software Engineer"_ [@WhatResearchSoftware]
(RSE, a term that emerged from the UK a little over 10 years ago [@Hettrick2016]),
now provides a base on which sustainable career opportunities can be (and are being) built,
allowing for better training of researchers and more effective support for the development of high
quality research software.
There is still a long way to go, but positive change is well underway.

RSEs may work within one of the increasing number of Research Software Engineering teams that
have been set up at universities and research
organisations over the past decade, or they may be embedded within a research
team. They may have a job title that officially recognises them as an RSE, or
they may have a standard research or technical job title such as Research
Assistant, Research Fellow, or Software Engineer. Regardless of their job title,
RSEs share a set of core skills that are required to write software, understand
the research environment, and ensure that they produce sustainable, maintainable
code that supports reproducible research outputs, following the FAIR principles [@FAIR4RS].

This paper defines a set of core values and competencies,
agnostic of specific technical capabilities or research domains,
which an RSE should acquire during training and formal education.
By defining these competencies,
we provide a guiding framework to facilitate
the training and continuous professional development of RSEs,
thus helping to provide a positive impact on
research outputs and, ultimately, society as a whole.
These competencies draw upon skills from traditional software engineering practice,
established research culture, and the commitment to being part of a team.
While there is anecdotal evidence that academic software engineering practitioners
would have chosen different competencies, we will argue that this trifecta of skills
is exactly what is needed for modern digital research.

While this paper is based on workshop discussions that were attended largely by Research Software Engineers (deRSE23 in Paderborn, un-deRSE23 in Jena, Germany),
we believe that the competencies formulated here can offer far-reaching
impact beyond the domain of RSE into adjacent fields of science and, indeed, the wider research community,
since most research involves some amount
of data management, processing and visualisation.
At the same time, funding bodies and computing infrastructure providers
prioritise projects that generate archived,
annotated, re-usable, and potentially remotely executable data.
In particular, funding agencies and research managers will find the discussion in this paper
valuable in order to discover where RSEs see their place in the existing landscape of scientific domains.
and how to support the work of RSEs at different positions and career levels.

The outline of the paper is as follows.
We start with a non-exhaustive overview of existing initiatives in @sec:related-work.
@sec:values elaborates on the values that
provide the guiding principles for the work of an RSE.
@sec:required-generic-skills defines a set of core skills based on these values.
The skills themselves fall into three categories, namely
"software engineering", "research", and "communication skills",
reflecting the hybrid nature of an RSE.
To justify the selection of these skills,
we also list some current tasks
and discuss the skills used therein.
As with any general skill set, not all RSEs will need
to use all the skills highlighted to the same level of expertise.
Therefore, @sec:how-much-to-know examines how much a person
needs to know depending on their education or career level
or on the type of projects they would like to be involved with.
@sec:rse-specialisations provides a list of RSE specialisations
and discusses the level of skill needed to work in each of them,
before we conclude the paper with details of future work in @sec:future-work
and conclusions in @sec:conclusion.
Finally, the [appendix](#appendix) provides an [example curriculum](#an-example-master-s-programme-for-research-software-engineering),
an example [career path](#an-example-of-a-possible-career-path) for an RSE through the hierarchy,
and a list of existing skills and certifications in related fields, such as [bioinformatics](#bioinformatics-skills-and-certification).

## Terminology

Depending on the national research
environments and processes that readers are familiar with, the notion of the terms *software* and *research* might differ.
Therefore, to avoid ambiguities, we define these as follows:

**Software**: Source code, documentation, tests, executables
and all other artefacts that are created by humans during the development process
that are necessary to understand its purpose.

**Research Software**: Foundational algorithms, the software itself,
as well as scripts and computational workflows that were created
during the research process or for a research purpose, across all domains of research.
This definition is broader than in [@FAIR4RS] and is the outcome of a recent
discussion in [@Gruenpeter2021].

**Research Software Engineers**: People who
create or improve research software and/or the structures that the software interacts with
in the computational ecosystem of a research domain.
They are highly skilled team members who may also choose to conduct their own research as
part of their role.
However, we also recognise that many RSEs have chosen specifically to focus on a technical
role as an alternative to a traditional research role because they enjoy and wish to focus
on the development of research software.

# Related Work {#sec:related-work}

Various initiatives are working to support technical professionals develop their computational skills.
Particularly related to this work are initiatives that aim to define sets of such skills
and guide the community with certification programs and training resources.

#### RSE Competencies Toolkit

The RSE Competencies Toolkit [@RSECompetenciesToolkit2023] is a community project
that developed out of a hack day activity at the 2023 edition of the annual
Software Sustainability Institute Collaborations Workshop [@SSICW23]. The
toolkit provides a web application that aims to support technical professionals
in understanding how to develop their skills. It enables them to build a profile
of their competencies within the system, while it also provides a set of training
resources that are linked to a competency framework.

#### HPC Certification Forum

The HPC Certification Forum [@HPCCF] is working towards providing a certification
process for High Performance Computing skills.
As part of this process, the group is developing a Competence Standard [@HPCCFCompetencies]
and an associated skill tree that provides a classification of HPC competencies.
This work aims to develop a standardised representation of relevant HPC knowledge
and skills which can, in turn, lead to structured and recognised sets of skills
that can underpin the certification process.

#### EMBL/EBI Competency Hub

The EMBL/EBI Competency Hub [@CompetencyHub] provides a bioinformatics/computational
biology-focused example of a competency portal. In addition to collecting
information on a range of competencies that can be browsed within the
web-based tool, it also provides career profiles for roles
within the domains that EMBL/EBI focuses on. The hub provides
access to variety of training resources that are linked to the specific
competencies that they relate to. This enables learners to more easily
find the right training materials in order to support their career
development journey, helping them to identify what they might want to
learn and in what order.

#### Training-focused initiatives

Further initiatives implicitly define sets of competencies by providing (open)
teaching material for selected skills. This is a non-exhaustive list of related
initiatives, which will be discussed in more detail in a separate publication.
In some cases, the activities extend beyond training, but they do not focus
on defining frameworks of competencies.

One prominent example is the Carpentries [@Carpentries], a non-profit entity that supports
a range of open source training materials and international communities
of volunteer instructors and helpers who run courses around these materials.
A similar framework is provided by CodeRefinery [@CodeRefinery], currently
funded by the Nordic e-Infrastructure,
as well as SURESOFT [@SURESOFTLink] [@SURESOFT2022], a DFG funded project at TU Braunschweig and
FAU Erlangen-Nürnberg, targeting more advanced software engineering topics like
Software Design Principles, Design Patterns, Refactoring, Continuous Integration and Test Driven Development.

There are also several initiatives focused on training HPC-oriented RSEs,
such as the Partnership for Advanced Computing in Europe (PRACE) [@PRACE]
(with material aggregated on various websites, e.g. on EuroCC Training [@EuroCCTraining]),
UNIVERSE-HPC (Understanding and Nurturing an Integrated Vision for
Education in RSE and HPC) [@UNIVERSEHPC] (a project funded under the UK's
ExCALIBUR research programme [@EXCALIBUR]),
and the EuroCC National Competence Center Sweden (ENCCS) [@ENCCS], which offers
a collection of lessons for HPC skills [@ENCCSLessons].

Initiatives focused on Germany include EduTrain [@EDUTRAIN] (a section of NFDI [@NFDI]),
the Helmholtz Federated IT Services platform (HIFIS) [@HIFIS], and the already mentioned SURESOFT [@SURESOFTLink].

# Values {#sec:values}

The activities of an RSE are guided by ethical values.
In addition to the values for good scientific practice [@dfg_gsp], RSEs also adhere to
the Software Engineering Code of Ethics [@Gotterbarn1999].
Central to that code is the RSE's obligation to
commit to the health, safety and welfare of the public and act in the interest of society, their employer and their clients.
Further values loosely based on that code include the obligations

+ to commit to objectivity and fact-based, honest research conclusions,
+ to promote openness and accountability in the research process,
+ to take great care to develop software that adheres to current best practices,
+ to judge independently and maintain professional integrity,
+ to treat colleagues and collaborators with respect and work towards a fair and inclusive environment, and
+ to promote these values whenever possible and make sure that they are passed on to new practitioners.

RSEs often assume a multifaceted role at the junction of research, software engineering and data management.
They work with a varying and diverse set of colleagues that might include other developers,
support unit staff and academics of different fields and all career stages.
This situation yields a specific set of challenges RSEs should be aware of
to consciously make ethically sound judgement calls.
We list some example areas that highlight present-day challenges.

## Current Challenges

### Handling of data and personal data

A lot of RSE work involves the manipulation or creation of data processing devices.
We highlight that professional conduct requires these creations to be reliable and to maintain data integrity.
In particular, the way that personal data is handled can have far reaching implications for society.
Independent from the encoding into the respective national law in an RSE's jurisdiction,
the right to information privacy is internationally recognised as a fundamental human right,
e.g. in the European Convention on Human Rights [@CouncilOfEuropeProtocol1988; @Hirvela2022].
RSEs need to be aware of this topic's importance
and deal with tensions that might arise with researchers' desire for trouble-free sharing of data, thereby expecting openness about the research process,
versus the integrity expectations of the society towards IT systems.
Handling personal data also has ramifications for information security considerations during the software development process.
Data protection is a difficult subject, so RSEs should notice when they need to consult external expertise, for example when dealing with
special topics such as cryptography or re-identification attacks [@Henriksen2016].


### Mentoring and diversity

RSEs are often experienced professionals who instruct and work closely with early career researchers.
Similarly to academic supervisors, they bear a certain responsibility to guide and advise younger colleagues
with respect to career development and the achievement of academic goals.
According to the UNESCO Science Report [@Schneegans2021] women account for 33.3% of all researchers while the majority of researchers come from G20 countries (88.8%).
This imbalance is even more pronounced in software engineering with a majority of developers identifying as white male [@StackOverflow2022].
Thereby, to promote their values of an honest, open, and inclusive research space, they should be aware of
the diversity problem and help to mediate it whenever they have the chance to do so.

### The scientific community

Through writing research software, RSEs have a pivotal position in the process of scientific production.
Their choices might determine whether the respective research is reproducible or not,
whether the results can be re-used, whether future research can build on existing tools or has to start from scratch.
Builders of larger research-infrastructure projects determine to some extent the possibilities and limitations of future research
and therefore need to be able to make a value-based judgement on topics
such as Open Science, path dependence, and vendor lock-in.

### Emerging challenges

RSEs often operate at the cutting edge of technological development
and therefore might have to deal with technologies of which the dangers and drawbacks are still poorly understood.
A current example is the rush for the application of Large Language Models (LLMs),
where RSEs working in these fields should stay up-to-date and be able to help researchers assess topics
such as training-data bias, LLM "hallucinations" or malicious use, with the greater goal of
making these powerful tools work for the welfare of society.

# Required Generic RSE skills {#sec:required-generic-skills}

The role of an RSE lies somewhere on the spectrum between that of a researcher
(the "R") and a software engineer (the "SE") and, therefore, requires
competencies in both fields. RSEs typically apply their knowledge and
experience in larger teams which allows them to cultivate this hybrid nature.
Therefore, we categorise the competencies into software engineering skills,
research skills, and team skills with a particular focus on the software and
research cycle and the scientific process. The generic skills are relevant in a
broad setting and form the foundation for specific specialisations.
These competencies have been chosen in order to make RSEs contribute to an open and inclusive research
environment, with tools that respect their professional values.

These skills and competencies come into play in various forms: first of all the
RSEs themselves need to acquire and develop them as their career progresses
(**Career level**). However, some knowledge of software and data processing is
required at all academic levels and for all positions
(**Academic Progression/better title**). The relative importance of the skills
and competencies also depends on the size of the RSE team
(**Project team size**). Finally, different sets of skills are emphasised in
the different RSE specialisations (**RSE specialisations**).

## Software Engineering Skills

There are many software engineering curricula out there, that try to define
which tasks a software engineer should be able to perform. A recent example
highlighting some aspects in more detail than here is [@Landwehr2017].
The software skills outlined here are required to make research software adhere
to the FAIR principles, which are aspects of good scientific practice.
[@ChueHong2014] defines different levels of research
software reusability and the extent to which the software engineering skills
need to be applied to reach them.

### Creating documented code building blocks (DOCBB)

The RSE should be able to create building blocks from source code that are
reusable. This ranges from simple libraries of functions up to complex
architectures consisting of multiple software packages. An important part of
reusability is that at least oneself, and ideally others, are able to understand
what a piece of software aims to do and how to enable others to use the provided functionality. This
is primarily achieved through a "clean" implementation and enhanced by
documentation. Documentation ranges from commenting code blocks to using
documentation (building) tools.

### Building distributable libraries (LIBS)

The RSE should be able to distribute their code on their domain/language
specific distribution platforms. This almost always encompasses
handling/documenting dependencies with other packages/libraries. It sometimes
requires knowledge of using build systems to enable interoperability with other
systems.


### Adapting to the software life-cycle (SWLC)

The traditional software life-cycle defines the stages that form the process of building a piece of software.
Initial development generally involves a creative process where requirements are gathered and analysed,
followed by a formulation of a plan to fulfil them that is finally implemented.
This is then followed by testing that things work as expected and that they continue to do so into the future.
Often the development is iterated.
We emphasise that the life-cycle is not complete here but also includes periods of maintaining a software
and also withdrawing software from its original use.
The RSE should be aware of this life-cycle
and be able to predict and cater to the changing needs of software as it moves through the stages.


### Use repositories (SWREPOS)

The RSE should be able to use public platforms (so-called software repositories or repos) to share the artefacts they have
created and invite the public to scrutinise them for public review.

### Software Behaviour Awareness and Analysis (MOD)

We define this as a certain quality of analytical thinking that enables an RSE to
form a mental model of a piece of software in a specific environment.
Using that, an RSE should be able to make predictions about a software's behaviour.
This is a required skill for common tasks like debugging, profiling, optimising, designing good
tests, or predicting user interaction.
An important facet of this capability relates to information security.
RSEs need to consider the safety and integrity of personal data and other sensitive information
and make sure that they do not negatively impact the integrity of their institution's network.

## The research skills

### Curiosity (NEW)

RSEs gain their reputation from their effectiveness in interacting with their
domain peers. Therefore, some curiosity together with a broad overview of the
research field is required as this enables the RSE to learn new methods and algorithms directly from domain peers.
Curiosity is also reflected when an RSE is actively
trying out new tools. Lifelong learning is then no longer just a phrase but
becomes a motivation to work.

### Understanding the research cycle (RC)

One of the crucial skills of RSEs is their mental proximity to research.
They embrace being part of a larger community which,
despite friendly competition, shares the common goal of gaining knowledge
for its own sake and not just for personal or commercial gain.
Thereby they know, that they are part of a bigger cycle that involves many other parties in and outside of
their domain, and also that their software can be utilised at different stages of the research cycle by different people.
Like other researchers, RSEs are open to discussions and arguments beyond
their own expertise and appreciate the underlying principles of
good research, like publications, reviews and reproducibility.

### Software re-use (SRU)

One goal of FAIR software is to avoid unnecessary duplication of work by reusing
existing work instead. To (re-) use software, researchers have to be able to
find it and then easily evaluate if the software actually suits their needs.
Apart from functionality, the integration with other software,
expected sustainability, and extensibility also have to be part of this evaluation.

### Software publication (SP)

The second part of FAIR software is concerned with publishing new and derived works
and making them available for re-use by the research community and the general public.
RSEs need to have a basic understanding of common software license types, such as "proprietary", "copyleft", and "permissive",
the compatibility of different common licenses and the ramifications for re-using and composing programs.
Finally, RSEs will need to properly execute the technicalities of software publishing,
such as applying licenses, honouring copyright statements and crediting contributors.

### Using domain repositories/directories (DOMREP)

Almost all research software is developed within a specific scientific domain.
Some software may be able to cross boundaries, but the majority will have a
home domain, with which it needs to be able to interact. The RSE needs to be
aware of any domain specific software repositories, data sets and catalogues.
The RSE also needs to be aware of how their software can interact with the existing
domain-specific data repositories.

## Communication Skills

RSEs do not work in isolation.
They are embedded in a research group or work within a team of RSEs supporting particular research projects.
RSEs often need to interact with and facilitate communication among colleagues, clients and contractors
with a very broad spectrum of background-knowledge, specialisation, expectations and experience.
Communication skills are therefore crucially important.
Team skills are also mentioned in common guides for software engineering such as the Software Engineering Body of Knowledge [@swebok_2014].
However, the interpersonal and organisational skills and the capacity for adaption required to work in a research setting
warrants a much stronger emphasis on this field of competence.

### Working in a team (TEAM)

Working in a team is all about communication and teamwork.
For example, RSEs need to be able to explain particular implementation choices made and may even need to defend them.
Within a team of RSEs code reviews improve knowledge transfer and increase team cohesion.
Code review within a multi-disciplinary team fosters mutual understanding and
can be a knowledge transfer between the RSE and domain scientists.
The team might change on a project-to-project basis and might be comprised of colleagues with very different backgrounds
including, for example, IT staff, domain scientists and technicians working alongside software engineers.
The shared values come into play and each RSE needs to ensure that these values are lived by and passed on to others.
Senior RSEs may lead a team of RSEs.

### Teaching (TEACH)

RSEs have many opportunities to teach.
These range from inducting new colleagues to teaching digital skills either through short courses,
for example from The Carpentries [@Carpentries], or entire lecture series.
RSEs may also act as mentors and consultants.
Code review also includes aspects of the teaching skill.

### Project Management (PM)

The RSE should have knowledge about project management. At some institutes, it follows the practices of the local research groups,
but it is useful, if an RSE knows its place in a PM scheme, or can bring in new ideas for improvement.
Project management in research software engineering poses specific challenges (see [USERS](#interaction-with-users-and-other-stakeholders-users)) that might require the capacity
to flexibly adapt to changing conditions and deviate from common project management methods.

### Interaction with users and other stakeholders (USERS)

Since research software is often developed as part of the research process itself,
its requirements and specifications might change with the progression of research.
Stakeholders of research software often change across different research projects
or even within the course of one project.
Roles in connection with research software are often in flux and diffuse.
For example, a single person might be user, developer and project manager at the same time.
Often this means it is necessary for an RSE to think "outside their comfort zone",
but at the same time to be able to convey their knowledge and experience to experts
of other fields or persons at different hierarchy levels in a way they can understand more easily.
These conditions pose specific challenges for requirements analysis, project management, training and support.

## RSE Tasks and Responsibilities

These skills, while already numerous are also generic on purpose. They span a
multidimensional space in which the day-to-day tasks and responsibilities of an
RSE can be found. A snapshot of what this means today was obtained
from learners and novice RSEs that we asked during the Paderborn workshop
what they would like to have learnt. Among the top five things mentioned were:

- Testing. This task is a manifestation of the SE competencies of DOCBB and MOD
  since a model of the software is required in order to write good tests that
  facilitate understanding and documentation. Today this encompasses the
  knowledge of testing frameworks and CI/CD practices.
- Contributing to large projects. This is a topic that requires competency in
  SWREPOS, SRU, SP in order to understand the ramifications of sharing, and DOCBB,
  since the contributed code has to be understood by others. Interacting with
  project members depends on the TEAM skill. Today this entails the effective
  use of collaborative platforms like GitHub/GitLab, honouring a project's Code of
  Conduct, and some knowledge of popular software licenses like e.g. GPL.
- When or why to keep repositories private. This decision requires knowledge in
  the RC, to understand when it makes sense to open up or close down a repository.
  The USERS, TEAM and sometimes SP skills are required to make this decision.
  Furthermore, knowledge of the practices and contractual regulations of the
  RSE's institution are also required.
- Proper Development. This broad topic requires all of the SE skills. Of course,
  these are the competencies that are the most fluid since they have to adapt at
  a high rate to technological advancements. Additionally, proper SE skills
  often require knowledge of TEAM, and PM. Today this means effective use of IDEs,
  static analysis tools, design patterns, documentation (for oneself and others),
  etc.
- Finding a community. This can be interpreted in two different ways. First,
  we have the aspect of community building for a research project. Since this
  deals with software that is supposed to be used in research this requires
  knowledge of RC, USERS, and also NEW, in order to effectively interact with
  domain scientists. Today, an example is a presence on social media. The other
  TEAM-related aspect is the embedding of RSE graduates into the community of
  RSEs. We envision our RSE graduates to be a part of a strong network of other
  RSEs, tool-related communities and the classical domain communities. This point
  is further elaborated in @sec:reachout.

Beyond that, we feel that today other important tasks of RSEs are

- Mentoring colleagues.
  This necessitates giving good advice that fits to a projects stage in its life-cycle,
  thereby requiring knowledge of (SWLC), and its context in its research domain and thus (RC).
  Research software often starts out as a tool to answer a personal research
  question and becomes more important when other researchers rely on it.
  Some research software might even be used to deal with critical questions such as weather forecasting or medical diagnosis.
  To formalise the process of giving good advice a classification of software is commonly used [@Wang2012; @Schlauch2018b]
  where research software can move from one class to another during its life-cycle.
  [@Schlauch2018b] classify applications based on their scope and criticality and provide software engineering recommendations.
  The RSE needs to be able to identify the application class they are dealing with and apply the respective RSE practices.
- Enforcing reproducibility. Projects like [@ReproHack] can greatly help in fostering that competency.

# How much do different people need to know? {#sec:how-much-to-know}

Now that we have the different competencies, we can explore various dimensions of these competencies,
depending on their circumstances. A strong beneficiary of specialised RSEs can also be newly formed RSE centres at research institutions.

## Career Level

At different career levels, differing skills are required. We have set this up according to the following separation often applied within a single project:

- Junior RSE: These are persons who have just started, but generally speaking they should have the skills to contribute to software projects.
- Senior RSE: They have gained experience and can set the standards in a software project.
- Principal RSE: Their actual job description varies a lot. These may be RSE team leaders based in a professional services type role, or they may be professors or research group leaders based in a more academic-focused role. They are often the people responsible for bringing in the funding that supports new projects and sustains existing projects. Generally speaking, they do not need to be actively involved in the day-to-day technical tasks but they should be able to guide projects from both a technical and a research perspective while providing an inclusive working space.

The following table elaborates on the required facets of the competencies in different roles.
A story-like example of an individual through the hierarchies can be found in @subsec:examplecareer .

\blandscape
\small
\renewcommand*{\arraystretch}{1.4}

|         | Junior                                                                                                                        | Senior                                                                                                                                | Principal RSE(brings in funding)                                                                                                                           |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DOCBB   | should be able to write reusable building blocks                                                                              | same as junior, but the quality should set the standard for the project, while following current best practices                       | should know the current best practices and point its people to the right resources.                                                                        |
| LIBS    | should be able to use package distribution platforms                                                                          | same as junior, but should set the project standard and follow current best practices.                                                | should ensure that their project is in an up-to-date distribution platform                                                                                 |
| MOD     | should have a basic grasp of their piece of the software in order to use basic tools like a debugger                          | Should understand the characteristics of large parts of the codebase considering a variety of the metrics                             | Should understand the big idea of the software project in order to define the task that the software solves                                                |
| SWLC    | Awareness about the existence of the software life-cycle.                                                                      | Should know which decisions lead to technical debt.                                                                                   | Should know in which part of the life-cycle their project is and how to steer development/project resources accordingly.                                    |
| SWREPOS | Seamless interaction with the swrepo of their project is a must                                                               | Should be well-versed in the intricacies of a swrepo, and probably interact with multiple projects' repos                             | Should be able to effectively interact with swrepos and especially the interaction with the connecting projects.                                           |
| NEW     | Some curiosity required to fit into research teams                                                                            | same as junior, but a curiosity to enhance the code base is required                                                                  | Curiosity to know in which direction to steer the project is required                                                                                      |
| RC      | Awareness about the RC                                                                                                        | should know the position of the project in the RC                                                                                     | Should know what is necessary for the project to fit into its position in the RC                                                                           |
| SRU     | Should be aware about tools for SRU                                                                                           | Should be able to find sth. with SRU tools                                                                                            | Should be able to effectively find sth. with SRU tools and be able to evaluate and perform the integration of a library into the project.                  |
| SP      | Should be aware that SP needs to consider issues of intellectual property                                                     | Should be able to correctly publish software in simple cases and be able to identify cases where professional legal advice is needed. | Same as Senior plus the ability to take the future publication of software into account when initiating and guiding larger software collaboration projects |
| DOMREP  | The RSE should be able to interact with the domain repository                                                                 | same as junior RSE                                                                                                                    | same as junior, and should know about how it fits into workflows surrounding these domain repositories                                                     |
| USERS   | The RSE should be able to communicate with non-SE users of the project                                                        | same as junior                                                                                                                        | same as junior, and take feedback into account of the steering                                                                                             |
| TEACH   | should be able to perform simple peer-to-peer on-boarding tasks                                                                | should be able to explain logical components to other RSEs                                                                            | Should be able to effectively communicate about all large-scale parts of the project.                                                                      |
| PM      | Awareness about the employed project management method                                                                      | Should be able to use the employed PM method                                                                                          | Should be able to design and adapt the employed PM method.                                                                                                 |
| TEAM    | Should be able to work in the team in order to effectively fulfil the given tasks. Should be able to learn from code review. | Should be able to break down tasks into more easily digestible sub-tasks                                                              | Should be able to lead the team and set the respective direction.                                                                                          |

Table: Levels of competency expected for different RSE career stages. {#tbl:comp-lvls}

\elandscape

## Helpful RSE skills for researchers in an academic career

In the previous section,
we looked at the competency levels needed for RSE specialists.
However, many of these competencies are important for researchers in academia as well.
Naturally, the 'R' competencies apply
and research in general is increasingly team based.
Additionally, many researchers in fields from classical examples like
numerical mathematics or theoretical physics
to newer disciplines like digital humanities
will spend time in their research on writing and developing software.
Therefore, RSE focused training, e.g. in a master's programme,
is also beneficial for students in these fields
resulting in a broader audience.

This section outlines how the RSE competencies could be reflected at all academic levels.
It is important to note that this section does not reflect the current state of academic training and research institutions.
Instead, it summarises the discussions with and between workshop participants at different levels of academic progression on what they would have liked to learn at an earlier stage or know before starting their current position.
While individuals already work at implementing some of these changes and teaching these skills, it has not yet reached a systemic level.

The text is organised along the academic progression path (bachelor's degree, master's degree, PhD, Postdoc, PI/Professor).
Since each level is based on the previous levels we presume that the skills and competencies at each level also encompass those of the previous levels.
Due to the broad need throughout academic specialisations,
the described levels serve as a baseline
and certain fields will require higher SE skill levels
as development is a large part of their actual research.

#### Bachelor's Level

Students at undergraduate level mostly consume science/knowledge.
During their studies, they should also learn about the existence of digital tools and structures.
Undergrad students should be aware that RSEs exist and that software has different quality aspects (DOCBB).
They should be aware of domain specific tools (LIBS, SRU) and where to find them (SWREPOS, DOMREP).
At this level it is sufficient to consider software as black boxes (USERS) although some training in data presentation would be very helpful and a good way to find out about programming (MOD, NEW).
They should have an awareness of software licenses and whom to ask if they have any questions (SP).
They will be taught about the research cycle (RC) and that researchers often work in groups (TEAM).
During practicals, they will have an opportunity for peer learning (TEACH).

#### Master's Level

A student at a master's level can participate in science and should therefore be able to use "some" digital structures.
A master's student needs to be aware of relevant tools and data sets for their domain, where to find them and how to use them (LIBS, SWREPOS, DOMREP).
They should be able to process and present their data (MOD).
They need to understand how their research depends on software (SWLC).
Working on their master's thesis allows them to understand the research cycle (RC), practice project management (PM) and collaborate with other members of their research group (TEAM).

#### PhD

A PhD student performs independent research under guidance.
They need to know relevant tools and structures.
They should know where to find information about tools and where to find help using them (DOCBB, SWREPOS).
They should be able to use the tools (LIBS) and identify and report bugs (MOD).
They need to be aware that the user's perspective is different from the developer's perspective in order to be able to write bug reports (USERS).
They might produce new software (MOD, SRU) in which case they need to understand how to license their code for publication (SP).
PhD students need to be curious to be able to conduct their research.
In order to be able to explore new tools (NEW) they must be able to evaluate research software (SWLC).
They need to be able to interact with services (RC) and domain specific repositories (DOMREP).
They should be able to supervise a student (TEACH).

#### Postdoc

Postdocs are independent researchers.
Their role is similar to that of a PhD student with a deepened focus on their research career.
However, they are proficient users of all relevant tools, which makes them active contributors to their domain of research.
They need to be aware of more advanced topics regarding intellectual property rights, such as patents (SP).

#### PI/Professor

They are experts in their field and should be able to give proper guidance to their students on which digital tools are currently relevant.
They should be aware of the skills of an RSE and when they might need one in their group.
They should encourage their students to use relevant tools (LIBS).
They need to be able to judge the suitability of the software (SWLC) and follow the interactions between relevant projects (SWREPOS).
They should be able to advise their students on the legal aspects of software production and distribution (SP).
They should be able to contribute meaningfully to the steering decisions of the software in their field (USERS).
They need to guide students and give full-size lectures (TEACH).
They need to manage and lead their research group (PM, TEAM).

## Project team structures

In this table, we look at individual or team competencies and approaches to them,
considering how these differ depending on whether an RSE or researcher is working alone on a software project,
or whether they are working as part of a team of research software developers.
We extend this to consider how things differ when a developer or a group
of developers is based locally within a research team or department,
or when they are based in a dedicated RSE team.
We also look at organisational aspects in the context of each of the considered
competencies since there are a variety of ways that organisations can contribute
to and support them. Some of them are brought to life in the example career path of the appendix.
We first summarise the meaning of each of the columns in the table:

- **Competency:** The code assigned to the competency being considered.
  See the list in @tbl:comp-lvls.
- **Individual developer (Locally-based):** A single person working on some
  research software - often a researcher with RSE skills.
- **Individual developer (RSE team-based):** A single person working on research
  software - generally a professional RSE supporting another team's software on its own.
- **Group of developers (Locally-based):** A group of RSEs/researchers within
  a research group or team, working together on developing software to support
  or undertake a single research goal/project.
- **Group of developers (RSE team-based):** A group of members of the RSE team
  working together on a research software project for a research group.
- **Organisation-level support:** How the defined competencies are recognised
  and represented at an organisational level.

\blandscape
\small
\renewcommand*{\arraystretch}{1.4}
\begin{longtable}{|p{1.8cm}|p{3.5cm}|p{3.5cm}|p{3.5cm}|p{3.5cm}|p{4.5cm}|}
    \hline
    \multirow{2}{*}{Competency} & \multicolumn{2}{c|}{Working as an individual developer}
    & \multicolumn{2}{c|}{Working with a group of developers} & \multirow{2}{*}{Organisation-level support} \\
    \cline{2-5}
              & locally-based & RSE-Team based & locally-based & RSE-Team based &\\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    DOCBB &
    Focus on getting outputs to support research. Often time-constrained,
      may be self-taught, less awareness/familiarity with code quality and
      structure. Simple Best Practice documents can be sufficient&
    Likely greater focus on reusability, documentation, and knowledge of best practices
      but potential lack of domain scientist support.&
    More opportunity to discuss and share ideas but team members may be
      self-taught and less aware of key practices. &
    Stronger ingrained focus on team-based project management and development
      methodologies resulting in higher quality, more reusable code.&
    Will offer training and other resources in core topics to support self-taught/embedded developers.
      Should have research software guidance/policies that provide advice.\\
    \hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    LIBS&
    Reusability and sharing/distribution of code often not a focus or considered relevant. &
    Greater trained focus on reusability/sharing but likely not part of the project aims.&
    May be looking to develop reusable shareable outputs but likely case-by-case basis. Need easy resources.&
    Focus on quality and practices, reusability/packaging driven by project needs and spec.&
    Should provide policies on sharing and reuse of software. May be driven by requirements/policies of the funding agency.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    SWLC&
    It's down to you to manage the complete life-cycle, if you move on,
      what will happen to the code?&
    More support with a team but do they have awareness/expertise
      of managing the life-cycle? What is the "bus factor"?&
    Even when working alone, team infrastructure and tooling can be vital
      in supporting the life-cycle and supporting sustainability.&
    As previous but with a large codebase, how many people know about each part?
      Need to think about coherent life-cycle management across the team - generally
      a key part of RSE team expertise.&
    Support for training important. Organisation may also provide site
      licences for e.g. management tools.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    SWREPOS&
    Where open source, use of repositories important for code management
      and demonstrating outputs - e.g. supporting academic credit.
      May not have awareness/skills if self-taught.&
    As previous but professional RSEs generally very experienced
      with use of repositories and their many features.&
    Repos are a vital aspect of modern team-based development.
      Short courses can facilitate effective use.&
    Repos used extensively by RSE teams - often the base for project
      management, issue tracking, etc. in addition to code itself.
      May train others.&
    Organisations can offer enterprise repository set ups,
      site licences etc. Also fund either internal or external training
      for this vital research software development tooling.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    MOD&
    Needs full awareness of entire codebase to support extension/maintenance.
      May not need/get additional experience or support.
      If project taken on from another individual developer,
      there may be challenges in transferring this mental model of the software.&
    As local but greater awareness of need for future transition to other
      developer(s), likely provide e.g. docs/issues/project board and other
      support from central services to support this. May only need to know
      part of code.&
    Internal team training important to ensure ability to build necessary
      mental model of codebase and to document it via text or tools to support
      sustainability.&
    As local team but likely stronger awareness of tooling and practices
      in place within RSE team to support this. Distributing work makes it only necessary
      for each developer to understand code related to their assigned tasks.&
    Training and experience are key here and organisations can help
      to coordinate and provide support for training and mentoring/community activities.
      Establishing RSE departments with specialists for certain aspects of software
      will improve overall turnaround times.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    NEW&
    An individual's curiosity has now to be shared between the research
      goal and the software project, therefore learning new methods and
      skills may be challenging and is often not the core aim.&
    RSE teams should support their team members, especially when working
      individually on a project, to explore new tools and approaches,
      make relevant contacts and learn more about the research in the project domain.&
    Likely to be an area of interest for an embedded development team
      but if they are researchers, they definitely have curiosity in their domain.
      A curiosity for tools would be appreciated.&
    As per Individual (RSE team).&
    Organisations should reach out to relevant groups locally to help share
      information on new technical processes and tooling, and facilitate training.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    RC&
    This is likely to be familiar to individuals, who are often researchers,
      especially if they are embedded within a research team.&
    Many RSEs will have familiarity with the research life-cycle,
      although they may not have domain knowledge. This can be alleviated by interacting with a group&
    Likely to be familiar to software teams (often researchers) working
      in a research group. Can share knowledge among themselves or reach
      out to colleagues.&
    Teams of RSEs from an RSE group are likely to include one or more
      team members with strong awareness of the research life-cycle.&
    Research organisations have extensive infrastructure to manage
      the research life-cycle, this can support researchers/RSEs.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    SRU&
    Need to know how to find other work to build awareness of existing
      solutions. Researchers sometimes like to do things themselves.
      Working individually means there may not be someone to highlight this.&
    RSE team members will generally be familiar with software sharing
      and discovery tools and platforms.&
    As per individual (Local) but being part of a team can help to address this.&
    As per individual (RSE Team).&
    Can choose to run local environments to host software or catalogue software,
      they can also provide institution-level access to platforms that support this.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    SP&
    Responsibility may be with an individual but they may not have necessary knowledge/skills.&
    This is a core area that RSE teams need to be aware of.
    An RSE team might have established practices, workflows and policies at hand to routinely publish software.&
    As with individual (local) developer.&
    As with individual (RSE Team).&
    The organisation should raise awareness about software as publishable scientific output, provide recommendations and checklists to support software-publications and have legal experts in place to deal with complex cases.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    DOMREP&
    Domain researchers working on software are likely to be more familiar
      with the domain-specific solutions.&
    RSEs may need guidance from domain researchers around domain-specific
      repositories if they have a background in a different domain.&
    As per individual (Local).&
    As per individual (RSE Team)&
    May host domain-specific repositories for areas that they work
      extensively in but this is likely to be handled at a research group level.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    USERS&
    Is the software developed to support external users?
      If so, additional technical skills may be required,
      especially if future sustainability is an aim.&
    Is there a plan for external use? RSEs generally have the skills
      to support this or can access assistance via team colleagues.&
    If a team of embedded researchers/developers are involved in a larger
      project, there's more chance that there's a case for external use.
      Do they have the skills and resources to support this?&
    A team of RSEs can generally better prepare code for external users
      (e.g. by applying development best practices) and provide infrastructure
      or specialised RSEs for dealing with user support. &
    Should have institutions that are able to offer support with outreach and publicising outputs.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    TEACH&
    May be independently involved in training activities.&
    May be able to support researchers with core technical skills.&
    Sharing knowledge and skills within their group - peer support.&
    Often support teaching more widely, either through organised courses
      or ad hoc activities such as "code clinics".&
    Should have programs for a diverse range of teaching/training activities.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    PM&
    Limited requirement beyond being well organised - can be important
      if someone else might take over codebase.&
    Limited requirement but team will likely have standard PM approaches
      to be followed.&
    Challenging for groups of local researchers/developers on larger projects.
      May not have awareness/experience of key skills, but this can be alleviated with some low-key courses.&
    Likely have well structured approaches and tooling to support this.&
    Can offer training to support management of projects.
      May offer organisation-level tooling.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    TEAM&
    N/A&
    Will need to work effectively with their home RSE team, as well as,
      potentially with researchers they are developing code for.&
    Effective teamwork vital - do they have the skills and knowledge
      to support team-based software development?&
    Will need to be able to work and collaborate effectively in a team,
      use required tools and processes, infrastructure, etc.&
    Can offer support with team work. Should support team-building initiatives
    also on a social level.
    \\\hline
\end{longtable}
\elandscape

In the table above, we have looked at how different competencies can be related
to and handled by researchers and RSEs working in different environments within
an organisation and how the organisations themselves can contribute.
We recognise that this is a challenging area to gain a detailed view of
and that our content in the table is still a significant generalisation.
We talk about the "Research Software Engineer" as a single entity but as the field expands,
we expect to see more roles and job titles emerging around the RSE concept,
many of which fit under the wider umbrella of Research Technology Professionals (RTPs).
Examples are different RSE-like computational roles of
the European Bioinformatics Institute (EMBL-EBI)'s BioExcel competency framework [@BIOEXCEL] (also @subsec:emblbio),
as is a range of different roles from King's Digital Lab at King's College London [@KDL].

# RSE specialisations {#sec:rse-specialisations}

What we have defined above are intended to be base skills that an RSE irrespective of domain, place, and time should know about.
But not all RSEs are created equal, they specialise in different areas,
some of which we want to present below. Many of the specialisations may overlap,
so the same RSE might for example work on data management and Open Science.
We categorise them into those, that can be viewed as a specialisation within RSE-specific topics,
while other RSEs might expand their skill set and profession to areas, that are not typical for an RSE.


## Specialisations within the core RSE competencies

#### OpenScience RSE
Open Science and FAIRness of Data and Software are increasingly important topics in research,
as exemplified by the demand of an increasing amount of research funding agencies requiring openness.
Hence an Open Science RSE is required to have a deeper knowledge in (RC) and how to distribute software publicly (SRU, SP).
Open Science RSEs can help researchers navigate the technical questions that come up
when practising Open Science, such as "How do I make my code presentable?",
"What do I need to do to make my software FAIR?", or
"How do I sustainably work with an (international) team on a large code base?".
Like the Data-focused RSE, they have a deep understanding of RDM topics.

#### Project/Community Manager RSEs

When research software projects become larger, they need someone who manages
processes and people. This gap can be filled by people who invest in the (PM), (USERS), and (TEAM) skills, as exemplified in @subsec:examplecareer.
Building a community around a research project is an
important building block in building sustainable software [@Segal2009], so these RSEs play
an important role, even if they do not necessarily touch much of the code themselves.

#### Teaching RSEs
RSEs interested in developing their (TEACH) skill can focus on teaching the next generation of researchers and/or RSEs and will play
a vital role in improving the quality of research software.
They need to have a good understanding of all RSE competencies relevant to their domain and
additionally should have experience or training in the educational field.


#### User Interface/User Experience Designers for Research Software
Scientific software is a complex product that often needs to be refined in order to be usable even by other scientists.
To facilitate this, there are people required that specialise in the (DOCBB) and probably the (LIBS) competency
with a focus on making end-user facing software really reusable and hence FAIR.
This task is supported by strong (MOD) skills to reason about the behaviour of potential users of the software.

## Specialisations outside the core RSE competencies


<!--
Research focused specialisations
-->

#### ${DOMAIN}-RSE
While software is the lingua franca of all RSEs there will be RSEs that have specialised in the intricacies of one particular research domain,
such as medical RSEs, digital humanities RSEs or physics RSEs.
This can often serve as a base domain for RSE specialisation as in @subsec:examplemaster

#### Data-focused RSE
RSEs working at the flourishing intersection between data science and RSE.
They are skilled in cleaning data and/or running data analyses and can help researchers
in setting up their analysis pipeline and/or research data management (RDM) solutions.
When the field requires research on sensitive data or information, e.g. patient information in medicine,
this RSE should have knowledge about secure transfer methods and/or ways to anonymise the data.
As part of RDM, this RSE profile is able to support all stages of the research data life-cycle [@Nieva2020], with synchronous data management processes.
Those processes implement established best practices for planning and documenting of data acquisition in a data management plan (DMP) as well as for management,
storage, and preservation of data, and publication and sharing of data in repositories according to the FAIR principles [@FAIR].


<!--
New areas of expertise
-->

#### Research Infrastructure RSE
This RSE is interested in SysOps and system administration and sets up IT infrastructures for and with researchers.
Therefore, this specialisation on the one hand requires a deep knowledge of physical computer and network hardware and
on the other hand knowledge about setup and configuration of particular server software, like
e.g. setup of virtual machines on hypervisors or the planning and setup of compute server clusters machine learning.
As an interface between the researchers and the infrastructure, they take care of user management, access permissions, and configuration of required services.

#### Maintenance RSEs
The constantly evolving software environment can hinder or prevent reproducibility.
In this changing environment, a significant amount of effort in (research) software development
needs to be spent on maintenance to ensure that software remains useful or even installable.
With regard to which additional competency is required,
these are people having experience with ancient software stacks that are not part of the general curricula any more (think of COBOL and FORTRAN).
Another skill-set required is (automated) testing.

#### High Performance Computing (HPC) - RSE

RSEs with a focus on High Performance Computing (HPC) have specialist knowledge
about programming models that can be used to efficiently undertake large-scale
computations on parallel computing clusters. They may have knowledge of (automatic)
code optimisation tools and methods and will understand how to write code that is
optimised for different types of computing platforms, leveraging various efficiency
related features of the target hardware. They are familiar with HPC-specific
package managers and can build dependencies from sources. They also understand the process of
interacting with job scheduling systems that are often used on HPC clusters to
manage the queuing and running of computational tasks. HPC-focused RSEs may be
involved with managing HPC infrastructure at the hardware or software level (or
both) and understand how to calculate the environmental impact of large-scale
computations. Their knowledge of how to run HPC jobs and write successful HPC
access proposals can be vitally important to researchers wanting to make use of
HPC infrastructure.

<!--
They may also be familiar with High-Throughput Computing (HTC) and manage
a network of heterogeneous compute resources, typically desktop workstations
equipped with multicore processors and possibly GPU accelerators.
They can apply their node-level performance engineering skills to maximise
the utilisation of the available resources.

Finally, they typically have expert knowledge in at least one compiled language,
and can assist domain scientists who have excellent command of scripting languages
but only a cursory understanding of compiled languages get up to speed with
compiled software.-->

#### Machine Learning(ML) - RSE
The development of research software based on machine learning (ML) requires specialised theoretical background and experienced handling of appropriate software in order to produce meaningful results.
This involves knowledge about data analysis and feature engineering, metrics that are involved in ML, ML algorithm selection and cross validation, and knowledge in mathematical optimisation methods and statistics.
ML-RSEs analyse and check the suitability of an algorithm if it fulfils the needs of a certain task and they play a main role in deciding and selecting machine learning libraries for a given task.
The increasing usage of ML in numerous scientific areas with social impact involves an emphasised awareness and consideration of possible manipulative or discriminatory influences.
At the intersection of data science [@SSIDataScience] and Data-focused RSEs, the complex way of solving problems utilising machine learning calls for this separate specialisation.

#### Web-Development RSE
This RSE is skilled in web applications, front- and/or backend, and/or building
and using APIs, for example for research data portals or big research projects.
Ideally, this RSE should also have knowledge about (web) accessibility to allow a broad
range of researchers or even the public to use the resulting applications.
Therefore a deep knowledge of web skills is a required additional skill for this RSE.

#### Legal-RSE
All RSEs are a go-to person for questions about licensing, mixing and matching of software.
But with the rising requirements from legislation,
we foresee the need for RSEs that still have a background in RSE but extend it with a knowledge of legal processes,
that cover corner cases and go beyond applying Best Practice guides.
These requirements may arise in the area of publication of research software,
as this also requires knowledge about particular laws or regulatory frameworks concerning data protection,
like the GDPR within the EU [@GDPR].
Another area are legal aspects of cybersecurity and export control in science and research (see [@ExportControl] for Germany).
Legal-RSEs focus on facilitating the achievement of technically feasible solutions while adhering to regulatory mandates.
They are able to communicate and collaborate with lawyers.

<!--
social skill-set focused specialisations
-->

# Reaching out to potential RSEs {#sec:reachout}

Many current RSEs have found their way to being an RSE during their doctoral studies.
This transition usually happens slowly.
A typical RSE development path starts off with a PhD student programming a tool that others notice and find useful.
Soon the proto RSE is known to have programming skills and is sought after to join other projects.
The researcher is now well on the way to becoming an RSE.
If they enjoy this role and would like to take it further they need to know that there is an RSE career path as well as that specialised training materials exist.
Beyond that, for an RSE it is important to be a part of a network with other RSEs, irrespective of the career level.
A perfect first step for forming this network is topic-related conferences, workshops or meet-ups.
Beyond that, there is the broader RSE community organised at the local and regional level with chapters or local/regional communities, at the national level with societies and the international RSE society.
Each of them offers possibilities for connecting within or beyond an individual institution and is a great way to find like-minded people to grow a wider network and thereby facilitate the sharing of information on interesting events or help each other out.
This available layered network can greatly benefit the RSE in finding help with issues outside of their own comfort zone
and provides a welcoming, social safety net providing a home for the RSE. Since we feel providing aspiring RSEs with this net
is of utmost importance we envision compulsory events introducing that to young RSEs.
Qualification badges are another option for RSEs to find people with the same technical interests.
Structuring and institutionalising the education and structures for the add-on courses that are also open to others in academia,
will be topics of a follow-up paper.
These networks are a lifelong manifestation where RSEs work to provide an inclusive environment
for their peers and provide opportunities for life-long learning.

# Future Work {#sec:future-work}

Having the competencies is a first step to finding common ground around which to structure
curricula, institutions, and teachers in this framework.
Applications of them in an individual's career can be found in the appendix.
An omission that we found and that we would like to highlight in order to spark a community discussion,
is that RSEs that choose explicitly a science supporting role outside of research will not be eligible
for funding under the statutes of a lot of funding organisations that require a PhD at minimum.
To alleviate that and give RSEs in leadership positions a means
to become eligible for funding themselves we propose the introduction of a "science enabling doctor"
that can be handed out on an honorary basis by certain institutions.
Beyond having that discussion, a diverse set of publications is already in the making.
Next, we will work on how to institutionalise education.
Here we will detail how we organise our institutions and what qualifications our teachers
need to have in order to effectively communicate our values.
We will put forward ideas on how to build up bachelor's and master's programmes,
of which a glimpse can already be found in this paper's appendix.
We will show how we intend to provide the necessary continuous education for RSEs after graduation.
This publication is again intentionally free of regional specifics, to also serve
as a blueprint that other national RSE societies can build upon.
Another important building block is to provide people with online resources for use in their
courses. This is the intention of the so-called "survey-publication".
This work will not be carried out as a traditional publication, but
this survey of existing resources will be made available as a
continuously evolving online resource.
And finally, we will formulate the call to action - building on the previous
publication on the necessary institutions,
to lay down what is required to best support the continuous need
for young RSEs to support digital science specifically in Germany.

# Conclusion {#sec:conclusion}

This paper started from a community workshop at deRSE23 in Paderborn
where people working in RSE related fields got together to figure out
structures and ideas for educating newcomers to this field.
One outcome of this diverse gathering is that RSEs from far away fields gather
around similar core concepts but at the same time share a vision of how to
update the scientific ecosystem to the age of digitalization.
In this publication, we have tried to formalise these concepts.
We have formulated a set of values that guide our actions in society,
manifestly making RSEs part of the scientific community that shares the ideals of good scientific practice,
but at the same time,
being Software Engineers, we cherish that we have to take responsibility for our tools.
We continue with core competencies that have been intentionally formulated
abstractly without referencing any particular information processing device.
As expected, we draw equally upon notions from software engineering and research,
but find that we likewise require teamwork capabilities.
We continue with detailing these competencies in various dimensions and find that
a different amount is required in different positions and scientific domains.
Nevertheless, they are required and hence the values and competencies form a common denominator
that unifies RSEs and enables them to identify with this domain that will become critically
important for many areas of science.
These competencies at the intersection of research and software engineering
coupled with a firm belief in team processes makes RSEs sought after on the job market
and their values make them responsible members of a digital society.
This yields a qualification profile which makes
an education based on it highly attractive to young people.
At an institutional level, research performing organisations have a growing
interest in fostering RSE training to support the use of FAIR data and FAIR software in the academic world,
a direction determined by new incentives created by scientific journals and librarians.
How we update existing institutions and set up new ones
that provide this education will be the topic of a follow-up paper.

# Appendix {#sec:appendix}

## An Example Master's Programme for Research Software Engineering {#subsec:examplemaster}

The target audience for such a master's programme would be students holding a bachelor's degree from
a domain science, which we will call "home domain" in the following. There is explicitly
no restriction on the candidates' home domain, it may be from the STEM disciplines, life
sciences, humanities or social sciences. Candidates with a bachelor's degree in computer science are also
explicitly included, although we acknowledge that their master's programme should include adaptations
to make their interaction effective with other domain scientists.
In order to give the future RSE the necessary breadth we expect this to be a four semester curriculum.

The curriculum is formed from a combination of modules,
some of which are core modules teaching essential skills that must be completed by all students.
Other modules introduce more specialised concepts and skills.
During the master's programme, students should pick an RSE specialisation from the list in this paper
and attend these additional modules to deepen their knowledge in the field.

Core modules are of course drawn from the three pillars of the RSE and can be categorised accordingly.

- Research Skills:
  - Optional Domain Mastery Module: Additional minor research courses, but students with a home-domain already have the research part well-covered.
  - Research Tools Module: Here we teach tools used to distribute and publish software, as well as introducing students to domain specific data repositories. Thereby gaining foundational knowledge in (SRU, SP, DOMREP).
  - Meta-Research Module: Here we teach people how research works. The research life cycle is introduced, as well as the data life cycle and the software life cycle are abstractly introduced.

- Software Engineering Skills:
  - Foundational Module: Here we have an introduction to programming: Students learn at least two languages: a language that facilitates prototyping and data processing (e.g., Python or R) and a language for designing complex, performance-critical systems (e.g., C/C++). This exposes them to computers in a hands-on fashion and is the foundation for (DOCBB, LIBS).
  - Digital Ecosystem Module: Programming languages are not enough to work in a digital ecosystem, hence we require something like Software Craftsmanship, where tools like the Unix Shell, version control systems, Build Systems, Documentation generators, Package distribution platforms, and Software Discovery systems are taught to strengthen skills in (LIBS, DOCBB, SWREPOS, SRU).
  - Software Architecture Module: Here we teach Software Design and Software Engineering, again strengthening (DOCBB, LIBS) on a more abstract level.

- Communication Skills:
  - Project Management Methods: Here we teach project management methods that are useful in science, such as agile ones(PM).
  - Communication Skills Module: Here we have courses focusing on interdisciplinary communication, interacting across cultures, communication in hierarchies, supporting end users effectively. These are all facets of the (USERS) skill.
  - Teaching Module: This module covers topics to effectively design courses and teaching material for the various digital tools, thereby strengthening the (TEACH) skill.

Given that RSE work also involves a lot of craftsmanship skills,
hands-on practice is an integral part of the curriculum.
At least two lab projects are required within the mandatory curriculum.
These should be executed as a team and involve a question from a domain science.
We recommend covering both the candidate's home domain as well as another domain of science.
Ideally, projects stem from collaborations with scientists within the institution and RSE
students take the role of a consultant. This setup strengthens the (TEAM, TEACH, USERS) skill
and most likely also the (MOD) skill through interaction.

To emphasise the exposure to domains outside of their bachelor's degree domain,
we recommend that RSEs also support their non-home-domain project by supporting it with introductory
courses from this discipline. We support the idea of broadening the interaction with other domains even more.
This schools their ability to quickly adapt their vocabulary and thinking to other disciplines. This is an aspect of (MOD).

To align with the specialisations listed in this paper, example optional modules include topics on
HPC engineering/parallel programming, numerical mathematics/scientific computing, web technologies,
data stewardship, AI models/statistics, and community management/training.

The programme is finalised with a master's thesis which should be dual-supervised by an
RSE supervisor from an actual project, and a domain supervisor.
The thesis should answer a relevant research question (strengthening (NEW)) from the domain using computational methods.
Software development is required, and the code is part of the gradable deliverables.
The RSE supervisor ensures and grades the software craftsmanship aspects of the project.
This setup ensures that we are grading the effectiveness of applying RSE skills in an actual research environment.

## An example of a possible career path {#subsec:examplecareer}
#### Setting the stage

Meet Kay, Kim's younger sister [@Anzt2021] who currently studies researchology in a bachelor's programme in the established domain of researchonomy at University of Orithena (UofO).
We will follow Kay’s fictional career to illustrate how education, job-experience and a career in academic institutions could lead to become a successful RSE.
In Kay’s world, some of the measures proposed in this paper have already been implemented.

#### Bachelor's Degree

Through a program like Software Carpentry [@CarpentriesSoftware] or The Missing Semester [@Athalye2023],
Kay learns about using computational tools to support the sophisticated statistical analysis typical for researchology.
She uses those tools to create and automate the steps of processing data and producing outcomes for her bachelor's thesis
(generating plots with matplotlib and even CI for automatic building)
and takes pride in a fully open and reproducible bachelor's thesis enabling her to graduate with honours from the faculty of researchonomy.

#### Master's Degree

Kay ponders whether to continue with computational researchology, which her bachelor's supervisor is responsible for,
or enrol in a domain-agnostic RSE master's programme.
Researchers in computational researchology need to acquire a large part of the general RSE know-how presented
in this paper and specialise in Quantum-Accelerated Bayesian Optimisation methods.
However, Kay decides to go for the more generic route of a dedicated RSE programme because she wants to continue in academia,
but does not like the idea of becoming stuck with one research topic.
She also experienced the immediate satisfaction gained by helping colleagues from her research group with tricky technical problems,
which makes her happier than the subdued sense of achievement from having a research paper accepted long after she had written it.
For her, coding and sharing knowledge in the form of software is of similar importance to writing a paper focused mostly on the obtained results.

The domain-agnostic RSE Master programme consists of a core of RSE topics with various electives for specialisation, some of them domain-specific (e.g., chemistry) or topic-specific (e.g., cloud computing for research).
Kay chooses digital archaeology and develops a pipeline for reconstructing 3D models from ground penetrating radar data, to simplify the process for archaeologists (Reproducibility, Big Data, Machine Learning).
The project management skills that are being taught as part of the core RSE curriculum really help her to not get lost in this project.
Apart from working with the researchers in her archaeology group,
she has to work with members of the central RSE department to help her with the pipelines.
She also has to liaise with the central IT department to organise storage for the large data sets.
Towards the end of the programme, she visits her first RSE conference where she sees a lot of notions (SWLC, RC) in action
that so far have been abstract in her master's degree.

The exposure to the wider RSE community inspires her to invest additional time into her thesis to publish
her software project under a license approved by the Open Source Initiative and write an accompanying article in the open source journal JOSS[@JOSS].
Kay has now completed the RSE programme and has reached Junior RSE level.

#### Junior RSE

Kay finds a position in the central RSE department at her university with a competitive IT salary.
Although the contract is temporary, there is a good chance that it will lead to a permanent position.
Kay completes the Software Carpentry Instructor training and teaches basic research computing,
while advising fellow students of her department on better programming (DOCBB and MOD skill).
She also runs a seminar in the RSE Master's programme. She publishes a condensed version of that in JOSE[@JOSE].
During her teaching duties, she becomes aware of a new project in her department that requires a community manager RSE
and she gladly signs up to focus more on her communication skills.
After three years, she takes an exciting opportunity to work in another university.

#### Senior RSE

The new position involves taking responsibility for the RSE related aspects of a large inter-organisational project involving different organisations.
With her new responsibilities comes a shift in the importance of various aspects of her work.
Having this position in an inter-organisational project places far more emphasis on communication and organisation skills.
She is spending time teaching people (TEACH skill) to onboard them into the project.
There is a lot of interaction with different stakeholders in the project like funders and user groups (USERS skill).
To oversee the project, she uses an amalgam of both agile and traditional project-management concepts and methods which she acquires on-the-job (PM skills).
Her work so far has already been heavy on (TEAM) skills, but now also the leadership aspect comes into play.

#### RSE-focused Principal Investigator

The job experience as a leading RSE for a large project was the last requirement necessary to be awarded the title of a "Certified Research Software Professional" (CRSP) 
from an institutionalised centre of RSE education.
The certificate confirms her track record of valuable software contributions
and of teaching and mentoring people,
as well as her capability to enable, foster and contribute to high-quality research in a leading position.
It is recognised by various funding agencies, such as the DFG, and hence enables RSEs to act as a Principal Investigator for RSE-focused grant applications. It is also recognised by many prestigious universities and opens many career options that are also typical for PhDs.
Kay can now write her own grant proposals to effectively fund work of moving research software projects from prototypes to infrastructure.

## Existing Frameworks

### HPC skills and certification

As an area that generally requires a range of advanced skills,
High Performance Computing (HPC) is one field where there is ongoing work
to identify relevant sets of skills for HPC practitioners and potential paths
to develop these skills. The HPC Certification Forum [@HPCCFCompetencies] has
developed a competence standard for HPC that defines a range of skills and
how they are related in the context of a skill tree [@Kunkel2020a; @Kunkel2020b].
This competence standard is currently being built upon by the CASTIEL 2 [@CASTIEL2] project
in collaboration with initiatives funded by the European High Performance Computing
Joint Undertaking (EuroHPC JU) to create a framework for HPC certification [@EuroHPCJU2023].
While this framework focuses mostly on skills specific to HPC, there are a couple of similarities
to the framework proposed in this paper. The "SD: Software Development" skill set
is very similar to the Software Engineering skills discussed in @sec:required-generic-skills,
describing a wide range of such skills.
This skill set contains
Programming Best Practices (SD2), Software Configuration Management (SD3), Software Quality (SD5),
Software Design and Software Architecture (SD6), and explicit mention of documentation (SD7, see our DOCBB).
Besides the Software Concepts for HPC (SD1), which mainly concerns HPC-focused RSEs,
most of the skills contained in the SD2-SD7 categories apply to all RSEs.
A significant difference compared to the framework proposed in this paper is
the absence of skills related to research or communication.
Noteworthy is already now the level of detail in their skill tree which is more similar to @subsec:examplemaster.

Also looking at pathways and how different skills are related,
the UNIVERSE-HPC project [@UNIVERSEHPC], funded under the UK's ExCALIBUR
research programme [@EXCALIBUR], is looking to understand and develop
training pathways to support the development of specialist skills in the HPC
and exascale domains. The project is gathering open source training materials
to develop curricula that support the training pathways that are underpinned
by high-quality training materials.

### Bioinformatics skills and certification {#subsec:emblbio}

Bioinformatics is another field that actively works on developing skill trees.
The Bioinformatics Core Competencies [@Mulder2018; @Welch2016; @Welch2014],
the BioExcel competency framework [@Matser2016],
the PerMedCoE competency framework [@Lloret-Llinares2021],
the Research Data Management and Data Stewardship competence framework [@Demchenko2021]
and the ELIXIR Data Stewardship Competency Framework for Life Sciences [@Scholtens2019]
are examples of grassroots efforts aiming at defining the set of skills
of various bioinformatics specialities,
one of them as a taxonomy [@Mulder2018].
These frameworks eventually converged into the EMBL-EBI Competency Hub
[@CompetencyHub; @Lloret-Llinares2022],
where typical RSE and bioinformatician profiles at different levels
of seniority can be queried
(e.g. [Junior RSE](https://competency.ebi.ac.uk/framework/bioexcel/3.0/profile/view/10115/alex-2),
[Senior Computational Chemist](https://competency.ebi.ac.uk/framework/bioexcel/3.0/profile/view/10121/kim-0))
and compared against one another
(e.g. [Junior vs. Senior RSE](https://competency.ebi.ac.uk/framework/bioexcel/3.0/profiles/compare/10115/10117)).

Competencies can be divided into more fine-grained building blocks:
knowledge, skills and abilities (KSAs). They can be organised in a taxonomy,
and are also transferable, i.e. a KSA can be a pre-requisite to multiple competencies.
The Mastery Rubric for Bioinformatics [@Tractenberg2019] and the ELIXIR
Data Stewardship Competency Framework for Life Sciences [@Scholtens2019]
are examples of KSA frameworks for bioinformatics curricula.

The Curriculum Task Force of the International Society for Computational
Biology (ISCB) curates a database of degrees and certificates
in bioinformatics [@BioinformaticsCertification; @Mulder2018].
The database includes bachelor's and master's degree programs and specialisations,
PhD programs, and certificates from graduate schools.

BioExcel has research competencies that combine some of our research competencies and some notions from the communication skills.
Their computing competencies roughly map to our software skills.
Here, we find competencies such as "Package and distribute Software", which maps to our (LIBS) competencies,
and "comply with licensing policy", which would in our framework be part of (SP) in the research competencies.
In addition, they have a dedicated parallel computing competency section,
thereby shifting the emphasis of the knowledge of their computational tools towards the HPC-RSE specialisation in our framework.
Career profiles, such as the computational chemist, bring additional domain specific knowledge;
we would classify those as a mixture of DOMAIN-RSE and HPC-RSE.
It is noteworthy, however, that the BioExcel framework puts very little emphasis on communication skills, which are often involved in RSE-related tasks.
