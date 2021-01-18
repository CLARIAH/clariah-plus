# Retrodigitization of Text-critical Editions

## Metadata

* **Status:** In Progress
* **Type:** Specific
* **Work Package**: WP3
* **Coordinators:** Piroska Lendvai (Bayerische Akademie der Wissenschaften) (external), Maarten van Gompel (for this
    use case in CLARIAH)
* **Participating Institutes:** Bayerische Akademie der Wissenschaften
* **End-users**: Bayerische Akademie der Wissenschaften
* **Developers**: Maarten van Gompel (HuC), Ko van der Sloot (retired), Martin
    Reynaert (UvT, incapacited)
* **Interest Groups**: Text
* **Task IDs**: T062 (FLAT), T108 (FoLiA), T098 (LaMachine), T139 (Frog & ucto)

## Description

### What is the research about?

The goal is to establish a pipeline to retrodigitize text-critical editions. We do not merely reproduce printed text
(which has a sort of linear reading logic), like e.g. the Deutches Textarchiv, but we need to represent complex edition
logic, thus one needs to treat rich typographic style and page-layout logic.

This will be initially applied to the Max Weber oeuvre, 50+ thick books containing German historical data from the 1910s, but is
more generic in set-up.

### What problem is hindering the research?

Bottlenecks in conversion; how to preserve as much information from the OCR output? and how to represent this
information? These bottlenecks depends greatly on what pipeline is chosen. They are investigated multiple options and
conversion pathways. The existing pipeline solution in PICCL is not adequate enough to preserve all data.

### What is needed to do the research?

#### Data

Needed is a data format capable of representing text structure, text markup as well as (linguistic) annotations. They are
looking at FoLiA to provide an integrated solution for this, so support is being provided as part of the normal FoLiA
support task (T108).

#### Tools

A proper pipeline to go from the scanned books to digitised versions is needed, retaining as much information as
possible, including information about text markup, structure and layout. This includes an OCR component, a
post-correction component, semantic transformation components with respect to text structures, and components capable of
visualising the output and allowing further annotation for manual post correction.

We are providing support for all the various FoLiA-based tools that may help them,
including a conversion from ABBY output to FoLiA by Ko van der Sloot,
who is still lending a helpful hand despite being retired now.

I do have to explicitly note that we can not provide proper PICCL support, as Ko is retired and the underlying TICCL-tools have no official maintainer anymore, and Martin is unfortunately ill.

### What software and services are involved?

* PICCL for automatic post-OCR correction (possibly).
* FoLiA as a storage format capable of representing both the structure of the text as well as linguistic annotations.
* The FoLiA tools and FoLiA utilities play an important role in offering conversions here.
* FLAT as a means of manual post-OCR correction (i.e. annotation), and visualisation.
* LaMachine is used as a research environment containing all these tools.


### How to evaluate this?

-

## References

Some of the specific issues that popped up thus-far, and have been mostly dealt with already:

* [Rendering problem in FLAT](https://github.com/proycon/flat/issues/166)
* [FLAT wat not yet able to visualise PICCL output properly](https://github.com/proycon/flat/issues/139)
* [Extend PICCL to work better with FLAT](https://github.com/LanguageMachines/PICCL/issues/62)
* [Error during spelling correction in FLAT](https://github.com/proycon/flat/issues/163)
* [An issue with text content representation in FoLiA](https://github.com/proycon/folia/issues/88)
* [Style annotation in FoLiA](https://github.com/proycon/folia/issues/90)
* [Request to extend folia2html with more style support](https://github.com/proycon/foliatools/issues/26)
* Enhance conversion from ABBY OCR output to FoLiA: [51](https://github.com/LanguageMachines/foliautils/issues/51),
[53](https://github.com/LanguageMachines/foliautils/issues/53), [54](https://github.com/LanguageMachines/foliautils/issues/54)
* [FoLiA-correct fails with text consistency error in PICCL](https://github.com/LanguageMachines/foliautils/issues/45)
* [Allow mixing metadata schemes in FoLiA](https://github.com/proycon/folia/issues/91)
