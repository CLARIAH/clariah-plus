---
#(This frontmatter block follows YAML syntax)
id: fair-tool-discovery #epic-title-in-lowercase-with-hyphens
coordinator: Maarten van Gompel #person or list of people
wp: [ 1, 2, 3, 4, 5, 6] #involved workpackages
github-projects-link: https://github.com/orgs/CLARIAH/projects/1 #link to a specific project under here
participants:
    - Maarten van Gompel (KNAW HuC)
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

One key goal of the CLARIAH infrastructure is to provide scholars with information where they can find tools that they
need for their work. CLARIAH and its predecessor projects have developed a lot of useful tools already. Some of these
can be found in repositories such as the CLARIN switchboard. Others are distributed and disseminated on an individual or
work package level. However, it would be in the benefit of both scholars and tool providers to have a central place
(INEO) where scholars can go to **find** and/or discover tools. At the same time, the tools that they find via the CLARIAH
infrastructure should also be **accessible**, so that these tools can indeed be used. From a CLARIAH perspective, we would
to some extent also like to guarantee accessibility/usability of tools, and also, that tools are **interoperable** with
other tools or CLARIAH infrastructure components. Finally, ideally tools should also be **re-usable**, even if tools change
during time (related to sustainability of tools). In practice, it will be hard to warrant full FAIRness of tools
provided/disseminated by CLARIAH. We could however at least aim for making tools findable and accessible. For
interoperability and re-usability (sustainability) we could aim for a system that informs scholars of the status of
tools that are disseminated, e.g., by labeling tools (giving “stars”) for it compatibility level, documentation level,
and adherence to CLARIAH software requirements. One of the key requirements of a tools discovery service that we propose
therefore, is a sound system for aggregating and updating information on tools that reside in various places, the tool
metadata.

It is not the aim of the tool discovery service itself to provide means for execution. We assume that (if applicable)
the service provides links to individual services (e.g., LaMachine) for executing code using data. However, as being
able to execute code is key to “accessibility”, making (CLARIAH) tools executable on e.g., web services or local
services is part of the development roadmap for this service.

### User Stories

> Describe, from a high-level scholarly perspective and in minimal and generic terms, the user stories that define this epic.
> We recommend using sublists (i.e. a simple tree structure) for breaking down user stories into parts when needed.

1. **As a scholar, I** am looking for tools (please see the definition in the next subsection) and want to browse through and search in a registry of available tools **in order to** select the tools I need to further my research. The registry should offer sufficient information for me to make an informed decision on suitable tools to explore.
2. **As a scholar, I** want to upload my data and automatically be presented with tools that can operate on such data **in order to** more effectively find tools suited for my data. I want to be automatically redirected to the tool I choose, with my data
3. **As a scholar, I** am looking for tools offering a particular interface **in order to** be able to find tools I can communicate with in the fashion I need. For instance, I want tools I can access through the web using a UI; web services with a web API so I can programmatically interact with it from my own scripts; tools I can use locally from the command line; tools that are software libraries which I can use in my own scripts; or even tools that are apps I can run on a smartphone or GUI tools on a desktop.
4. **As an infrastructure provider, I** want all tool metadata to be automatically harvested from the source **in order to** ensure the data is always up to date and facilitate maintenance.
5. **As an infrastructure provider, I** want to be interoperable with the wider CLARIN infrastructure **in order to** have tools available in other CLARIN portals.

### Needs & Dependencies

> Describe organisational and technical dependencies that are crucial for the success of this service.
>
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

This core service provides infrastructure for finding tools. The term “tool” here is deliberately ambiguous and can
refer to a piece of software in the broadest sense, it may be a web application, web service, programming library, or
any composition thereof. Tools may live in a wide variety of places. We seek to standardize the way by which their
metadata is described using Codemeta and OpenAPI, which will be posited as software & infrastructure requirements.
Codemeta provides basic software metadata, whilst OpenAPI provides metadata covering web service specification. We
automatically collect this metadata from as close to the source as possible using a CLARIAH Tool Harvester, the source
being either a source code repository or a webservice endpoint. We aggregate all metadata into a central backend
solution called the CLARIAH Tool Store. Portals like Ineo, the CLARIN Switchboard or others can either directly query
the tool store over an API, or we offer export facilities over an API.

### Components

> Describe the components and subcomponents involved in this epic in a simple tree form; specify whether the component
> is: a service (instance), software, data, and estimate a TRL. Please consult the
> [definitions](introduction.md#definitions) and [data model](introduction.md#data-model). In case of multiple
> implementations, use multiple detached trees/lists and add a level four heading for each.

* **Service Component:** **Ineo**
    * **Function** Web-frontend for scholarly end-users for CLARIAH-wide tool discovery (amongst other things)
    * **URL:** ?
    * **Provider**: ?
    * **Implements:** 1
    * **Interface**: WebUI
    * **TRL**: ?
    * **Software Component:** **Ineo**
        * **Provider**: KNAW HuC with external party
        * **URL:** ?
* **Service Component:** **CLARIN Switchboard**
    * **Function** Web-application for end-user for tool discovery focussed on tools that take direct data input from a user upload throughout CLARIN.
    * **URL:** <https://switchboard.clarin.eu/>
    * **Provider**: CLARIN-ERIC (partner)
    * **Implements:** 1, 2, 5
    * **Interface**: WebUI
    * **TRL**: 8
    * **Software Component:** **CLARIN Switchboard**
        * **URL:** <https://github.com/clarin-eric/switchboard>
        * **Provider**: CLARIN-ERIC (partner)
    * **Data Component**: **CLARIN Switchboard Tool Registry**
        * **URL:** <https://github.com/clarin-eric/switchboard-tool-registry/>
        * **Provider**: CLARIN-ERIC (partner)
        * **Function**: Registry holding all tool metadata descriptions for the switchboard
* **Service Component:** **CLARIAH Tool Store**
    * **Function** Stores all harvested/aggregated tool metadata
    * **Function:** API for updating (invoked by harvester)
    * **Function:** API for querying (invoked by end-user, portals)
    * **Interface**: REST, possibly SPARQL
    * **TLR:** 0
    * **Software Component:** **CLARIAH Tool Harvester**
        * **URL**: (does not exist yet)
        * **Function:** Harvester for software & service metadata. Periodically queries all endpoints listed in the CLARIAH Tool Source Registry and updates the tool store.
        * **Provider**: ?
        * **Implements:** 4
        * **Interface**: CLI
        * **TRL**: 0
        * **Comment:** There may be a role for dataverse here to serve as the implementation, but it kind of feels like overkill to me for this purpose.
        * **Comment:** Another option is to use the baserow database we aim to use for components and instances, but here we don’t have actual Linked Open Data
    * **Data Component**: **CLARIAH Tool Source Registry**
        * **URL**: (does not exist yet)
        * **Provider**: ?
        * **Function:** Simple registry of software source repositories and service endpoints. Serves as input for the harvester.
        * **Comment:** Could be Implemented as a simple plain text list of URLs in a git repository on github, new registrations can be added using pull requests. Or implemented using the planned baserow database that holds all software components.
        * **TRL**: 0
    * **Software Component:** **Ineo Export**
        * **URL**: (does not exist yet)
        * **Provider**: ?
        * **Function:** Client using the tool store API (or a direct extension thereof) converting output to a format understood by Ineo, for interoperability with it. Needed if (and only if) we can't make Ineo correct directly to our tool store backend
        * **Implements:** 4
        * **Interface**: CLI or WebAPI
        * **TRL**: 0
    * **Software Component:** **Switchboard Export**
        * **URL**: (does not exist yet)
        * **Provider**: ?
        * **Function:** Client using the tool store API (or a direct extension thereof) converting output to the format required by the CLARIN Switchboard, for interoperability with it
        * **Implements:** 4, 5
        * **Interface**: CLI or WebAPI
        * **TRL**: 0
    * **Software Component:** **CMDI Export**
        * **URL**: (does not exist yet)
        * **Provider**: ?
        * **Function:** Client using the tool store API (or a direct extension thereof) converting output to an established CMDI software metadata profile for interoperability with CLARIN
        * **Implements:** 4, 5
        * **Interface**: CLI or WebAPI
        * **TRL**: 0
    * **Interoperability Standard:** **CodeMeta**
        * **URL**: <https://codemeta.github.io>
        * **Provider**: The CodeMeta Project (3rd party)
        * **Function**: Software metadata schema (Linked open data, aligning with schema.org)
        * **Function**: Crosswalks for mappings with other existing metadata schemes
        * **TRL**: 8
    * **Interoperability Standard:** **OpenAPI**
        * **URL**: <https://openapi.org>
        * **Provider**: OpenAPI Initiative (3rd party)
        * **Function**: Service API specification schema
        * **TRL**: 8
    * **Interoperability Standard:** **CMDI**
        * **URL**: <https://openapi.org>
        * **Provider**: CLARIN? (partner)
        * **Function**: Metadata Schema
        * **TRL**: 8
    * **Interoperability Standard:** **CLARIAH Tool Metadata**
        * **URL**: (does not exist yet)
        * **Provider**: ?
        * **Function**: Extra domain-specific vocabulary need for CLARIAH
        * **Comment**: CodeMeta's vocabulary is too limited to cover all our needs, we need to define extra vocabulary
        * **Comment**: Earlier work in the WP3 ‘metadata for tools project’ can serve as valuable input here
        * **TRL**: 0

### Workflow Schema

> Draw a schema indicating how the various software and data components interact. This is required only when many
> components are involved and their connection is not immediately obvious.

### Evaluation

> Estimate the overall readiness of the implementation(s) for this epic in the frontmatter. You may add any additional
> evaluation here.

### Context

> Sketch the wider context of the implementations for this epic in relation to other (existing/proposed) projects and initiatives.

* Ineo is supposed to become the entry point for CLARIAH tools, however, it can be considered a thin layer and back-end
  functionality and automatic harvesting needs to be resolved separately.
* A system called CLAPOP was developed in CLARIN and uses manually crafted software metadata descriptions in CMDI (no harvesting) with rich information for scholars. The
  information may be outdated however.
* A LaMachine Portal (labirinto) was developed as a solution to provide a portal page for any LaMachine installation/deployment,
  automatically harvesting the tools available within. It uses CodeMeta which is more generic but less specific for scholars.
* The CLARIN Switchboard is developed by CLARIN-ERIC and gives users the option
  to select tools from a wider CLARIN ecosystem, based on the data they upload. It is largely limited to singular data
  (single files).


### Use cases

> Link to specific use cases for which this user story is relevant, use cases should reside in the [use cases directory](../../use-cases/)

### Planning

> A rough planning for this epic. The GitHub Projects kanban board for this epic should be used for more detailed planning during development

### Resources

> Resources? I don't really know what goes here yet


