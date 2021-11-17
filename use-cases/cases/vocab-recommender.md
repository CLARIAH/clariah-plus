# Vocab Recommender

## Metadata

* **Status:**  In progress
* **Type:** Specific
* **Work Package**: WP4
* **Participating Institutes:** International Institute of Social History (IISG), Vrije Universiteit Amsterdam (VU), DANS, Triply
* **Coordinators:**  Richard Zijdeman (IISG), Auke Rijpma (UU/IISG), Joe Raad (IISG)
* **Developers**: Rosaline de Haan (Triply)
* **End-users**: The software is designed for the so called ‘digital’ historian: e.g. someone with basic command line skills.
* **Interest Groups**: IG-LOD, IG-Curation, and Worflows
<!-- * **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks) -->

## Description

### What is the research about?
Clariah provides tools to create (CoW, LDWizard) and explore/analyse linked data (Triple Workbench/Druid). However, to analyse the various linked data graphs, and above all to combine them to create new insights, it is important that they are described well, and that they share the same linked data vocabularies as much as possible. The proposed tool will help researchers make better, more informed choices in modeling their linked data.

### What problem is hindering the research?
Users, especially researchers with limited knowledge of linked data, do not know which vocabularies exist to model their data, which are commonly used in the field, and which are currently in use in the Clariah LD cloud. This makes it challenging for them to model their data efficiently in a way that is compatible with other data. On the basis of the column names and content of a csv-file, the Vocab Recommender should suggest vocabularies from datasets already present on the Triple Workbench, and from the social sciences and humanities through YALC, DANS' forthcoming version of YALC, and other sources.
 
### What is needed to do the research?

#### Data

Any CSV dataset is required as input, using UTF-8 encoding. RDF graphs on the Triple Workbench could also be used.

#### Tools


### What software and services are involved?

conversion tools in general, in particular
* The recommender should work with [COW](https://github.com/CLARIAH/COW)
* The recommender should work with [LD Wizard](https://github.com/netwerk-digitaal-erfgoed/LDWizard)
* [YALC](https://github.com/TriplyDB/YALC) provides vocabularies 
* DANS is developing a service that will expose vocabularies from the humanities and social sciences in the LD cloud.

### How to evaluate this?

Users with limited technical knowledge will be able to efficiently choose vocabularies to describe their dataset in a way that links up with best practice in the (Clariah) LD cloud.

## References
