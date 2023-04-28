# Teaching and Learning Research Software Engineering
## Working Title:  Identifying core competencies of an RSE and an application with a sample curriculum.

---

**Abstract**:
Being an outcome of a community workshop held in Paderborn, Germany in February 2023 this paper tries 
for the first time(? true?) to define which competencies are required to participate in modern digital sciences.
Some of these competencies are required in more depth, therefore, giving rise to the trade of the RSE, scientific personnel that specializes in writing research software that facilitates research in all stages of the research cycle.
Due to their generality, we explore these competencies in various contexts and elaborate on some examples for further specialization.

But knowing a set of competencies is not enough, therefore we discuss explicitly how to make people aware that these skills are
required and how these are taught(Do we want to add this pedagogical dimension?).
In order to also facilitate structural change in the German research institution landscape
we will discuss the organizations and structures that support this change and educate new RSEs.
The discussion in this paper is meant to be general therefore we will discuss specific applications in an appendix.

---

**Keywords**: research software engineering, training, learning

## Introduction
- background
    - RSEs have been around for a long time but the name is new.
    - RSEs have a specialist skill set that brings together technical and research knowledge.
    - Skills development traditionally provided largely through peer learning, self learning, introductory training courses not targeted specifically at RSEs, ...
    - Requirements for RSE skills growing rapidly across all domains.
- past attempts, other initiatives
- contributions

Computers and software have played a key role in the research lifecycle for many decades. Traditionally, they were specialist tools used only in a small number of fields and the Computer Scientists who maintained and programmed them needed extensive technical training over several years to gain the necessary skills and expertise. Fast forward 50-60 years and software and computation are all around us, underpinning our everyday lives. This shift is also true within research.

With the ability to capture and process ever more data, undertake larger scale, higher resolution simulations and, increasingly, to automate complex tasks through Artificial Intelligence and Machine Learning approaches, computers and software are now vital elements of the research process across almost all domains. However, this shift means that there is a much greater need for core research software skills across a vast array of research fields where these were not previously required.

The people who focus on writing research software are now known as Research Software Engineers (RSEs) - a term that was coined a little over 10 years ago [Hettrick2016].  RSEs may work within one of the many Research Software Engineering teams that have been set up at universities and research organisations over the last decade, or they may be embedded within a research team. They may have a job title that officially recognises them as an RSE, or they may have a standard research or technical job title such as Research Assistant, Research Fellow or Software Engineer. Regardless of their job title, RSEs share a set of core skills that are required to write software, understand the research environment and ensure that they produce sustainable, maintainable code that supports reproducible research outputs.

Developing and maintaining these skills is time consuming and often challenging. Part of the challenge is that there is not a standard pathway to becoming an RSE and, partly as a result of this, there is something of an ad hoc approach to training within the community. We also see increasing amounts of basic-level training materials that are great to put researchers or technical professionals on a path towards gaining significant RSE expertise, but the trail often ends as developing RSEs want to progress to intermediate and advanced level material. In particular, recent technology developments are ensuring that there is a growing need for specialist expertise, for example in areas such as making efficient use of high-performance computing infrastructure. This is an area where there is a skills shortage and a shortage of training materials.

In this paper, we look at the challenge of understanding the core competencies that underpin Research Software Engineering and the way that these competencies may be combined to help support a more coordinated approach to future RSE skills development. The paper builds on a workshop session held as part of the German Research Software Engineering Conference (deRSE23), held in Paderborn, Germany in February 2023.

_[Information on key contributions to add]_

_[Overview of paper sections to add]_

## Related Work and Activities

The challenges of understanding the current state of skills within the research software community and related areas, as well as identifying required competencies, developing training pathways and providing training materials are areas that are being looked at and addressed by various groups and projects. In this section, we highlight some of these other projects and activities.

### Identifying skills and pathways

As an area that generally requires a range of advanced skills, High Performance Computing (HPC) is one field where there is ongoing work to identify relevant sets of skills for HPC practitioners and potential paths to develop these skills. The HPC Certification Forum has developed a "competence standard" (CS) for HPC that defines a range of skills and how they are related in the context of a skill tree [HPC-CF Competencies]. Also looking at pathways and how different skills are related, the UNIVERSE-HPC project [UNIVERSE-HPC], funded under the UK's ExCALIBUR research programme [EXCALIBUR], is looking to understand and develop training pathways to support the development of specialist skills in the HPC and exascale domains. The project is gathering open source training materials to develop curricula that support the training pathways that are underpinned by high-quality training materials.

 - There are some projects / papers looking at skills pathways - if we're going to include a separate section on related work, as proposed here, this should probably be expanded to include more of this content?

### RSE-related Training Materials

A wide range of software-related training materials and supporting organisations exist within the research software community and beyond. The Carpentries [The Carpentries] is a non-profit entity that supports a range of open source training materials and international communities of volunteer instructors and helpers who run courses around these materials. The community also maintains the materials which are based around three core syllabuses - Software Carpentry, Data Carpentry and Library Carpentry. The training materials within these areas have been developed, reviewed and enhanced over several years ensuring that they represent best practice in training on these topics. The core Carpentries lessons are targeted primarily at the beginner-level. However, the Carpentries Incubator [Carpentries Incubator] provides an environment for hosting additional community developed training modules covering a wide range of other topics that haven't gone through the peer review process of the core lessons. The material in the Incubator increasingly includes more intermediate-level training modules.

CodeRefinery is another group who host a set of open source training material that they use in workshops primarily run in the Nordic region. CodeRefinery's material includes both beginner and intermediate-level material _[Samantha to expand description of CodeRefinery?]_

The ReproHack Team offers resources to host events where students and researchers can get together to try and reproduce the results 
of published papers with the methods described there or ideally with the software provided by the authors.

 - Add other related training groups/activities...


## Challenges
- Point out gaps
- What is missing

Depending on the specific domain there is a gap between the basic software carpentry courses and the required skills to build domain-specific research software. For example, scientists in the field of High-Performance Computing need to know how to use concurrency to speed up their simulation and communicate efficiently using message-passing interface (MPI) libraries. The same is true for researchers from other domains who make use of other specialized technologies, methods and/or tools. To bridge those gaps more specialized courses would be needed like the one mentioned in section [Identifying skills and pathway] for the HPC community.

Moreover, software development is a craft, i.e. it is not only about knowledge but also requires practical experience. Hence we need to create an environment that allows young researchers to practice and gain experiences efficiently. Ideally, this learning environment would allow those younger scientists to be guided by more experienced RSEs. We know such practices e.g. from human medicine, where young doctors first assist experienced doctors before they work independently. In the field of software development, this approach could be implemented, in the form of peer programming. The prerequisite for this, however, is that experienced academics get better career opportunities at German Universities so that they don't leave for the industry. 

## Results

### Required Generic RSE skills
As it stands the RSE role requires competencies in two fields.
The "R", the person being a researcher, and the "SE" the Software skills.
And this hybrid nature is brought about, since RSEs need to apply their knowledge usually in teams.
Therefore we structure our competencies among SE Skills, Research Skills and Team Skills.

We will have to consider the broad variety in the field of research software.
Still, there is probably a set of skills that is relevant to all developers (versioning, code quality, documentation).
This could be a Body of Knowledge (BoK).
In addition, RSEs should be able to adapt to specific (domain) specific requirements/environments which requires additional competences (Body of Competences) like communication, networking, (life long) learning, ...
(There is a paper from David Parnas/Landwehr on Body of Competences in software engineering)

Also, different software at different stages of evolution require different skills (CI, larger application architectures, ...)

**ADD YOUR COMPETENCIES HERE. SPECIALIZATIONS BELOW**


#### Software Engineering Skills
There are lots of software engineering curricula out there, that try to define which tasks a software engineer should be able to perfom.
A recent one highlighting some aspects in more detail than what we are doing here is (Landwehr2017).

#### Creating documented code building blocks (DOCBB)
The RSE should be able to create building blocks from source code that are reusable. This ranges from simple libraries of functions up to complex architectures consisting of multiple softwares.
An important part of the reusability is that at least oneself and ideally others are able to understand what the code aims to do and how to use the provided functionality, which is primarily achieved through a "clean" implementation and enhanced by documentation. This ranges from commenting code blocks to the usage of documentation (building) tools.

#### Building distributable libraries (LIBS)
The RSE should be able to distribute their code with their domain/language specific distribution platforms.
This almost always encompasses handling/documenting dependencies to other packages/libraries and sometimes 
requires knowledge of using build systems to enable interoperability with other systems.

#### Software Behaviour Awareness and Analysis(MOD)
A certain quality of analytical thinking that enables you to form a mental model of the piece of software under consideration in the current environment.
Using that an RSE should be able to make predictions about a software's behaviour. This is a required skill for tasks like debugging, profiling, designing good tests, or predicting user interaction.

#### Understanding the software lifecycle (SWLC)
Software has a lifetime and this necessitates the respective strategies for its usage along the intended time scale.

#### Use repositories (SWREPOS)
The RSE should be able to use public platforms to share the artifacts they have created and invite public scrutiny on them for public review.

#### Legal things (LEG)
The RSE should know licenses and their respective domains for data or software. On an entry level, the competency is mostly about awareness. 
Namely that different (open source) licenses exist, 
that those might not be combinable when using multiple libraries with different licenses 
and that use of third party software might restrict licensing of the resulting work. 

#### The research skills
#### Curiosity (NEW)
The RSE gains its reputation from its effectiveness to interact with their domain peers. Therefore some curiosity together with a broad overview of the research field is required.
A manifestation can also be the curiosity for new tools which is a great asset for an RSE.
Lifelong learning then becomes more bearable.

#### Understanding the research cycle (RC)
Knowing that ones own research is not only a means to personal ends, but that one is part of a bigger cycle that involves a lot of other parties in and outside of your domain
should foster an appreciation for the underlying principles of science like review and reproducibility.

#### Finding/discovering software and attribution (SD)
One goal of FAIR software is to avoid reimplementation of already working packages and thereby reducing the need for doubled work. 
To (re-) use software the individual researchers have to be able to find out if that software already exists.

After finding the software the researcher has to be able to evaluate if the software actually suits their needs.
Apart from the functionality, licensing, integration with other software and expandability have to be part of this evaluation.

Finally, after obtaining results by modifying and/or using the software, the original authors should get the proper attribution.
How this should be done is not immediately clear, especially when there is no accompanying software paper.

#### Use Domain repositories/directories (DOMREP)
Almost all Research software is developed within a specific scientific domain.
Some software may be able to cross boundaries, but the majority will have a home domain, with which it needs to be able to interact.
Especially for data-driven research having software that is able to use existing sets and repositories is a valuable part.
The RSE should be able to interact with the repositories of this specific domain.


#### Outside Party interaction (USERS)
While in a traditional SE context you might get away with not interacting with people outside your project.
But in a research context this will certainly be the case and involves users, other developers,  upto funders.
Additionally, this is oftentimes a two-way interaction with RSEs in a specific domain learning new findings, techniques, algorithms, 
etc. to be able to implement software that is up-to-date with the body of knowledge of that domain.

#### Team Skills
#### Teaching (TEACH)
Working in a group means being able to effectively perform e.g. onboarding, or more formal teaching procedures to their colleagues.
We deliberately mention, that giving code review is also part of teaching.
Code review can be part of teaching people on improving their skills.

#### Project Management (PM)
The RSE should have knowledge about project management.


#### working in a team (TEAM)
There are various facets to working in a team. They range from functioning in a team to leading a team.
It includes following measures that increase team cohesion like performing code reviews.

### How much do different people need to know?
Now that we have the different competencies, we can explore various dimensions of these competencies,
depending on their circumstances. A strong beneficiary of specialized RSEs can also be newly formed RSE centers at research institutions.

#### Career level
At different career levels differing skills are required. We have set this up according to the following separation often applied within a single project:

- Junior RSE: These are persons that have just started, but generally speaking they should have the skills to contribute to software projects
- Senior RSE: They have gained experienced and can set the examples in the software project.
- Principal RSE: Their actual job description varies a lot. These can be professors or group leaders and are often people bringing in the money that sustains the project. Generally speaking, they do not need to know the day-to-day tasks but should know the direction that is required for their project.

The required skills are distributed according to this table
First Dimension: Career path e.g. Junior RSE -> Senior RSE -> PI scale (1->6) (less -> lot)

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
| TEACH | should be able to perform simple peer-to-peer onboarding tasks | should be able to explain logical components to other RSEs | Should be able to effectively communicate about al large-scale parts of the project. |
| PM    | Awareness about the employed project managemement method | Should be able to use the employed PM method | Should be able to design and adapt the employed PM method. |
| TEAM  | Should be able to work in the team in order to effectively fulfill the given tasks. Should be able to learn from code review. | Should be able to break down tasks into more easily digestable sub-tasks | Should be able to lead the team and set the respective direction. |

#### Academic Progression (Help me for better title)
Modern digital science requires some digital proficiency at every level.
To be a bit more precise, these are how we define the academic levels:

- Bachelor: These are people in their undergrad studies, that mostly consume science/knowledge. They should also learn about the existence of certain digital structures.
- Master: At the end their study should have brought them to a level, where they can participate in science, hence they should be able to use "some" digital structures.
- PhD: Under guidance they perform independent research and hence they should get to know all relevant structures.
- PostDoc: Independent researchers, they are proficient users of all tools.
- PI/Professor: Experts in their field, they should be able to give proper guidance to their students which digital tools are currenty relevant.

FIXME: Highlight that a lot of items are not yet part of the structures of research institutions or workgroups.

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


#### Project team Size
Some explanation of the team sizes:

- individual: A single person working on their research software
- Small team(~4 persons) This is a small team, that has decided to work together on something
- Organizations( >10 persons): These are big organizations with clear structures and a bigger degree of specialization.

|       | individual | small team | organization  |
| ----  | ------ | ------ | --- |
| DOCBB |   you might get away with less satisfactory code, as long as the product is OK | think about your colleagues    | your organization most likely has guides here |
| LIBS  |   you will only be successful if your artifact is usable by others    |  same here   | your organization probably has rules here |
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

Bonus points may be distributed if managing teams remotely

https://competency.ebi.ac.uk/framework/bioexcel/3.0/carreer-profiles

### RSE specializations
What we have defined above are intended to be base skills that an RSE irrespective of domain, place, and time should know about.
But not all RSEs are created equal, they specialize in different areas,
some of which we want to present below. Many of the specializations may overlap,
so the same RSE might for example work on data management and on Open Science.

#### HPC-RSE
This RSE manages research infrastructure for high performance comuting (HPC), 
knows how to run complex computations, and/or helps researchers compute on the 
cluster. They have knowledge about (automatic) code optimization and building code 
that is able to leverage as many (efficiency) features the target hardware for the 
simulation offers as possible. This is not only about researchers obtaining their 
results in a reasonable time or even at all but also about the environmental impact 
of these simulation.

#### Research Infrastructure RSE
This RSE is interested in SysOps and sets up infrastructure for and with researchers.
This RSE therefore requires a deep knowledge of physical computer and network hardware.
FIXME: While required, is this an RSE? this sets of the usual infrastructure vs. research disussion....

#### Web-Development RSE
This RSE is skilled in web applications, front- and/or backend, and/or building 
and using APIs, for example for research data portals or big research projects.
Ideally this RSE should also have knowledge about (web) accessibility to allow a broad
range of researchers or even the public to use the resulting applications.
Therefore a deep knowledge of web skills is a requierd skill for this RSE.

#### Legal-RSE
With the prevalence of software we foresee the need to RSEs that specialize in legal questions around software.
They are the go-to person if people have a question on licensing, mixing and matching software, and/or patenting.

#### Data-focused RSE
RSEs working at the flourishing intersection between data science and RSE. 
They are skilled in cleaning data and/or running data analyses and can help researchers
in setting up their analysis pipeline and/or research data management (RDM) solutions.
When the field requires research on sensitive data or information, e.g. patient information in medicine, 
this RSE should have knowledge about secure transfer methods and/or ways to anonymize the data. 

#### OpenScience RSE
Open Science and FAIRness of Data and Software are increasinly important topics
in reasearch, as examplified by the demand of an increasing amount of research funding agencies requiring openness.
Open Science RSEs can help researcher navigate the technical questions that come up 
when practicing Open Science, such as "How do I make my code presentable?", 
"What do I need to consider when it comes to licensing?", or 
"How can I use version control / automation for my project?".

#### Project/Community manager RSEs
When research software projects become larger, they need someone who manages
processes and people. Building a community around a research project is an
important building block in building sustainable software, so these RSEs play
an important role, even if they do not neccessarily touch much of the code themselves.

#### Teaching RSEs
RSEs who focus on teaching the next generation of researchers and/or RSEs play
a vital role in quality research software.

#### ${DOMAIN}-RSE
While software is the lingua franca of all RSEs there will be RSEs that have specialized into the initricacies of one particular research domain, such as medical RSEs, digital humanities RSEs or physics RSEs.

### Optional RSE competencies
FIXME: I think it would be nice if we could move each of these optional competencies to a different specialization.
- Managing/Updating/Refurbishing legacy software

### How do we reach people in different stages at their career?
- We have resources, now we need to connect them to people to improve science

### Organizational Infrastructures
So we have defined our set of competencies that we feel every RSE should possess.
Table 2 from above nevertheless already hints at the fact that some RSE skills are required during the domain studies, while Table 1 tells us that we also need an ongoing qualification programm for people that want to become specialized RSEs.

Some basic education might be covered by the domain curricula or the libraries/compute centers.
but we need to provide them guidance to have a proper foundation 
on which to build the specialized courses that are performed by specialized teachers from specialized structures.

#### What issues are trainers facing?
The community discussion shed some light on the current issues our trainers are facing, which are currently teaching workshop like formats in research institutions.

- There are outreach issues. We emphasize that there are two dimensions to this: First we need to inform students that workshops exist, but also the more important part, we also need to motivate people to invest the time for a workshop.
- Adaptation to the audience has been identified as a time consuming task.
- Organization and Preparation is a challenge, since currently no standardized formats exist.
- Expectation management of students.
- Language barriers. This can range from the use of technical jargon up to the disparities of you teaching in a foreign language.
- Setting up a feedback loop. You want to improve from your workshop experinces
- staying up-to-date


#### What mindset makes up a good teacher
Irrespective of where people come from they need to have the proper mindset to properly foster aspiring RSEs.

#### Where do we get our teachers from and in which structures are they
The community discussion brought about the need for a mixture of people, thereby 
the education of aspiring RSEs will involve people from close domain sciences or  experienced RSEs
and people that have respective additional skills to teach RSE competencies to the new generation.
In that respect this follows the carpentries model that offers certifications, but is still open to non-certified trainers.
We highlight and emphasize, that since a topic like RSE education, is constantly evolving, trainers strongly require the opportunity to and the recognition to educate themselves.
Therefore our teachers will be sourced from the workplace but their will also be certified RSE Trainers.
(FIXME: in classical university speak, these would be people who have done their habilitation on that topic, right?)

We propose to create common Infrastructures that can be utilized in this ongoing effort to professionalize 
the RSE education further, to easily share education resources across the country.
(DETAIL ME FURTHER!!!!)

#### Certificates
With the ever-growing demand for RSEs in science it is helpful for the job-market that people can earn the respective certificates.
Certainly a big demand for specialized RSEs will come from the newly established RSE centers at research institutions that require skilled people to fill their vacant positions.
Then this demand can find its market with people offering this skill
Having these certificates provides finally a clear understanding of which tasks an RSE can perform and thereby helps defining the career path and the job description.

## Required Next steps
### Implementation Strategies
- Ideally over time scientific software engineering becomes part of the curricula at universities 
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
?

## Appendix
### An applied example curriculum

### An example of a possible career path
- We can follow Kim, who has been the protagonist of the original deRSE Paper.


## References

[HPC-CF Competencies] The HPC Certification Forum, Competencies. [https://www.hpc-certification.org/cs/](https://www.hpc-certification.org/cs/). Accessed 16th March 2023.

[UNIVERSE-HPC] UNIVERSE-HPC: Understanding and Nurturing an Integrated Vision for Education in RSE and HPC. [https://www.universe-hpc.ac.uk](https://www.universe-hpc.ac.uk). Accessed 16th March 2023.   _(new URL not yet active, currently at https://universe-hpc.github.io/)_

[EXCALIBUR] ExCALIBUR - Exascale Computing ALgorithms & Infrastructures Benefiting UK Research. [https://excalibur.ac.uk/](https://excalibur.ac.uk/). Accessed 17th March 2023.

[The Carpentries] The Carpentries. [https://carpentries.org/](https://carpentries.org/). Accessed 16th March 2023.

[Carpentries Incubator] The Carpentries Incubator. [https://carpentries-incubator.org/](https://carpentries-incubator.org/). Accessed 16th March 2023.

[CodeRefinery] CodeRefinery. [https://coderefinery.org/](https://coderefinery.org/).  Accessed 16th March 2023.

[Hettrick2016] S. Hettrick. A not-so-brief history of Research Software Engineers. Software Susitainability Institute blog, August 2016. Available at [https://www.software.ac.uk/blog/2016-08-17-not-so-brief-history-research-software-engineers-0](https://www.software.ac.uk/blog/2016-08-17-not-so-brief-history-research-software-engineers-0). Accessed 16th March 2023.

[Cohen2021] J. Cohen, D. S. Katz, M. Barker, N. Chue Hong, R. Haines and C. Jay, "The Four Pillars of Research Software Engineering," in IEEE Software, vol. 38, no. 1, pp. 97-105, Jan-Feb. 2021, DOI: [https://doi.org/10.1109/MS.2020.2973362](https://doi.org/10.1109/MS.2020.2973362).

[Lamprecht2022] A-L. Lamprecht, C. Martinez-Ortiz, M. Barker, et al. What Do We (Not) Know About Research Software Engineering?. _Journal of Open Research Software_, 10(1), p.11. DOI: [https://doi.org/10.5334/jors.384](https://doi.org/10.5334/jors.384)

[Landwehr2017] Carl Landwehr, Jochen Ludewig, Robert Meersman, David Lorge Parnas, Peretz Shoval, Yair Wand, David Weiss, Elaine Weyuker, Software Systems Engineering programmes a capability approach, [https://doi.org/10.1016/j.jss.2016.12.016](https://doi.org/10.1016/j.jss.2016.12.016)
