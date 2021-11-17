# Wp6 Use case 3: Tools to data

## Metadata

* **Status:**  In Progress
* **Type:** Specific/Generic (is this a specific use-case, with identifiable end-users, or a more generic use case?)
* **Work Package**: WP6
* **Research Coordinators:**  (who is coordinating the research? If decided)
* **Coordinators for CLARIAH:**  (who is coordinating this use case for CLARIAH? If decided)
* **Participating Institutes:** (what institutes are participating in handling this use case?)
* **End-users**: (Who is involved as end-user for this use-case? Try to mention name, institute, role/responsibility)
* **Developers**: (Who is involved in implementing this use-case (if any)? Try to mention name, institute, role/responsibility)
* **Interest Groups**: (a list of CLARIAH interest groups, such as Text and DevOps, for which this use case may be relevant. See the list of IG's at: https://github.com/clariah/ig/.
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

For some time now, researchers and content experts of the Koninklijke Bibliotheek (KB) have been wanting to realise digital access for text- and data-mining-based research on digital and digitised sources in the collections of the KB, without the need to copy the collection to the user. In short, the idea is that a researcher can query the textual content of selections from the collections in the Digital Repository (DM) of the KB by API, by graphical interface or by "kerend algorithm", and receive as a result vocabulary, word frequencies, "word embeddings" or the result of the algorithm.

### Purpose
The purpose of the use case is to investigate the possibilities of such an environment using KB collections, with as one of the results a proof of concept that can be fitted into CLAAS.

This use case aims to deliver the following:

* Descriptions of the foreseen users and their issues
* Requirements developed from a researcher/user perspective by means of extensive user testing
* Insight into the possibilities of making (copyright protected) collections available from the KB:
 * in relation to general policy choices
 * in relation to the Digital Repository
* Insight into the legal (im)possibilities
* Infrastructural requirements/possibilities according to CLAAS (theory)
* Proof of concept environment in cooperation with WP2-CLAAS with various possibilities such as;
 * Selection mechanism to compile collections based on metadata and/or full text
 * Reliable EPUB parser for (on demand) conversion of EPUB to plain text
 * Services to parse and metadata plain text for:
   * Tokens, types
   * Type frequencies
   * n-grams
   * Embeddings
   * Lemma
   * Context
   * Syntactic function
 * API for above
 * Jupyter Notebook-like interface/access
 * Graphical shell for above
* Recommendations for the development of a production version that fits within CLARIAH+ and the KB infrastructure

At the end of the use case we will have as much knowledge as possible about this new way of making (copyright protected) collections available, we will know what the user requirements are for the proposed service and we will have a proof of concept on which we can build further.


### What is the research about?

Two research cases are planned, one is already selected, the other case is still to be determined. The former case is about 'bringing' software that automatically finds and analyses correlations between word usage in bestsellers and high sales volumes in dutch literature 'to the data'.

### What problem is hindering the research?

Currently, with data-to-tools scenarios, there are at least three important problems for collection providers:

1. data proliferation: many different versions of collection data exist at many places, without proper data about provenance.
2. rights issues: for substantial parts of digital collections there are restrictions on availability because of copyright.
3. the collection provider does not benefit from enrichments of collection data by external researchers.

### What is needed to do the research?

#### Data

(if known, describe the data that are needed for the intended research, be as specific as possible)

- born digital publications of the KB in different formats (in a.o. PDF and ePub format)
- parts of the DBNL collection (in TEI format)

#### Tools

(if known, describe what tools or functionalities you need to work with the data and do the research. Take the different stadia of the research into account, such as exploration phase, distant reading, close reading, annotating data, publishing, etc. Be as specific as possible)

### What software and services are involved?

Surf Data Exchange platform
https://www.surf.nl/data-exchange-vertrouwd-data-delen:
‘Data-aanbieders zoals bedrijven of academische ziekenhuizen willen hun data wel beschikbaar stellen voor onderzoek, maar willen zelf in de hand houden wie de data gebruikt en waarvoor. Ook moet voldaan worden aan wettelijke eisen op het gebied van persoonsgebonden gegevens. SURF heeft een prototype gebouwd van een platform waarop data kunnen worden gedeeld zonder de controle over of de vertrouwelijkheid van de data te verliezen.’

### How to evaluate this?

(How do we evaluate the solution to the problem?)

## References

References to related resources and publications and especially links to related use-cases:

* [CLARIAH](https://clariah.nl)

