---
#(This frontmatter block follows YAML syntax)
id: distribution-and-deployment #epic-title-in-lowercase-with-hyphens
coordinator:
    - Maarten van Gompel
    - Mario Mieldijk
wp: [ 1, 2, 3, 4, 5, 6] #involved workpackages
github-projects-link: https://github.com/orgs/CLARIAH/projects/5 #link to a specific project under here
participants:
    - Maarten van Gompel (KNAW HuC)
    - Mario Mieldijk (KNAW HuC)
    - David de Boer (NDE)
    - Jaap Blom (NIBG)
    - Martijn van de Donk (NIBG)
themes: [ DevOps, Sustainability, Processing ]
evaluation: #overall evaluation for the (best) implementation of this epic
    trl: 0 #technology readiness level
    cl: 0 #compliance level
    srl: 0 #stakeholder readiness level
---

## FAIR Distribution and Deployment

### Rationale

> Describe, from a high-level perspective, the rationale of what important role
> the service(s) that implement this epic fulfill in the CLARIAH infrastructure

Making data and tools available, and facilitating the interplay between them, is at the heart of CLARIAH. In order to
make tools available to either end-users or hosting partners they need to be distributed in a certain standardized way. When
distributed properly, they can be deployed as part of a larger infrastructure, interconnecting with other software
components and data collections.

Different scholarly use-cases and differently skilled audiences may require different ways of distribution and
deployment. Relevant factors are the kind of interfaces that are needed, the scale at which the application will be
used, security/privacy concerns surrounding data.

This epic addresses typical DevOps aspects, in which scalability is one that receives particular focus.

### User Stories

> Describe, from a high-level scholarly perspective and in minimal and generic terms, the user stories that define this epic.
> We recommend using sublists (i.e. a simple tree structure) for breaking down user stories into parts when needed.

* **As a scholar, I** want to apply a processing tool on a (possibly large) data set in the CLARIAH infrastructure, either using computational resources provided by the CLARIAH infrastructure in order to be able to do quick and efficient processing on (large) data sets without needing my own infrastructure.

* **As a scholar, I** want to apply a processing tool on a large data set *within my own infrastructure* in order to take the tools to my (possibly restricted) data and work in my own secure environment.

* **As a scholar, I** expect to have access to low-level CLARIAH tools in industry-standard ways **in order to**
  use the tools in my own development setting.

### Needs & Dependencies

> Describe organisational and technical dependencies that are crucial for the success of this service.

* Compliance to the software/infrastructure requirements as described in the next section

### Requirements

> Describe software, infrastructure & interoperability requirements that arise from this service or that are especially relevant for this service. These must be formulated in further detail in the corresponding requirements documents.

The vast majority of the [software and infrastructure requirements](../../requirements/README.md) relate to this epic.

### Service Description

> Describe the service(s) that implement(s) this epic, mention software components, data components and interoperability standards where appropriate.

This epic first of all results in clear [software and infrastructure requirements](../../requirements/README.md),
that formulate how CLARIAH developers should package, publish software and how CLARIAH infrastructure operators can be
deploy these in their infrastructure. WE aim to align with existing industry-standards and best practises.

This resulting service can be seen as a broad Infrastructure-as-a-Service setup that provides computing, network and
storage resources for CLARIAH, this includes components for monitoring, continuous integration/deployment,
authentication, automated security checks. This is a broad scope of provisioning services that and implementation of
this is in the realm of CLARIAH WP2. This focus of the current epic is rather on coordinating, developing and
communicating these requirements cross-WP and cross-institute.

Particular extra focus of this epic is scalability of processing-tools (e.g. NLP tools). Solutions to facilitate such
scalabity may also emerge as part of this epic, i.e. instructions/recommendations for operating workflow systems like DANE or
NextFlow.

For software/service metadata, we defer to the Tool Discovery service.

### Components

> Describe the components and subcomponents involved in this epic in a simple tree form; specify whether the component
> is: a service (instance), software, data, and estimate a TRL. Please consult the
> [definitions](introduction.md#definitions) and [data model](introduction.md#data-model). In case of multiple
> implementations, use multiple detached trees/lists and add a level four heading for each.

### Workflow Schema

> Draw a schema indicating how the various software and data components interact. This is required only when many
> components are involved and their connection is not immediately obvious.

### Context

> Sketch the wider context of the implementations for this epic in relation to other (existing/proposed) projects and initiatives.

This epic is directly related to a lot of the existing efforts in CLARIAH WP2.

* **Service Component:** **CLARIAH Docker Registry**

### Use cases

> Link to specific use cases for which this user story is relevant, use cases should reside in the [use cases directory](../../use-cases/)

### Planning

> A rough planning for this epic. The GitHub Projects kanban board for this epic should be used for more detailed planning during development

### Resources

Mostly covered by existing WP2 funding?
