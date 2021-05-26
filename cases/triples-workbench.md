# Storing, sharing, archiving, querying, browsing and visualizing triples 

## Metadata

* **Status:**  Proposed
* **Type:** Generic: institutes within NDE, CLARIAH-NL and specifically IISG, UVA UB and CLARIAH Vlaanderen
* **Work Package**: WP4
* **Research Coordinators:**  Richard Zijdeman
* **Coordinators for CLARIAH:**  
* **Participating Institutes:** UU, VU, IISG, DANS
* **End-users**: Researchers from various institutes, for example Ruben Schalk (UU), Micon Schorseij (IISG), Leon van Wissen (UvA)
* **Developers**: Laurens Rietveld for Druid (Triply), Menzo Windhouwer (HuC-DI) for Anansi, Slava Tykhonov (DANS) for LD Resolver (LDProxy)
* **Interest Groups**: Linked Open Data, UI/UX, Workflow
* **Task IDs**: ?

## Description
To create FAIR data, we transpose tables (datasets) into Linked Open Data. This helps to share and augment our data and enhances efficiency in data preparation.
After the creation we need a place to store the Linked Data (triples). The problem is manyfold:
- where to store our triples?
- how to interact with our triples?
	- create endpoints;
	- browse triples;
	- manage datasets visually;
	- store and save queries;
	- visually query output (as tables, graphs, maps, etc)


### What is the research about?
This use case applies to any question from social economic history that is based on LOD. For example on social inequality or migration. For an overview see these [datastories](https://stories.datalegend.net/).

### What problem is hindering the research?
There are several problems hindering the research:
- in itself Druid[https://druid.datalegend.net] fits the entire use case. However, the use itself costs money and if others than the IISG want to use Druid in large quantities, they would need to pay for it. Some partners are even willing to do that, but how would the financing work in relation to CLARIAH? (e.g. can institutes pay money to CLARIAH and CLARIAH upholds DRUID?)
- Anansi also stores triples, but I'm unsure to what extent it ticks the other boxes;
- Druid and Anansi were set up with different goals in mind (Druid the user-friendly data store) and Anansi as the all-encompassing CLARIAH data store), but currently it is unclear how they relate to each other and whether either of them can be sold as CLAAS services; 

### What is needed to do the research?
An answer to the questions under description. In other words, the answer to what CLARIAH offers as LOD services.


#### Data

For all datasets see [Druid](https://druid.datalegend.net). Currently 185 datasets, 22000 graphs, 1.3 billion unique triples and 100 endpoints. 	

#### Tools
To create triples we use [CoW](https://github.com/clariah/cow/), but any means to create triples is possible (e.g. [LDwizard](https://github.com/netwerk-digitaal-erfgoed/LDWizard), RML, python script). Except for LDWizard that provides the possibility for a token based login and storage to TriplyDB instances such as Druid. LDWizard has a modular architecture and one of the components, [LD Resolver](https://github.com/Dans-labs/ld-serverless-resolver) developed by DANS. The main purpose of LD Resolver is to archive and preserve concept URI in json-ld and resolve it back to the archived version if some URI isn't available online. 

Queries are preferably stored in [grlc](https://grlc.io) metadata format.

Visualisation of queries is handled via [Yasgui](https://github.com/YASGUI).

### What software and services are involved?
In addition to the software mentioned under 'Tools', there is a login procedure that for Druid is just for Druid. This could be part of the CLARIAH federated login service.

### How to evaluate this?
The use case is resolved once the questions under 'description' can be answered using CLARIAH software/services.

## References

References to related resources and publications and especially links to related use-cases:

* [CLARIAH](https://clariah.nl)
* [WP4 workflow](https://docs.google.com/document/d/1U_gHHm6np3IlKOih-VWYpuByHFCUrrpsNcnMxT127G8/edit?usp=sharing)
