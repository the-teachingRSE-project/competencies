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

[CodeRefinery] is a project currently funded by the Nordic e-Infrastructure and thus active priliminarily in the Nordics with the goal of teaching essential tools around research software development, that are usally skipped in academic education. CodeRefinery hosts a set of open source training materials including both beginner and intermediate-level material and organizes multiple highly interactive large scale workshops per year. Skills learned from the workshops and/or material allows researchers to produce more reproducible, open and efficient software and thus promoting FAIR research practices. One goal of the project is to evolve into a community project that seamlessly integrates with other intitaives. 

The ReproHack Team offers resources to host events where students and researchers can get together to try and reproduce the results 
of published papers with the methods described there or ideally with the software provided by the authors.

The [Intersect] project ....

[Better Scientific Software (BSSW)] ...


 - Add other related training groups/activities...


## Challenges
- Point out gaps
- What is missing

## Results

### Required Generic RSE skills
In the workshop defined a set of core skills that we believe can stand the test of time.

**ADD YOUR COMPETENCIES HERE. SPECIALIZATIONS BELOW**
#### working in a team

#### Creating documented code building blocks

#### legal things

#### building libraries

#### Use repositories

#### Finding/discovering software and attribution
One goal of FAIR software is to avoid reimplementation of already working packages and thereby reducing the need for doubled work. 
To (re-) use software the individual researchers have to be able to find out if that software already exists.

After findind the software the researcher has to be able to evaluate if the software actually suits their needs.
Apart from the functionality, licensing, integration with other software and expandability have to be part of this evaluation.

Finally, after obtaining results by modifying and/or using the software, the original authors should get the proper attribution.
How this should be done is not immediately clear, especially when there is no accompanying software paper.

source code, research data, 
Ideas so far:
- building libraries, versioning, software discovery, social skills, communication, legal things

We will have to consider that the broad variety in the field of research software. Still, there is probably a set of skills that is relevant to all developers (versioning, code quality, documentation). This could be a Body of Knowledge (BoK). In addition, RSEs should be able to adapt to specific (domain) specific requirements/environments which requires additional competences (Body of Competences) like communication, networking, (life long) learning, ... (There is a paper from David Parnas on Body of Competences in software engineering)

Also, different software at different stages of evolution require different skills (CI, larger application architectures, ...)

If we think about competencies, we should point out which tasks the persons should be able to perform:
social skills vs. "The person is able to work in a team", "The person is able to lead a team", ...

Ideally we have a list of 7 time-invariant concepts/notions of what makes up an RSE.

|  teamwork 	| 	|  |  |   	|   	|   	|
|---	|---	|---	|---	|---	|---	|---	|
| create code |   	|   	|   	|   	|   	|   	|
| legal advice |   	|   	|   	|   	|   	|   	|
| Use repositories|   	|   	|   	|   	|   	|   	|
| Training |   	|   	|   	|   	|   	|   	|
|   	|   	|   	|   	|   	|   	|   	|
|   	|   	|   	|   	|   	|   	|   	|

### How much do different people need to know?
Explore the different dimensions that a person can require a different set of skills in.
Examples are The domain, organization, career path, ...

https://competency.ebi.ac.uk/framework/bioexcel/3.0/carreer-profiles
Remember the matrix structuring idea

### RSE specialization
Examples: HPC-RSE, Legal-RSE, RDM-RSE, OpenScience-RSE, $DOMAIN-RSE, ...
- further specialized RSE skills

### Optional RSE competencies
- Hardware Maintenance?
- Managing/Updating/Refurbishing legacy software
- developing (web)services, e.g. for surveys, esp. in digital humanities (accessibility of UIs gets important)

### How do we reach people in different stages at their career?
Many current RSEs have found their way to being an RSE during doctoral studies. This transition usually happens slowly. You start programming a tool, someone else likes it, it becomes known that  you can do those things and suddenly you are the programmer of the group everyone wants something from. If you enjoy those things, you will need to know that something like an RSE career exists as well as the training materials. One place to generate awareness of the career option and training is universities doctoral onboarding process, or right therafter. RSE training could be offered as elective courses. RSE presented as a career path in suitable events. Since many RSE-minded people also at some point find their way to an HPC cluster,, mailing lists of said clusters could be utiliuzed to advertise RSE courses. One important aspect to think about is also the wording in the advertisement. Potential future RSEs might not know the term yet or knwo that the course advertised includes topics that are of interest to them. If the university or organization has a git * organizatiobn/project, having a banner there might reach the right people. Most important is that people working in IT helpdesks know about the courses offered so that they can advise students /researchers on visiting the course/reviewing the materials if related questions are asked. 
- We have resources, now we need to connect them to people to improve science

### Organizational Infrastructures
- Defining who should be teachers and in which structures they are
- What mindset makes up a good teacher
- Do we need an organisation for teaching RSE skills?
- Certificates? Remember that they help to define what an RSE is and therefore help the career path definition.

- Ideally over time scientific software engineering becomes part of the curricula at universities 

## Required Next steps
### Implementation Strategies
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

[Better Scientific Software] BSSW [https://bssw.io/](https://bssw.io/) . Accessed 30th March 2023.

[Intersect] project [https://intersect-training.org/](https://intersect-training.org/). Accessed 30th March 2023.

[Hettrick2016] S. Hettrick. A not-so-brief history of Research Software Engineers. Software Susitainability Institute blog, August 2016. Available at [https://www.software.ac.uk/blog/2016-08-17-not-so-brief-history-research-software-engineers-0](https://www.software.ac.uk/blog/2016-08-17-not-so-brief-history-research-software-engineers-0). Accessed 16th March 2023.

[Cohen2021] J. Cohen, D. S. Katz, M. Barker, N. Chue Hong, R. Haines and C. Jay, "The Four Pillars of Research Software Engineering," in IEEE Software, vol. 38, no. 1, pp. 97-105, Jan-Feb. 2021, DOI: [https://doi.org/10.1109/MS.2020.2973362](https://doi.org/10.1109/MS.2020.2973362).

[Lamprecht2022] A-L. Lamprecht, C. Martinez-Ortiz, M. Barker, et al. What Do We (Not) Know About Research Software Engineering?. _Journal of Open Research Software_, 10(1), p.11. DOI: [https://doi.org/10.5334/jors.384](https://doi.org/10.5334/jors.384)

