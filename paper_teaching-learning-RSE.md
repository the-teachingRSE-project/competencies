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
  - Samatha Wittke
  - Jean-Noël Grad
  - Fredo Erxleben
  - Magnus Hagdorn
  - Harald von Waldow
output:
  pdf_document:
    citation_package: biblatex
    toc: true
    number_sections: true
bibliography: bibliography.bib
header-includes:
    - \usepackage{pdflscape}
    - \newcommand{\blandscape}{\begin{landscape}}
    - \newcommand{\elandscape}{\end{landscape}}
---

## Working Title: Identifying foundational competencies of Research Software Engineers across all specializations.

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
career-levels across a vast array of research fields where these were not
previously required. Researchers often lack the skills to write and use software
for their research and even to effectively request help from and interact with
more experienced staff at their institutions. There still exists a gap in the
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

Developing and maintaining these skills is time consuming and often challenging.
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

'Related work and activities' gives a brief overview over other initiatives in the area of digital skills for researchers.
The content is twofold. Firstly, we consider other initiatives trying to identify relevant skills for and pathways to becoming an expert at their specific but related area, 
e.g. high performance computing, . Secondly, we look at groups and organisations that compose specific training material that can be 
used for teaching RSE skills.

'Challenges' discusses the challenges in the current academic training and research landscape when it comes to 
students and researchers learning the necessary skills to write FAIR software in their specific domain.

In 'Results' we describe the main results of the workshop, namely the set of relevant skills as well as 
the levels of expertise needed in these skills for students and researchers at different career levels.
Furthermore, we look at different RSE specializations which may additonally need skills not relevant 
to RSEs of different specialisations.
The skills themselves belong to one of the three main categories needed to perform RSE tasks. 
Those are the 'R', i.e. an understanding of how research is performed, 
the 'SE', i.e. writing and maintaining reusable software, as well as team skills.

'Organizational Infrastructures' focuses on changes that are required to at best support
the training of new RSEs.

FIXME (finalization): Exchange chapter titles by numbers?


### Some Definitions
A couple of definitions are in order.
First as software we define source code, documentation, tests
and all other artefacts that are created by humans during the development process
that are necessary to understand its purpose.

We define research to encompass all domains of research.
Since we expect a sizeable portion of readers from Germany we
quickly want to address a common false friend.
The german 'Wissenschaft' encompasses all domains of publicly funded
research, while the english 'science' is generally limited to natural sciences.
Therefore, we will use 'research' to encompass all domains therefore gives the employability of RSEs.
Of course 'research' as well as 'Forschung' is not limited to public funding
but also part of industrial and other private companies.
We surmise that the same software engineering and team skills will be needed there,
but we limit our considerations to the views of public research.

This enables us to define Research Software in this paper to include source code files,
algorithms, scripts, computational workflows and executables that were created
during the research process or for a research purpose.
This definition is broader than in [@FAIR4RS] and is the outcome of a recent
discussion in [@definingrs2021].

Using this, Research Software Engineers are now people that 
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
institutionalised. Finally, the strong emphasis on team-skills allows RSEs to be
very employable in industrial workplaces.

### National Context
Having been developed at a workshop in Paderborn in Germany, naturally a part
of the discussion in this paper focusses on the german academic landscape.
So, although there are germany specific traits found in this document
we are nevertheless dealing with the education of humans to become RSEs -
A topic that is of major relevance also in an international context.

### Related Work and Activities

The challenges of understanding the current state of skills within the research software community and related areas, as well as identifying required competencies, developing training pathways and providing training materials are areas that are being looked at and addressed by various groups and projects. In this section, we highlight some of these other projects and activities.

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
- skill gaps for software verification/testing (fig. 1 in [@Hannay2009])
  and bioinformatics [@MacLean1999; @Pevzner2009]
- software evaluation criteria [@Jackson2011a; @ChueHong2014]

### RSE-related Training Materials

A wide range of software-related training materials and supporting organisations exist within the research software community and beyond.

#### The Carpentries
The Carpentries [@Carpentries] is a non-profit entity that supports a range of open source training materials and international communities of volunteer instructors and helpers who run courses around these materials.
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
Carpentry instructors must be certified before organizing a workshop.
There is a selection process [@CarpentriesBecomingInstructor] as well as
an instructor training course, upon which a certificate is delivered [@Wilson2013a].

#### Coderefinery
CodeRefinery [@CodeRefinery] is a project currently funded by the Nordic e-Infrastructure and thus active primarily in the Nordics with the goal of teaching essential tools around research software development, that are usually skipped in academic education.
CodeRefinery hosts a set of open source training materials including both beginner and intermediate level material and organizes multiple highly interactive large scale workshops per year.
Skills learned from the workshops and/or materials allow researchers to produce more reproducible, open and efficient software and thus promote FAIR [@FAIR] research practices.
One goal of the project is to evolve into a community project that seamlessly integrates with other initiatives. FIXME: elaborate on the integration part if it's relevant, else leave out.

#### Reprohack
The ReproHack Team offers resources to host events where students and researchers
can get together to try and reproduce the results of published papers with the methods
described there or ideally with the software provided by the authors.
FIXME: This is applied FAIR principles elaborate a bit on why this is related for RSE competencies? Or do we want to make the point, that this teaches reproducible science?

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
As part of its push towards a better RSE environment, the Helmholtz Association launched the Helmholtz Federated IT Services platform (HIFIS) [@HIFIS] which provides educational material and trainings amongst other services for an audience of over 10,000 scientists in Germany and internationally.
All of these materials focus on RSE basics to refresh and expand the software engineering knowledge for recent graduates or to update the existing knowledge in established researchers.
They are published under OER licenses and can serve as either self-learning instructions or form the basis of a hands-on training.
To allow these educational offers to be easier brought to the scientists, the Helmholtz Information and Data Science Academy (HIDA) [@HIDA] sustains a large network within the Helmholtz Association and beyond with a strong focus on graduate schools.
Further RSE training offers within the Helmholtz context are provided by the Helmholtz-AI [@HAI] and Helmholtz-Imaging [@HImaging] platforms as well as the Helmholtz Metadata Collaboration plaftorm [@HMC].

#### ENCCS
The [National Competence Center Sweden (ENCCS)](https://enccs.se/)
has created a collection of lessons for HPC-oriented RSEs [@ENCCSLessons] and
has adapted instructor training material from The Carpentries and CodeRefinery
to create their own instructor manual [@ENCCSInstructorTraining; @ENCCS2022].
The ENCCS lessons are targeted at individuals who already have general RSE
skills and are seeking new skills relevant to HPC and software engineering.

### Open Source Resources
Due to the ever-evolving nature of skills and infrastructure in the RSE field,
training material is often version-controlled, so that trainers can update it
between iterations. For example, core lessons from the Carpentries and CodeRefinery
are stored on GitHub, and any change is automatically mirrored to their website.
Likewise, the reference work on RSE by Fogel [@Fogel2005] was released in its
second edition as a living document [@Fogel2017]. The ENCCS instructor
training manual [@ENCCS2022] is also available as a living document
[@ENCCSInstructorTraining]. The Carpentry instructor guide [@Wilson2019a]
is available as living documents in both English [@Wilson2019b] and Spanish [@Wilson2019c].
From the MIT Computer Science & Artificial Intelligence Laboratory comes an
unofficial course [The Missing Semester of Your CS
Education](https://missing.csail.mit.edu/) which covers a lot of basic computer
skills typically taught by RSEs. The skills covered here also provide an
important set of core capabilities for anyone looking to become an RSE.

More generally, it is important for training material to follow the FAIR
principles [@FAIR], so that the community of trainers and learners can make
the most out of it [@Garcia2020].
Core lessons from The Carpentries were translated in multiple languages
to make workshops more accessible to communities where the English language
poses a barrier to learning (for more details, see section
[How do we reach people in different stages of their careers?]).
Material with rich metadata are indexed in online databases, such as
the INTERSECT [@Carver2020] collection [@INTERSECTOnlineResources]
and the US-RSE collection [@usRSETraining] for all RSE specialisations,
the ELIXIR [@Gurwitz2020] Training e-Support System (TeSS) platform
[@Beard2020; @Bacall2023] for bioinformatics and life sciences,
or the now-defunct Educational Resource Discovery Index (ERuDIte)
[@VanHorn2017; @Ambite2021] for data science.

FIXME:

- [Better Scientific Software (BSSW)](https://bssw.io/) ...
- [Software Sustainability Institute (SSI)](https://www.software.ac.uk/) [@Crouch2013] ...
- Add NFDI initiatives like edutrain.
- ELIXIR/EXCELERATE/GOBLET train-the-trainer programme [@Via2017; @Morgan2017]
- Library-RSE resources [@Clarke2019] (no longer updated since 2019)
- Happy Belly Bioinformatics [@Lee2019]
- software energy consumption and "green software engineering"
  [@Pinto2017; @Pereira2021; @Oprescu2022],
  teaching by SusTrainable [@SusTrainable; @Koopman2022]
- reference works for self-study [@Fogel2005], [@Irving2021], [@Wilson2019a]

## Challenges
- Point out gaps
- What is missing
- domain application?

Depending on the specific domain there is a gap between the basic software carpentry courses and the required skills to build domain-specific research software. For example, scientists in the field of High Performance Computing (HPC) need to know how to make effective use of concurrency to speed up their simulations and communicate efficiently using message-passing interface (MPI) libraries. The same is true for researchers from other domains who make use of other specialized technologies, methods and/or tools. To bridge those gaps more specialized courses would be needed like the one mentioned in section [Identifying skills and pathways] for the HPC community.

Moreover, software development is a craft, i.e. it is not only about knowledge but also requires practical experience. Hence we need to create an environment that allows less experienced researchers to practice and gain experience efficiently. Ideally, this learning environment would allow less experienced scientists to be guided by more experienced RSEs. We know such practices e.g. from human medicine, where junior doctors first assist experienced doctors before they work independently. In the field of software development, this approach could be implemented in the form of peer programming, for example. The prerequisite for this, however, is that experienced academics get better career opportunities at German universities so that they do not leave for industry roles. 

## Workshop Results

## Required Generic RSE skills
The role of an RSE lies somewhere on the spectrum between that of a researcher
(the "R") and a software engineer (the "SE") and, therefore, requires
competencies in both fields. RSEs typically apply their knowledge and
experience in larger teams which allows them to cultivate this hybrid nature.
Therefore, we categorise the competencies into software engineering skills,
research skills, and team skills with particular focus on the software and
research cycle and the scientific process. The generic skills are relevant in a
broad setting and form the foundation for specific specialisations.

These skills and competencies come into play in various forms: first of all the
RSEs themselves need to acquire and develop them as their career progresses
(**Career level**). However, some knowledge of software and data processing is
required at all academic levels and for all positions
(**Academic Progression/better title**). The relative importance of the skills
and competencies also depend on the size of the RSE team
(**Project team size**). Finally, different sets of skills are emphasised in
the different RSE specialisations (**RSE specialisations**).

### Software Engineering Skills
There are many software engineering curricula out there, that try to define
which tasks a software engineer should be able to perform. A recent example
highlighting some aspects in more detail than here is [@Landwehr2017].
The software skills outlined here are required to make research software adhere
to the FAIR principles. [@ChueHong2014] defines different levels of research
software reuseability and the extent to which the software engineering skills
need to be applied to reach them.

#### Creating documented code building blocks (DOCBB)
The RSE should be able to create building blocks from source code that are
reusable. This ranges from simple libraries of functions up to complex
architectures consisting of multiple software packages. An important part of
reusability is that at least oneself, and ideally others, are able to understand
what a piece of code aims to do and how to use the provided functionality. This
is primarily achieved through a "clean" implementation and enhanced by
documentation. Documentation ranges from commenting code blocks to using
documentation (building) tools.

#### Building distributable libraries (LIBS)
The RSE should be able to distribute their code with their domain/language
specific distribution platforms. This almost always encompasses
handling/documenting dependencies with other packages/libraries. It sometimes
requires knowledge of using build systems to enable interoperability with other
systems.

#### Understanding the software lifecycle (SWLC)
The traditional software lifecycle defines the stages that form the process of building a piece of software.
This generally involves a creative process where you try to understand what it is that you need to build,
work out how you are going to build it and then implement it.
This is then followed by testing that things work as expected and that they continue to do so into the future.
We emphasize the the lifecycle is not complete here but also includes periods of maintaining a software
and also phasing out a software of its original use.

#### Use repositories (SWREPOS)
The RSE should be able to use public platforms to share the artefacts they have
created and invite the public to scrutinise them for public review.

#### Legal aspects (LEG)
The RSE should know licenses and their respective domains for data or software.
On an entry level, the competency is mostly about awareness: namely that different
(open source) licenses exist, that those might not be compatible with each other,
and that use of third party software might restrict licensing of the resulting work.

#### Software Behaviour Awareness and Analysis (MOD)
We define this as a certain quality of analytical thinking that enables an RSE to
form a mental model of a piece of software in a specific environment.
Using that, an RSE should be able to make predictions about a software's behaviour.
This is a required skill for common tasks like debugging, profiling, designing good
tests, or predicting user interaction.

### The research skills
#### Curiosity (NEW)
RSEs gain their reputation from their effectiveness to interact with their
domain peers. Therefore, some curiosity together with a broad overview of the
research field is required. Curiosity is also reflected when an RSE is actively
trying out new tools. Lifelong learning is then no longer just a phrase, but
becomes a motivation to work.

#### Understanding the research cycle (RC)
One of the crucial skills of RSEs is their mental proximity to research
and they embrace being part of a larger community which,
despite friendly competition, shares the common goal of gaining knowledge
for its own sake and not just for personal or commercial gain.
Thereby they know, that they are part of a bigger cycle that involves many other parties in and outside of
their domain, and also that their software can be utilized in different stages of the research cycle by different persons.
Like other researchers, RSEs are open to discussions and arguments beyond
their own expertise and appreciate the underlying principles of
good research, like publications, review and reproducibility.

#### Finding/discovering software and attribution (SD)
One goal of FAIR software is to avoid unnecessary duplication of work by reusing
existing work instead. To (re-) use software, researchers have to be able to
find it and then to easily evaluate if the software actually suits their needs.
Apart from functionality also licensing, integration with other software,
expected sustainability and expandability have to be part of this evaluation.
Finally, after obtaining/publishing results by modifying and/or using the
software, the original authors need to receive proper attribution.

#### Using domain repositories/directories (DOMREP)
Almost all research software is developed within a specific scientific domain.
Some software may be able to cross boundaries, but the majority will have a
home domain, with which it needs to be able to interact. The RSE needs to be
aware of any domain specific software repositories, data sets and catalogues
and the RSE's software needs to be able to interact with the existing
domain-specific data repositories.

#### Outside Party interaction (USERS)
Research software is often developed as part of the research process itself,
and like research, it will change in unpredictible ways
hence it often has to be developed very closely to its users, the researchers.
Therefore, roles like developers and users can seldomly be distinguished
as most people represent multiple roles ranging from end-users, up to funders.
However, regardless if this is the case or not: compared to other SE environments,
there is an unusually close interaction between and within different roles in research,
as well as between experts from different domains.
Often this means it is necessary for an RSE to think "outside their comfort zone",
but at the same time to be able to convey their knowledge and experience to experts
of other fields in a way they can understand more easily.
This includes their own domain knowledge in discussions with RSEs (from other domains),
as well as their SE knowledge when talking to domain scientists and also the
exchange of new techniques and algorithms to keep their software up-to-date.

### Team Skills
#### Teaching (TEACH)
Working in a group means being able to effectively perform e.g. onboarding, or more formal teaching procedures to their colleagues.
This includes tasks such as consulting and mentoring since these also often aim at educating people.
We deliberately mention, that giving code reviews is also part of this skill, since
Code review can be part of teaching people on improving their skills.

#### Project Management (PM)
The RSE should have knowledge about project management. At some institutes, it follows the practices of the local research groups,
but it is useful, if an RSE knows its place in a PM scheme, or can bring in new ideas for improvement.

#### Working in a team (TEAM)
There are various facets to working in a team. They range from functioning in a team to leading a team.
It includes following measures that increase team cohesion like performing code reviews.

### RSE Tasks and Responsibilities
These skills, while already numerous are also generic on purpose. They span a
multidimensional space in which the day-to-day tasks and responsibilities of a
RSE can be found. A snapshot of what this means today can be obtained 
from  learners and novice RSEs that we asked during the Paderborn workshop
what they would like to have learnt. Among the top five things mentioned were:

- Testing. This task is a manifestation of the SE competencies of DOCBB and MOD
since a model of the software is required in order to write good tests that
facilitate understanding and documentation. Today this encompasses the
knowledge of testing frameworks and CI/CD practices.
- Contributing to large projects. This is a topic that requires competency in
SWREPOS, LEG, in order to understand the ramifications of sharing, and DOCBB,
since the contributed code has to be understood by others. Interacting with
project members depends on the the TEAM skill. Today this entails the effective
use of collaborative platforms like github/gitlab, honouring a projects Code of
Conduct, and some knowledge of software licenses like the GPL.
- When or why to keep repositories private. This decision requires knowledge in
the RC, to understand when it makes sense to open up or close down a repository.
The USERS, TEAM and sometimes LEG skills are required to make this decision.
Furthermore, knowledge of the practices and contractual regulations of the
RSE's institution are also required.
- Proper Development. This broad topic requires all of the SE skills. Of course
these are the competencies that are the most fluid since they have to adapt at
a high rate to the technological advancements. Additionally proper SE skills
often require knowledge of TEAM, and PM. Today this means effective use of IDEs,
static analysis tools, design patterns, documentation (for oneself and others),
etc.
- Finding a community. This can be interpreted in two different facets. First
we have the aspect of community building for a research project. Since this
deals with software that is supposed to be used in research this requires
knowledge of RC, USERS, and also NEW, in order to effectively interact with
domain scientists. Today, an example is a presence on social media. The other
TEAM-related aspect is the embedding of RSE graduates into the community of
RSEs. We envision our RSE graduates to be a part in a strong network of other
RSEs, tool-related communities and the classical domain communities. This point
is further elaborated in [How do we reach people in different stages of their careers](#how-do-we-reach-people-in-different-stages-of-their-careers).


Beyond that, we feel that today Other important tasks of RSEs are

- Mentoring colleagues.
  This necessitates giving good advice that fits to a projects stage in its lifecycle,
  thereby requiring knowledge of (SWLC), and its context in its research domain, thereby requiring knowledge of (RC).
  Research software often starts out as a tool to answer a personal research
  question and becomes more important when other researchers rely on it.
  Some research software might even be used to deal with critical questions such as weather forecasting or medical diagnosis.
  To formalize the process of giving good advice a classification of software is commonly used [@WANG2012; @dlr121502]
  where research software can move from one class to another during its lifecycle.
  [@dlr121502] classify applications based on their scope and criticality and provide software engineering recommendations.
  The RSE needs to be able to identify the application class they are dealing with and apply the respective RSE practices.

- Enforcing reproducibility. Projects like [@ReproHack] can greatly help in fostering that competency.

## How much do different people need to know?
Now that we have the different competencies, we can explore various dimensions of these competencies,
depending on their circumstances. A strong beneficiary of specialized RSEs can also be newly formed RSE centers at research institutions.

### Career level
At different career levels, differing skills are required. We have set this up according to the following separation often applied within a single project:

- Junior RSE: These are persons that have just started, but generally speaking they should have the skills to contribute to software projects
- Senior RSE: They have gained experience and can set the examples in the software project.
- Principal RSE: Their actual job description varies a lot. These may be RSE team leaders based in a professional services type role, or they may be professors or research group leaders based in a more academic-focused role. They are often the people responsible for bringing in the money that supports new projects and sustains existing projects. Generally speaking, they do not need to to be actively involved in the day-to-day technical tasks but they should be able to guide projects from both a technical and research perspective.

The required skills are distributed according to this table
First Dimension: Career path e.g. Junior RSE -> Senior RSE -> PI scale (1->6) (less -> lot)

\blandscape

|       | Junior | Senior | Principal RSE(brings in funding)  |
| ----  | ------ | ------ | --- |
| DOCBB | should be able to write reusable building blocks |same as junior, but the quality should set the standard for the project, while following current best practices | should know the current best practices and point its people to the right resources. |
| LIBS  | should be able to use package distribution platforms      | same as junior, but should set the project standard and follow current best practices. | should ensure that their project is in an up-to-date distribution platform |
| MOD   | should have a basic grasp of their piece of the software in order to use basic tools like a debugger | Should understand the characteristics of large parts of the codebase considering a variety of the metrics | Should understand the big idea of the software project in order to define the task that the software solves  |
| SWLC  | Awareness about the existence of the software lifecycle. | Should know which decisions lead to technical debt. | Should know in which part of the lifecycle their project is and how to steer development/project resources accordingly. |
|SWREPOS| Seamless interaction with the swrepo of their project is a must | Should be well-versed in the intricacies of a swrepo, and probably interact with multiple projects' repo's | Should be able to effectively interact with swrepos and especially the interaction with the connecting projects. |
| LEG   | Awareness about legal intricacies about sharing code | Should be able to give advice on legal issues and resolve the most common issues | same as Senior RSE |
| NEW   | Some curiosity required to fit into research teams | same as junior, but a curiosity to enhance the code base is required | Curiosity to know in which direction to steer the project is required |
| RC    | Awareness about the RC | should know the position of the project in the RC | Should know what is necessary for the project to fit into its position in the RC |
| SD    | Should be aware about tools for SD |   Should be able to find sth. with SD tools    | Should be able to effectively find sth. with SD tools and be able to evaluate and perform the integration of a library into the project. |
| DOMREP| The RSE should be able to interact with the domain repository | same as junior RSE | same as junior, and should know about how it fits into workflows surrounding these domain repositories |
| USERS | The RSE should be able to communicate with non-SE users of the project | same as junior | same as junior, and take feedback into account of the steering |
| TEACH | should be able to perform simple peer-to-peer onboarding tasks | should be able to explain logical components to other RSEs | Should be able to effectively communicate about all large-scale parts of the project. |
| PM    | Awareness about the employed project managemement method | Should be able to use the employed PM method | Should be able to design and adapt the employed PM method. |
| TEAM  | Should be able to work in the team in order to effectively fulfill the given tasks. Should be able to learn from code review. | Should be able to break down tasks into more easily digestable sub-tasks | Should be able to lead the team and set the respective direction. |

\elandscape

### Academic Progression / Career Path? (Help me for better title) 
Modern digital science requires some digital proficiency at every level.
To be a bit more precise, these are how we define the academic levels:

- Bachelor: These are people in their undergrad studies, that mostly consume science/knowledge. They should also learn about the existence of certain digital structures.
- Master: Ultimately, their study should have brought them to a level, where they can participate in science, hence they should be able to use "some" digital structures.
- PhD: Under guidance they perform independent research and hence they should get to know all relevant structures.
- PostDoc: Independent researchers, they are proficient users of all tools.
- PI/Professor: Experts in their field, they should be able to give proper guidance to their students on which digital tools are currently relevant.

It is important to note that the following table does not reflect the current state of academic training and research institutions.
Instead, it summarizes the discussions with and between workshop participants at different levels of academic progression on 
what they would have liked to learn at an earlier stage or know before starting their current position.
While individuals already work at implementing some of these changes and teaching these skills it has not yet reached 
a systemic level.

Additionally, this table tries to cover all domains that rely on software tools in at least a basic level.
Certain fields, e.g. sciences relying on simulations, might require higher skill levels in the SE competencies 
as software development is a large part of their actual research.

\blandscape

|       | Bachelor | Master | PhD | PostDoc | PI/Professor | 
| ----  | ------ | ------ | ---   | ------  | ---|
| DOCBB | They should be aware that RSEs exist and that software has different quality aspects | Same as Bachelor | They should know where they can get help, and maybe able to use libraries | same as PhD | They should know the skills of an RSE and when they might need one in their group |
| LIBS  | They should be aware that RSEs exist and that there are tools available in their domain | They should be aware that there are tools that they can use in their research and maybe are able to use these libraries  | same as Master, but able to use libraries |  same as PhD  | They should be aware of the output of RSEs and motivate their students to use developed tools  |
| MOD   | It is sufficient to consider digital tools as black boxes | It is sufficient to be able to _use_ software as black boxes |  same as Master, but being able to write bug reports | same as PhD | same as PostDoc  |
| SWLC  | Awareness of the SWLC  | Know that one depends on software in their own research | Being able to evaluate software for their research |  same as PhD | Should be able to judge the sustainability of the performed research |
|SWREPOS| Should know that swrepos exist | same as Bachelor | same as Master, but should be able to find information on them |  same as PhD | same as PostDoc, but should be able to follow the interactions among different projects relevant for their research |
| LEG   | Should know that mixing/using software has legal issues and whom to ask | same as Bachelor | same as Bachelor |  same as PhD, but should know some simple Open Source guidelines | same as PostDoc, but should know the relevant patterns for their domain and sensitive their students  |
| NEW   | Still consumers of lectures | same as Bachelor | Curiosity for their research is required, curiosity for digital tools helpful |  same as PhD | same as PostDoc and expert in their field  |
| RC    | An awareness that research follows a cycle | Know that research follows a cycle and locate their masters thesis' stages in it. | Same as Master, but applied to the PhD. Additionally awareness about interaction with services |  Same as PhD. But proficient in the domain | Same as PostDoc, but ability to lead a topic  |
| SD    | They should know that their domain has relevant tools | same as Bachelor | Should know how to find full applications for their research | same as PhD | Should motivate their students to reuse existing tools  |
| DOMREP| Should be aware that their domain has repos | same as Bachelor      | Should be able to interact with their domain repos | Proficient users of their domain repos | same as PostDoc |
| USERS | Should be aware that they are users of a software | same as Bachelor  | Should be aware that their user view is different from the developer, in order to write bug reports |  same as PhD | Should be able to contribute meaningfully to the steering decisions of the software in their fields |
| TEACH | Ability to peer-to-peer teaching | Small exercise groups | Ability to supervise a student. |  Ability to supervise students and create a course? | Ability to guide students. Give full-size lectures |
| PM    | Awareness about project management optional | Awareness that research teams are structured according to some project management   | same as Master, or more depending on structure of research |  same as PhD | Should know about the required project management they require for their group |
| TEAM  | Awareness that research is often performed in groups | Ability to work in their group for doing their master's thesis | same as master |  same as master | Should be able to lead a research team |

\elandscape

### Project team Size
Some explanation of the team sizes:

- individual: A single person working on their research software
- Small team(~4 persons) This is a small team, that has decided to work together on something
- Organizations( >10 persons): These are big organizations with clear structures and a bigger degree of specialization.

\blandscape

|       | individual | small team | organization  |
| ----  | ------ | ------ | --- |
| DOCBB |   you might get away with less satisfactory code, as long as the product is OK | think about your colleagues    | your organization most likely has guides here |
| LIBS  |   you will only be successful if your artefact is usable by others    |  same here   | your organization probably has rules here |
| MOD   | you should precisely know what your entire code is doing where | you should know what your part is doing and have a feeling about the others contributions | You should know what your small part is doing |
| SWLC  | it's you and your software | You should know the Bus factor | The organization takes care of that |
|SWREPOS|   you need academic credit.    |   same here    | your organization probably has rules here |
| LEG   |   you carry the responsibility    |  someone in your group needs to take car of this    | your organization will have specialized people for it |
| NEW   |   You need a motivation to do this alone    |   ?    | Not so much, since other people might do this task |
| RC    | ? | you should maybe talk among your peers where your software fits in | You define your research cycle |
| SD    |   you need to be able to build on other work to be successful    |   same here    | there might be someone in your organization who does this |
| DOMREP|   You're doing science in a domain    |   there should be a person in your team who knows how to do it    | your organization might have specialists for that, but some basic familiarity |
| USERS | at one point you hope to have users | same here | maybe you have specialists for outreach |
| TEACH |   N/A   |   able to peer teach    | teaching to groups |
| PM    |   Not much required  |  able to follow checklist     | Working with PM tools, or use them for organization |
| TEAM  |   N/A    |   should be able to give equal feedback to their colleagues    | should be able to work within their role |

\elandscape

Bonus points may be distributed if managing teams remotely

[BIO Excel framework](https://competency.ebi.ac.uk/framework/bioexcel/3.0/carreer-profiles)

## RSE specializations
What we have defined above are intended to be base skills that an RSE irrespective of domain, place, and time should know about.
But not all RSEs are created equal, they specialize in different areas,
some of which we want to present below. Many of the specializations may overlap,
so the same RSE might for example work on data management and on Open Science.

### HPC-RSE
RSEs with a focus on High Performance Computing (HPC) have specialist knowledge
about programming models that can be used to efficiently undertake large-scale
computations on parallel computing clusters. They may have knowledge of (automatic)
code optimization tools and methods and will understand how to write code that is
optimized for different types of computing platforms, leveraging various efficiency
related features of the target hardware. They are familiar with HPC-specific
package managers and can build dependencies from sources. They also understand the process of
interacting with job scheduling systems that are often used on HPC clusters to
manage the queuing and running of computational tasks. HPC-focused RSEs may be
involved with managing HPC infrastructure at the hardware or software level (or
both) and understand how to calculate the environmental impact of large-scale
computations. Their knowledge of how to run HPC jobs and write successful HPC
access proposals can be vitally important to researchers wanting to make use of
HPC infrastructure.

They may also be familiar with High-Throughput Computing (HTC) and manage
a network of heterogeneous compute resources, typically desktop workstations
equipped with multicore processors and possibly GPU accelerators.
They can apply their node-level performance engineering skills to maximize
utilization of the available resources.
Finally, they typically have expert knowledge in at least one compiled language,
and can assist domain scientists who have excellent command of scripting languages
but only a cursory understanding of compiled languages get up to speed with
compiled software.

### Research Infrastructure RSE
This RSE is interested in SysOps and sets up infrastructures for and with researchers.
This RSE, therefore, requires a deep knowledge of physical computer and network hardware.
FIXME: While required, is this an RSE? this sets off the usual infrastructure vs. research discussion....

### Web-Development RSE
This RSE is skilled in web applications, front- and/or backend, and/or building 
and using APIs, for example for research data portals or big research projects.
Ideally, this RSE should also have knowledge about (web) accessibility to allow a broad
range of researchers or even the public to use the resulting applications.
Therefore a deep knowledge of web skills is a required skill for this RSE.

### Legal-RSE
With the prevalence of software, we foresee the need for RSEs that specialize in legal questions around software.
They are the go-to person if people have a question about licensing, mixing and matching software, and/or patenting.

### Data-focused RSE
RSEs working at the flourishing intersection between data science and RSE. 
They are skilled in cleaning data and/or running data analyses and can help researchers
in setting up their analysis pipeline and/or research data management (RDM) solutions.
When the field requires research on sensitive data or information, e.g. patient information in medicine, 
this RSE should have knowledge about secure transfer methods and/or ways to anonymize the data. 

### OpenScience RSE
Open Science and FAIRness of Data and Software are increasingly important topics in research, as exemplified by the demand of an increasing amount of research funding agencies requiring openness.
Open Science RSEs can help researchers navigate the technical questions that come up 
when practicing Open Science, such as "How do I make my code presentable?", 
"What do I need to consider when it comes to licensing?", or 
"How can I use version control / automation for my project?".

### Project/Community manager RSEs
When research software projects become larger, they need someone who manages
processes and people. Building a community around a research project is an
important building block in building sustainable software [@Segal2009], so these RSEs play
an important role, even if they do not necessarily touch much of the code themselves.

### Teaching RSEs
RSEs who focus on teaching the next generation of researchers and/or RSEs play
a vital role in quality research software.

### ${DOMAIN}-RSE
While software is the lingua franca of all RSEs there will be RSEs that have specialized in the initricacies of one particular research domain, such as medical RSEs, digital humanities RSEs or physics RSEs.

### Optional RSE competencies -> Maintenance RSEs 
Oftentimes, a significant amount of effort in (research) software development needs to be spent on maintenance to ensure that software remains useful for researchers now and in the future.
The research environment is constantly changing and this can also apply to the software requirements.
Accordingly, software often needs to be adapted continuously. If it isn't, the software can reach a point where it simply isn't useful to the researchers anymore.
To avoid this, regular work needs to be invested. 
While ensuring maintenance and sustainability of research software is of huge importance to the communities that build and use it, a particular challenge is that it's often very difficult to obtain ongoing research funding for software maintenance tasks. As a result, when a project that developed or extended a piece of software finishes, it can often be the case that support for the software fades as team members move on to other research, academic or RSE roles, or become busy with other funded work.
While this is not a core concern of this paper, we wanted to highlight this important issue that is frequently faced when working with software in the research community.
With regard to which additional competency is required, these are people having experience with ancient software stacks that are not anymore part of the general curricula(think of COBOL and FORTRAN).

FIXME: I think it would be nice if we could move each of these optional competencies to a different specialization.


## How do we reach people in different stages of their careers?

Many current RSEs have found their way to being an RSE during their doctoral studies. This transition usually happens slowly. You start programming a tool, and someone else likes it, it becomes known that you have programming skills and suddenly you are the RSE of the group that everyone would like to have in their projects. If you enjoy this role, you need to be aware that there is a RSE career path as well as that specialized training materials exist. One place to generate awareness of the career option and training is universities' doctoral onboarding processes or right thereafter. RSE training could be offered as elective courses at universities organized by some central organization. RSE could be presented as a career path in suitable events. Since many RSE-minded people also at some point find their way to an HPC cluster, mailing lists of said clusters could be utilized to advertise RSE courses. One important aspect to think about is also the wording in the advertisement. Potential future RSEs might not know the term yet or know that the course advertised includes topics that are of interest to them. If the university or organization has a GitHub/Lab organization/project, having a banner there might reach the right people. Most important is that people working in IT helpdesks know about the courses offered so that they can advise students/researchers on visiting the course/reviewing the materials if related questions are asked. 
For an RSE it is important to be a part of a network with other RSEs, irrespective of the career level.
A perfect first step for forming this network is topic-related conferences, workshops or meetups.
Beyond that, there is the broader RSE community organized at the local and regional level with chapters or local/regional communities, at the national level with societies and the international RSE society. Each of them offers possibilities for connecting within or beyond an individual institution and is a great way to find like-minded people to grow a wider network and thereby facilitate the sharing of information on interesting events or help each other out.
This available layered network can greatly benefit the RSE in finding help with issues outside of their own comfort zone
and provides a welcoming, social safety net providing a home for the RSE. Since we feel providing aspiring RSEs this net
is of utmost importance we envision compulsory events introducing that to young RSEs. Qualification badges are another venue, that RSEs to find people with the same technical interest.

Short primers on RSE skills, infrastructure and good coding practices
can be found in field-specific scientific articles and conference proceedings,
such as [@Roberts1969; @Baxter2006; @Prlic2012; @Leprevost2014; @Wilson2014c;
@Stodden2014; @Crusoe2016; @Crick2017; @Fehr2021; @Grossfield2022], some of
which are specifically tailored to group leaders, institutions and scientific
journal editors rather than RSEs [@ChueHong2013; @ChueHong2014; @Katerbow2018; @Strasser2022].
Scientific journals have the advantage of reaching a large spectrum of
research scientists at all stages of their career.

Localizing RSE teaching material and RSE information in languages other than English
can help reach a much wider audience by lowering the barrier to entry in the field.
In 2014 the community behind The Carpentries engaged in an international
effort to translate their training material into Spanish [@Wilson2014a],
Korean [@Wilson2014b] and Portuguese [@Silva2014].
Core lessons have been translated to Korean in 2015 [@Lee2015], and the Spanish
core lessons are now officially part of the Software Carpentry material [@CarpentriesSpanish].
Similarly, in the period 2015-2017, the Stack Overflow website launched localized
versions in Portuguese [@StackOverflowPortuguese], Russian [@StackOverflowRussian]
and Spanish [@StackOverflowSpanish] to reach a wider community.
There are also RSE short primers [@Astigarraga2022] and
RSE guidelines [@ClementFontaine2019b; @Appel2021; @Haim2021] in non-English
languages to address the need of specific communities.

Teaching RSE in relevant undergraduate courses of domain scientists
can be the first point of entry in the field.
However, considering many RSEs come from domain studies, only fundamental
concepts (of RDM and RSE) can be explained to and experienced by all of them.
Those interested in domain-specific RSE skills or even programming will gain the
special knowledge in classes and projects they choose.
For example, statistics curricula can
be used to showcase RSE infrastructure, e.g. the R programming language and
its ecosystem of statistics libraries and integrated development environments
[@Reinhart2021; @Beckman2021; @CetinkayaRundel2018].
There are also bioinformatics courses designed for high school students that
cover topics such as pen-and-paper algorithm design, genomic database querying
and data mining, and open data [@Form2011; @Bain2020], as well as graduate
courses designed for Master's degrees and Ph.D. programs [@BioinformaticsCertification].

Teaching incubators can be leveraged to develop and test new academic curricula
that introduce basic RSE topics, such as the "Algorithmic Battle"
[@AlgorithmicBattle] (version control, documentation, good coding practices),
"digit@L" [@DigitalLearning] (coding, data analysis, machine learning)
and "DigiFlex" [@DigiFlex] (digital tools) experimental modules funded by the German
Foundation for Innovation in Higher Education [@StiftungInnovationHochschullehre]
to reduce skill gaps among first-year university students.
Likewise, The Carpentries teaching material can be made more modular
and re-usable in domain-specific contexts to better suit the needs
of specialized RSEs. Examples include HPC Carpentry [@OCais2020]
and Data Carpentry for Biologists [@White2022].

FIXME:

- find more examples of teaching material in non-English languages
- discuss the role of translations in overcoming linguistic and cultural barriers?

Further ideas:

- making RSE best practice guides fun to read with memes or satire [@Balaban2021; @Laginja2022; @Astigarraga2022; @Fehr2021]
- reducing the skill gap by organizing more inclusive workshops [@McInerney2017; @Akoh2017; @Shelton2017; @NatlAcadSci2022],
  to address gender disparities or take into account economic status, cultural background, or special educational needs;
  peer-reviewing of code of conducts by the CHAOSS Diversity and Inclusion Badging organization [@CHAOSSDEIBadging; @GitHubCHAOSS]
- related discussion in CSE [@Webb2017]

## Organizational Infrastructures
So we have defined our set of competencies that we feel every RSE should possess.
Table 2 above nevertheless already hints at the fact that some RSE skills are required during the domain studies,
while Table 1 tells us that we also need an ongoing qualification programme for people that want to become specialized RSEs.
In order to set up a proper educational scheme we need to discuss two more items:

- Who are our teachers?
- How is this teaching organised?

### The teachers
#### What issues are trainers facing today?
There are already some people out there who are teaching RSE related topics sometimes in university structures, but often outside of formal structures.
The community discussion shed some light on the issues our trainers are facing now.
Currently, they are often teaching workshop like formats in research institutions.

- There are outreach issues. We emphasize that there are two dimensions to this: First it is important that we inform students that workshops exist, and then, the more important part, we also need to motivate people to invest the time for a workshop. [@EuroCC2022]
- Adaptation of material to the target audience has been identified as a time consuming task.
- Organization and preparation is a challenge, since currently no standardized formats exist.
- Expectation management of students. Existing knowledge of students is often diverse.
- Language barriers. This can range from the use of technical jargon up to the disparities of you teaching in a foreign language.
- Setting up a feedback loop that facilitates a reflection of the workshop for the teacher.
- staying up-to-date with fast-moving RSE topics.
- Understanding the difficulties of students [@Cereceda2020; @Williams2019].
- Carpentries retrospective [@Wilson2016a].


#### What mindset makes up a good teacher
Irrespective of where people come from they need to have the proper mindset to properly foster aspiring RSEs.

- "If you want to go fast, go alone; if you want to go far, go together?"
- Not every "good" scientist wants to become a "good" software engineer, too!
- The Carpentries philosophy [@Duckles2016]

#### Where do we get our teachers from
The community discussion brought about the need for a mixture of people, thereby 
the education of aspiring RSEs will involve people from close domain sciences or experienced RSEs
and people that have respective additional skills to teach RSE competencies to the new generation.
In that respect, this follows the carpentries model that offers certifications but is still open to non-certified trainers.
We highlight and emphasize, that since a topic like RSE education, is constantly evolving, trainers strongly require the opportunity to and the recognition to educate themselves.
Therefore our teachers will be sourced from the workplace but there will also be certified RSE Trainers.
(FIXME: in classical university speak, these would be people who have done their habilitation on that topic, right?)

We propose to create common Infrastructures that can be utilized in this ongoing effort to professionalize the RSE education further, to easily share education resources across the country.
(FIXME: DETAIL ME FURTHER!!!!)

### Organization of teaching

#### Certificates

With the ever-growing demand for RSEs in science it could be helpful for
people to earn certificates for skills needed in certain RSE positions.
This would possibly make hiring easier and could incentivise researchers
to go through proper courses on these skills instead of learning on the go.
For certain skills it would also be good for finding jobs outside academia,
e.g. in industry where certain practices are already state-of-the-art.
However, these certificates are only helpful if there is a certain level of
standardization, which would require a central authority or collaboration
between multiple stakeholders to decide on contents and allow participating
institutions to issue these certificates.
Additionally, it can be excluding capable applicants who already use these
skills but never got a certificate for it.

The possible types of certificates can of course differ.
The [HPC skills and certification] Appendix explores current efforts at creating
a HPC certification program for both academic and industry RSEs. Course attendance
sheets and digital tokens [@Ifenthaler2016; @Chakroun2018; @Fanfarelli2015; @McDaniel2016]
are another option (see Appendix: [Micro-accreditation]).

Having certificates provides finally a clear understanding of which tasks an RSE can perform and thereby helps defining the career path and the job description.
A big demand for specialized RSEs will certainly come from the newly established RSE centers at research institutions that require skilled people to fill their vacant positions.
And using the certificates, the demand can now be satisfied with people offering this skill.

Some exemplary skills for which courses are already held are version control tools like git, HPC topics like multithreading, MPI and GPU computations, FAIR principles.

## Required Next Steps
We have identified the RSE as an individual who brings a unique set of skills for
supporting and undertaking modern digital research into research groups and teams.
We have elaborated on the basic competencies that RSEs may have, and we have
provided a detailed picture of how these competencies manifest along different
dimensions.
We have discussed who can deliver the necessary skills and the approaches to
support skills development. Now, in the final step, we want to discuss how this
specialization can become a natural part of the landscape of professions and which
steps we need to take to professionalize their education.

We foresee that the development of RSE skills will rest on two pillars:
A first qualification phase, possibly through academic structures, giving newcomers
to the field highly sought after professional skills, either directly from high school,
or as a result of a career change. But since the type of work undertaken by RSEs is
highly dynamic and often relies on knowledge about latest technologies, things change
quickly and an ongoing learning phase is also necessary to remain up-to-date with the
current developments, tools and techniques. 
In this context, we put forward the idea of having institutionalized structures that
facilitate continuous learning. These structures may be integrated within an academic
environment but they may also exist fully or partially outside of the academic sphere,
also providing opportunities for education on digital skills into wider society or
industry (see [@HPCAkademie] for an existing, HPC focused instance of this).

### First Professional Qualification
#### A possible graduation path within the classical university structures
We have put forward the idea that familiarity with research is a prerequisite for an RSE in order to be able to work effectively in the research space and in collaboration with researchers.
To generate the required number of skilled persons we propose to offer a classical Bachelor's and Master's curriculum at selected sites.
In this particular example, we consider a path into RSE via a traditional university route involving Bachelor's and Master's degree studies that include a RSE element.

However, we recognise that there are other routes into an RSE career and these are increasing.
For example, some RSEs come from an industry background, others may come through apprenticeship or similar programmes.
In both cases, gaining knowledge of the research lifecycle and understanding the ways that researchers work towards solutions
to research challenges is something that can be developed on-the-job alongside training opportunities and the chance to work directly with researchers.
This leads naturally to the question, whether it is possible to become an RSE without a home research domain.
With software being a core element of the research process in so many different domains,
it is not helpful for everybody working in RSE to have a background in computing or software engineering.
Indeed, we consider it much more useful if new graduates looking to work in the RSE space come from a wide range of different domains.
Expertise, beyond software development skills,
in another research domain can be an important element of an RSE team being able to support RSE projects in that domain.

A \${Domain}-RSE in the STEM domains can start with a Bachelor's degree in their domain that shares large portions
of the curriculum with their original domain. There will only be some courses that advance peoples knowledge about digital
tools and how to create tools from them.
The Master's years bring them forward to actually applying their knowledge. So during these years they
simultaneously work on deepening their knowledge about team skills, a topic they have been neglecting so far,
they work towards getting to the current research in their domain, and getting up to speed about the current collaborative development practices.
So we can assume that the lectures to that point contain a mixture of domain specific content and RSE specific content
(A good starting point for an RSE in the natural sciences), then we come to the question of the topic of the master's thesis.
In order for young RSEs to get their research experience we believe it is necessary that already
in their master's thesis young RSE students are given computational research tasks
that can be solved with the RSE specific skills of that domain.
This gives them a Master's degree of a ${DOMAIN}-RSE that has learnt in their lectures a research domain specific part and a software engineering specific part,
and enabled them to get a first dip into actual science in their master's thesis.
Of course special care has to be taken to integrate them at some point in their studies into mature projects
to expose them to the eperience of senior RSEs and how they approach problems.
An example of this \${DOMAIN} - RSE can be found in Appendix: [Bioinformatics skills and certification].
Of course, the next question for their future is whether a master's degree enables them to really be effective parts of a research group.
While we accept this is something of a generalisation, we argue that this is most likely not the case since
undertaking a PhD provides a much more extensive set of research training and experience that can be vital for a researcher's future.
Research environments differ internationally but in many cases there are formal barriers in the research landscape that require a PhD (e.g. eligibility for funding).
Hence a PhD is required to actively participate in science and hence we argue the regular RSE
should do a PhD that on one end combines knowledge of a research domain with software engineering heavy task
such that both pillars are suitably covered and have been exposed to research, software development and team dynamics.
Having gone through this, this opens to them a future career as a lead RSE in their domain.

#### Specialised Master's Programs
On the other hand, when pursuing a PhD,
scientists are increasingly required to do RSE-type work as part of their research as data
and computation are becoming part of research tasks in a huge range of fields.
It is not uncommon for researchers to be faced with RSE topics for the first time, because it has not been part of their academic curricula.
Many are faced with a steep learning curve that requires them to invest a huge amount of time to catch up.
Naturally, many would only invest as much as necessary to get the job done regardless of whether the solution is sustainable or not.
Support from RSEs is one way to resolve this challenge.
Another would be to lay more effective foundations for future RSE work at a much earlier stage in undergraduate/postgraduate studies.
We see scope for establishing dedicated RSE Master's programmes which specialise in developing RSE skills and practices.
Some universities already offer dedicated master's programs in some domains.
Examples would be Computational Sciences in Engineering (CSE) or Bioinformatics
(see Appendix: [Bioinformatics skills and certification]).
Where appropriate similar programs should also be established in other domains.

#### Alternative first qualification paths
For completeness we mention that vocational programs like the MATSE [@MATSE] can provide a more application oriented less research oriented profile for individuals.
Since a certain amount of overlap with sciences is expected, it is expected that programs can be switched with minimal friction.

### Extra-academic institutions for continuous learning
As elaborated in the instruction the dynamic working place of an RSE requires continuous learning.
Knowledge-based industries have long recognized the value of qualifying their employees and hence invest time and money into this.
We propose institutionalized structures that offer graduates a venue for life-long learning, or to deepen their skills.
Centralizing this notion in a few institutions has some major benefits for society and industry as well,
since these become central hubs for offering the skills with digital tools.
The HPC-Akademie [@HPCAkademie] is a good example in the HPC space that offers its services to graduated
researchers that want to deepen their HPC skills for research or to practitioners tht require them for industrial applications.
specializing the centres to certain skillsets enables them to effectively reach out into the sciences with their brand.
With the existence of these resources we believe that their acceptance gradually increases over time.
The tasks of these centres is facilitated by reusing the work of initiatives like edutrain [@edutrain] and platforms like DALIA [@DALIA].
Naturally, other existing structures outside of academia mentioned before like the Carpentries [@Carpentries] can be nicely integrated
and offered to a broad audience on a regular basis.

### Micro-accreditation
With the existence of institutions for continuous learning
after the first professional level of education the question of certification arises.
We propose, digital certificates and
learner badges [@Ifenthaler2016] as one possibility for experienced RSEs
to showcase that they posess a certain technical skill.
For example, the Software Carpentries minted digital badges in 2012
[@Wilson2012a; @Wilson2012c] as a form of institutional accreditation.
Despite initial plans to create skill-specific badges [@Wilson2012b],
learner badges were ultimately abandoned in 2013 [@Wilson2013a] and recycled
as participation certificates [@CarpentriesCertificates].
Instructor badges were introduced instead [@Wilson2013a],
which are now mandatory tokens to lead a Carpentry workshop or vote in
council elections [@CarpentriesInstructorBadges].
Ireland's Professional Development Framework [@Donnelly2018]
provides accreditation to higher education teachers who successfully complete
training on the National Forum's Open Courses via digital badges [@OpenCoursesBadges].
The Extreme Science and Engineering Discovery Environment organization
delivers badges to incentivise participation in HPC training events
[@Kappes2015; @Sale2017]. IBM delivers badges to promote continuous learning and
provide micro-credentials to its staff and customers [@Leaser2020; @Leaser2019]
There are 1360 badges as of July 2023 [@IBMBadges]
and 1 million badges were issued as of July 2018 [@Daniels2018];
they are recognized by a few academic institutions
[@NortheasternUniversityIBMBadges; @NCCentralUniversityIBMBadges; @BluefieldIBMBadges]
and in some cases are convertible to graduate credit [@Leaser2020].

The Open Source Software Security Mobilization Plan [@OSSMobilizationPlan]
is proposing that code repositories and recruiting sites work on recognising
digital badges certifying RSE skills in secure software development.
Some code repositories already feature an infrastructure to automatically issue
digital tokens, from personal badges measuring contributions
[@GitHubProfileAchievements; @GitHubProfileTrophy] or community work
(e.g. outreach efforts, workshop attendance and package maintenance in Fedora [@FedoraBadges]),
to project-specific badges [@OSSFBestPracticeBadge; @Trockman2018; @Legay2020]
that illustrate best practices, such as high code coverage or code quality,
or signal commitment to diversity, equity, and inclusion [@CHAOSSDEIBadging; @GitHubCHAOSS].

FIXME or remove me:

- an argument could be made for having less metrics (GitHub allows users to hide their badges)
- which institution would create RSE-badges? how would this institution drive adoption of RSE-badges?
- downside of fine-grained badges: number of badges can grow quickly
- badges can also fade away, i.e. have diminishing relevance or usefulness over
  time (e.g. old workshop participation badge, or technologies that have since
  become less relevant in the RSE field)
- reviews [@Zhou2019; @Hansch2015; @Ahsan2023; @Liyanagunawardena2017] and
  case studies [@Morris2019; @BorrasGene2018; @Higashi2020] on digital badges

remaining Plan:
- Lehrer ist damit natürlich ein Karriere-Pfad für RSEs
- beides braucht geeignete Lehrer
- pointer to the qualification paths and career paths outside of the appendix.

FIXME: The career path discussion.


#### Academic Considerations
- Awareness of existing teaching programs
- "Branded" Add-on courses
- External Institutions provide resources
- fully recognized in the academic system. Students get ECTS points.
- Bachelor/Master specializations

#### Broader Considerations
- Instilling more respect for people that want to educate themselves for digital competencies
- Outreach to people that now have the feeling that they require this training.

## Conclusion
We have indentified the RSE as an individual that contributes to research teams with their knowledge about digital tools.
Then we have defined generic core competencies from the pillars of Software Engineering, Research and Team processes.
We fleshed them out with some possible specializations of RSEs.
Given the competencies and a demand(FIXME: Do the calculation) in the research landscape for them we moved on to define who the teachers are for this new field.
We closed with a discussion of possible structures and organization forms that educate new generations of RSEs in more structured programs than what is available today.
Therefore this closes the gap, that the research landscape requires RSEs, but there are no structures where these persons are educated, by detailing the career path that a young person might want to take to become an RSE.(FIXME: also aspirational...)

## Appendix
### An applied example curriculum

### An example of a possible career path
- We can follow Kim, who has been the protagonist of the original deRSE Paper.

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

Also looking at pathways and how different skills are related,
the UNIVERSE-HPC project [@UNIVERSEHPC], funded under the UK's ExCALIBUR
research programme [@EXCALIBUR], is looking to understand and develop
training pathways to support the development of specialist skills in the HPC
and exascale domains. The project is gathering open source training materials
to develop curricula that support the training pathways that are underpinned
by high-quality training materials.

### Bioinformatics skills and certification

Bioinformatics is another field that actively works on developing skill trees.
The Bioinformatics Core Competencies [@Mulder2018; @Welch2016; @Welch2014],
the BioExcel competency framework [@Matser2016],
the PerMedCoE competency framework [@Lloret-Llinares2021],
the Research Data Management and Data Stewardship competence framework [@Demchenko2021]
and the ELIXIR Data Stewardship Competency Framework for Life Sciences [@Scholtens2019]
are examples of grassroot efforts aiming at defining the set of skills
of various bioinformatics specialties,
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
knowledge, skills and abilities (KSAs). They can be organized in a taxonomy,
and are also transferable, i.e. a KSA can be a pre-requisite to multiple competencies.
The Mastery Rubric for Bioinformatics [@Tractenberg2019] and the ELIXIR
Data Stewardship Competency Framework for Life Sciences [@Scholtens2019]
are examples of KSA frameworks for bioinformatics curricula.

The Curriculum Task Force of the International Society for Computational
Biology (ISCB) curates a database of degrees and certificates
in bioinformatics [@BioinformaticsCertification; @Mulder2018].
The database includes Bachelor and Master's degree programs and specializations,
Ph.D. programs, and certificates from graduate schools.

