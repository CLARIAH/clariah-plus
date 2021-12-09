---
#(This frontmatter block follows YAML syntax)
id: fair-datasets #epic-title-in-lowercase-with-hyphens
coordinator: TODO #person or list of people
wp: [ 1, 2, 3, 4, 5, 6] #involved workpackages
github-projects-link: https://github.com/orgs/CLARIAH/projects/2 #link to a specific project under here
participants:
    - Willem Melder (NISV)
    - Jaap Blom (NISV)
    - tbd
themes: [ Datasets, Linked Data, Metadata, DevOps, Search, Sustainability]
evaluation: #overall evaluation for the (best) implementation of this epic
    trl: 0 #technology readiness level
    cl: 0 #compliance level
    srl: 0 #stakeholder readiness level
---

## FAIR Datasets

### Rationale

> Describe, from a high-level perspective, the rationale of what important role
> the service(s) that implement this epic fulfill in the CLARIAH infrastructure

Providing a view on datasets that could be of interest for scholarly research on a national level at research institutes or heritage institutes, is a core functionality of a research infrastructure. At least, potential  should be “findable” and provide scholars with information on the contents of the data. In addition to making datasets findable, within CLARIAH we want to stimulate access to these collections and increase the levels of interoperability for reuse. The aim is to create a CLARIAH “dataset registry” (e.g., operated via Ineo) that requires entries to be findable, accessible, interoperable (formats, schema’s) and reusable (persistent) within the CLARIAH infrastructure. As such, the FAIR Datasets service also includes work on making individual datasets accessible/interoperable/reusable via domain services, e.g., end-points/apis (sparql/search-api) or domain portals (Media Suite, Linguistic corpus search, Nederlab), but also a shared service such as Data Stories.

The goal of this epic is to enable FAIR use of datasets within CLARIAH: a central data set discovery (provided by DCAT or schema.org formatted metadata on the dataset level, e.g. using CKAN as dataset registry), searching within data sets via domain services, accessing data sets via endpoints either on domain level or via a central facility, with persistent identifiers. Practically speaking, we would like to "migrate" from for example the CKAN registry that was implemented in WP5 (Media Suite) as a domain registry service, to a central registry service and make an inventory of additional central services that are needed to enable FAIR use of the datasets.


### User Stories

> Describe, from a high-level scholarly perspective and in minimal and generic terms, the user stories that define this epic.
> We recommend using sublists (i.e. a simple tree structure) for breaking down user stories into parts when needed.

**As a scholar**, I want to have an overview of datasets providing me with information from collection metadata, including the dataset’s distribution (e.g. SPARQL endpoint, full text search API endpoint, RDF or CSV data dump file) where the dataset is distributed, the organization that publishes the dataset and the license under which it is published, **in order to** select interesting data sets for my research and access them either via domain portals or central services, by downloading the content myself, or by visiting an organisation.

### Needs & Dependencies

> Describe organisational and technical dependencies that are crucial for the success of this service.

* Make datasets findable (metadata) via a Data Registry (linked to INEO)
* Make datasets accessible (resource) via domain portals (Media Suite, Linguistic Corpus Search, Nederlab, etc.) 
* Stimulate interoperability and reusability via requirements for the registry using a “star model” (Data Readiness Level)
* Cross-WP agreement on the dataset metadata model (e.g. DCAT)
* Cross-WP agreement on the dataset registry software to be promoted and used

### Requirements

> Describe software, infrastructure & interoperability requirements that arise from this service or that are especially relevant for this service. These must be formulated in further detail in the corresponding requirements documents.

* Dataset registries MUST define CodeMeta software metadata along with the source code
* Registered datasets SHOULD include a link to a publicly accessible API
* TODO
* TODO

### Service Description

> Describe the service(s) that implement(s) this epic, mention software components, data components and interoperability standards where appropriate.

TODO

### Components

> Describe the components and subcomponents involved in this epic in a simple tree form; specify whether the component
> is: a service (instance), software, data, and estimate a TRL. Please consult the
> [definitions](introduction.md#definitions) and [data model](introduction.md#data-model). In case of multiple
> implementations, use multiple detached trees/lists and add a level four heading for each.


### Workflow Schema

> Draw a schema indicating how the various software and data components interact. This is required only when many
> components are involved and their connection is not immediately obvious.

### Evaluation

> Estimate the overall readiness of the implementation(s) for this epic in the frontmatter. You may add any additional
> evaluation here.

### Context

> Sketch the wider context of the implementations for this epic in relation to other (existing/proposed) projects and initiatives.

* Use existing knowledge & code (VLO, NDE register, ODISSEI data registry, EOSC)
* Align with existing metadata curation activities (WP3, WP5, MPI, RU, DANS)


### Use cases

> Link to specific use cases for which this user story is relevant, use cases should reside in the [use cases directory](../../use-cases/)

### Planning

> A rough planning for this epic. The GitHub Projects kanban board for this epic should be used for more detailed planning during development

See [FAIR Datasets Planning](https://github.com/orgs/CLARIAH/projects/2/)

### Resources

> Resources? I don't really know what goes here yet


