---
#(This frontmatter block follows YAML syntax)
id: fair-tool-discovery #epic-title-in-lowercase-with-hyphens
coordinator: Maarten van Gompel #person or list of people
wp: [ 1, 2, 3, 4, 5, 6] #involved workpackages
github-projects-link: https://github.com/orgs/CLARIAH/projects/1 #link to a specific project under here
participants:
    - Maarten van Gompel (KNAW HuC), developer and coordinator
    - Jan Odijk (UU)
    - Roeland Ordelman (NIBG), stakeholder
    - Menzo Windhouwer (KNAW HuC), liason FAIR Datasets and IG Vocabularies
    - David de Boer (NDE)
    - Jaap Blom (NIBG)
    - Sebastiaan Fluitsma, liason for Ineo
themes: [ Metadata, DevOps, Curation, Vocabularies, Sustainability, Processing, Search ]
evaluation: #overall evaluation for the (best) implementation of this epic
    trl: 0 #technology readiness level
    cl: 0 #compliance level
    srl: 0 #stakeholder readiness level
---

## FAIR Tool Discovery

### Rationale

> Describe, from a high-level perspective, the rationale of what important role
> the service(s) that implement this epic fulfill in the CLARIAH infrastructure

One key goal of the CLARIAH infrastructure is to provide scholars with
information where they can find tools that they need for their work. CLARIAH and
its predecessor projects have developed a lot of useful tools already. Some of
these can be found in repositories such as the CLARIN switchboard. Others are
distributed and disseminated on an individual or work package level. However, it
would be in the benefit of both scholars and tool providers to have a central
place (INEO) where scholars can go to **find** and/or discover tools. At the
same time, the tools that they find via the CLARIAH infrastructure should also
be **accessible**, so that these tools can indeed be used. From a CLARIAH
perspective, we would to some extent also like to guarantee
accessibility/usability of tools, and also, that tools are **interoperable**
with other tools or CLARIAH infrastructure components. Finally, ideally tools
should also be **re-usable**, even if tools change during time (related to
sustainability of tools). In practice, it will be hard to warrant full FAIRness
of tools provided/disseminated by CLARIAH. We could however at least aim for
making tools findable and accessible. For interoperability and re-usability
(sustainability) we could aim for a system that informs scholars of the status
of tools that are disseminated, e.g., by labeling tools (giving “stars”) for it
compatibility level, documentation level, and adherence to CLARIAH software
requirements. One of the key requirements of a tools discovery service that we
propose therefore, is a sound system for aggregating and updating information on
tools that reside in various places, the tool metadata.

It is not the aim of the tool discovery service itself to provide means for
execution. We assume that (if applicable) the service provides links to
individual services (e.g., LaMachine) for executing code using data. However, as
being able to execute code is key to “accessibility”, making (CLARIAH) tools
executable on e.g., web services or local services is part of the development
roadmap for this service.

### User Stories

> Describe, from a high-level scholarly perspective and in minimal and generic terms, the user stories that define this epic.
> We recommend using sublists (i.e. a simple tree structure) for breaking down user stories into parts when needed.

1. **As a scholar, I** am looking for tools (please see the definition in the next subsection) and want to browse through and search in a registry of available tools **in order to** select the tools I need to further my research. The registry should offer sufficient information for me to make an informed decision on suitable tools to explore.
2. **As a scholar, I** want to upload my data and automatically be presented with tools that can operate on such data **in order to** more effectively find tools suited for my data. I want to be automatically redirected to the tool I choose, with my data
3. **As a scholar, I** am looking for tools offering a particular interface **in order to** be able to find tools I can communicate with in the fashion I need. For instance, I want tools I can access through the web using a UI; web services with a web API so I can programmatically interact with it from my own scripts; tools I can use locally from the command line; tools that are software libraries which I can use in my own scripts; or even tools that are apps I can run on a smartphone or GUI tools on a desktop.
4. **As an infrastructure provider, I** want all tool metadata to be automatically harvested from the source **in order to** ensure the data is always up to date and facilitate maintenance.
5. **As an infrastructure provider, I** want to be interoperable with the wider CLARIN infrastructure **in order to** have tools available in other CLARIN portals.

User stories 1-3 are not directly implemented by this epic/service, but are facilitated by it. This epic focusses on the
data provisioning pipeline that makes these user stories possible.

### Needs & Dependencies

> Describe organisational and technical dependencies that are crucial for the success of this service.

* Compliance to the software/infrastructure requirements as described in the next section
* Cross-WP agreement on some additional vocabulary
* WP4 involvement

### Requirements

> Describe software, infrastructure & interoperability requirements that arise from this service or that are especially relevant for this service. These must be formulated in further detail in the corresponding requirements documents.

* Software MUST define CodeMeta software metadata along with the source code
* Services MUST expose a public endpoint providing their specification
* Services SHOULD expose a public endpoint providing high-level CodeMeta metadata
* Services MAY participate in the CLARIN switchboard

### Service Description

> Describe the service(s) that implement(s) this epic, mention software components, data components and interoperability standards where appropriate.

This core service provides infrastructure for finding tools, where the metadata for the tools is automatically and
periodically harvested and converted to a unified representation. The term “tool” here is deliberately ambiguous and can
refer to a piece of software in the broadest sense, it may be a web application, web service, programming library, or
any composition thereof. Tools may live in a wide variety of places. We seek to standardize the way by which their
metadata is described using Codemeta and OpenAPI, which will be posited as software & infrastructure requirements.
Codemeta provides basic software metadata, whilst OpenAPI provides metadata covering web service specification. We
automatically collect this metadata from as close to the source as possible using a CLARIAH Tool Harvester, the source
being either a source code repository or a webservice endpoint. We aggregate all metadata into a central backend
solution called the CLARIAH Tool Store. Portals like Ineo, the CLARIN Switchboard or others can either directly query
the tool store over an API.

### Components

> Describe the components and subcomponents involved in this epic in a simple table form (in a stand-off CSV file);
> specify whether the component is: a service (instance), software, data or standard. Indicate what user stories are
> implemented/facilitated (under the description) and indicate dependencies between components in the last column.
> Please consult the [definitions](introduction.md#definitions) and [data model](introduction.md#data-model).

```table
---
table-width: 1.0
width: [ 0.03, 0.1, 0.1, 0.30, 0.1, 0.10, 0.27 ]
alignment: LLLLLRL
include: tool-discovery-components.csv
markdown: true
---
```
**Note:** Interoperability with Ineo will be handled at the Ineo side: https://github.com/CLARIAH/clariah-plus/issues/35


### Workflow Schema

> Draw a schema indicating how the various software and data components interact. This is required only when many
> components are involved and their connection is not immediately obvious.

![Components](tool-discovery-components.png)

### Evaluation

> Estimate the overall readiness of the implementation(s) for this epic in the frontmatter. You may add any additional
> evaluation here.

end Q1 2022 - Initial prototype has been delivered

### Context

> Sketch the wider context of the implementations for this epic in relation to other (existing/proposed) projects and initiatives.

* Ineo is meant to become the entry point for CLARIAH tools, however, it can be considered a thin layer and back-end functionality and automatic harvesting needs to be resolved separately, as done by this epic.
* A system called CLAPOP was developed in CLARIN and uses manually crafted software metadata descriptions in CMDI (no harvesting) with rich information for scholars. The information is largely outdated however.
* A LaMachine Portal (labirinto) was developed as a solution to provide a portal page for any LaMachine installation/deployment, automatically harvesting the tools available within. It uses CodeMeta which is more generic but less specific for scholars.
* The CLARIN Switchboard is developed by CLARIN-ERIC and gives users the option to select tools from a wider CLARIN ecosystem, based on the data they upload. It is largely limited to singular data (single files).

### Use cases

> Link to specific use cases for which this user story is relevant, use cases should reside in the [use cases directory](../../use-cases/)
n/a

### Deliverables

1. **Document:** Software Metadata Requirements
2. **Software + documentation:** [codemetapy](https://github.com/proycon/codemetapy)
3. **Software + documentation:** [codemeta-harvester](https://github.com/proycon/codemeta-harvester)
4. **Software + documentation:** [codemeta-server](https://github.com/proycon/codemeta-server)
5. **Service + documentation:** [Tool Store](https://tools.clariah.nl)

### Planning

> A rough planning for this epic. The GitHub Projects kanban board for this epic should be used for more detailed planning during development

We identify the following primary tasks, more or less in chronological order, and add a rough indication (PM=person
months) of the work we expect and who will perform it.

* [Define cross-WP team for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/30)
* [Define components, standards, requirements for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/31) - 0.5PM (68 hours)
* [Define extra vocabulary for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/32) - 0.5PM (68 hours) - entire team
    * [Development status vocabulary](https://github.com/CLARIAH/clariah-plus/issues/98)
* [Implement codemeta validation component for tool discovery, against clariah requirements](https://github.com/CLARIAH/clariah-plus/issues/50) - +0.5PM (+68 hours) - NDE (David de Boer)
* [Write software metadata requirements](https://github.com/CLARIAH/clariah-plus/issues/40) - 0.5PM (68 hours) - KNAW HuC (Maarten vG and others)
* [Implement harvester component for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/33) - 1.5PM (204 hours) - KNAW HuC (Maarten vG)
    * Includes work on the underlying conversion component (codemetapy)
    * [Extract software metadata from the web (service endpoints and/or webpages)](https://github.com/CLARIAH/clariah-plus/issues/92)
* [Implement tool store for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/34) - 2.0PM (272 hours) - KNAW HuC (Maarten vG)
    * [Implement simple visualisation (portal page) for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/99)

* [Implement Ineo export/import for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/35) - 0.5PM (68 hours) - KNAW HuC (Maarten vG)
    * This involves only support for the Ineo developers to make the link. The actual implementation for
      connectivity between tool discovery and ineo is on the Ineo side and requires more hours. The hours listed
      here are only for supporting the Ineo developers from our side.
* [Implement Switchboard export for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/36) - 0.5PM (68
    hours) - Not assigned yet
* [Implement CMDI export for tool discovery](https://github.com/CLARIAH/clariah-plus/issues/37) - 1PM (136 hours) - Not assigned yet
* [Compose and publish metadata for all software/services](https://github.com/CLARIAH/clariah-plus/issues/38) - 3PM??? (very hard to estimate, this is a function of the number of tools, this is spread over all participating institutes)
    * [Populate tool source registry](https://github.com/CLARIAH/clariah-plus/issues/91)

Total: 10.5PM (1428 hours)

### Resources

Some comments on resource allocation:

* The "compose metadata for all software/services" subtask may be argued to be financed from already existing WP budgets
rather than this one.
* Any funds still open for the WP3 MD4T project (Utrecht University) should be reallocated on behalf of this shared epic.
* Composing metadata for software/service should probably come from the existing WP budgets that maintain the software


