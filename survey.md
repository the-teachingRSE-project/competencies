---
title: "A Survey of Initiatives Providing Educative Material in the RSE Space"
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
header-includes:
  - \input{preamble.sty}
output:
  pdf_document:
    citation_package: biblatex
    toc: true
    number_sections: true
bibliography: bibliography.bib
keywords:
  - research software engineering
  - training
  - learning
  - open educational resources
  - lifelong learning
  - digital competence
abstract: "
In this publication we survey the existing RSE-training related resources and initiatives.
"
---

## Related Work and Activities

The challenges of understanding the current state of skills
within the research software community and related areas,
as well as identifying required competencies, developing training pathways
and providing training materials are areas that are being looked at
and addressed by various groups and projects.
In this section, we highlight some of these other projects and activities.

### RSE-related training resources

The day-to-day work of many RSEs often includes teaching activities to improve the RSE-related skill-set of researchers,
e.g. in university courses, workshops or one-on-one.
Therefore, RSEs' work often includes the use of as well as the contribution to pertinent teaching material.
Various organisations and initiatives provide courses and workshops
to convey software-related capabilities aimed at the research community.
Often they make their training material available as Open Educational Resources
permitting free access, re-use, adaptation and redistribution.
The collaborative advancement of these resources in the fast evolving environment
of RSE related skills and infrastructure can be further facilitated by putting them under version control.
For example, core lessons from the Carpentries and CodeRefinery are stored on GitHub,
and any change is automatically mirrored to their websites.
The organisations and initiatives listed below provide support for teaching activities conducted by RSEs
but are also helpful to fill gaps in the capabilities of professional RSEs.

#### The Carpentries

The Carpentries [@Carpentries] is a non-profit entity that supports
a range of open source training materials and international communities
of volunteer instructors and helpers who run courses around these materials.
The community also maintains the materials which are based around three core syllabuses --
Software Carpentry [@CarpentriesSoftware; @Wilson2006; @Wilson2016a],
Data Carpentry [@CarpentriesData; @Teal2015] and
Library Carpentry [@CarpentriesLibrary; @Baker2016; @Cope2018].
The training materials within these areas have been developed,
reviewed and enhanced over several years ensuring that they represent
best practice in training on these topics.
The core Carpentries lessons are targeted primarily at the beginner level.
However, the Carpentries Incubator [@CarpentriesIncubator] provides an environment
for hosting additional community-developed training modules covering a wide range
of other topics that have not gone through the peer review process of the core lessons.
The material in the Incubator increasingly includes more intermediate-level training modules.
After completion of a Carpentry workshop, learners can claim a certificate
of attendance [@CarpentriesLearnerCertificates].
Carpentry instructors must be certified before organising a workshop.
There is a selection process [@CarpentriesBecomingInstructor] as well as
an instructor training course, upon which a certificate is delivered [@Wilson2013a].

#### CodeRefinery

CodeRefinery [@CodeRefinery] is a project currently funded by the Nordic
e-Infrastructure and thus active primarily in the Nordics with the goal
of teaching essential tools around research software development,
that are usually skipped in academic education.
CodeRefinery hosts a set of open source training materials including
both beginner and intermediate level material and organises multiple
highly interactive large scale workshops per year.
Skills learned from the workshops and/or materials allow researchers
to produce more reproducible, open and efficient software and thus
promote FAIR [@FAIR] research practices.
One goal of the project is to evolve into a community project that
seamlessly integrates with other initiatives.

FIXME: elaborate on the integration part if it's relevant, else leave out.

#### PRACE

The Partnership for Advanced Computing in Europe (PRACE) [@PRACE] offers training
in the form of massive open online courses (MOOCs), online and on-site training
events at European HPC facilities (aggregated on various websites, e.g. EuroCC
Training [@EuroCCTraining]), and white papers. While most training events are
tailored for HPC-RSE, several recurring courses about programming languages
(C++, Fortran, Python) are suitable for general RSEs, as they teach coding
best practices, modern software design [@LRZModernCpp], project management and
version control [@LRZIntroCpp].

#### Helmholtz

As part of its push towards a better RSE environment, the Helmholtz Association
launched the Helmholtz Federated IT Services platform (HIFIS) [@HIFIS]
which provides educational material and training amongst other services
for an audience of over 10,000 scientists in Germany and internationally.
All of these materials focus on RSE basics to refresh and expand the software
engineering knowledge for recent graduates or to update the existing
knowledge in established researchers.
They are published under OER licenses and can serve as either self-learning
instructions or form the basis of a hands-on training.
To allow these educational offers to be easier brought to the scientists,
the Helmholtz Information and Data Science Academy (HIDA) [@HIDA] sustains
a large network within the Helmholtz Association and beyond with a strong
focus on graduate schools.
Further RSE training offers within the Helmholtz context are provided
by the Helmholtz-AI [@HAI] and Helmholtz-Imaging [@HImaging] platforms
as well as the Helmholtz Metadata Collaboration platform [@HMC].

#### ENCCS

The [National Competence Center Sweden (ENCCS)](https://enccs.se/)
has created a collection of lessons for HPC-oriented RSEs [@ENCCSLessons] and
has adapted instructor training material from The Carpentries and CodeRefinery
to create their own instructor manual [@ENCCSInstructorTraining; @ENCCS2022].
The ENCCS lessons are targeted at individuals who already have general RSE
skills and are seeking new skills relevant to HPC and software engineering.

#### German National Research Data Infrastructure (NFDI)

EduTrain (Training & Education) [@EDUTRAIN] is a section of the NFDI [@NFDI].
Based on the slogan "data literacy from the beginning",
it contributes to the further development of scientific methods
and good scientific practice.
The targeted education also involves research software engineering.
As described in its concept [@EduTrain2022], there will be a collaboration
with "The Carpentries" regarding their lesson program.
Moreover, the approach of how "The Carpentries" are organised will be adopted.

Through the close connection to the DALIA project [@DALIA],
the NFDI and its section EduTrain will benefit from a knowledge-base
which is implemented as semantically linked knowledge graph.
- FIXME: Is there any connection to RSE?

According to the goals of the NFDI consortium NFDI4ING (National Research Data
Infrastructure for Engineering Sciences) [@NFDI4ING], engineers treat software
as research data that possibly connects the different stages of stored data.
Therefore, it aims to enable engineers to develop validated quality-assured
engineering research software.
One specific example is the lecture 'Sustainable Development of Simulation Software'
that has been developed as master's course at the Institute for Modelling Hydraulic
and Environmental Systems at the University of Stuttgart [@SDSSCOURSE; @SDSSMATERIAL].

#### SureSoft

SureSoft [@SURESOFTLink] is a DFG funded project at TU Braunschweig and
FAU Erlangen-Nürnberg fostering the sustainability of research software
by helping researchers adopt practices and tools from the software
engineering community [@SURESOFT2022].
The project implements a twofold approach that combines tools and
infrastructure with education in the form of workshops and training.

#### Programming Historian

The [Programming Historian](https://programminghistorian.org/)
is an open-source, peer-reviewed journal of digital humanities
edited in English, Spanish, French, and Portuguese.
It publishes hands-on tutorials on shell, Python,
and software specialised for digital humanities.

### FAIRness of RSE-related (open) educational resources(OER)

Due to the ever-evolving nature of skills and infrastructure in the RSE field,
training materials are often open educational resources(OER) that are often version-controlled, so that trainers can update them
between iterations. For example, core lessons from the Carpentries and CodeRefinery
are stored on GitHub, and any change is automatically mirrored to their website.
The ENCCS instructor training manual [@ENCCS2022] is available as a living document
[@ENCCSInstructorTraining], and The Carpentry instructor guide [@Wilson2019a]
is available as living documents in both English [@Wilson2019b] and Spanish [@Wilson2019c].
Core lessons from The Carpentries were translated in multiple languages
to make workshops more accessible to communities where the English language
poses a barrier to learning (for more details, see section
[How do we reach people in different stages of their careers?]
from paper `competencies.pdf`).
These considerations are part of the more general concept of Open Educational
Resources (OER) [@Pownall2023], which are part of the UNESCO recommendations
since 2019[@UNESCO2019].

It is also important for training material to follow the FAIR principles [@FAIR],
so that the community of trainers and learners can make the most out of it [@Garcia2020].
Material with rich metadata can be indexed in online databases,
such as the INTERSECT [@Carver2020] collection [@INTERSECTOnlineResources]
and the US-RSE collection [@usRSETraining] for all RSE specialisations,
the ELIXIR [@Gurwitz2020] Training e-Support System (TeSS) platform
[@Beard2020; @Bacall2023] for bioinformatics and life sciences,
or the now-defunct Educational Resource Discovery Index (ERuDIte)
[@VanHorn2017; @Ambite2021] for data science.

FIXME: better integrate this MIT course, maybe move it to the introduction?
From the MIT Computer Science & Artificial Intelligence Laboratory comes an
unofficial course "The Missing Semester of Your CS Education" [@Athalye2023]
which covers a lot of basic computer
skills typically taught by RSEs. The skills covered here also provide an
important set of core capabilities for anyone looking to become an RSE.

Many RSE OER lack in findability, which could be greatly improved by better annotation with metadata.
The RSE community of lacks an agreed-upon standard of metadata with which to annotate RSE OER, which would help learners as well as teachers to find suitable resources to satisfy their concerns.
Building on such annotations, a community agreed-upon registry for RSE OER would additionally improve the situation.

ADDME:

- [Software Sustainability Institute (SSI)](https://www.software.ac.uk/) [@Crouch2013] ...
- ELIXIR/EXCELERATE/GOBLET train-the-trainer programme [@Via2017; @Morgan2017]
- Library-RSE resources [@Clarke2019] (no longer updated since 2019)
- deRSE19 collected resources [@Gey2019]
- Happy Belly Bioinformatics [@Lee2019]
- software energy consumption and "green software engineering"
  [@Pinto2017; @Pereira2021; @Oprescu2022; @Couto2020],
  teaching by SusTrainable [@SusTrainable; @Koopman2022]

## Challenges
- Point out gaps
- What is missing
- domain application?

### A fundamental skills gap

A major challenge for the future of Research Software Engineering
is the significant gap between the availability of basic training
and the comparatively small number of experts in specialist topics
such as High Performance Computing (HPC), parallel algorithms and
neural network design.
For example, scientists working with HPC may need to know how to
make effective use of concurrency to speed up their simulations and
communicate efficiently using message-passing interface (MPI) libraries.
The same is true for researchers from other domains who make use of
other specialised technologies, methods and/or tools.
Organisations such as [The Carpentries] and [CodeRefinery] provide
extensive introductory training materials and, increasingly some more
intermediate-level content.
However, to bridge the gap between introductory and expert-level skills,
more specialised courses are needed like the ones mentioned in section
[Identifying skills and pathways] from paper `intro.pdf` for the HPC community.

Moreover, software development is a craft, i.e. it is not only about
knowledge but also requires practical experience.
Hence we need to create an environment that allows less experienced
researchers to practice and gain experience efficiently.
Ideally, this would be facilitated through learning environments
that allow less experienced scientists to be guided by more experienced RSEs.
We know such practices e.g. from human medicine, where junior doctors
first assist experienced doctors before they work independently.
In the field of software development, this approach could be implemented
in the form of peer programming, for example.
In the German context, the prerequisite for this, however,
is that experienced academics/researchers get better career opportunities
at German universities so that they do not leave for industry roles.

As the need for research software engineering skills and expertise grows,
there is a fundamental need to address this challenge in order to support
the future of computational research.
Indeed, computational approaches are increasingly becoming the standard
approach for tackling large research challenges across almost all domains
and we see the potential for a huge growth in demand for the skills
required to support this.

As seen in the previous section, there already exist a number
of open educational resources in the field of RSE.
However, what is missing is a practical way to search all of these at once.
This is mainly due to the lack of a metadata standard concerning EOR resources
within the RSE community, as well as some simple way to collect potentially
existing metadata in one place in order to enable a comprehensive search.

Building on this: courses exist on different knowledge and experience levels and,
at least in part, build upon each other. However, there is currently no (unified)
way to clearly label
- what are the topics taught by a course
- what are the topics recommended to know to start the course
- what are the topics required to know to start the course
This, in part, is due to a missing (metadata) standard to express these dependencies.

FIXME:
- metadata standards: Bioschemas [@Castro2023]
- survey of 8 OER repositories with non-standardised metadata [@SimaodeDeus2020]
- OER certification proposal in Austria [@Schon2023]
- databases: see Appendix section [Directories of resources]

## Appendix
### Sources for RSE-related training material

#### Books

+ "Producing Open Source Software" ([@Fogel2005; @Fogel2017]) describes
  a lot of aspects for running a free software project.

+ "Research Software Engineering with Python" ([@Irving2021]) targets
  Python programming novices and introduces a set of essential tools
  next to the programming language itself.

#### Course material

+ The Software Carpentries Lessons [@CarpentriesSoftware] provide extensive teaching
  material for basic research software skills geared towards researchers.

+ The unofficial MIT course "The Missing Semester of Your CS Education" ([@Athalye2023])
  covers a lot of basic computer skills typically taught by RSEs.

#### Train-the-trainers material

+ "Teaching Tech Together" is a book that derives from and extends the
  Carpentries Instructor Training [@Brown2023],
  which is a continuously updated and extended online-resource.
+ The National Competence Center Sweden ([ENCCS](https://enccs.se/)) provides
  instructor training material [@ENCCSInstructorTraining; @ENCCS2022]
  developed from Carpentries and CodeRefinery material,
  as well as lessons for HPC-oriented RSEs [@ENCCSLessons].

#### Directories of resources

+ Better Scientific Software [BSSW](https://bssw.io/)
  (Collection of resources for computational science and engineering)
+ TeSS platform [@Beard2020; @Bacall2023] for bioinformatics and life sciences
+ Curriculum Task Force of the International Society for Computational
  Biology (ISCB) database of degrees and certificates in bioinformatics
  [@BioinformaticsCertification; @Mulder2018]
+ HPC Portal: academic programmes database [@AcademicProgrammesHPC]
+ HPC Portal: training events database [@TrainingEventsHPC]
  (successor of EuroCC Training [@EuroCCTraining])
