---
title: "EDUCATING RSEs in GERMANY - WHAT NEEDS TO BE DONE"
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

**Abstract**:
The previous papers dealt with a survey of the disparate sources of education for RSEs.
A follow-up publication dealt with specific competencies that define and RSEs and have shown
some career pathways that emerge from them. In the next paper we have set out structre sthat facilitate
the education of RSEs, thereby setting the ground for this paper where we 
detail what needs to be done specifically in Germany.

---

**Keywords**: research software engineering, training, learning, competencies

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

