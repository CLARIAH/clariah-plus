# WP6 Use Case 005 Lossless Text Data Exchange

## Metadata

* **Status:**  Proposed
* **Type:** Specific/Generic (is this a specific use-case, with identifiable end-users, or a more generic use case?)
* **Work Package**: WP6
* **Research Coordinators:**  (who is coordinating the research? If decided)
* **Coordinators for CLARIAH:**  
* **Participating Institutes:** (what institutes are participating in handling this use case?)
* **End-users**: (Who is involved as end-user for this use-case? Try to mention name, institute, role/responsibility)
* **Developers**: Dirk Roorda, ....
* **Interest Groups**: (a list of CLARIAH interest groups, such as Text and DevOps, for which this use case may be relevant. See the list of IG's at: https://github.com/clariah/ig/.
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

A long standing problem is the lack of a academically wide accepted standard to address arbitrary parts of “a text”. This is a thorny problem as perspectives on what “the text” is, vary from researcher to researcher and from context to context. The problem is aggravated by the fact that it is common research practice and pragmatism to remove existing annotation data from digital texts and to add new annotation layers without concern for annotation and text legacy. Also many domain specific communities and projects (e.g. W3C web annotation, TEI, LAF, FOLIA, The Codex, TAG-ML to name but a few) have proposed pragmatic but very different standards to link annotations to parts of texts. 

These practices are defendable on the basis of specific research aims, but questionable with regard to uniquely identifiable and addressable text data, information, and annotation. Ideally we would have a common text coordinate system that is community standard agnostic and that may thus allow seamless transformation from one community specific standard to another. Or there might be a Pandoc (https://pandoc.org/) like solution, but one that guarantees information-losslessness. Alternatively a blockchain like solution might turn out to be the most practical and pragmatic solution.

In Work Package 6 “Text” of the CLARIAH-PLUS project one goal is to investigate different solutions for this problem and to what extent they could be integrated and advocated through CLARIAH-PLUS infrastructure. Solutions (non-exhaustively listed here) that may be explored are “turntable”, “blockchain”, and “common coordinates” solutions.


### What is the research about?

(mention the research project, the research domain, e.g., linguistics or media studies, and research question if relevant)

### What problem is hindering the research?

(What is currently lacking that inhibits this research?)

### What is needed to do the research?

(How can we go about solving this problem?)

#### Data

* The General Missives (for which Dirk already has produced much cleaner data than existed, which is already in Text-Fabric). The General Missives are the subject of WP6-Use Case 1

* The NENA corpus (https://github.com/CambridgeSemiticsLab/nena ), a native speaker corpus of Neo-Aramaic, phonologically marked up. It is already in Text-Fabric, it is a growing corpus under development, and Dirk is paid by Cambridge to provide it with a search interface. Blacklab seems to be a good first shot, but probably we do need add-ons.

* The Fusus corpus (https://github.com/among/fusus). An Arabic corpus which is being developed by Dirk and Cornelis van Lit (https://github.com/among/digitized-manuscripts Univ. Utrecht). It consists of commentary texts on a classic mystico-philosophical work by Ibn Arabi. We are working from printed pages, do OCR, and preserve the outcome in Text-Fabric. Cornelis will do data oriented research on it, but in order to cater for a wider public, a blacklab like interface is desirable. Dirk is paid by Utrecht to produce this corpus.

* The Hebrew Bible. The BHSA (https://github.com/ETCBC/bhsa) is a mature text-fabric representation of the Biblia Hebraica Stuttgartensia and is used in Biblical research. Recently Martijn Naaijer got his Ph.D. cum laude for his thesis in which he applies machine learning to rank the books of the bible in time. The BHSA is online through SHEBANQ, a DANS service built for CLARIN, which is in continued use for research and education. In order to explore alternative interfaces, it would be welcome to have the BHSA available in a Blacklab interface. Even better, the Dead Sea Scrolls (https://github.com/ETCBC/dss), which overlap with the BHSA but date from much earlier, are a case in point where focused linguistic annotations on one source are being transferred to another source.


#### Tools

(if known, describe what tools or functionalities you need to work with the data and do the research. Take the different stadia of the research into account, such as exploration phase, distant reading, close reading, annotating data, publishing, etc. Be as specific as possible)

### What software and services are involved?

(if known, what existing software and services are involved, which need to be developed? Please link to the tools if possible and specify whether it can be used as is, needs extra work, needs to be developed from scratch etc.)

### How to evaluate this?

(How do we evaluate the solution to the problem?)

## References

References to related resources and publications and especially links to related use-cases:

* [CLARIAH](https://clariah.nl)

