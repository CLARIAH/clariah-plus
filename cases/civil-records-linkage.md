# Linkage of Dutch civil records (burgerLinker)

## Metadata

* **Status:**  In Progress
* **Type:** Specific
* **Work Package**: WP4
* **Participating Institutes:** International Institute of Social History (IISG) and Vrije Universiteit Amsterdam (VU)
* **Coordinators:**  Richard Zijdeman (IISG)
* **Developers**: Joe Raad (VU)
* **End-users**: The burgerLinker software is designed for the so called "digital historians" (e.g. someone with basic command line skills) who are interested in using the Dutch civil registries for their studies or linking their data to it.
* **Interest Groups**: [IG-LOD](https://github.com/CLARIAH/IG-LOD), [IG-Workflows](https://github.com/CLARIAH/IG-Workflows), and [IG-Curation](https://github.com/CLARIAH/IG-Curation)
<!-- * **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks) -->

## Description

### What is the research about?
Historians use archival records to describe persons' lives. Each record (e.g. a marriage record) just describes a point in time. Hence historians try to link multiple records on the same person to describe a life course. This tool focuses on "just" the linkage of civil records. By doing so, pedigrees of humans can be created over multiple generations for research on social inequality, especially in the part of health sciences where the focus is on gene-social contact interactions.

### What problem is hindering the research?
This tool is being developed to improve and replace the current [LINKS](https://iisg.amsterdam/en/hsn/projects/links) software. Points of improvement are:
- extremely fast and scalable matching procedure (using Levenshtein automata and HDT);
- considers all first names of individuals with multiple first names in order to find a candidate match;
- blocking is not required (i.e. all candidate records can be considered for matching, with no restrictions on their registration date or location, and no requirements on blocking parts of their individual names);
- detected links contains detailed provenance metadata, and can be saved in different formats (CSV and RDF are covered in the current version);
- allows family and life course reconstruction (by computing the transitive closure over all detected links);
- open software

<!-- ### What is needed to do the research?

(How can we go about solving this problem?) -->

### Data

In its current version, the tool cannot be used to match entities from just any source. The current tool is solely focused on the linkage of civil records, relying on the sanguineous relations on the civil record, modelled according to our [Civil Registries schema](https://druid.datalegend.net/LINKS/civ/). An overview of the Civil Registries schema is available in the [burgerLinker Wiki](https://github.com/CLARIAH/burgerLinker/wiki).

### Software

[LINKS source code and documentation](https://github.com/CLARIAH/burgerLinker)

<!-- (if known, describe what tools or functionalities you need to work with the data and do the research. Take the different stadia of the research into account, such as exploration phase, distant reading, close reading, annotating data, publishing, etc. Be as specific as possible) -->

<!-- ### What software and services are involved?

(if known, what existing software and services are involved, which need to be developed? Please link to the tools if possible and specify whether it can be used as is, needs extra work, needs to be developed from scratch etc.)

### How to evaluate this?

(How do we evaluate the solution to the problem?) -->

## References

References to related resources and publications and especially links to related use-cases:

* [Raad, J., Mourits, R., Rijpma, A., Schalk, R., Zijdeman, R., Mandemakers, K., & Meroño-Peñuela, A. (2020, October). Linking Dutch civil certificates. In 3rd Workshop on Humanities in the Semantic Web, WHiSe 2020 (pp. 47-58). CEUR-WS.](http://ceur-ws.org/Vol-2695/paper6.pdf)
