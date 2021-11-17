# Annotation of spelling correction for CLIN28 Shared Task

## Metadata

* **Status:* Completed
* **Type:** Specific
* **Work Package**: WP3
* **Research Coordinators:** Merijn Beeksma
* **Coordinators for CLARIAH:**  Maarten van Gompel
* **Participating Institutes:** Radboud University, Nijmegen
* **End-users**: The CLIN28 shared-task organisers
* **Developers**: The CLIN28 shared-task organisers
* **Interest Groups**: Text
* **Task IDs**: T062 (FLAT), T108 (FoLiA)

## Description

A gold-standard corpus with spelling errors and corrections thereof needed to be established for the [CLIN28 Shared
Task](https://github.com/LanguageMachines/CLIN28_ST_spelling_correction) (2018).

### What is the research about?

The efficacy of spelling correction systems by shared task participants was to be assessed. An annotation
environment was needed so annotators could establish a gold standard.

### What problem is hindering the research?

(What is currently lacking that inhibits this research?)

### What is needed to do the research?

#### Data

Data was extracted from Wikipedia and stored in the FoLiA format.

#### Tools

We need an annotation environment with support for spelling correction in many forms, including complexities such as run-on
errors, split-errors, missing words and redundant words. FLAT was used as a solution, as it, and the underlying FoLiA
format, has significant correction spelling correction features.

### What software and services are involved?

* [FLAT](https://github.com/proycon/flat)
* [FoLiA](https://github.com/proycon/folia)

## References

References to related resources and publications and especially links to related use-cases:

* [CLIN28 Shared Task: Spelling Correction](https://github.com/LanguageMachines/CLIN28_ST_spelling_correction)
* Beeksma et al (2018) - [Detecting and correcting spelling errors in high-quality Dutch Wikipedia text](https://clinjournal.org/clinj/article/view/83). CLIN Journal

