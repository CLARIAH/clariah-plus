# Syntactic Movement Annotation

## Metadata

* **Status:** Completed
* **Type:** Specific
* **Work Package**: WP3
* **Research Coordinators:** Alex Luu (Brandeis University)
* **Coordinators for CLARIAH:**  Maarten van Gompel (Radboud University, Nijmegen)
* **End-users**: Various annotators
* **Developers**: Maarten van Gompel
* **Interest Groups**: Text Processing
* **Task IDs**: T062 (FLAT), T108 (FoLiA)

## Description

### What is the research about?

A project regarding annotation on Syntactic Movement was conducted at Brandeis Univesity. An annotation environment was
needed to facilitate this and the researchers opted for FLAT.

### What problem is hindering the research?

* How to represent hidden/implicit words/tokens?
    * [FoLiA was augmented to support this](https://github.com/proycon/flat/issues/141)
* FLAT was not ready for full syntactic annotation yet; further implementations were needed
    * Tree visualisation needed to be improved
    * [FLAT needed support to annotate arbitrary relations](https://github.com/proycon/flat/issues/84)

### What software and services are involved?

* [FLAT](https://github.com/proycon/flat) - FoLiA Linguistic Annotation Tool
* [foliadocserve](https://github.com/proycon/foliadocserve) - Back-end for FLAT
* [FoliA](https://github.com/proycon/folia) - File format
* [foliapy](https://github.com/proycon/foliapy) - Python library for FoLiA

## References

References to related resources and publications and especially links to related use-cases:

* [FLAT issue #138: Add syntactic movement support](https://github.com/proycon/flat/issues/138)
