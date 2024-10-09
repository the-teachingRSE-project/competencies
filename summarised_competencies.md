---
title: "Foundational Competencies and Responsibilities of a Research Software Engineer - A summary"
geometry: "top=0.5cm,right=2.5cm,bottom=2.5cm,left=2.5cm" # Only for the title page, see include-before for the rest.
author:
  - The teachingRSE project

output:
  pdf_document:
    citation_package: biblatex
    toc: true
    number_sections: true
secnumdepth: 3
biblatexoptions: [alldates=iso]
bibliography: bibliography.bib
header-includes:
  - \input{preamble.sty}
  - \usepackage{pdflscape}
  - \usepackage{multirow}
  - \usepackage{array}
  - \usepackage{longtable}
  - \usepackage[inkscapepath=svg-inkscape]{svg}
  - \pdfsuppresswarningpagegroup=1
  - \newcommand{\blandscape}{\begin{landscape}}
  - \newcommand{\elandscape}{\end{landscape}}
  - \newcommand{\fonticon}[2]{\includesvg[height=1.5ex]{{../fonts/#1}}\nobreakspace{}#2}
  - \newcommand*{\DOCBB}{\fonticon{sitemap}{DOCBB}}
  - \newcommand*{\DIST}{\fonticon{boxes-packing}{DIST}}
  - \newcommand*{\SWLC}{\fonticon{arrows-spin}{SWLC}}
  - \newcommand*{\SWREPOS}{\fonticon{code-pull-request}{SWREPOS}}
  - \newcommand*{\MOD}{\fonticon{laptop-code}{MOD}}
  - \newcommand*{\NEW}{\fonticon{lightbulb}{NEW}}
  - \newcommand*{\RC}{\fonticon{graduation-cap}{RC}}
  - \newcommand*{\SRU}{\fonticon{recycle}{SRU}}
  - \newcommand*{\SP}{\fonticon{newspaper}{SP}}
  - \newcommand*{\DOMREP}{\fonticon{folder}{DOMREP}}
  - \newcommand*{\TEAM}{\fonticon{user-group}{TEAM}}
  - \newcommand*{\TEACH}{\fonticon{chalkboard-user}{TEACH}}
  - \newcommand*{\PM}{\fonticon{clipboard-list}{PM}}
  - \newcommand*{\USERS}{\fonticon{comments}{USERS}}
  - \usepackage[acronym,toc,shortcuts,nogroupskip]{glossaries}
  - \newglossary[skills.glg]{skills}{skills.gls}{skills.glo}{Skill codes}
  - \makeglossaries
  - \input{glossary.tex}
  - \newglossaryentry{DOCBB}{name={\DOCBB},type={skills},description={Creating documented code building blocks}}
  - \newglossaryentry{DIST}{name={\DIST},type={skills},description={Building distributable software}}
  - \newglossaryentry{SWLC}{name={\SWLC},type={skills},description={Adapting to the software life cycle}}
  - \newglossaryentry{SWREPOS}{name={\SWREPOS},type={skills},description={Use software repositories}}
  - \newglossaryentry{MOD}{name={\MOD},type={skills},description={Software behaviour awareness and analysis}}
  - \newglossaryentry{NEW}{name={\NEW},type={skills},description={Conducting and leading research}}
  - \newglossaryentry{RC}{name={\RC},type={skills},description={Understanding the research cycle}}
  - \newglossaryentry{SRU}{name={\SRU},type={skills},description={Software re-use}}
  - \newglossaryentry{SP}{name={\SP},type={skills},description={Software publication and citation}}
  - \newglossaryentry{DOMREP}{name={\DOMREP},type={skills},description={Using domain repositories/directories}}
  - \newglossaryentry{TEAM}{name={\TEAM},type={skills},description={Working in a team}}
  - \newglossaryentry{TEACH}{name={\TEACH},type={skills},description={Teaching}}
  - \newglossaryentry{PM}{name={\PM},type={skills},description={Project management}}
  - \newglossaryentry{USERS}{name={\USERS},type={skills},description={Interaction with users and other stakeholders}}
include-before:
  - \newpage
  - \newgeometry{top=2.5cm,right=2.5cm,bottom=2.5cm,left=2.5cm}
include-after:
  - \printglossary
  - \printglossary[type=skills]
  - \printglossary[type=\acronymtype]
xnos-cleveref: True
xnos-capitalise: True
toc-baselinestretch: 0.85
keywords:
  - research software engineering
  - RSE
  - competencies
  - curriculum design
  - teaching
acknowledgements-before: ""
acknowledgements-after: "
We appreciate the comments and suggestions from Yves Vincent Grossmann,
Wilhelm Hasselbring, and Bernhard Rumpe.
"
abstract: "
The term Research Software Engineer, or RSE,
emerged a little over 10 years ago as a way to represent
individuals working in the research community but focusing on software development.
The term has been widely adopted and there are a number of high-level definitions of what an RSE is.
However, the roles of RSEs vary depending on the institutional context they work in.
At one end of the spectrum, RSE roles may look similar to a traditional research role.
At the other extreme, they resemble that of a software engineer in industry.
Most RSE roles inhabit the space between these two extremes. Therefore, providing a straightforward,
comprehensive definition of what an RSE does
and what experience, skills and competencies are required to become one is challenging.
In this community paper we define the broad notion of what an RSE is, explore the different types of work they undertake, and
define a list of foundational competencies as well as values that outline the general profile of an RSE.
Further research and training can build upon this foundation of skills 
and focus on various aspects in greater detail. 
We expect that graduates and practitioners will have a larger 
and more diverse set of skills than outlined here.
We look at specific types of RSE roles, propose recommendations for organisations, and give examples of future specialisations.
"
---

# Introduction {#sec:introduction}

Computers and software have played a key role in the research life cycle for many
decades.
They are now vital elements of the research process across almost all domains.
They enable researchers to collect and process ever-increasing amounts of data,
simulate a wide range of physical phenomena across previously unexplored scales of the universe,
and discover previously inconceivably complex structures in nature and societies via \ac{ML}.
This prevalence of computation and digitally-aided data analysis in research means that
digital skills are now required by researchers at all
career levels, and in fields significantly beyond those that would previously
have been expected.
Research software is now used and developed not only in \ac{STEM} domains,
but also in other fields, like medicine and the humanities.

Researchers often lack the skills to use specialised software
for their research, let alone write it [@NamingPain]. If they come from a non-technical domain, they may
also struggle to know what to ask when trying to request help from and interact with
more experienced colleagues. A gap still exists in
academic education, as many curricula do not sufficiently prepare students
in this regard. This situation is exemplified by the extracurricular \ac{MIT} class
"The Missing Semester of Your CS Education" [@MIT], which aims to increase 
"computing ecosystem literacy" even among students of Computer Science at \ac{MIT}.

Researchers investing increasing amounts of their time developing their \ac{SE}
skills to support their research work can find themselves with little time to do the research
itself.
This, in turn, presents career development challenges since the experience required to gain
and progress in research and academic roles is traditionally assessed through metrics that
do not directly include software outputs.
A recent shift towards the establishment of the distinct role of a
_"Research Software Engineer"_ [@WhatResearchSoftware]
(RSE, a term that was coined in the \ac{UK} a little over 10 years ago [@Hettrick2016]),
now provides a base on which sustainable career opportunities can be (and are being) built,
allowing for better training of researchers and more effective support for the development of high
quality research software.
There is still a long way to go, but positive change is well underway.

RSEs may work within one of the increasing number of research software engineering teams that
have been set up at universities and research
organisations over the past decade, or they may be embedded within a research
team. They may have a job title that officially recognises them as an RSE, or
they may have a standard research or technical job title such as Research
Assistant, Research Fellow, or Software Engineer. Regardless of their job title,
RSEs share a set of core skills that are required to design and develop research software, understand
the research environment, and ensure that they produce sustainable, maintainable
code that supports reproducible research outputs, following the \ac{FAIR} principles [@FAIR4RS].

This community paper defines a set of core values and foundational competencies,
which an RSE should acquire during training and formal education.
These skills are formulated independently of a specific research domain 
and current technical tools used to support the application of the skills.
By defining these competencies,
we provide a guiding framework to facilitate
the training and continuous professional development of RSEs,
thus helping to provide a positive impact on
research outputs and, ultimately, society as a whole.
These competencies draw upon skills from traditional SE practice,
established research culture, and the commitment to being part of a team.
However, we see this set of skills as a foundation to build upon. 
We envision that through specialised training, the set of skills 
of graduate RSEs and domain researchers will grow. 
This is underlined by a growing interest to perform RSE research, 
i.e. research into methods and tools more catered to the unique 
challenges that research software provides.

While this community paper is based on workshop discussions that were attended
largely by RSEs (deRSE23 in Paderborn, un-deRSE23 in
Jena, and deRSE24 in Würzburg, all in Germany),
we believe that the competencies formulated here can offer far-reaching
impact beyond the domain of RSE into adjacent aspects of research and, indeed, the wider research community.
This is especially important given that much research involves some amount of
data management, processing and visualisation, or the creation of tools for these tasks,
and funding bodies and computing infrastructure providers will sometimes prioritise projects that generate archived,
annotated, re-usable, and potentially remotely executable data.
In particular, funding agencies and research managers will find the discussion in this paper
valuable in order to discover where RSEs see their place in the existing landscape of scientific domains
and how to support the work of RSEs at different positions and career levels.

This paper is a condensed version of a more comprehensive paper published at FIXME:INSERTREFHERE .
A non-exhaustive overview of similar initiatives can be found in FIXME:INSERTREFHERE .
In this paper, we start to elaborate in
@sec:values on the values that
provide the guiding principles for the work of an RSE.
@sec:required-generic-skills defines a set of core skills based on these values.
We categorise these skills into three pillars, namely
"software/technical", "research", and "communication" skills,
reflecting the hybrid nature of an RSE.
To justify the selection of these skills,
we also list some current tasks
and discuss the skills used therein.

As with any general skill set, not all RSEs will need
to use all the skills highlighted to the same level of expertise.
But the Discussion of how much a person
needs to know depending on their education or career level
or on the type of projects they would like to be involved with can be found in FIXME:INSERTREFHERE .
Also, the overview of what skills and limitations
an RSE in different team structures typically has, and
recommendations for organisations that need to support RSEs is in expanded paper in FIXME:INSERTREFHERE .
@sec:rse-specialisations provides a list of RSE specialisations
and discusses the level of skill needed to work in each of them,
before we conclude the paper with details of future work in @sec:future-work
and conclusions in @sec:conclusion.

## Terminology

### The term Research Software Engineer

Research Software Engineering can be considered an interface discipline,
 linking traditional Software Engineering with Research itself [@Lamprecht2024-giradar].
Due to this nature there is a plethora of different variations of RSE depending on the particular Research domain they are working in.
Therefore the broad notion of Research Software Engineers is better thought of as a collection of sub-communities.
The term Research Software Engineer is made more difficult to grasp
 since an internationally recognised definition is still missing.
While there is consensus about the general notion that an RSE is a person with one leg in their research domain and the other in software development,
 this spans a whole spectrum depending on which one is more emphasised.
There is also the question of what level of professionalism concerning both non-SE research and SE is expected.
A more inclusive definition allows more people to self-identify as RSEs,
 thereby also fostering an inclusive community of people working in digital science (see also @sec:values on the values of an RSE).
RSEs fall therefore somewhere on the spectrum between a researcher at one end and a software engineer at the other.
Common to all of them is, that they need to be able to work in the research environment the software is used in, ideally at eye-level with native researchers, but at least as close as possible.
RSEs often need to deal with non-technical complexities that are characteristic for research environments:
 organisational, motivational, with respect to the size of projects, independence and heterogeneous goals of stakeholders, boundary conditions for funding and future funding, to name just a few.
Summarising, RSEs have skills and experience in three important areas: in the research area(s) their software is used in, in software engineering topics, as well as in interdisciplinary communication.

### Further definitions

Depending on the national research
environments and processes that readers are familiar with, the notion of the terms *software* and *research* might differ.
Therefore, to avoid ambiguities, we define these as follows:

**Software**: Source code, documentation, tests, executables
and all other artefacts that are created during the development process
that are necessary to understand its purpose.

**Research software**: Foundational algorithms, the software itself,
as well as scripts and computational workflows that were created
during the research process or for a research purpose, across all domains of research.
This definition is broader than in [@FAIR4RS] and is the outcome of a recent
discussion in [@Gruenpeter2021].

**Research software engineers**: People who
create or improve research software and/or the structures that the software interacts with
in the computational environment of a research domain.
They are highly skilled team members who may also choose to conduct their own research as
part of their role.
However, we also recognise that many RSEs have chosen specifically to focus on a technical
role as an alternative to a traditional research role because they enjoy and wish to focus
on the development of research software.

**Researchers**:
People who are using the services provided by Research Software Engineers.
This, on purpose, is a very broad definition and was chosen for easier readability.

# Values {#sec:values}

It is important that the activities of an RSE are guided by ethical values.
In addition to the values for good scientific practice [@dfg_gsp], RSEs also adhere to
the \ac{SE} Code of Ethics [@Gotterbarn1999].
Central to that code is the RSE's obligation to
commit to the health, safety and welfare of the public and act in the interest of society, their employer and their clients.
Further values loosely based on that code include the obligations

+ to commit to objectivity and fact-based, honest research conclusions,
+ to promote openness and accountability in the research process,
+ to take great care to develop software that adheres to current best practices,
+ to judge independently and maintain professional integrity,
+ to treat colleagues and collaborators with respect and work towards a fair and inclusive environment, and
+ to promote these values whenever possible and make sure that they are passed on to new practitioners.

The deployment of computer-based modelling and simulation has dramatically changed the practice of science in a large number of fields.
It has enabled the hitherto impossible study of new classes of problems,
often replacing traditional experimentation and observation.
It can also serve to integrate a communal body of knowledge [@Parker2022].
Humphreys [@humphreys_extending_2004] regards this development as "more important than the invention of the calculus in the 1660s, an event that remained unparalleled for almost 300 years".
The epistemological status of computer modelling and simulation is still the subject of debate,
which ranges from the postulate of a new process of knowledge creation that has its own, unique, epistemology [@winsberg_sanctioning_1999]
to the perception that from a philosophy of science perspective, there is nothing really new [@frigg_philosophy_2009].
In any case, it is clear that a number of decisions in the construction of a simulation-model
will have a significant impact on the adequacy for purpose [@bokulich_data_2021] of the model.
These decisions include the selection of the salient characteristics of the system to be modelled,
the choice of the mathematical representation of the processes to be represented,
the choice of numerical methods and other algorithms
and even including the design of the user-interface.

The relationship between initial state, inputs and final state of a computer simulation is "epistemically opaque" [@humphreys_extending_2004],
in that not every step of the process is directly observable.
The current trend of an increasing application of computationally irreducible systems, such as those based on artificial neural networks,
further exacerbates this inherent limitation of explainability.
An RSE usually takes a pivotal role in assessing this adequacy for purpose of a model
as well as in characterising and communicating the domain of its legitimate application
and its limits of interpretability.
This role, together with the enormous reliance on modelling and simulation of scientific results,
as well as real-world decision-making,
places a large responsibility on the RSE.
It is important that RSEs are aware of this responsibility and continuously improve their capabilities to live up to it.

Research software is also well on its way to being ever-present in data-driven research, in all research fields.
This can probably be most prominently seen by considering software used to analyse data, e.g. within experimental research.
It is not unusual for RSEs to support those more research data oriented efforts as well.
Here, specifically, they closely interact with research data management professionals
and practices by designing research software 
that is better able to adhere to the \ac{FAIR} principles for research data,
but also to follow similar rules for research software (FAIR4RS [@FAIR4RS]).
As such, they are then familiar with special requirements stemming from the field itself, e.g., in medical research, and with privacy related issues especially for personal data, e.g., for conducting surveys.

RSEs often assume a multifaceted role at the junction of research, \ac{SE} and data management.
They work with a varying and diverse set of colleagues that might include other developers,
support unit staff and academics of different fields and all career stages.
This situation yields a specific set of challenges RSEs should be aware of
to consciously make ethically sound judgement calls.
We list some example areas that highlight present-day challenges.

<!---
## Current challenges

### Handling of data and personal data

A lot of RSE work involves the manipulation or creation of data processing tools.
We highlight that professional conduct requires these creations to be reliable and to maintain data integrity.
In particular, the way that personal data is handled can have far-reaching implications for society.
Independent of the encoding into the respective national law in an RSE's jurisdiction,
the right to information privacy is internationally recognised as a fundamental human right,
e.g., in the European Convention on Human Rights [@CouncilOfEurope-ETS005-2021; @Hirvela2022].
RSEs need to be aware of this topic's importance
and deal with tensions that might arise with researchers' desire for trouble-free sharing of data, thereby expecting openness about the research process,
versus the integrity expectations of the society towards \ac{IT} systems.
Handling personal data also has ramifications for information security considerations during the software development process.
Data protection is a complex topic, so RSEs should be aware that they may need to consult external expertise, for example when dealing with
special topics such as cryptography or re-identification attacks [@Henriksen2016].


### Mentoring and diversity {#sec:mentoring-and-diversity}

RSEs are often experienced professionals who work closely with and provide technical training and guidance to early career researchers.
Similarly to academic supervisors, they bear a certain responsibility to guide and advise less-experienced colleagues
with respect to career development and the achievement of academic goals.
This can take the form of supervising a student or mentoring a fellow RSE.
The RSE needs to be aware of the biases arising from the sociological imbalances in research and academia.
According to the \ac{UNESCO} Science Report [@Schneegans2021] women account for 33.3% of all researchers.
60.2% of researchers come from high-income countries which account for 17.5% of the global population in 2018.
Furthermore, the socioeconomic background of academics is not representative of the general population, for example in the US a tenure-track academic is 25 times more likely to have a parent with a PhD [@Morgan2022].
Thereby, to promote their values of an honest, open, and inclusive research space, they should be aware of
the diversity problems and help to mitigate them whenever they have the chance to do so.

### Shaping digital science

Through writing research software, RSEs have a pivotal position in the process of scientific production.
Their choices might determine whether the respective research is reproducible or not,
whether the results can be re-used, whether future research can build on existing tools or has to start from scratch.
Builders of larger research-infrastructure projects determine to some extent the possibilities and limitations of future research
and therefore need to be able to make a value-based judgement on topics
such as open science, path dependence, and vendor lock-in.


### Addressing environmental sustainability within planetary limits

The last two decades saw transistor technology approach the limits of attainable miniaturisation, 
and maximum chip clock frequency begin to plateau [@Sutter2005].
Nevertheless, a misleading belief in limitless growth of computing capabilities
(storage, computing power, transfer speed) is still widespread within popular perception.
A practical consequence of this is an ever-growing demand for resources to cover
the expanding need of storage and processing, with no clear deceleration in
sight (e.g. the IEA estimates a doubling in data centres energy consumption from
2024 to 2026 [@IEA2024]). At the same time, current science is well aware of

several planetary boundaries being exceeded due to human activities [@Richardson2023].
Data processing, storage and transfer account for a non-negligible fraction [@IEA2024].
Demands to move resource consumption to a sustainable rate are well justified and supported by science [@Sills2019].

RSEs have the opportunity to contribute to this effort by, for example,
choosing computationally adequate approaches (e.g. recognising where a
proven statistical method may suffice in place of a power-hungry AI model,
or configuring a test pipeline to minimise redundancy), and embracing data
frugality measures (e.g. recognising sufficient resolution when sampling data
for processing or storage). If past computational solutions were frugal because
of technological limits, in future they should tend to that by virtue of an
awareness of what may be adequate. The \ac{GREENER} principles [@Lannelongue2023] suggest how
these concerns can be addressed and how research computing can become more environmentally
sustainable.

### Emerging challenges

RSEs often operate at the cutting edge of technological development
and therefore might have to deal with technologies of which the dangers and drawbacks are still poorly understood.
A current example is the rush for the application of \acp{LLM},
where RSEs working in these fields should stay up-to-date and be able to help researchers assess topics
such as training-data bias, \ac{LLM} "hallucinations" or malicious use, with the greater goal of
making these powerful tools work for the welfare of society.

--->

# Foundational RSE competencies {#sec:required-generic-skills}

The role of an RSE lies somewhere on the spectrum between that of a researcher
(the "R") and a software engineer (the "SE") and, therefore, requires
competencies in both fields. RSEs typically have a background in research or software engineering,
but they definitely have obtained broader knowledge in both fields.
Even when working as the only RSE on a task or project, they typically apply
their knowledge and experience as part of larger teams of researchers and
technical professionals, which allows them to cultivate this hybrid nature.
There are many ways to categorise the competencies of an RSE. We chose to
distribute these competencies over three pillars to reflect the fact
that RSEs are both competent researchers (the research skills,
@sec:research-skills) and software engineers (the software/technical skills,
@sec:software-skills). The third pillar (communication skills,
@sec:communication-skills) forms the bridge between the former two
categories, with a particular focus on the software and
research cycle and the scientific process. These competencies are relevant in a
broad setting and form the foundation for specific specialisations.
These competencies have been chosen in order to make RSEs contribute to an open and inclusive research
environment, with tools that respect their professional values.

These skills and competencies come into play in various forms: The
RSEs themselves need to acquire and develop them as their career progresses
(**Career level**). However, some knowledge of software and data processing is
required at all academic levels and for all positions
(**Academic Progression**). The relative importance of the skills
and competencies also depends on the size of the RSE team
(**Project team size**). Finally, different sets of skills are emphasised in
the different RSE specialisations (**RSE specialisations**).


During the Paderborn workshop (deRSE23) we asked learners and novice RSEs what they would
like to have learnt. The top five items mentioned were: testing, contributing to
large projects, when or why to keep repositories private, high-quality software development, and
finding a community.
Those topics comprise combinations of the skills and competencies defined below.

## Software/Technical skills {#sec:software-skills}

\newcommand{\skillsection}[1]{\hypertarget{skills-#1}{%
\subsubsection{\glsentrydesc{#1} (\texorpdfstring{\glsentrytext{#1}}{#1})}\label{skills-#1}}}

Besides skilled researchers, RSEs are also competent software engineers.
As such, they ideally can solve complex software engineering problems and design software as a user-oriented, future-proof product.
The technical skills required by an RSE overlap to a large extent with
 the common fundamental software engineering skills (see, e.g., @Landwehr2017),
 but put greater emphasis on aspects related to achieving good scientific practice and to serving special needs of research software.
In addition, a lot of RSEs are either self- or peer taught in these skills (see, e.g., figure 14 in @Barker2023).
These skills include requirements analysis, design, construction, testing, program analysis, and maintenance of software.
On the other hand, RSEs also know how to make research software adhere to the \ac{FAIR} principles [@FAIR4RS],
 and how to achieve different levels of research software reusability (see, e.g., @ChueHong2014),
 while they have deeper understanding of the scientific context around the research software projects they work on.
To reflect this, the technical skills listed below complement competencies regarding the standard life cycle of software development (as summarised in \autoref{subsec:technical-general}) with RSE-specific focus skills. 

\subsubsection{Classical software engineering skills}\label{subsec:technical-general}

To summarise the vast range of the skills a software engineer is typically equipped with,
we refer to the Guide to the Software Engineering Body of Knowledge (@swebok_2014).
Because research software engineering is an interface discipline,
RSEs are often stronger in topics more commonly
encountered in research software contexts (e.g., mathematical and engineering foundations)
than in other areas (e.g., software engineering economics).
However, they bring a solid level of competence in all software engineering topics.
Therefore, RSEs can set and analyse software requirements in the context of
open-ended, question-driven research. They can design software so that it can sustainably grow, often
in an environment of rapid turnover of contributors. They are competent in implementing
solutions themselves in a wide range of technologies fit for different scientific applications.
They can formulate and implement various types of tests, they can independently maintain software
and automate operations of the integration and release process. They can
provide working, scalable, and future-proof solutions in a professional context and with common
project and software management techniques, adapted to the needs of the research environment.
Finally, as people who have often gained significant research experience
in a particular discipline, they combine the necessary foundations from their domain with software
engineering skills to develop complex software.

<!-- Adapting to the software life cycle -->
\skillsection{SWLC}

The traditional software development life cycle defines the stages that form the process of building a piece of software.
Initial development generally involves an analytic process where requirements and ideas are gathered and analysed (requirements engineering),
followed by formulating a plan to fulfil them (design) that is finally turned into running code (implementation).
This is accompanied by different measures of quality control (e.g., reviews, testing), validating and verifying 
that things work as expected and that they continue to do so when development progresses further. Depending on the software project, this can mean a simple "Think-before-you-do", or more elaborate and formal processes.
Often the development cycles are executed iteratively and incrementally.
The life cycle further includes periods of deployment, maintenance and further development (software evolution),
as well as software retirement.
To assess the current state and needs of the software, 
the RSE should be familiar with different maturity metrics, 
e.g. the DLR application classes [@Schlauch2018b], the research software maturity model [@Deekshitha2024] or technology readiness levels (TRLs).
Additionally, the research software life cycle extends the traditional life cycle
with \gls{software-publication}. The RSE should be aware of this life cycle
and be able to predict and cater to the changing needs of a software project as it moves through the stages.


<!-- Creating documented code building blocks -->
\skillsection{DOCBB}

The RSE should be able to create building blocks from source code that are
reusable. This ranges from simple libraries of functions up to complex
architectures consisting of multiple software packages. An important part of
enabling code reusability is the provision of sufficient information in the
form of comments within code, documentation or other means. This is vital to
ensure that developers and maintainers understand what a piece of software aims
to do and how to enable others to use the provided functionality.
This is primarily achieved through a "clean" implementation and enhanced by
documentation. Documentation ranges from commenting code blocks to using
documentation (building) tools.
It should be written with consideration for the different audiences who may need it 
depending on their goals and expertise, 
for example by following the Diátaxis framework [@Procida_Diataxis_documentation_framework].

<!-- Building distributable libraries -->
\skillsection{DIST}

The RSE should be able to distribute their code on their domain/language
specific distribution platforms. This almost always encompasses
handling/documenting dependencies with other packages/libraries. It sometimes
requires knowledge of using build 
or package management systems to enable interoperability with other projects.
In terms of usability and needs of the user community the RSE should be able
to decide whether a library or a framework is the right type of program
to build and distribute.


<!-- Use repositories -->
\skillsection{SWREPOS}

The RSE should be able to identify and use fitting public platforms (so-called software repositories or "repos")
to share the artefacts they have created and invite the public to scrutinise them in public reviews.
These software repositories usually provide facilities for software development, which 
differentiate them from the domain repositories described later.


<!-- Software behaviour awareness and analysis -->
\skillsection{MOD}

We define this as a certain quality of analytical thinking that enables an RSE to
form a mental model of a piece of software in a specific environment (program comprehension).
Using that, an RSE should be able to make predictions about a software's behaviour.
This is a required skill for common tasks such as debugging, profiling, optimising, designing good
tests, or predicting user interaction.
Many tools exist to help with understanding and evaluating existing code,
especially from a structural point of view. 
An RSE should understand their output and its implications.
An important facet of this capability relates to information security.
RSEs need to consider the safety and integrity of personal data and other sensitive information
and make sure that they do not negatively impact the integrity of their
institution's network and computing infrastructure.

## Research skills {#sec:research-skills}

<!-- Conducting and leading research -->
\skillsection{NEW}

RSEs are curious and able to conduct research, both on research software engineering,
and on their research-wise "home domain".
Senior RSEs are also able to lead research, and many RSEs have a doctorate [@hettrick_survey_2022].
Since RSEs often operate in different research fields, they also gain their reputation from their effectiveness in interacting with researchers from the same or other domains. Therefore, some curiosity together with a broad overview of the
research field is required, as this enables the RSE to learn new methods and algorithms directly from domain peers.
Similarly, a broad overview of the field of SE research 
and the growing field of RSE research enables the RSE to learn, apply, and teach
new methods and tools for improving the way they develop software. 
This curiosity, together with the ability to convert it into new ideas, is also reflected when an RSE is actively
trying out new tools or discovering related literature from adjacent domains. Lifelong learning is then no longer just a phrase but
becomes a motivation to work.

<!-- Understanding the research cycle -->
\skillsection{RC}

One of the key skills that RSEs have is their understanding of how research
works.
They embrace being part of a larger community which,
despite friendly competition, shares the common goal of gaining knowledge
to disseminate it.
Thereby they know that they are part of a bigger undertaking 
that involves many other parties in and outside their domain, 
and also that their software can be utilised at different stages 
of the research cycle by different people.
They may be asked to contribute to the ethical and regulatory evaluation of a project 
to ensure integrity of the research performed therein.
Like other researchers, RSEs are open to discussions and arguments beyond
their own expertise and appreciate the underlying principles of
good research, including publications, reviews and reproducibility.

<!-- Software re-use -->
\skillsection{SRU}

The re-use of existing assets such as libraries and pieces of code
to improve efficiency and quality
belongs to the fundamentals of software construction [@swebok_2014].
To discover software, RSEs rely on domain-specific knowledge and
domain repositories, as well as research skills, discovering related
software via software citations and metadata.
To evaluate whether the artefacts to be re-used suit their needs,
RSEs often need to consider the scientific context of their origin.
For example, a paper that references the code under consideration
might be crucial to validate its fitness for purpose or lack of suitability.
Code that incorporates research-domain specific knowledge
needs to be understood at a very detailed level
and its re-use documented to meet standards of good research practice.
Not only the technical compatibility needs to be understood and documented
(programming languages, system interoperability), but also the underlying
models and computational methods need to fit the purpose; this question
often requires wider research skills and deeper understanding of the
research domain at hand.

<!-- Software publication -->
\skillsection{SP}

Another part of \ac{FAIR} software is concerned with publishing new and derived works
and making them available for re-use by the research community and the general public.
RSEs need to have a basic understanding of common software licence types, including
proprietary and open source licences and how "copyleft" and "permissive" open
source licences differ. They should also understand compatibility between
different licences, and the ramifications for re-using and composing programs.
Beyond that, RSEs will need to properly execute the technicalities of software publishing.
These include the application of licences and copyright statements,
understanding and assigning software authorship, crediting contributors,
maintaining FAIR software metadata and publishing software artefacts.
Finally, RSEs will need to understand the principles of software citation [@smith_SoftwareCitationPrinciples2016].
This concerns both the potential for reuse of their own work,
which demands the provision of complete and correct up-to-date citation metadata for their software,
as well as their own citation obligations deriving from building on previous work in the form of dependencies.

<!-- Using domain repositories/directories -->
\skillsection{DOMREP}

Almost all research software is developed within a specific scientific domain.
Some software may be able to cross boundaries, but the majority will have a
home domain, with which it needs to be able to interact.
The RSE then needs to be aware of any domain specific repositories that will contain
data sets, catalogues, and other domain specific artefacts, in addition to software.
The RSE also needs to be aware of how their software can interact with the existing
domain-specific data repositories.
Finally, they need to be able to assess and use software repositories -
domain-specific or generic - for publishing software with the relevant metadata.

## Communication skills {#sec:communication-skills}

RSEs do not work in isolation.
They are embedded in a research group or work within a team of RSEs supporting particular research projects.
RSEs often need to interact with and facilitate communication among colleagues, clients and contractors
with a very broad spectrum of background-knowledge, specialisation, expectations, and experience whilst keeping diversity issues in mind.
Communication skills are therefore crucially important.
Team skills are also mentioned in common guides for \ac{SE} such as the software engineering body of knowledge [@swebok_2014].
However, the interpersonal and organisational skills and the capacity for adaption required to work in a research setting
warrants a much stronger emphasis on this field of competence.

<!-- Working in a team -->
\skillsection{TEAM}

Being able to work, and effectively communicate in teams is essential for RSEs.
For example, RSEs need to be able to explain particular implementation choices made and may even need to defend them.
Within a team of RSEs, code reviews improve knowledge transfer and increase team cohesion.
The team might change on a project-to-project basis and might be comprised of colleagues with very different backgrounds
including, for example, \ac{IT} staff, domain scientists and technicians working alongside software engineers.
The shared values come into play and each RSE needs to ensure that these values are lived by and passed on to others.
Senior RSEs may lead a team of RSEs.

<!-- Teaching -->
\skillsection{TEACH}

RSEs have many opportunities to teach.
These range from inducting new colleagues to teaching digital skills either through short courses,
for example from The Carpentries [@Carpentries], or entire lecture series.
RSEs may also act as mentors and consultants.
Code review also includes aspects of the teaching skill.

<!-- Project management -->
\skillsection{PM}

The RSE should have knowledge of project management processes. At some
institutes, project management tools and approaches differ between individual research groups,
but it is useful if an RSE understands general structures of a \gls{PM} scheme, or can bring in new ideas for improvement.
Project management in research software engineering poses specific challenges (see \gls{USERS}) that might require the capacity
to flexibly adapt to changing conditions and deviate from common project management methods.
Additionally, the RSE should know that SE offers various methods and approaches
specifically tailored to management of software projects and products.

<!-- Interaction with users and other stakeholders -->
\skillsection{USERS}

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



# RSE specialisations {#sec:rse-specialisations}

What we have defined above are intended to be base skills that an RSE irrespective of domain, position, and experience should know about.
There is a large variety of RSEs. They specialise in different areas,
some of which we want to present below. Many of the specialisations may overlap,
so the same RSE might for example work on data management and open science.
We categorise them into those that can be viewed as a specialisation within RSE-specific topics,
while other RSEs might expand their skill set and profession to areas that are not typical for an RSE.


## Specialisations within the core RSE competencies

#### Open science RSE
Open science and FAIRness of data and software are increasingly important topics in research,
as exemplified by the demand of an increasing amount of research funding agencies requiring openness.
Hence, an open science RSE is required to have a deeper knowledge of (\gls{RC}) and how to distribute software publicly (\gls{SRU}, \gls{SP}).
Open Science RSEs can help researchers navigate the technical questions that come up
when practising Open Science, such as "How do I make my code presentable?",
"How do I make my code citable?",
"What do I need to do to make my software \ac{FAIR}?", or
"How do I sustainably work with an (international) team on a large code base?".
Like the Data-focused RSE, they have a deep understanding of \ac{RDM} topics.

#### Project/community manager RSEs

When research software projects become larger, they need someone who manages
processes and people.
In practice, this concerns change management for code and documentation
and community work to safeguard usability and adaptability,
but also handling project governance and scalable decision-making processes.
This gap can be filled by people who invest in the (\gls{PM}), (\gls{USERS}), and (\gls{TEAM}) skills.
Building a community around a research project is an
important building block for sustainable software [@Segal2009], so these RSEs play
an important role, even if they do not necessarily touch much of the code themselves.

#### Teaching RSEs
RSEs interested in developing their (\gls{TEACH}) skill can focus on teaching the next generation of researchers and/or RSEs and will play
a vital role in improving the quality of research software.
They need to have a good understanding of all RSE competencies relevant to their domain and
additionally should have teaching experience and training in didactics and pedagogy.


#### User interface/user experience designers for research software
Scientific software is a complex product that often needs to be refined in order to be usable even by other scientists.
To facilitate this, there are people required that specialise in the (\gls{DOCBB}) and probably the (\gls{DIST}) competency
with a focus on making end-user facing software really reusable and hence \ac{FAIR}.
This task is supported by strong (\gls{MOD}) skills to reason about the behaviour of potential users of the software.

## Specialisations outside the core RSE competencies


<!--
Research focused specialisations
-->

#### \${DOMAIN}-RSE
While software is the common focus of all RSEs,
there will be RSEs that have additionally specialised in the intricacies of one particular research domain,
such as medical RSEs, digital humanities RSEs, or physics RSEs.

#### Data-focused RSE
Data-focused RSEs work at the flourishing intersection between data science and RSE.
They are additionally skilled in cleaning data and/or running data analyses and can help researchers
in setting up their analysis pipeline and/or \ac{RDM} solutions.
When the field requires research on sensitive data or information, e.g., patient information in medicine,
this RSE should have knowledge about secure transfer methods and/or ways to anonymise the data.
As part of \ac{RDM}, this RSE profile is able to support all stages of the research data life cycle [@Nieva2020], with synchronous data management processes.
Those processes implement established best practices for planning and documenting of data acquisition in a \ac{DMP}, as well as for management,
storage, and preservation of data, and publication and sharing of data in repositories according to the \ac{FAIR} principles [@FAIR].


<!--
New areas of expertise
-->

#### Research infrastructure RSE
This RSE has a special interest in \glspl{SysOp} and system administration and sets up \ac{IT} infrastructures for and with researchers.
Therefore, this specialisation on the one hand requires a deep knowledge of physical computer and network hardware and
on the other hand knowledge about setup and configuration of particular server software,
e.g., setup of virtual machines on hypervisors or the planning and setup of compute server clusters for special purposes, e.g., \ac{ML}.
As an interface between the researchers and the infrastructure, they take care of user management, access permissions, and configuration of required services.

#### HPC-RSE

RSEs with a focus on \ac{HPC} have specialist knowledge
about programming models that can be used to efficiently undertake large-scale
computations on parallel computing clusters. They may have knowledge of (automatic)
code optimisation tools and methods and will understand how to write code that is
optimised for different types of computing platforms, leveraging various efficiency
related features of the target hardware. They are familiar with \acrshort{HPC}-specific
package managers and can build dependencies from sources. They also understand the process of
interacting with job scheduling systems that are often used on \ac{HPC} clusters to
manage the queuing and running of computational tasks. \acrshort{HPC}-focused RSEs may be
involved with managing \ac{HPC} infrastructure at the hardware or software level (or
both) and understand how to calculate the environmental impact of large-scale
computations. Their knowledge of how to run \ac{HPC} jobs and write successful \ac{HPC}
access proposals can be vitally important to researchers wanting to make use of
\ac{HPC} infrastructure.


#### ML-RSE
The development of research software based on \ac{ML} requires additional specialised theoretical background and experienced handling of appropriate software in order to produce meaningful results.
This involves knowledge about data analysis and feature engineering, metrics that are involved in \ac{ML}, \ac{ML} algorithm selection and cross validation, and knowledge in mathematical optimisation methods and statistics.
Here, we use \ac{ML} in a broad sense of machine-based learning including deep learning, reinforcement learning, neuro-symbolic learning and similar.

ML-RSEs analyse and check the suitability of an algorithm. They check if it
fulfils the needs of a certain task and they play a central role in deciding on
and selecting \ac{ML} libraries for a given task.
The increasing usage of \ac{ML} in numerous scientific areas with social impact involves an emphasised awareness and consideration of possible influences and biases.
At the intersection of data science [@SSIDataScience] and data-focused RSEs,
the complex way of solving problems utilising \ac{ML} calls for this separate specialisation.

#### Legacy RSEs
Research software may have evolved over generations of researchers without change management or governance processes, while software "ecosystems" (e.g., programming languages, frameworks, operating systems) constantly evolve.
This may lead to the emergence of legacy code that is still actively used.
To safeguard continued usability and adoption,
these RSEs have experience in working with
code written in language standards and on software stacks considered deprecated by their communities.
Adaption of existing, large-scale codebases to evolving dependencies (\gls{DIST}) or changing hardware (\ac{HPC}; see the HPC-RSE specialisation)
may require mastery in refactoring techniques and in the usage of specialised code transformation tools.

#### Web-development RSE
This RSE is skilled in the development of web applications and/or mobile apps.
They have expertise in one or more of frontend development, backend development
and the design or implementation of APIs, for example to support research data portals or big research projects.
Since a lot of web services for research may be accessible to a large audience or even to the public,
this RSE is also familiar with aspects relating to cybersecurity, usability and accessibility.
Not only do they need to balance these concerns while adhering to their values from @sec:values,
but they also need to efficiently communicate the decisions made to stakeholders.

#### Legal-RSE
RSEs are often the go-to person for questions about software licensing, in particular when mixing software components that use different licences.
But with the rising requirements from legislation,
we foresee the need for RSEs that still have a background in RSE but extend it with a knowledge of legal processes that cover corner cases and go beyond applying Best Practice guides.
These requirements may arise in the area of publication of research software,
as this also requires knowledge about particular laws or regulatory frameworks concerning data protection,
like the \ac{GDPR} within the \ac{EU} [@GDPR].
Another area are legal aspects of cybersecurity and export control in science and research (see [@ExportControl] for Germany).
Legal-RSEs focus on facilitating the achievement of technically feasible solutions, while adhering to regulatory mandates.
They are able to communicate and collaborate effectively with lawyers.

<!--
social skill-set focused specialisations
-->

# Future work {#sec:future-work}

This list and description of competencies is a first step to finding common ground
 around which to structure curricula, institutions, and teachers in this framework.
An omission that we found and that we would like to highlight in order to spark a community discussion is
 that RSEs that choose explicitly a science-supporting role outside of research will not be eligible for funding
 under the statutes of many funding organisations that require at least a PhD.

To alleviate this and to give RSEs in leadership positions a means to become eligible for funding themselves,
 since completion of scientific training is often a requirement [@DFG_50_01],
 we see two possible parts of a solution.
One is to allow for doctorates primarily based on software contributions to the scientific community.
Secondly, we propose the introduction of new, standardised certificates
 and to officially accept them as PhD-equivalent concerning eligibility to be a \ac{PI}.
Beyond this discussion, a diverse set of publications on the topic RSE teaching is already in the making.

Within this set, we will work next on how to institutionalise education.
In that publication, we will detail how we organise our institutions
 and what qualifications our teachers need to have in order to effectively communicate our values.
We will put forward ideas on how to build up bachelor's and master's programmes,
 of which a glimpse can already be found in FIXMEPROPERCITATION.
We will show how we intend to provide the necessary continuous education for RSEs after graduation,
 and we will connect that with the integration of RSEs into a mesh of community networks aimed at supporting research,
 while providing them with an inclusive social network that further facilitates lifelong learning.
That publication will again intentionally be free of regional specifics,
 to also serve as a blueprint that other national RSE societies can build upon.

Online resources for courses are another important building block.
This is the general intention of the learn-and-teach project [@learnandteach].
Surveying and curating of existing resources is not carried out as a traditional publication,
but it is made available as a continuously-evolving online resource at [@learnandteach].

And finally, we plan to formulate a call to action,
 building on the previously mentioned publication on the necessary institutions,
 that spells out everything that is required to best support the continuous need for young RSEs to support digital science specifically in Germany.

# Conclusion {#sec:conclusion}

This paper started from a community workshop at deRSE23 in Paderborn
where people working in RSE related fields got together to figure out
structures and ideas for educating newcomers to this field.
One outcome of this diverse gathering is that RSEs from differing fields gather
around similar core concepts, At the same time they share a vision of how to
renew scientific research practice making extensive use of digital tools.
In this publication, we have tried to formalise these concepts.
We have formulated a set of values that guide our actions in society,
manifestly making RSEs part of the scientific community that shares the ideals of good scientific practice.
At the same time,
being close to software engineers, we cherish that we have to take responsibility for our tools.
We listed core competencies that have been intentionally formulated
abstractly without referencing any particular information-processing device.
As expected, we have drawn equally upon notions from \ac{SE} and other research fields,
but found that we likewise require teamwork capabilities.
We detailed these competencies in various dimensions and found that
a different amount is required in different positions and scientific domains.
Using this, we proposed recommendations for organisations to foster the development of these competencies.

The gathered values and competencies form a common denominator that unifies RSEs
 and enables them to identify with this domain,
 in the knowledge that it is already or will soon become critically important for many areas of science.
These competencies at the intersection of research and SE,
coupled with a firm belief in team processes, make RSEs sought after on the job market
and their values make them responsible members of a digital society.
The result is a qualification profile which is highly attractive for young people.

At an institutional level, research performing organisations have a growing
interest in fostering RSE training to support the use of \ac{FAIR} data and \ac{FAIR} software in the academic world,
a direction determined by new incentives created by scientific journals and librarians.
How we update existing institutions and set up new ones
that provide this education will be the topic of a follow-up paper.

# Contribution details {-}

Heidi Seibold came up with the original idea for the deRSE23 workshop in Paderborn.
Heidi Seibold, Jeremy Cohen, Florian Goth, Renato Alves, Jan Philipp Thiele, and Samantha Wittke organised the deRSE23 workshop.
We thank all the participants of this community workshop!
Toby Hodges conceptualised and organised the un-deRSE23 workshop together with Jan Philipp Thiele and Florian Goth.
We also thank all the participants of this follow-up community workshop!
Jeremy Cohen, Gerasimos Chourdakis, Magnus Hagdorn, Jean-Noël Grad, Jan Philipp Thiele, and Matthias Braun organised the deRSE24 workshop in Würzburg.
We are also grateful to the participants of this third community workshop!
Heidi Seibold, Jeremy Cohen, Florian Goth, Renato Alves, Jan Philipp Thiele,
Jan Linxweiler, Jean-Noël Grad, and Samantha Wittke contributed the initial draft.
Florian Goth supervised the project and did the project administration.
Jean-Noël Grad designed and implemented the software tooling for the collaborative writing of this manuscript on GitHub.
Everybody contributed to the final review and editing.


The CRediT system [@Brand2015] is far too generic to adequately describe the contributions of everybody in various workshops, spread over a two year period.
While everybody contributed to the discussion formulating and refining the ideas, and to collaboratively writing and/or reviewing and editing the entirety the script, some parts merit special mention.
Renato Alves quickly jumped in to host the first deRSE23 workshop to take over from a sick organiser.
Matthias Braun contributed early versions of the specialisations and also contributed to the survey.
Leyla Jael Castro contributed to the initial draft of the example career path, and provided helpful insights in discussions on metadata.
Gerasimos Chourdakis' contributions to the paper are numerous (extensively editing large parts of the initial draft), but he especially wrote first drafts for clarifying
the relationship of the RSE competencies to the SE competencies. He also designed the "Learning and teaching RSE" website [@learnandteach].
Simon Christ helped with typesetting and contributed the competencies' symbols and the spell-checker script.
Jeremy Cohen drafted the initial introduction and contributed the tables for RSEs in centralised RSE departments.
Stephan Druskat contributed parts on proper software citation and publication and sharpened various RSE specialisations.
Fredo Erxleben contributed to early discussions of the paper and added the contributions by the Helmholtz Association.
Jean-Noël Grad contributed initial drafts for the ELIXIR framework and the section on the work of the HPC certification forum
as well as numerous other contributions to the BibTeX infrastructure and the GitHub actions.
Magnus Hagdorn drafted and supervised the ethics and values section for an RSE and made sure that these values are reflected in the competencies of RSEs.
Toby Hodges contributed parts on the Carpentries, and helped steer the curriculum discussion.
Guido Juckeland contributed experiences from his first RSE course for students.
Dominic Kempf drafted the first version of the example curriculum.
Anna-Lena Lamprecht helped with proper wording, especially with awareness about established SE terminology, that was misused earlier.
Jan Linxweiler drafted various RSE specialisations and made sure that clean coding techniques got their due recognition.
Frank Löffler rewrote numerous parts to be actually legible, and helped with preparation for the final steps of a de-RSE position paper.
Michele Martone wrote the first draft of the environmental sustainability section.
Moritz Schwarzmeier drafted the categorisation of the specialisations.
Heidi Seibold contributed the idea and started everything.
Jan Philipp Thiele drafted initial parts of the technical pillar of the RSE competencies, and represented the project on numerous discussions.
Harald von Waldow contributed to initial drafts of the Masters program and contributed his knowledge to the explainability of computer simulations.
Samantha Wittke contributed the parts on CodeRefinery and how to reach out to new RSEs.
Florian Goth has the pleasure of being grateful to all collaborators in this project for contributing their time and knowledge into this project!
