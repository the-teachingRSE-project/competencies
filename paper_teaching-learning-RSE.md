# Teaching and Learning Research Software Engineering
## Working Title:  Identifying core competencies of an RSE and an application with a sample curriculum.

---

**Abstract**:  
In this paper we provide a survey(?) about the experiences that people had in teaching RSE skills,
and from these experiences we derive a set of core competencies that people working in RSE should have
and we try to answer the question how deeply people should know something about the respective topics
in different carreer stages, organizations, etc...
We close with a domain specific sample curriculum.

---

**Keywords**: research software engineering, training, learning

## Introduction
- background
    - RSEs have been around for a long time but the name is new.
    - RSEs have a specialist skill set that bring together technical and research knowledge.
    - Skills development traditionally provided largely through peer learning, self learning, introductory training courses not targeted specifically at RSEs, ...
    - Requirements for RSE skills growing rapidly across all domains.
- past attempts, other initiatives
- contributions

Computers and software have played a key role in the research lifecycle for many decades. Traditionally, they were specialist tools used only in a small number of fields and the Computer Scientists who maintained and programmed them needed extensive technical training over several years to gain the necessary skills and expertise. Fast forward 50-60 years and software and computation are all around us, underpinning our everyday lives. This shift is also true within research.

With the ability to capture and process ever more data, undertake larger scale, higher resolution simulations and, increasingly, to automate complex tasks through Artifical Intelligence and Machine Learning approaches, computers and software are now vital elements of the research process across almost all domains. However, this shift means that there is a much greater need for core research software skills across a vast array of research fields where these were not previously required.

The people who focus on writing research software are now known as Research Software Engineers (RSEs) - a term that was coined a little over 10 years ago [Hettrick2016].  RSEs may work within one of the many Research Software Engineering teams that have been setup at universities and research organisations over the last decade, or they may be embedded within a research team. They may have a job title that officially recognises them as an RSE, or they may have a standard research or technical job title such as Research Assistant, Research Fellow or Software Engineer. Regardless of their job title, RSEs share a set of core skills that are required to write software, understand the research environment and ensure that they produce sustainable, maintainable code that supports reproducible research outputs.

Developing and maintaining these skills is time consuming and often challenging. Part of the challenge is that there is not a standard pathway to becoming an RSE and, partly as a result of this, there is something of an ad hoc approach to training within the community. We also see increasing amounts of basic-level training materials that are great to put researchers or technical professionals on a path towards gaining signifciant RSE expertise, but the trail often ends as developing RSEs want to progress to intermediate and advanced level material. In particular, recent technology developments are ensuring that there is a growing need for specialist expertise, for example in areas such as making efficient use of high-performance computing infrastructure. This is an area where there is a skills shortage and a shortage of training materials.

In this paper, we look at the challenge of understanding the core competencies that underpin Research Software Engineering and the way that these competencies may be combined to help support a more coordinated approach to future RSE skills development. The paper builds on a workshop session held as part of the German Research Software Engineering Conference (deRSE23), held in Paderborn, Germany in February 2023.

_[Information on key contributions to add]_

_[Overview of paper sections to add]_

## Related Work and Activities

The challenges of understanding the current state of skills within the research software community and related areas, as well as identifying required competencies, developing training pathways and providing training materials are areas that are being looked at and addressed by various groups and projects. In this section we highlight some of these other projects and activities.

### Identifying skills and pathways

As an area that generally requires a range of advanced skills, High Performance Computing (HPC) is one field where there is ongoing work to identify relevant sets of skills for HPC practitioners and potential paths to develop these skills. The HPC Certification Forum has developed a "competence standard" (CS) for HPC that defines a range of skills and how they are related in the context of a skill tree [HPC-CF Competencies]. Also looking at pathways and how different skills are related, the UNIVERSE-HPC project [UNIVERSE-HPC], funded under the UK's ExCALIBUR research programme [EXCALIBUR], is looking to understand and develop training pathways to support the development of specialist skills in the HPC and exascale domains. The project is gathering open source training materials to develop curricula that support the training pathways that are underpinned by high-quality training materials.

 - There are some projects / papers looking at skills pathways - if we're going to include a separate section on related work, as proposed here, this should probably be expanded to include more of this content?

### RSE-related Training Materials

A wide range of software-related training materials and supporting organisations exist within the research software community and beyond. The Carpentries [The Carpentries] is a non-profit entity that supports a range of open source training materials and international communities of volunteer instructors and helpers who run courses around these materials. The community also maintains the materials which are based around three core syllabuses - Software Carpentry, Data Carpentry and Library Carpentry. The training materials within these areas have been developed, reviewed and enhanced over several years ensuring that they represent best practice in training on these topics. The core Carpentries lessons are targeted primarily at the beginner-level. However, the Carpentries Incubator [Carpentries Incubator] provides an environment for hosting additional community developed training modules covering a wide range of other topics that haven't gone through the peer review process of the core lessons. The material in the Incubator increasingly includes more intermediate-level training modules.

CodeRefinery is another group who host a set of open source training material that they use in workshops primarily run in the Nordic region. CodeRefinery's material includes both beginner and intermediate-level material _[Samantha to expand descriptio of CodeRefinery?]_

The ReproHack Team offers resources to host events where students and researchers can get together to try and reproduce the results 
of published papers with the methods described there or ideally with the software provided by the authors.

 - Add other related training groups/activities...


## Challenges
- Point out gaps
- What is missing

## Results

### Required Generic RSE skills
As it stands the RSE role requires competencies in two fields.
The "R", the person being a researcher, and the "SE" the Software skills.
And this hybrid nature is brought about, since RSEs need to apply their knowledge usually in teams.
Therefore we structure our competencies among SE Skills, Research Skills and Team Skills.

We will have to consider that the broad variety in the field of research software.
Still, there is probably a set of skills that is relevant to all developers (versioning, code quality, documentation).
This could be a Body of Knowledge (BoK).
In addition, RSEs should be able to adapt to specific (domain) specific requirements/environments which requires additional competences (Body of Competences) like communication, networking, (life long) learning, ...
(There is a paper from David Parnas on Body of Competences in software engineering)

Also, different software at different stages of evolution require different skills (CI, larger application architectures, ...)

**ADD YOUR COMPETENCIES HERE. SPECIALIZATIONS BELOW**
unclassified: Being able to form a model about a piece of code

#### Software Engineering Skills
There are lots of software engineering curricula out there, that try to define which tasks a software engineer should be able to perfom.
A recent one highlighting some aspects in more detail than what we are doing here is (Landwehr2017).

#### Creating documented code building blocks (DOCBB)
The RSE should be able to create building blocks from source code that are reusable.

#### building distributable libraries (LIBS)
The RSE should be able to distribute their code with their domain/language specific distribution platforms.

#### Software Behaviour Awareness and Analysis(MOD)
A certain quality of anlytical thinking that enables you to form a mental model of the piece of software under consideration in the current environment.
Using that an RSE should be able to make predictions about a software's behaviour. This is a required skill for tasks like debugging, profiling, or predicting user interaction.
#### Understanding the software lifecycle (SWLC)
Software has a lifetime and this necessitates the respective strategies for its usage along the intended time scale.

#### Use repositories (SWREPOS)
The RSE should be able to use public platforms to share the artifacts they have created and invitit public scrutiny on them for public review.

#### legal things (LEG)
The RSE should know licenses and their respective domains for data or software. On an entry level, the competency is mostly about awareness. 
Namely that different (open source) licenses exist, 
that those might not be combinable when using multiple libraries with different licenses 
and that use of third party software might restrict licensing of the resulting work. 

#### The research skills
#### Curiosity (NEW)
The RSE gains its reputation from its effectiveness to interact with their domain peers. Therefore some curiosity together with a broad overview of the research field is required.
A manifestation can also be the curiosity for new tools and is a great asset for an RSE. Lifelong learning then becomes more bearable.

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
The RSE should be able to interact with the repositories of this specific domain.

#### Outside Party interaction (USERS)
While in a traditional SE context you might get away with not interacting with people outside your project.
But in a research context this will certainly be the case and involves users, other developers,  upto funders.

#### Team Skills
#### Teaching (TEACH)
Working in a group means being able to effectively perform e.g. onboarding, or more formal teaching procedures to their colleagues
#### Project Management (PM)
The RSE should have knowledge about project management
#### working in a team (TEAM)
If we think about competencies, we should point out which tasks the persons should be able to perform:
social skills vs. "The person is able to work in a team", "The person is able to lead a team", ...

Ideally we have a list of 7 time-invariant concepts/notions of what makes up an RSE.

### How much do different people need to know?
Explore the different dimensions that a person can require a different set of skills in.
Examples are The domain, organization, career path, ...

#### Career level
At different career levels differing skills are required. We have set this up according to the following separation:

- Junior RSE:
- Senior RSE:
- Software Lead RSE: Their actual job description varies a lot. These can be professors or group leaders and are often people bringing in the money that sustains the project.

The required skills are distributed according to this table
First Dimension: Career path e.g. Junior RSE -> Senior RSE -> PI scale (1->6) (less -> lot)

|       | Junior | Senior | Software Lead(brings in funding)  |
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
| TEAM  | Should be able to work in the team in order to effectively fulfill the given tasks | Should be able to break down tasks into more easily digestable sub-tasks | Should be able to lead the team and set the respective direction. |

#### Academic Progression (Help me for better title)
Modern digital science requires some digital proficiency at every level.
We detail what is relevant here.
A related one(non-specialized RSEs) The distinction is that numbers smaller then 4 indicate non-expert level:


|       | Bachelor | Master | PhD | PostDoc | PI/Professor | 
| ----  | ------ | ------ | ---   | ------  | ---|
| DOCBB | 1      | 1      | 2     |  2      | 2  |
| LIBS  | 2      | 3      | 3     |  3      | 2  |
| MOD   | 1      | 2      | 3     |  3      | 2  |
| SWLC  | 1      | 2      | 3     |  3      | 4  |
|SWREPOS| 1      | 1      | 2     |  2      | 3  |
| LEG   | 1      | 1      | 1     |  2      | 3  |
| NEW   | 1      | 1      | 3     |  3      | 3  |
| RC    | 1      | 2      | 3     |  5      | 6  |
| SD    | 1      | 1      | 2     |  2      | 2  |
| DOMREP| 1      | 1      | 2     |  3      | 3  |
| USERS | 1      | 1      | 2     |  3      | 5  |
| TEACH | 1      | 2      | 3     |  3      | 6  |
| PM    | 1      | 1      | 1     |  2      | 3  |
| TEAM  | 1      | 2      | 2     |  2      | 2  |


#### Organization Size
Second Dimension: individual -> small team of individuals(~4) -> big organisation(>10) scale (1->6) (less -> lot)

|       | single | small team | organization  |
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
Which brings us to the follow-up topic of specializations

#### HPC-RSE
These are people skilled in the use of a profiler and knowledgeable about the intricacies of hardware.

#### Legal-RSE
With the prevalence of software we foresee the need to have people that are specialized in this field.
They are the go-to persons if people in a department have a question on mixing and matching software.

#### RDM-RSE
These are people working at the flourishing intersection between RDM and RSE. In order to effectively design automated workflows
around RDM solutions that are useful to researchers we foresee the need for people that know both worlds.

#### OpenScience RSE
With so much going on around the buzzwords of Open Science and FAIRness of Data and Software which is wanted by research funding agencies,
we foresee the need for RSEs that are less technical but have the social skills to transform research grous/organizations.

#### ${DOMAIN}-RSE
While software is the lingua franca of all RSEs there will be RSEs that have specialized into the initricacies of one particular domain.

### Optional RSE competencies
- Hardware Maintenance?
- Managing/Updating/Refurbishing legacy software
- developing (web)services, e.g. for surveys, esp. in digital humanities (accessibility of UIs gets important)

### How do we reach people in different stages at their career?
- We have resources, now we need to connect them to people to improve science

### Organizational Infrastructures
So we have defined our set of competencies that we feel every RSE should possess. Table 2 from above nevertheless already hints at the fact 
that some RSE skills are required during the domain studies, while Table 1 tells us that we need an ongoing qualification programm.
Some basic education might be covered by the domain curricula or the libraries/compute centers but we need to provide them guidance to have a proper foundation 
on which to build the specialized courses that are performed by specialized teachers from specialized structures.

#### Where do we get our teachers from and in which structures are they
These will be a mixture of experienced RSEs and people specialized in teaching RSE things. There will be shared structures
(DETAIL ME!!!!)

#### What mindset makes up a good teacher
Irrespective of where people come from they need to have the proper mindset to properly foster aspiring RSEs.

#### Certificates
With the ever-growing demand for RSEs in science it is helpful for the job-market that people can earn the respective certificates.
Then this demand can find its market with people offering this skill.
Having these certificates provides finally a clear understanding of which tasks an RSE can perform and thereby helps defining the career path.

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
