#### Project team structures

Project teams working on research software may have different sizes and structures, and different approaches to how they undertake their work. Within a project, there may be only a single RSE undertaking software development, based either locally or within an RSE team. For individual developers based locally in research groups/teams, they may be classed as a researcher, even if the bulk of their work is software development. Alternatively, in a larger project, a group of RSEs might be involved - these RSEs could be based locally within a research group or team and the individuals may be classed as researchers, or they could be a group of RSEs from a departmental or central RSE team. In the context of an RSE team, RSEs may be working on multiple projects which can change the way that they plan and work on development tasks and the tools and approaches that they use.

In this table, we look at individual or team competencies and approaches to them,
considering how these differ depending on whether an RSE or researcher is working alone on a software project,
or whether they are working as part of a team of research software developers.
We extend this to consider how things differ when a developer or a group of developers is based locally within a research team or department,
or when they are based in a dedicated RSE team.
We also look at organizational aspects in the context of each of the considered competencies since there are a variety of ways that organizations can contribute to and support them. We first summarise the meaning of each of the columns in the table:

- **Competency:** The code assigned to the competency being considered. See the list in **[Table ?????]**.
- **Individual developer (Locally-based):** A single person working on some research software - often a researcher with RSE skills.
- **Individual developer (RSE team-based):** A single person working on research software - generally a professional RSE supporting another team's software single-handedly.
- **Group of developers (Locally-based):** A group of RSEs/researchers within a research group or team, working together on developing software to support or undertake a single research goal/project.
- **Group of developers (RSE team-based):** A group of members of the RSE team working together on a research software project for a research group.
- **Organization-level support:** How the defined competencies are recognised and represented at organisational level.




Table: Required Competencies in different organization forms.

+---------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Competency          |   *Working as an individual developer*|   *Working with a group of developers*|  *Organization-level support*         |
|                     +-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|                     |   Locally-based   |    RSE Team-based |   Locally-based   |    RSE Team-based |   Locally-based   |    RSE Team-based |
+=====================+===================+===================+===================+===================+===================+===================+
|  DOCBB              | Focus on          |  Likely greater   | -89.2 °C          |                   | -89.2 °C          |                   |
+---------------------+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+





<table>
  <thead>
    <tr>
      <th rowspan="2">Competency</th>
      <th colspan="2">Working as an individual developer</th>
      <th colspan="2">Working with a group of developers</th>
      <th rowspan="2">Organization-level support</th>
    </tr>
    <tr>
      <th>Locally-based</th><th>RSE Team-based</th>
      <th>Locally-based</th><th>RSE Team-based</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DOCBB</td>
      <td>Focus on getting outputs to support research. Often time-constrained, may be self-taught, less awareness/familiarity with code quality and structure best practices. </td>
      <td>Likely greater focus on reusability, documentation, and best practice but potential lack of developer support.</td>
      <td>More opportunity to discuss and share ideas but team members may be self-taught and less aware of key practices.</td>
      <td>Stronger focus on team-based project management and development methodologies resulting in higher quality, more reusable code.</td>
      <td>Can offer training in core topics to support self-taught/embedded developers. May have research software guidance/policies that provide advice.</td>
    </tr>
    <tr>
      <td>LIBS</td>
      <td>Reusability and sharing/distribution of code often not a focus or considered relevant.</td>
      <td>Greater focus on reusability/sharing but likely not part of project aims.</td>
      <td>May be looking to develop reusable shareable outputs but likely case-by-case basis.</td>
      <td>Focus on quality and practices, reusability/packaging driven by project needs and spec.</td>
      <td>May provide policies on sharing and reuse of software. May be driven by funder requirements/policies.</td>
    </tr>
    <tr>
      <td>MOD</td>
      <td>Needs full awareness of entire codebase to support extension/maintenance. May not need/get additional experience or support. If project taken on from another individual developer, there may be challenges.</td>
      <td>As local but greater awareness of need for future transition to other developer(s), likely provide e.g. docs/issues/project board and other support from central services to support this. May only need to know part of code.</td>
      <td>Internal team training important to ensure ability to build necessary mental model of codebase and to document via text or tools to support sustainability.</td>
      <td>As local team but likely stronger awareness of tooling and practices in place within RSE team to support this. It may only be necessary for each developer to understand code related to their assigned tasks.</td>
      <td>Training and experience are key here and organisations can help to coordinate and provide support for training and mentoring/community activities.</td>
    </tr>
    <tr>
      <td>SWLC</td>
      <td>It's down to you to manage the complete lifecycle, if you move on, what will happen to the code?</td>
      <td>More support with a team but do they have awareness/expertise of managing the lifecycle? What is the "bus factor"?</td>
      <td>Even when working alone, team infrastructure and tooling can be vital in supporting the lifecycle and supporting sustainability.</td>
      <td>As previous but with a large codebase, how many people know about each part? Need to think about coherent lifecycle management across the team - generally a key part of RSE team expertise.</td>
      <td>Support for training important. Organization may also provide site licences for e.g. management tools.</td>
    </tr>
    <tr>
      <td>SWREPOS</td>
      <td>Where open source, use of repositories important for code management and demonstrating outputs - e.g. supporting academic credit. May not have awareness/skills if self-taught.</td>
      <td>As previous but professional RSEs generally very experienced with use of repositories and their many features.</td>
      <td>Repos a vital aspect of modern team-based development. Is the necessary expertise available?</td>
      <td>Repos used extensively by RSE teams - often the base for project management, issue tracking, etc. in addition to code itself. May train others.</td>
      <td>Organizations can offer enterprise repository set ups, site licences etc. Also fund either internal or external training for this vital research software development tooling.</td>
    </tr>
    <tr>
      <td>LEG</td>
      <td>Responsibility may be with individual but they may not have necessary knowledge/skills.</td>
      <td>A developer from an RSE team should have basic awareness of aspects such as licensing. Also know where to get additional support via team/organization.</td>
      <td>As with individual (local) developer, are the skills available within the group? Who can they ask?</td>
      <td>This is a core area that RSE teams need to be aware of. Can also often provide advice to projects themselves or provide links with other parties who can help.</td>
      <td>Organizational support, guidance and policies important. So are knowing how to find them and who to contact for advice.</td>
    </tr>
    <tr>
      <td>NEW</td>
      <td>An individual's curiousity has now to be shared between the research goal and the software project, therefore learning new methods and skills may be challenging and is often not the core aim.</td>
      <td>RSE teams should support their team members, especially when working individually on a project, to explore new tools and approaches, make relevant contacts and learn more about the project domain.</td>
      <td>Likely to be an area of interest for an embedded development team but if they are researchers, they may not have the local knowledge or contacts to know where to look.</td>
      <td>As per Individual (RSE team).</td>
      <td>Organizations can work with relevant groups locally to help share information on new technical processes and tooling, and facilitate training.</td>
    </tr>
    <tr>
      <td>RC</td>
      <td>This is likely to be familiar to individuals, who are often researchers, especially if they are embedded within a research team.</td>
      <td>Many RSEs will have familiarity with the research lifecycle, although they may not have domain knowledge.</td>
      <td>Likely to be familiar to software teams (often researchers) working in a research group. Can share knowledge between themselves or reach out to colleagues.</td>
      <td>Teams of RSEs from an RSE group are likely to include one or more team members with strong awareness of the research lifecycle.</td>
      <td>Research organizations have extensive infrastructure to manage the research lifecycle, this can support researchers/RSEs.</td>
    </tr>
    <tr>
      <td>SD</td>
      <td>Need to know how to find other work to build awareness of existing solutions. Researchers sometimes like to do things themselves. Working individually means there may not be someone to highlight this.</td>
      <td>RSE team members will generally be familiar with software sharing and discovery tools and platforms.</td>
      <td>As per individual (Local) but being part of a team can help to address this.</td>
      <td>As per individual (RSE Team).</td>
      <td>Can choose to run local environments to host software or catalgoue software, they can also provide institution-level access to platforms that support this.</td>
    </tr>
    <tr>
      <td>DOMREP</td>
      <td>Domain researchers working on software are likely to be more familiar with the domain-specific solutions.</td>
      <td>RSEs may need guidance from domain researchers around domain-specific repositories if they have a background in a different domain.</td>
      <td>As per individual (Local).</td>
      <td>As per individual (RSE Team)</td>
      <td>May host domain-specific repositories for areas that they work extensively in but this is likely to handled at research group level.</td>
    </tr>
    <tr>
      <td>USERS</td>
      <td>Is the software developed to support external users? If so, additional technical skills may be required.</td>
      <td>Is there a plan for external use? RSEs generally have the skills to support this or can access assistance via team colleagues.</td>
      <td>If a team of embedded researchers/developers are involved in a larger project, there's more chance that there's a case for external use. Do they have the skills and resources to support this?</td>
      <td>A team of RSEs can generally better prepare code for external users (e.g. by applying development best practices) and provide infrastructure or specialized RSEs for dealing with user support </td>
      <td>May be able to offer support with outreach and publicising outputs.</td>
    </tr>
    <tr>
      <td>TEACH</td>
      <td>May be independenly involved in training activites.</td>
      <td>May be able to support researchers with core technical skills.</td>
      <td>Sharing knowledge and skills within their group - peer support.</td>
      <td>Often support teaching more widely, either through organised courses or ad hoc activities such as "code clinics".</td>
      <td>Can run a range of teaching/training activities.</td>
    </tr>
    <tr>
      <td>PM</td>
      <td>Limited requirement beyond being well organised - can be important if someone else might take over codebase.</td>
      <td>Limited requirement but team will likely have standard PM approaches to be followed.</td>
      <td>Challenging for groups of local researchers/developers on larger projects. May not have awareness/experience of key skills.</td>
      <td>Likely have well structured approaches and tooling to support this.</td>
      <td>Can offer training to support management of projects. May offer organisation-level tooling.</td>
    </tr>
    <tr>
      <td>TEAM</td>
      <td>N/A</td>
      <td>Will need to work effectively with their home RSE team, as well as, potentially with researchers they are developing code for.</td>
      <td>Effective teamwork vital - do they have the skills and knowledge to support team-based software development?</td>
      <td>Will need to be able to work and collaborate effectively in a team, use required tools and processes, infrastructure, etc.</td>
      <td>Can offer support with team work. Many examples of courses around working effectively in a team.</td>
    </tr>
</table>

In the table above, we've looked at how different competencies can be related to and handled by researchers and RSEs working in different environments within an organisation and how the organisations themselves can contribute. We recognise that this is a challenging area to gain a detailed view of and that our content in the table is still a significant generalisation. We talk about the "Research Software Engineer" as a single entity but as the field expands, we expect to see more roles and job titles emerging around the RSE concept, many of which fit under the wider umbrella of Research Technology Professionals (RTPs).
The European Bioinformatics Institute (EMBL-EBI)'s BioExcel competency framework [**[BIOEXCEL-FRAMEWORK]**](https://competency.ebi.ac.uk/framework/bioexcel/3.0/carreer-profiles) provides some examples of different RSE-like computational roles. Work by King's Digital Lab at King's College London also provides some examples of a range of different roles within the research software careers space [**[KDL-CAREERS](https://zenodo.org/record/2559235)**].

