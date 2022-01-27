---
#(This frontmatter block follows YAML syntax)
id: #epic-title-in-lowercase-with-hyphens
coordinator: #person or list of people
wp: [ 1, 2, 3, 4, 5, 6] #involved workpackages
github-projects-link: https://github.com/orgs/CLARIAH/projects?type=beta #link to a specific project under here
participants: [ ] #list of people
themes: [ Text, Audio, Visual, Geo, Metadata, Annotation, DevOps, Curation, Vocabularies, Sustainability, Monitoring, Publication, Processing, Search, UI-and-UX, Workflows ] #remove what is not relevant
evaluation: #overall evaluation for the (best) implementation of this epic
    trl: ? #technology readiness level
    cl: ? #compliance level
    srl: ? #stakeholder readiness level
---

## $Epic title

### Rationale

> Describe, from a high-level perspective, the rationale of what important role
> the service(s) that implement this epic fulfill in the CLARIAH infrastructure

### User Stories

> Describe, from a high-level scholarly perspective and in minimal and generic
> terms, the user stories that define this epic.  We recommend using sublists
> (i.e. a simple tree structure) for breaking down user stories into parts when
> needed.

1. **As a scholar, I** ... **in order to** ...

### Needs & Dependencies

> Describe organisational and technical dependencies that are crucial for the
> success of the implementation(s) for this epic.

### Requirements

> Describe software, infrastructure & interoperability requirements that arise
> from this epic or that are especially relevant. These must be formulated in
> further detail in the corresponding requirements documents.

### Service Description

> Describe the service(s) that implement(s) this epic, mention software
> components, data components and interoperability standards where appropriate.

### Components

> Describe the components and subcomponents involved in this epic in a simple
> tree form; specify whether the component is: a service (instance), software,
> data, and estimate a TRL. Please consult the
> [definitions](introduction.md#definitions) and [data
> model](introduction.md#data-model). In case of multiple implementations, use
> multiple detached trees/lists and add a level-4 heading for each.

* **Service Component:** **$Name**
    * **Provider**: (Institute that hosts the service)
    * **URL:** (URL to the instance)
    * **Function:** (Function/description of the component, may be repeated)
    * **Implements:** (the numbers of the user stories implemented)
    * **Interface**: (WebUI, REST, GraphQL, multiple options allowed)
    * **TRL**: ?
    * **SRL**: ?
    * **CL**: ?
    * **Software Component:** **$Name**
        * **Provider**: (Institute that maintains/develops the software)
        * **URL:** (URL to the source code repository, NOT to an instance!)
        * **Function:** (function of the software, may be repeated)
        * **Implements:** (the numbers of the user stories implemented)
        * **Interface**: (WebUI, WebAPI, API, CLI, GUI, GraphQL, multiple options allowed)
        * **TRL**: ?
        * **CL**: ?
        * **Data Component:** **$Name**
            * **Provider**: (Institute that provides the data)
            * **URL:** (Direct URL to where the data is provided, if possible)
            * **Function:** (Function/description of the component, may be repeated)
            * **TRL**: ?
            * **CL**: ?
    * **Interoperability Standard:** **$Name**
        * **Function:** (function/description of the component, may be repeated)
        * **URL:** (URL to the specification of the standard)

### Workflow Schema

> Draw a schema indicating how the various software and data components
> interact. This is required only when many components are involved and their
> connection is not immediately obvious.

### Evaluation

> Estimate the overall readiness of the implementation(s) for this epic in the
> frontmatter. You may add any additional evaluation here.

### Context

> Sketch the wider context of the implementations for this epic in relation to
> other (existing/proposed) projects and initiatives.

### Use cases

> Link to specific use cases for which this user story is relevant, use cases
> should reside in the [use cases directory](../../use-cases/)

### Planning

> A rough planning for this epic. The GitHub Projects kanban board for this epic
> should be used for more detailed planning during development

### Resources

> Resources? I don't really know what goes here yet


