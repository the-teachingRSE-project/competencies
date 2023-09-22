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
output:
  pdf_document:
    citation_package: biblatex
    toc: true
    number_sections: true
bibliography: bibliography.bib
header-includes:
    - \usepackage{pdflscape}
    - \usepackage{multirow}
    - \usepackage{array}
    - \usepackage{longtable}
    - \newcommand{\blandscape}{\begin{landscape}}
    - \newcommand{\elandscape}{\end{landscape}}
---

**Abstract**:
The term Research Software Engineer, or RSE, 
emerged a little over 10 years ago as a way to represent 
individuals working in the research community but focusing on software development.
The term has been widely adopted and there are a number of high-level definitions of what an RSE is.
However, RSE roles are varied. At one end, RSE roles may look similar to a traditional research role.
At the other extreme, they resemble that of a software engineer in industry.
Most RSE roles inhabit the space in between these two examples and providing a straightforward, 
comprehensive definition of what an RSE does 
and what experience, skills and competencies are required to become one is therefore challenging.
In this paper we define the broad notion of what an RSE is, explore the different types of work they undertake, and
define a list of foundational competencies as well as values that define the general profile of an RSE.
Using this information, we elaborate on the progression of these skills along different
dimensions, looking at specific types of RSE roles and giving examples of future specializations.
An Appendix details how existing curricula fit into this framwork.

---

**Keywords**: research software engineering, training, learning, competencies


# Required Generic RSE skills
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

## Software Engineering Skills
There are many software engineering curricula out there, that try to define
which tasks a software engineer should be able to perform. A recent example
highlighting some aspects in more detail than here is [@Landwehr2017].
The software skills outlined here are required to make research software adhere
to the FAIR principles. [@ChueHong2014] defines different levels of research
software reuseability and the extent to which the software engineering skills
need to be applied to reach them.

### Creating documented code building blocks (DOCBB)
The RSE should be able to create building blocks from source code that are
reusable. This ranges from simple libraries of functions up to complex
architectures consisting of multiple software packages. An important part of
reusability is that at least oneself, and ideally others, are able to understand
what a piece of code aims to do and how to use the provided functionality. This
is primarily achieved through a "clean" implementation and enhanced by
documentation. Documentation ranges from commenting code blocks to using
documentation (building) tools.

### Building distributable libraries (LIBS)
The RSE should be able to distribute their code on their domain/language
specific distribution platforms. This almost always encompasses
handling/documenting dependencies with other packages/libraries. It sometimes
requires knowledge of using build systems to enable interoperability with other
systems.

### Understanding the software lifecycle (SWLC)
The traditional software lifecycle defines the stages that form the process of building a piece of software.
This generally involves a creative process where you try to understand what it is that you need to build,
work out how you are going to build it and then implement it.
This is then followed by testing that things work as expected and that they continue to do so into the future.
We emphasize that the lifecycle is not complete here but also includes periods of maintaining a software
and also withdrawing software from its original use.

### Use repositories (SWREPOS)
The RSE should be able to use public platforms to share the artefacts they have
created and invite the public to scrutinise them for public review.

### Software Behaviour Awareness and Analysis (MOD)
We define this as a certain quality of analytical thinking that enables an RSE to
form a mental model of a piece of software in a specific environment.
Using that, an RSE should be able to make predictions about a software's behaviour.
This is a required skill for common tasks like debugging, profiling, designing good
tests, or predicting user interaction.
An important facet of this capability relates to information security.
RSEs need to consider the safety and integrity of personal data and other sensitive information
and make sure that they don't negatively impact the integrity of their institution's network.

## The research skills
### Curiosity (NEW)
RSEs gain their reputation from their effectiveness to interact with their
domain peers. Therefore, some curiosity together with a broad overview of the
research field is required. Curiosity is also reflected when an RSE is actively
trying out new tools. Lifelong learning is then no longer just a phrase, but
becomes a motivation to work.

### Understanding the research cycle (RC)
One of the crucial skills of RSEs is their mental proximity to research.
They embrace being part of a larger community which,
despite friendly competition, shares the common goal of gaining knowledge
for its own sake and not just for personal or commercial gain.
Thereby they know, that they are part of a bigger cycle that involves many other parties in and outside of
their domain, and also that their software can be utilized in different stages of the research cycle by different persons.
Like other researchers, RSEs are open to discussions and arguments beyond
their own expertise and appreciate the underlying principles of
good research, like publications, review and reproducibility.

### Software re-use (SRU)
One goal of FAIR software is to avoid unnecessary duplication of work by reusing
existing work instead. To (re-) use software, researchers have to be able to
find it and then to easily evaluate if the software actually suits their needs.
Apart from functionality also the integration with other software,
expected sustainability and expandability have to be part of this evaluation.

### Software publication (SP)
The second part of FAIR software is concerned with publishing new and derived works
and making them available for re-use by the research community and the general public.
RSEs need to have a basic understanding of common software license types, such as "proprietary", "copyleft", and "permissive",
the compatibility of different common licenses and the ramifications for re-using and composing programs.
Finally, RSEs will need to properly execute the technicalities of software publishing,
such as applying licenses, honoring copyright statements and crediting contributors.

### Using domain repositories/directories (DOMREP)
Almost all research software is developed within a specific scientific domain.
Some software may be able to cross boundaries, but the majority will have a
home domain, with which it needs to be able to interact. The RSE needs to be
aware of any domain specific software repositories, data sets and catalogues
and the RSE's software needs to be able to interact with the existing
domain-specific data repositories.

## Team Skills
RSEs do not work in isolation.
They are embedded in a research group or work within a team of RSEs supporting particular research projects.
RSEs often need to interact with and facilitate communication in-between colleagues, clients and contractors
with a very broad spectrum of background-knowledge, specialization, expectations and experience.
The team skills are therefore crucially important.
Teams skills are also mentioned in common guides for software engineering such as the Software Engineering Body of Knowledge [swebok_2024].
However, the interpersonal and organizational skills and the capacity for adaption required to work in a research setting
warrants a much stronger emphasis on this field of competence.

### Working in a team (TEAM)
Working in a team is all about communication.
For example RSEs need to be able to explain particular implementation choices made and may even need to defend them.
Within a team of RSEs code reviews improve knowledge transfer and increase team cohesion.
Senior RSEs may lead a team of RSEs.
The team might change on a project-to-project basis and might be comprised of colleagues with very different backgrounds
including, next to software engineers, for example IT staff, domain scientists and technicians.
The shared values come into play and each RSE needs to ensure that these values are lived by and passed on to others.

### Teaching (TEACH)
RSEs have many opportunities to teach.
These range from inducting new colleagues to teaching digital skills either through short courses, for example from The Carpentries [@Carpentries], or entire lecture series.
RSEs may also act as mentors and consultants.
Code review also includes aspects of the teaching skill.

### Project Management (PM)
The RSE should have knowledge about project management. At some institutes, it follows the practices of the local research groups,
but it is useful, if an RSE knows its place in a PM scheme, or can bring in new ideas for improvement.
Project management in research software engineering poses specific challenges that might require the capacity to flexibly adapt to changing conditions and deviate from common project management methods.

### Interaction with users and other stakeholders (USERS)
Since research software is often developed as part of the research process itself,
its requirements and specification might change with the progression of research.
Stakeholders of research software often change across different research projects
or even within the course of one project.
Roles in connection with research software are often in flux and diffuse.
For example a single person might be user, developer and project manager at the same time.
These conditions pose specific challenges for requirements analysis, project management, training and support.


## RSE Tasks and Responsibilities
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
use of collaborative platforms like github/gitlab, honouring a project's Code of
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
- Finding a community. This can be interpreted in two different ways. First
we have the aspect of community building for a research project. Since this
deals with software that is supposed to be used in research this requires
knowledge of RC, USERS, and also NEW, in order to effectively interact with
domain scientists. Today, an example is a presence on social media. The other
TEAM-related aspect is the embedding of RSE graduates into the community of
RSEs. We envision our RSE graduates to be a part in a strong network of other
RSEs, tool-related communities and the classical domain communities. This point
is further elaborated in [How do we reach people in different stages of their careers](#how-do-we-reach-people-in-different-stages-of-their-careers).


Beyond that, we feel that today other important tasks of RSEs are

- Mentoring colleagues.
  This necessitates giving good advice that fits to a projects stage in its lifecycle,
  thereby requiring knowledge of (SWLC), and its context in its research domain and thus (RC).
  Research software often starts out as a tool to answer a personal research
  question and becomes more important when other researchers rely on it.
  Some research software might even be used to deal with critical questions such as weather forecasting or medical diagnosis.
  To formalize the process of giving good advice a classification of software is commonly used [@Wang2012; @Schlauch2018b]
  where research software can move from one class to another during its lifecycle.
  [@Schlauch2018b] classify applications based on their scope and criticality and provide software engineering recommendations.
  The RSE needs to be able to identify the application class they are dealing with and apply the respective RSE practices.

- Enforcing reproducibility. Projects like [@ReproHack] can greatly help in fostering that competency.

# How much do different people need to know?
Now that we have the different competencies, we can explore various dimensions of these competencies,
depending on their circumstances. A strong beneficiary of specialized RSEs can also be newly formed RSE centers at research institutions.

## Career level
At different career levels, differing skills are required. We have set this up according to the following separation often applied within a single project:

- Junior RSE: These are persons that have just started, but generally speaking they should have the skills to contribute to software projects
- Senior RSE: They have gained experience and can set the examples in the software project.
- Principal RSE: Their actual job description varies a lot. These may be RSE team leaders based in a professional services type role, or they may be professors or research group leaders based in a more academic-focused role. They are often the people responsible for bringing in the money that supports new projects and sustains existing projects. Generally speaking, they do not need to to be actively involved in the day-to-day technical tasks but they should be able to guide projects from both a technical and research perspective.

The required skills are distributed according to this table
First Dimension: Career path e.g. Junior RSE -> Senior RSE -> PI scale (1->6) (less -> lot)

\blandscape
\small
\renewcommand*{\arraystretch}{1.4}

|       | Junior | Senior | Principal RSE(brings in funding)  |
| ----  | -------------- | -------------- | ------------------ |
| DOCBB | should be able to write reusable building blocks |same as junior, but the quality should set the standard for the project, while following current best practices | should know the current best practices and point its people to the right resources. |
| LIBS  | should be able to use package distribution platforms      | same as junior, but should set the project standard and follow current best practices. | should ensure that their project is in an up-to-date distribution platform |
| MOD   | should have a basic grasp of their piece of the software in order to use basic tools like a debugger | Should understand the characteristics of large parts of the codebase considering a variety of the metrics | Should understand the big idea of the software project in order to define the task that the software solves  |
| SWLC  | Awareness about the existence of the software lifecycle. | Should know which decisions lead to technical debt. | Should know in which part of the lifecycle their project is and how to steer development/project resources accordingly. |
|SWREPOS| Seamless interaction with the swrepo of their project is a must | Should be well-versed in the intricacies of a swrepo, and probably interact with multiple projects' repo's | Should be able to effectively interact with swrepos and especially the interaction with the connecting projects. |
| NEW   | Some curiosity required to fit into research teams | same as junior, but a curiosity to enhance the code base is required | Curiosity to know in which direction to steer the project is required |
| RC    | Awareness about the RC | should know the position of the project in the RC | Should know what is necessary for the project to fit into its position in the RC |
| SRU    | Should be aware about tools for SRU |   Should be able to find sth. with SRU tools    | Should be able to effectively find sth. with SRU tools and be able to evaluate and perform the integration of a library into the project. |
| SP    | Should be aware that SP needs to consider issues of intellectual property | Should be able to correctly publish software in simple cases and be able to identify cases where professional legal advice is needed. | Same as Senior plus the ability to take the future publication of software into account when initiating and guiding larger software collaboration projects |
| DOMREP| The RSE should be able to interact with the domain repository | same as junior RSE | same as junior, and should know about how it fits into workflows surrounding these domain repositories |
| USERS | The RSE should be able to communicate with non-SE users of the project | same as junior | same as junior, and take feedback into account of the steering |
| TEACH | should be able to perform simple peer-to-peer onboarding tasks | should be able to explain logical components to other RSEs | Should be able to effectively communicate about all large-scale parts of the project. |
| PM    | Awareness about the employed project managemement method | Should be able to use the employed PM method | Should be able to design and adapt the employed PM method. |
| TEAM  | Should be able to work in the team in order to effectively fulfill the given tasks. Should be able to learn from code review. | Should be able to break down tasks into more easily digestable sub-tasks | Should be able to lead the team and set the respective direction. |

\elandscape

## Academic Progression / Career Path? (Help me for better title) 
In the previous section, 
we looked at the competency levels needed for RSE specialists.
However, many of these competencies are important for typical researchers in academia.
Naturally, the 'R' competencies apply 
and research in general is increasingly team based.
Additionally, many researchers in fields from classical examples like 
numerical mathematics or theoretical physics 
to newer disciplines like digital humanities
will spend time in their research on writing and developing software.
Therefore, RSE focused training, e.g. in a Masters programme, 
is also beneficial for students in these fields
resulting in a broader audience. 

This section outlines how the RSE competencies could be reflected at all academic levels. 
It is important to note that this section does not reflect the current state of academic training and research institutions.
Instead, it summarises the discussions with and between workshop participants at different levels of academic progression on what they would have liked to learn at an earlier stage or know before starting their current position.
While individuals already work at implementing some of these changes and teaching these skills it has not yet reached a systemic level.

The text is organised along the academic progression path (Bachelor, Master, PhD, PostDoc, PI/Professor). 
Since each level is based on the previous levels we presume that the skills and competencies at each level also encompass those of the previous levels.
Due to the broad need throughout academic specializations,
the described levels serve as a baseline 
and certain fields will require higher SE skill levels 
as development is a large part of their actual research.

#### Bachelor
Students at undergraduate level mostly consume science/knowledge.
During their studies they should also learn about the existence of digital tools and structures.
Undergrad students should be aware that RSEs exist and that software has different quality aspects (DOCBB).
They should be aware of domain specific tools (LIBS, SRU) and where to find them (SWREPOS, DOMREP).
At this level it is sufficient to consider software as black boxes (USERS) although some training in data presentation would be very helpful and a good way to find out about programming (MOD, NEW).
They should have an awareness of software licenses and who to ask if they have any questions (SP).
They will be taught about the research cycle (RC) and that researchers often work in groups (TEAM).
During practicals they will have an opportunity for peer learning (TEACH).

#### Master
A student at Master level can participate in science and should therefore be able to use "some" digital structures. 
A master student needs to be aware of relevant tools and data sets for their domain, where to find them and how to use them (LIBS, SWREPOS, DOMREP).
They should be able to process and present their data (MOD).
They need to understand how their research depends on software (SWLC).
Working on their master thesis allows them to understand the research cycle (RC), practice project management (PM) and collaborate with other members of their research group (TEAM).

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

#### PostDoc
PostDocs are independent researchers. 
Their role is similar to that of a PhD student with a deepened focus on their research career.
However, they are proficient users of all relevant tools, that make them active contributors to their domain of research.
They need to be aware of more advanced topics regarding intellectual property rights, such as patents (SP).

#### PI/Professor
They are experts in their field and should be able to give proper guidance to their students on which digital tools are currently relevant. 
They should be aware of the skills of an RSE and when they might need one in their group (DOCBB). 
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
We also look at organizational aspects in the context of each of the considered
competencies since there are a variety of ways that organizations can contribute
to and support them. We first summarise the meaning of each of the columns in the table:

- **Competency:** The code assigned to the competency being considered.
  See the list in **[Table ?????]**.
- **Individual developer (Locally-based):** A single person working on some
  research software - often a researcher with RSE skills.
- **Individual developer (RSE team-based):** A single person working on research
  software - generally a professional RSE supporting another team's software single-handedly.
- **Group of developers (Locally-based):** A group of RSEs/researchers within
  a research group or team, working together on developing software to support
  or undertake a single research goal/project.
- **Group of developers (RSE team-based):** A group of members of the RSE team
  working together on a research software project for a research group.
- **Organization-level support:** How the defined competencies are recognised
  and represented at organisational level.

\blandscape
\small
\renewcommand*{\arraystretch}{1.4}
\begin{longtable}{|p{1.8cm}|p{3.5cm}|p{3.5cm}|p{3.5cm}|p{3.5cm}|p{4.5cm}|}
    \hline
    \multirow{2}{*}{Competency} & \multicolumn{2}{c|}{Working as an individual developer} 
    & \multicolumn{2}{c|}{Working with a group of developers} & \multirow{2}{*}{Organization-level support} \\
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
    Should provide policies on sharing and reuse of software. May be driven by funder requirements/policies.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    SWLC&
    It's down to you to manage the complete lifecycle, if you move on,
      what will happen to the code?&
    More support with a team but do they have awareness/expertise
      of managing the lifecycle? What is the "bus factor"?&
    Even when working alone, team infrastructure and tooling can be vital
      in supporting the lifecycle and supporting sustainability.&
    As previous but with a large codebase, how many people know about each part?
      Need to think about coherent lifecycle management across the team - generally
      a key part of RSE team expertise.&
    Support for training important. Organization may also provide site
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
    Organizations can offer enterprise repository set ups,
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
    An individual's curiousity has now to be shared between the research
      goal and the software project, therefore learning new methods and
      skills may be challenging and is often not the core aim.&
    RSE teams should support their team members, especially when working
      individually on a project, to explore new tools and approaches,
      make relevant contacts and learn more about the research in the project domain.&
    Likely to be an area of interest for an embedded development team
      but if they are researchers, they defintely have curiosity in their domain.
      A curiosity for tools would be appreciated.&
    As per Individual (RSE team).&
    Organizations should reach out to relevant groups locally to help share
      information on new technical processes and tooling, and facilitate training.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    RC&
    This is likely to be familiar to individuals, who are often researchers,
      especially if they are embedded within a research team.&
    Many RSEs will have familiarity with the research lifecycle,
      although they may not have domain knowledge. This can be alleviated by interacting with a group&
    Likely to be familiar to software teams (often researchers) working
      in a research group. Can share knowledge between themselves or reach
      out to colleagues.&
    Teams of RSEs from an RSE group are likely to include one or more
      team members with strong awareness of the research lifecycle.&
    Research organizations have extensive infrastructure to manage
      the research lifecycle, this can support researchers/RSEs.
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
    The organization should raise awareness about software as publishable scientific output, provide recommendations and checklists to support software-publications and have legal experts in place to deal with complex cases.
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
      or specialized RSEs for dealing with user support. &
    Should have institutions that are able to offer support with outreach and publicising outputs.
    \\\hline
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    TEACH&
    May be independenly involved in training activites.&
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

In the table above, we've looked at how different competencies can be related
to and handled by researchers and RSEs working in different environments within
an organisation and how the organisations themselves can contribute.
We recognise that this is a challenging area to gain a detailed view of
and that our content in the table is still a significant generalisation.
We talk about the "Research Software Engineer" as a single entity but as the field expands,
we expect to see more roles and job titles emerging around the RSE concept,
many of which fit under the wider umbrella of Research Technology Professionals (RTPs).
The European Bioinformatics Institute (EMBL-EBI)'s BioExcel competency framework
[**[BIOEXCEL-FRAMEWORK]**](https://competency.ebi.ac.uk/framework/bioexcel/3.0/carreer-profiles)
provides some examples of different RSE-like computational roles.
Work by King's Digital Lab at King's College London also provides
some examples of a range of different roles within the research software
careers space [**[KDL-CAREERS](https://zenodo.org/record/2559235)**].

# RSE specializations
What we have defined above are intended to be base skills that an RSE irrespective of domain, place, and time should know about.
But not all RSEs are created equal, they specialize in different areas,
some of which we want to present below. Many of the specializations may overlap,
so the same RSE might for example work on data management and on Open Science.

## HPC-RSE
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

## ML-RSE
The development of research software based on machine learning (ML) requires specialized theoretical background and experienced handling of appropriate software in order to produce meaningful results.
This involves knowledge about data analysis and feature engineering, metrics that are involved in ML, ML algorithm selection and cross validation, and knowledge in mathematical optimization methods and statistics.
ML-RSEs analyse and check the suitability of an algorithm if it fulfils the needs of a certain task and they play a main role in deciding and selecting machine learning libraries for a given task.
The increasing usage of ML in numerous scientific areas with social impact, involves an emphasized awareness and consideration of possible manipulative or discriminatory influences.
At the intersection of data science [@SSIDataScience] and Data-focused RSEs, the complex way of solving problems utilizing machine learning calls for this separate specialization.

## Research Infrastructure RSE
This RSE is interested in SysOps and system administration and sets up IT infrastructures for and with researchers.
Therefore, this specialization on the one hand requires a deep knowledge of physical computer and network hardware and
on the other hand knowledge about setup and configuration of particular server software.
Those specialised RSEs know how to acquire, setup and maintain general-purpose as well as domain specific infrastructure,
e.g. setup of virtual machines on hypervisors or the planning and setup of compute server clusters for GPU based machine learning.
As an interface between the researchers and the infrastructure, they take care of user management, access permissions, and configuration of required services, for example.

## Web-Development RSE
This RSE is skilled in web applications, front- and/or backend, and/or building 
and using APIs, for example for research data portals or big research projects.
Ideally, this RSE should also have knowledge about (web) accessibility to allow a broad
range of researchers or even the public to use the resulting applications.
Therefore a deep knowledge of web skills is a required skill for this RSE.

## Legal-RSE
With the prevalence of software, we foresee the need for RSEs that specialize in legal questions around software.
They are the go-to person if people have a question about licensing, mixing and matching of software as well as patenting or copyright.
The publication of research software also requires knowledge about particular laws or regulatory frameworks concerning data protection, like the GDPR within the EU [@GDPR].
Familiarity with legal aspects of cybersecurity and export control in science and research (see [@ExportControl] for Germany) complete the competencies of those RSEs.

## Data-focused RSE
RSEs working at the flourishing intersection between data science and RSE. 
They are skilled in cleaning data and/or running data analyses and can help researchers
in setting up their analysis pipeline and/or research data management (RDM) solutions.
When the field requires research on sensitive data or information, e.g. patient information in medicine, 
this RSE should have knowledge about secure transfer methods and/or ways to anonymize the data.
As part of RDM, this RSE profile is able to support all stages of the research data lifecycle[@Nieva2020], with synchronous data management processes. 
Those processes implement established best practices for planning and documenting of data acquisition in a data management plan (DMP) as well as for management,
storage, and preservation of data, and publication and sharing of data in repositories according to the FAIR principles [@FAIR].

## OpenScience RSE
Open Science and FAIRness of Data and Software are increasingly important topics in research, as exemplified by the demand of an increasing amount of research funding agencies requiring openness.
Open Science RSEs can help researchers navigate the technical questions that come up 
when practicing Open Science, such as "How do I make my code presentable?", 
"What do I need to consider when it comes to licensing?", or 
"How can I use version control / automation for my project?".

## Project/Community manager RSEs
When research software projects become larger, they need someone who manages
processes and people. Building a community around a research project is an
important building block in building sustainable software [@Segal2009], so these RSEs play
an important role, even if they do not necessarily touch much of the code themselves.

## Teaching RSEs
RSEs who focus on teaching the next generation of researchers and/or RSEs play
a vital role in improving the quality research software.

## ${DOMAIN}-RSE
While software is the lingua franca of all RSEs there will be RSEs that have specialized in the initricacies of one particular research domain,
 such as medical RSEs, digital humanities RSEs or physics RSEs.

## Optional RSE competencies -> Maintenance RSEs
Oftentimes, a significant amount of effort in (research) software development needs to be spent on maintenance to ensure that software remains useful for researchers now and in the future.
The research environment is constantly changing and this can also apply to the software requirements.
If software is not properly maintained, it becomes increasingly difficult to install and use. 
At some point, the software is no longer available and cannot be used to reproduce results.
While ensuring maintenance and sustainability of research software is of huge importance to the communities that build and use it,
a particular challenge is that it is often very difficult to obtain ongoing research funding for software maintenance tasks.
As a result, when a project that developed or extended a piece of software finishes, support for the software fades as team members move on to other research,
academic or RSE roles, or become busy with other funded work.
While this is not a core concern of this paper, we wanted to highlight this important issue that is frequently faced when working with software in the research community.
With regard to which additional competency is required,
these are people having experience with ancient software stacks that are not anymore part of the general curricula (think of COBOL and FORTRAN).

FIXME: I think it would be nice if we could move each of these optional competencies to a different specialization.

# Reaching out to potential RSEs
Many current RSEs have found their way to being an RSE during their doctoral studies.
This transition usually happens slowly. You start programming a tool, and someone else likes it, it becomes known that you have programming skills and suddenly you are the RSE of the group that everyone would like to have in their projects.
If you enjoy this role, you need to be aware that there is a RSE career path as well as that specialized training materials exist.
Beyond that, for an RSE it is important to be a part of a network with other RSEs, irrespective of the career level.
A perfect first step for forming this network is topic-related conferences, workshops or meetups.
Beyond that, there is the broader RSE community organized at the local and regional level with chapters or local/regional communities, at the national level with societies and the international RSE society.
Each of them offers possibilities for connecting within or beyond an individual institution and is a great way to find like-minded people to grow a wider network and thereby facilitate the sharing of information on interesting events or help each other out.
This available layered network can greatly benefit the RSE in finding help with issues outside of their own comfort zone
and provides a welcoming, social safety net providing a home for the RSE. Since we feel providing aspiring RSEs this net
is of utmost importance we envision compulsory events introducing that to young RSEs.
Qualification badges are another venue, that RSEs to find people with the same technical interest.
Structuring and institutionalizing the education and structures for the add-on courses that are also open to others in academia,
will be topics of a follow-up paper.

# Appendix

## An applied example curriculum
## An example of a possible career path
- We can follow Kim, who has been the protagonist of the original deRSE Paper.

## HPC skills and certification

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

## Bioinformatics skills and certification

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
