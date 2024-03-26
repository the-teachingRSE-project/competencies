---
title: "Institutionalised Organisation of RSE Education"
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
  - curriculum design
  - education policy
  - lifelong learning
  - digital competence
  - open educational resources
abstract: "
Previous publications have defined the core competencies of an RSE and surveyed
the state of existing RSE-related resources.
In this paper we detail how to structure the education of RSEs in existing
structures and which additional structures are required.
"
---

# Organisational Infrastructures
So we have defined our set of competencies that we feel every RSE should possess.
Table 2 above nevertheless already hints at the fact that some RSE skills are required during the domain studies,
while Table 1 tells us that we also need an ongoing qualification programme for people that want to become specialised RSEs.
In order to set up a proper educational scheme we need to discuss two more items:

- Who are our teachers?
- How is this teaching organised?

## The teachers
### What issues are trainers facing today?
There are already some people teaching RSE-related topics, sometimes within university structures, but often outside of formal structures.
Currently, they often teach in workshop-like formats at research institutions.
The community discussion shed light on the issues our trainers are faced with nowadays:

- There are outreach issues. We emphasise that there are two dimensions to this: First it is important that we inform students that workshops exist, and then, the more important part, we also need to motivate people to invest the time for a workshop. [@EuroCC2022]
- Adaptation of material to the target audience has been identified as a time-consuming task.
- Findability of existing open educational resources.
- Organisation and preparation are a challenge, since currently no standardised formats exist.
- Expectation management of students. Existing knowledge of students is often diverse.
- Language barriers. This can range from the use of technical jargon up to the disparities of you teaching in a foreign language.
- Setting up a feedback loop that facilitates a reflection of the workshop for the teacher.
- Staying up-to-date with fast-moving RSE topics.
- Understanding the difficulties of students [@Cereceda2020; @Williams2019].
- Carpentries retrospective [@Wilson2016a].
- Lack of 'Train the Trainer' opportunities makes self-improvement difficult.
- Get teaching effort attributed as further qualification that counts as a professional qualification.

### What mindset makes up a good teacher
Irrespective of where people come from they need to have the proper mindset to properly foster RSEs-to-be.
The basis for our proposed mindset is the conviction that research software engineering (RSEing) is an important topic that supports good scientific practice and reproducible research as well as the motivation to share their experience and skills with prospective RSEs.
In addition, we expect it is a fundamental part of a teacher's mindset to adopt a set of shared values, which we have detailed above in the [values](#values) section.
Good teachers engage with the different scientific backgrounds of the learners, regardless of their prior knowledge.
In order to identify relevant content and adapt content to the learners needs, they understand and appreciate the respective research environment.
We would presume good teachers to take responsibility in improving their own pedagogical skills to make their teaching more effective.
Since it is difficult to measure increased learning success and better RSEing applied by the learners, better methods for evaluation of a teacher’s effectiveness would be beneficial for teachers.
For example, a survey by The Carpentries [@Duckles2016] provides a detailed evaluation on the value and benefits of Software and Data Carpentry workshops to their instructors.
The expected mindset also encompasses that teachers should see setbacks and feedback as an opportunity to learn and grow their own skills.
A teacher's mindset should also include the acknowledgement that some learners acquire additional RSE skills out of necessity and not out of interest, meaning that not every "good" scientist wants to become a "good" software engineer, too.
Therefore, it is also inevitable that teachers have positive and high expectations of their students.
Inspired by the proverb "If you want to go fast, go alone; if you want to go far, go together?", teachers should actively engage with the RSE community and see the benefits of networking.
Finally, teachers should be motivated to follow up and offer continued support to their students after the training has ended.

### Where do we get our teachers from
The community discussion brought to light the need for a mixture of people, therefore
the education of aspiring RSEs will involve people from close domain sciences or experienced RSEs
and people that have respective additional skills to teach RSE competencies to the new generation.
In that respect, this follows The Carpentries model that offers certifications but is still open to non-certified trainers.
We highlight and emphasise that, since a topic like RSE education is constantly evolving, trainers strongly require the opportunity and the recognition to educate themselves.
Therefore our teachers will be sourced from the workplace but there will also be certified RSE Trainers.
(FIXME: in classical university speak, these would be people who have done their habilitation on that topic, right?)
Large online learning platforms such as edX [@edX] or Coursera [@coursera] serve as a resource of international teachers, who share their experiences in specific RSE-related topics in webinars.
These platforms enable the targeted recruitment of academic teachers, including those from leading research institutions.

We propose to create common infrastructures that can be utilised in this ongoing effort to professionalise the RSE education further and to easily share education resources across the country.
For the ongoing development, from the status quo of available courses and material to generally accepted, unified curricula, we suggest a centralised online RSE education platform.
Such a platform should allow to:
- collect and adapt available and new teaching material, like written lessons or pre-recorded courses
- review and evaluate uploaded teaching material
- compile curricula from the available material
- create different variations of a curriculum to fit domain specific or institutional requirements
- align a curriculum with the requirements of academic credit systems, like the European Credit Transfer and Accumulation System (ECTS) [@ECTS]
(FIXME: DETAIL ME FURTHER!!!!)

## Organisation of teaching

### Certificates

With the ever-growing demand for RSEs in science it could be helpful for
people to earn certificates for skills needed in certain RSE positions.
This would possibly make hiring easier and could create an incentive for researchers
to go through proper courses on these skills instead of learning on the go.
For certain skills it would also be good for finding jobs outside academia,
e.g. in industry where certain practices are already state-of-the-art.
However, these certificates are only helpful if there is a certain level of
standardisation, which would require a central authority or collaboration
between multiple stakeholders to decide on contents and allow participating
institutions to issue these certificates.
Additionally, it can be excluding capable applicants who already use these
skills but never got a certificate for it.


The possible types of certificates can of course differ.
Specific online learning platforms offer a wide range of RSE related, job-ready certified courses as well as complete degree programs.

The [HPC skills and certification] Appendix explores current efforts at creating
a HPC certification program for both academic and industry RSEs.
The [Digital competencies and certification] Appendix explores the European
"DigComp" framework [@Vuorikari2016] and a pilot study for the
European Digital Skills Certificate.
Course attendance sheets and digital tokens
[@Ifenthaler2016; @Chakroun2018; @Fanfarelli2015; @McDaniel2016]
are another option (see Appendix: [Micro-accreditation]).

Having certificates provides finally a clear understanding of which tasks an RSE can perform and thereby helps defining the career path and the job description.
A big demand for specialised RSEs will certainly come from the newly established RSE centres at research institutions that require skilled people to fill their vacant positions.
And using the certificates, the demand can now be satisfied with people offering this skill.
Some exemplary skills for which courses are already held are version control tools like git, HPC topics like multithreading, MPI and GPU computations, FAIR principles.

# Required Next Steps
We have identified the RSE as an individual who brings a unique set of skills for
supporting and undertaking modern software-enabled research into research groups and teams.
We have elaborated on the basic competencies that RSEs may have, and we have
provided a detailed picture of how these competencies manifest along different
dimensions.
We have discussed who can deliver the necessary skills and the approaches to
support skills development. Now, in the final section, we want to discuss how the
RSE can become a natural part of the landscape of professions and which
steps we need to take to professionalise their education.

We foresee that the development of RSE skills will rest on two pillars:
A first qualification phase, possibly through academic structures, giving newcomers
to the field highly sought after professional skills, either directly from high school,
or as a result of a career change. But since the type of work undertaken by RSEs is
highly dynamic and often relies on knowledge about latest technologies, things change
quickly and an ongoing learning phase is also necessary to remain up-to-date with the
current developments, tools and techniques.
In this context, we put forward the idea of having institutionalised structures that
facilitate continuous learning. These structures may be integrated within an academic
environment but they may also exist fully or partially outside of the academic sphere,
also providing opportunities for education on digital skills into wider society or
industry (see [@HPCAkademie] for an existing, HPC focused instance of this).

## First Professional Qualification
### A possible graduation path within the classical university structures
We have put forward the idea that familiarity with research is a prerequisite for an RSE in order to be able to work effectively in the research space and in collaboration with researchers.
To generate the required number of skilled persons we propose to offer a classical Bachelor's and Master's curriculum at selected sites.
In this particular example, we consider a path into RSE via a traditional university route involving Bachelor's and Master's degree studies that include a RSE element.

However, we recognise that there are other routes into an RSE career and these are increasing.
For example, some RSEs come from an industry background, others may come through apprenticeship or similar programmes.
In both cases, gaining knowledge of the research life-cycle and understanding the ways that researchers work towards solutions
to research challenges is something that can be developed on-the-job alongside training opportunities and the chance to work directly with researchers.
This leads naturally to the question, whether it is possible to become an RSE without a home research domain.
With software being a core element of the research process in so many different domains,
it is not helpful for everybody working in RSE to have a background in computing or software engineering.
Indeed, we consider it much more useful if new graduates looking to work in the RSE space come from a wide range of different domains.
Expertise, beyond software development skills,
in another research domain can be an important element of an RSE team being able to support RSE projects in that domain.

A \${DOMAIN}-RSE in the STEM domains can start with a Bachelor's degree in their domain that shares large portions
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
This gives them a Master's degree of a \${DOMAIN}-RSE that has learnt in their lectures a research domain specific part and a software engineering specific part,
and enabled them to get a first dip into actual science in their master's thesis.
Of course special care has to be taken to integrate them at some point in their studies into mature projects
to expose them to the experience of senior RSEs and how they approach problems.
An example of this \${DOMAIN}-RSE can be found in Appendix: [Bioinformatics skills and certification].
Of course, the next question for their future is whether a master's degree enables them to really be effective parts of a research group.
While we accept this is something of a generalisation, we argue that this is most likely not the case since
undertaking a PhD provides a much more extensive set of research training and experience that can be vital for a researcher's future.
Research environments differ internationally but in many cases there are formal barriers in the research landscape that require a PhD (e.g. eligibility for funding).
Hence a PhD is required to actively participate in science and hence we argue the regular RSE
should do a PhD that on one end combines knowledge of a research domain with software engineering heavy task
such that both pillars are suitably covered and have been exposed to research, software development and team dynamics.
Graduating from this PhD program, opens a future career path as a lead RSE in their domain to them.

### Specialised Master's Programs
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

### Alternative first qualification paths
For completeness we mention that vocational programs like the MATSE [@MATSE] can provide a more application oriented less research oriented profile for individuals.
Since a certain amount of overlap with sciences is expected, it is expected that programs can be switched with minimal friction.

## Extra-academic institutions for continuous learning
As elaborated in the instruction the dynamic working place of an RSE requires continuous learning.
Knowledge-based industries have long recognised the value of qualifying their employees and hence invest time and money into this.
We propose institutionalised structures that offer graduates a venue for life-long learning, or to deepen their skills.
Centralising this notion in a few institutions has some major benefits for society and industry as well,
since these become central hubs for offering the skills with digital tools.
The HPC-Akademie [@HPCAkademie] is a good example in the HPC space that offers its services to graduated
researchers that want to deepen their HPC skills for research or to practitioners that require them for industrial applications.
Specialising the centres to certain skill sets enables them to effectively reach out into the sciences with their brand.
With the existence of these resources we believe that their acceptance gradually increases over time.
The tasks of these centres is facilitated by reusing the work of initiatives like EduTrain [@EDUTRAIN] and platforms like DALIA [@DALIA].
Naturally, other existing structures outside of academia mentioned before like the Carpentries [@Carpentries] can be nicely integrated
and offered to a broad audience on a regular basis.

# How do we reach people in different stages of their careers?

Many current RSEs have found their way to being an RSE during their doctoral studies.
This transition usually happens slowly. You start programming a tool, and someone else likes it, it becomes known that you have programming skills and suddenly you are the RSE of the group that everyone would like to have in their projects. If you enjoy this role, you need to be aware that there is a RSE career path as well as that specialised training materials exist. One place to generate awareness of the career option and training is universities' doctoral on-boarding processes or right thereafter.
RSE training could be offered as elective courses at universities organised by some central organisation. RSE could be presented as a career path in suitable events. Since many RSE-minded people also at some point find their way to an HPC cluster, mailing lists of said clusters could be utilised to advertise RSE courses.
One important aspect to think about is also the wording in documents advertising these resources.
Potential future RSEs might not know the term yet or know that the course advertised includes topics that are of interest to them. If the university or organisation has a GitHub/Lab organisation/project, having a banner there might reach the right people. Most important is that people working in IT help-desks know about the courses offered so that they can advise students/researchers on visiting the course/reviewing the materials if related questions are asked.
For an RSE it is important to be a part of a network with other RSEs, irrespective of the career level.
A perfect first step for forming this network is topic-related conferences, workshops or meetups.
Beyond that, there is the broader RSE community organised at the local and regional level with chapters or local/regional communities, at the national level with societies and the international RSE society.
Each of them offers possibilities for connecting within or beyond an individual institution and is a great way to find like-minded people to grow a wider network and thereby facilitate the sharing of information on interesting events or help each other out.
This available layered network can greatly benefit the RSE in finding help with issues outside of their own comfort zone
and provides a welcoming, social safety net providing a home for the RSE. Since we feel providing aspiring RSEs this net
is of utmost importance we envision compulsory events introducing that to young RSEs.
Qualification badges are another venue, that RSEs to find people with the same technical interest.

Short primers on RSE skills, infrastructure and good coding practices
can be found in field-specific scientific articles and conference proceedings,
such as [@Roberts1969; @Baxter2006; @Prlic2012; @Leprevost2014; @Wilson2014c; @Stodden2014; @Crusoe2016; @Crick2017; @Fehr2021; @Grossfield2022],
some of which are specifically tailored to group leaders, institutions and scientific
journal editors rather than RSEs [@ChueHong2013; @ChueHong2014; @Katerbow2018; @Strasser2022].
Scientific journals have the advantage of reaching a large spectrum of
research scientists at all stages of their career.

Localising RSE teaching material and RSE information in languages other than English
can help reach a much wider audience by lowering the barrier to entry in the field.
In 2014 the community behind The Carpentries engaged in an international
effort to translate their training material into Spanish [@Wilson2014a],
Korean [@Wilson2014b] and Portuguese [@Silva2014].
Core lessons have been translated to Korean in 2015 [@Lee2015], and the Spanish
core lessons are now officially part of the Software Carpentry material [@CarpentriesSpanish].
Likewise, The Programming Historian journal translated RSE lessons [@Sichani2019]
for the digital humanities to Spanish in 2017 (resulting in a 10-fold increase
in traffic from Spanish-speaking countries [@Crymble2018]),
French in 2019 [@Papastamkou2019] and Portuguese in 2021 [@Alves2021].
Similarly, in the period 2015-2017, the Stack Overflow website launched localised
versions in Portuguese [@StackOverflowPortuguese], Russian [@StackOverflowRussian]
and Spanish [@StackOverflowSpanish] to reach a wider community.
There are also RSE short primers [@Astigarraga2022] and
RSE guidelines [@ClementFontaine2019b; @Appel2021; @Haim2021] in non-English
languages to address the need of specific communities.
The European Commission report Digital Competence Framework for Educators
(DigCompEdu) [@Redecker2017] was translated to German [@Redecker2019]
and French with modifications [@P8FutureUniversity2023a].

Annotating RSE open educational resources with metadata about required previous knowledge, covered material, and medium or media of the resources improves their findability and accessibility.
Though, a registry agreed on by the community, would be required to take full advantage of such annotations.
As open educational resources are often living documents they do not lend themselves well to publishing in the form of snapshots in repositories, such as Zenodo.
With the life sciences, there already exists a field, that started efforts to annotate their training data with the TrainingMaterial Schema [@Castro2023; @TrainingMaterial].

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
courses designed for Master's degrees and PhD programs [@BioinformaticsCertification].

Teaching incubators can be leveraged to develop and test new academic curricula
that introduce basic RSE topics, such as the "Algorithmic Battle"
[@AlgorithmicBattle] (version control, documentation, good coding practices),
"digit@L" [@DigitalLearning] (coding, data analysis, machine learning)
and "DigiFlex" [@DigiFlex] (digital tools) experimental modules funded by the German
Foundation for Innovation in Higher Education [@StiftungInnovationHochschullehre]
to reduce skill gaps among first-year university students.
Likewise, The Carpentries teaching material can be made more modular
and re-usable in domain-specific contexts to better suit the needs
of specialised RSEs. Examples include HPC Carpentry [@OCais2020]
and Data Carpentry for Biologists [@White2022].

FIXME:

- find more examples of teaching material in non-English languages
- discuss the role of translations in overcoming linguistic and cultural barriers?

Further ideas:

- making RSE best practice guides fun to read with memes or satire [@Balaban2021; @Laginja2022; @Astigarraga2022; @Fehr2021]
- reducing the skill gap by organising more inclusive workshops [@McInerney2017; @Akoh2017; @Shelton2017; @NatlAcadSci2022],
  to address gender disparities or take into account economic status, cultural background, or special educational needs;
  peer-reviewing of code of conducts by the CHAOSS Diversity and Inclusion Badging organisation [@CHAOSSDEIBadging; @GitHubCHAOSS]
- more inclusive RSE-Humanities teaching material [@Crymble2016; @Sichani2019]
- related discussion in CSE [@Webb2017]

## Improve findability of open educational resources

Although multiple organisations have published open educational resources for RSEs, in particular for foundational skills, their findability can be significantly improved.
The RSE community of lacks an agreed-upon standard of metadata with which to annotate RSE OER, which would help learners as well as teachers to find suitable resources to satisfy their concerns.
Building on such annotations, a community agreed-upon registry for RSE OER would additionally improve the situation.

## Micro-accreditation
With the existence of institutions for continuous learning
after the first professional level of education the question of certification arises.
We propose, digital certificates and
learner badges [@Ifenthaler2016] as one possibility for experienced RSEs
to showcase that they possess a certain technical skill.
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
The Extreme Science and Engineering Discovery Environment organisation
delivers badges to create an incentive for participation in HPC training events
[@Kappes2015; @Sale2017]. IBM delivers badges to promote continuous learning and
provide micro-credentials to its staff and customers [@Leaser2020; @Leaser2019]
There are 1360 badges as of July 2023 [@IBMBadges]
and 1 million badges were issued as of July 2018 [@Daniels2018];
they are recognised by a few academic institutions
[@NortheasternUniversityIBMBadges; @NCCentralUniversityIBMBadges; @BluefieldIBMBadges]
and in some cases are convertible to graduate credit [@Leaser2020].

The Open Source Software Security Mobilisation Plan [@OSSMobilizationPlan]
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
- being a teacher is a potential working field for RSEs
- we need good teachers for both
- pointer to the qualification paths and career paths outside of the appendix.

FIXME: The career path discussion.

\appendix

# Appendix

## Digital competencies and certification

The European Commission Joint Research Center developed the "DigComp" framework
to categorise general digital competencies in 8 levels of proficiency
[@Vuorikari2016; @Carretero2017; @Vuorikari2022a].
Proficiency levels 1 and 2 ("Foundation") represent simple tasks that can be
carried out with proper guidance from more experienced peers, levels 3 and 4
("Intermediate") represent tasks that can be carried out autonomously and
demonstrate a basic understanding of digital technologies, levels 5 and 6
("Advanced") demonstrate collaborative digital problem-solving skills,
and levels 7 and 8 ("Highly specialised") demonstrate the capacity to
contribute to the advancement of a discipline through digital technologies.
In a scientific work environment, proficiency levels 5-6 could correspond
to a Junior RSE while levels 7-8 could correspond to a Senior RSE.

For illustration purposes, individuals at levels 1-2 are able to formulate the
specifications and requirements of an algorithm to more experienced peers who
can use that information to find a suitable program for the digital environment
of the workplace. They are also able to write an actionable bug report.
At level 3-4, they are able to discover the programs they need in software
repositories, and can find workaround solutions to temporarily fix a bug.
They can guide their peers in finding the right software at level 5,
including in other scientific disciplines at level 6.
They can also write their own software at level 5. At level 6, they know good
coding practices, performance aspects of algorithms, and can submit successful
bug fixes in existing software.
At level 7 they have excellent command of digital tools, and can e.g. setup a
collaborative platform (wiki, instant messaging app, etc.), manage software
projects and write guidelines for their peers.
At level 8, they can develop complex software with many interacting factors
and propose new ideas in their field.

The DigComp framework can be used to:

- identify skill gaps (librarian: [@Zignani2020], information and communications
  technology: [@AllDigital2022])
- design curricula, e.g. [@Kluzer2019a] for proficiency levels 1 and 2
- design micro-credentials [@Centeno2022], such as in the European
  Digital Skills Certificate pilot study [@ESDCConsulation2023]
  <!-- pilot study report should be due November 2023 -->
- map digital skills to existing frameworks [@Law2018; @ICDLEurope2021]

The "DigCompEdu" framework [@Redecker2017] was developed to foster educators'
digital competence. The scale is based on the six proficiency levels used by
the Common European Framework of Reference for Languages, ranging from A1
(no use of digital technologies in the classroom) to C2 (champion the use
of digital technologies in teaching environments, actively contribute
to the palette of interoperable digital tools and curate open educational resources).

The "DigCompOrg" framework [@Kampylis2015] aims to facilitate the inclusion
of digital learning technologies by education organisation and provide
strategies to improve the digital competence of teachers and learners.
The latter can take several forms, e.g. assessing the digital competency
of the teaching staff and factoring it in performance reviews, creating
new roles centred around digital technologies, offering training and
accredited professional development opportunities, promoting the use and
creation of open educational resources.
