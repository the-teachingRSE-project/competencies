---
title: "INSTITUTIONALIZED ORGANIZATION OF RSE EDUCATION"
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

## Organizational Infrastructures
So we have defined our set of competencies that we feel every RSE should possess.
Table 2 above nevertheless already hints at the fact that some RSE skills are required during the domain studies,
while Table 1 tells us that we also need an ongoing qualification programme for people that want to become specialized RSEs.
In order to set up a proper educational scheme we need to discuss two more items:

- Who are our teachers?
- How is this teaching organised?

### The teachers
#### What issues are trainers facing today?
There are already some people teaching RSE-related topics, sometimes within university structures, but often outside of formal structures.
Currently, they often teach in workshop-like formats at research institutions.
The community discussion shed light on the issues our trainers are faced with nowadays:
- There are outreach issues. We emphasize that there are two dimensions to this: First it is important that we inform students that workshops exist, and then, the more important part, we also need to motivate people to invest the time for a workshop. [@EuroCC2022]
- Adaptation of material to the target audience has been identified as a time-consuming task.
- Organization and preparation are a challenge, since currently no standardized formats exist.
- Expectation management of students. Existing knowledge of students is often diverse.
- Language barriers. This can range from the use of technical jargon up to the disparities of you teaching in a foreign language.
- Setting up a feedback loop that facilitates a reflection of the workshop for the teacher.
- Staying up-to-date with fast-moving RSE topics.
- Understanding the difficulties of students [@Cereceda2020; @Williams2019].
- Carpentries retrospective [@Wilson2016a].
- Lack of 'Train the Trainer' opportunities makes self-improvement difficult. 
- Get teaching effort attributed as upskilling that counts as a professional qualification.

#### What mindset makes up a good teacher
Irrespective of where people come from they need to have the proper mindset to properly foster RSEs-to-be.
The basis for our proposed mindset is the conviction that research software engineering (RSEing) is an important topic that supports good scientific practice and reproducible research as well as the motivation to share their experience and skills with prospective RSEs. 
In addition, we expect it is a fundamental part of a teacher's mindset to adopt a set of shared values, which we have detailed above in the [values](#values) section.
Good teachers engage with the different scientific backgrounds of the learners, regardless of their prior knowledge.
In order to identify relevant content and adapt content to the learners needs, they understand and appreciate the respective research environment.
We would presume good teachers to take responsibility in improving their own pedagogical skills to make their teaching more effective.
Since it is difficult to measure increased learning success and better RSEing applied by the learners, better methods for evaluation of a teacher’s effectiveness would be beneficial for teachers.
For example, a survey by The Carpentries [@Duckles2016] provides a detailed evaluation on the value and benefits of Software and Data Carpentry workshops to their instructors.
The expected mindset also encompasses that teachers should see setbacks and feedback as an opportunity to learn and grow their own skills.
A teacher's mindset should also include the acknowledgment that some learners acquire additional RSE skills out of necessity and not out of interest, meaning that not every "good" scientist wants to become a "good" software engineer, too.
Therefore, it is also inevitable that teachers have positive and high expectations of their students.
Inspired by the proverb "If you want to go fast, go alone; if you want to go far, go together?", teachers should actively engage with the RSE community and see the benefits of networking.
Finally, teachers should be motivated to follow up and offer continued support to their students after the training has ended.

#### Where do we get our teachers from
The community discussion brought to light the need for a mixture of people, therefore 
the education of aspiring RSEs will involve people from close domain sciences or experienced RSEs
and people that have respective additional skills to teach RSE competencies to the new generation.
In that respect, this follows The Carpentries model that offers certifications but is still open to non-certified trainers.
We highlight and emphasize that, since a topic like RSE education is constantly evolving, trainers strongly require the opportunity and the recognition to educate themselves.
Therefore our teachers will be sourced from the workplace but there will also be certified RSE Trainers.
(FIXME: in classical university speak, these would be people who have done their habilitation on that topic, right?)
Large online learning platforms such as edX [@edx] or Coursera [@coursera] serve as a resource of international teachers, who share their experiences in specific RSE-related topics in webinars. 
These platforms enable the targeted recruitment of academic teachers, including those from leading research institutions.

We propose to create common infrastructures that can be utilized in this ongoing effort to professionalize the RSE education further and to easily share education resources across the country.
For the ongoing development, from the status quo of available courses and material to generally accepted, unified curriculums, we suggest a centralized online RSE education platform.
Such a platform should allow to:
- collect and adapt available and new teaching material, like written lessons or pre-recorded courses
- review and evaluate uploaded teaching material
- compile curriculums from the available material
- create different variations of a curriculum to fit domain specific or institutional requirements
- align a curriculum with the requirements of academic credit systems, like the European Credit Transfer and Accumulation System (ECTS) [@ECTS]
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
Specific online learning platforms offer a wide range of RSE related, job-ready certified courses as well as complete degree programs.

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
support skills development. Now, in the final section, we want to discuss how the
RSE can become a natural part of the landscape of professions and which
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
Graduating from this PhD program, opens a future career path as a lead RSE in their domain to them.

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
researchers that want to deepen their HPC skills for research or to practitioners that require them for industrial applications.
Specializing the centres to certain skill sets enables them to effectively reach out into the sciences with their brand.
With the existence of these resources we believe that their acceptance gradually increases over time.
The tasks of these centres is facilitated by reusing the work of initiatives like edutrain [@EDUTRAIN] and platforms like DALIA [@DALIA].
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

*** EDUCATING RSEs in GERMANY - WHAT NEEDS TO BE DONE ***

## Required Next steps
### Implementation Strategies
- Ideally over time scientific software engineering becomes part of the curricula at universities.

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

However, it is worth highlighting that answering the need for more RSEs
can only be achieved by simultaneously having a clear training path,
but also by ensuring that existing and trained RSEs are retained in academia.
This paper focused on the first component: training RSEs, but we still believe
that a discussion on creating viable RSE career paths in academia is necessary.
This might be even more true for RSEs than traditional researchers as RSEs
may have more opportunities to perform similar activities in the commercial sector,
while benefitting from better salaries and working conditions.

RSEs are valuable members of research teams in academia,
but the lack of institutional support leads to high turnover
and difficulties attracting applicants with the right skill set.
Several institutions have recognized these challenges and are taking steps
to professionalize RSE profiles and make them more visible via dedicated
funding programs [@Godoy2022; @DFGResearchSoftwareCall2022;
@EdinburghRSECollaborationCall2023; @EdinburghRSEFellowshipCall2023]
or by establishing RSE departments.
For the sake of completeness, we also would like to mention challenges that relate to the topic covered but are out of scope and would be subject of separate more in-depth considerations.

As outlined in [@UniStgtRS], the lack of long-term funding options and centralized agencies complicate the sustainable development and delivery of research software. 
Where applicable, it is important to raise awareness of the need for institutional support.
The creation of a curriculum for the continuing education of RSEs must go hand in hand with the creation of new permanent positions for RSEs at research institutions.
For one thing, attractive working conditions are indispensable in order to employ RSE teachers, e.g. to attract qualified and experienced software engineers from the industry to the field of research software.
For another thing, they are also important to retain trained RSEs at research institutions. 

Training and building up experience in research software engineering also rely on the long-term availability of required (domain-specific) infrastructure for software development. 
If this prerequisite is not met in the first place, research institutions either have to enable RSEs to access infrastructure that already exists off-premise or they have to provide the required infrastructure on-premise.
Sustainable software development benefits greatly from services for developing, testing and validating software.
Specifically, the lack of hardware and personnel support for Continuous Integration (CI) and Continuous Delivery (CD) limits efficient and up to date software development.

## Appendix
### Sources for RSE-related training material

#### Books

+ "Producing Open Source Software" ([@Fogel2005; @Fogel2017]) describes a lot of aspects for running a free software project.

+ "Research Software Engineering with Python" ([@Irving2021]) targets
  Python programming novices and introduces a set of essential tools
  next to the programming language itself.

#### Course material

+ The Software Carpentries Lessons [@CarpentriesSoftware] provide extensive teaching material
for basic research software skills geared towards researchers.

+ The unofficial MIT course "The Missing Semester of Your CS Education" ([@Athalye2023])
covers a lot of basic computer skills typically taught by RSEs.

#### Train-the-trainers material

+ "Teaching Tech Together" is a book that derives from and extends the Carpentries Instructor Training [@Brown2023],
which is a continuously updated and extended online-resource.

+ The National Competence Center Sweden (ENCCS) [https://enccs.se/] provides instructor training material
[@ENCCSInstructorTraining], [@ENCCS2022] developed from Carpentries and CodeRefinery material, as well as lessons for
HPC-oriented RSEs [@ENCCSLessons].


#### Directories  of resources

+ Better Scientific Software (BSSW)(https://bssw.io/) (Collection of resources for computational science and engineering) w


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

