---
title: "Educating RSEs in Germany - What Needs to Be Done"
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
---

**Abstract**:
The previous papers dealt with a survey of the disparate sources of education for RSEs.
A follow-up publication dealt with specific competencies that define and RSEs and have shown
some career pathways that emerge from them. In the next paper we have set out structre sthat facilitate
the education of RSEs, thereby setting the ground for this paper where we 
detail what needs to be done specifically in Germany.

---

**Keywords**: research software engineering, training, learning, competencies


## Reasons for a change
### Ensuring Maintenance and Sustainability
While ensuring maintenance and sustainability of research software is of huge importance to the communities that build and use it,
a particular challenge is that it is often very difficult to obtain ongoing research funding for software maintenance tasks.
As a result, when a project that developed or extended a piece of software finishes,
support for the software fades as team members move on
to other research, academic or RSE roles, or become busy with other funded work.

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

Answering the need for more RSEs
can only be achieved by simultaneously having a clear training path
and ensuring that existing and trained RSEs are retained in academia.
The best RSEs continue to develop their skills and knowledge through experience
well beyond the end of any formal training,
and strengthen collaborative relationships and institutional knowledge over time.
The combined cost of replacing such experienced and embedded RSEs is likely to 
exceed the resources required to keep them,
but retaining good RSEs requires intentional effort and support on the managerial and institutional level.
As Van Tuyl et al. put it,
"All other things being equal, [RSEs working in academia] can leave for industry with the expectation of a significant raise. 
Therefore it is important for academic institutions to ensure all other things  are not equal."[@VanTuyl2023]

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

