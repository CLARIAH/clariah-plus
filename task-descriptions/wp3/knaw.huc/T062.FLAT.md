# FLAT

**ID:** T062

**Author:** Maarten van Gompel

**Introduction**:

The FoLiA Linguistic Annotation Tool (FLAT) is web-based annotation tool for linguistic annotation, based on the underlying FoLiA format. It is a collaborative and document-based annotation tool with support for a wide variety of linguistic annotation.

**What must be adapted / extended / created anew:**

There were various proposals for extended functionality, implementation of these is uncertain due to lack of
interest and allocated funding:
    * [flat#111](https://github.com/proycon/flat/issues/111) - The current interface for syntax editing and dependency editing may not be the most convenient for end users yet. We should investigate whether more visual interfaces (interacting more directly with the actual tree visualisation) can be constructed, and implement them.
    * [flat#113](https://github.com/proycon/flat/issues/113) - A dual-document view needs to be implemented in FLAT, currently it only has a single-document view. This would be needed to support annotation of parallel corpora  (3PM)
    * [flat#112](https://github.com/proycon/flat/issues/112) - User-friendly tools for researchers to compute inter-annotator agreement of arbitrary FoLiA annotations.
    * [flat#135](https://github.com/proycon/flat/issues/135) - Currently the front-end technologies used in FLAT are fairly old and basic (jquery+js+css), and not leveraging the power of modern frontend javascript frameworks (angular, reactjs, vuejs). For sake of maintainability and extensibility towards the future, a refactoring project to such a modern front-end is desirable.

First and foremost, this task focusses on maintenance and support stemming from actual user requests, which tends to
lead us in other directions than initially foreseen.

**Why important for CLARIAH?**

A web-based annotation tool was the missing chain in the FoliA ecosystem until several years ago. FLAT ensures FoLiA
documents can be visualised and annotated by human annotators. It has been used in multiple projects, including by
international partners outside CLARIAH/CLARIN.

**Targeted/Actual users:** Researchers

**Actual use (quantify!):**

We had an external party who is very interested in this functionality (see
[flat#138](https://github.com/proycon/flat/issues/138)). FLAT has also been used in the PARSEME project and spin-offs.
Other external parties sometimes take and adopt FLAT; such
requests take precedence when interest from within CLARIAH seems low.

**Lead:** Maarten van Gompel (DI, KNAW)

**Participants** Maarten van Gompel (DI, KNAW)

**Actually allocated PMs:** 6PM

## Deliverables

1. ``(T062D1)`` Software: [FLAT](https://github.com/proycon/flat)
    * ``(T062D1.1)`` Documentation: [Administration Guide](https://flat.readthedocs.io/en/latest/administration_guide.html)
    * ``(T062D1.2)`` Documentation: [User Guide](https://flat.readthedocs.io/en/latest/user_guide.html)
    * ``(T062D1.3)`` Documentation: [Installation Guide](https://flat.readthedocs.io/en/latest/installation_guide.html)
* ``(T062D2)`` Software: [foliadocserve](https://github.com/proycon/foliadocserve) - The backend for FLAT
* ``(T062D3)`` Service: [FLAT installation](https://flat.cls.ru.nl) at CLST, Radboud University, Nijmegen

## Milestones

No new milestones scheduled yet due to higher priorities and under-allocation on other tasks.

* ``(T062M1)`` - [FLAT v0.9.0](https://github.com/proycon/flat/milestone/16) - (September 2019, **COMPLETED**) This release introduces relation support and finishes support for syntactic movement.
    * [flat#138: Syntactic Movement Support](https://github.com/proycon/flat/issues/138) **(COMPLETED)**
    * [flat#84](https://github.com/proycon/flat/issues/84): Facilities for FoLiA relations have to be implemented **(COMPLETED)**

* Potential milestones that are currently dismissed:
    * [flat#111](https://github.com/proycon/flat/issues/111) - Improved syntax editing interface
    * [flat#113](https://github.com/proycon/flat/issues/113) - Dual-document view
    * [flat#112](https://github.com/proycon/flat/issues/112) - Inter-annotator agreement interface
    * [flat#135](https://github.com/proycon/flat/issues/135) - Complete refactoring and migration to a newer more modern
        frontend

## Progress Reports

Detailed progression of this task is logged as part of our [regular progress reports](https://github.com/LanguageMachines/releasereport/tree/master/reports) .

## Changes

* Since 14 July 2020 - This task has moved from CLST, Radboud University Nijmegen to Digital Infrastructure, Humanities
    Cluster, KNAW. A FLAT installation and supported at CLST.
* Merged this task with other FLAT tasks (T063,T064,Txx1,T096), the allocated PMs however only suffice for a subpart. I explicitly listed proposed enhancements that will probably **not** be implemented (unless priorities/funding changes)
* More explicit deliverables and milestones

## Related tasks

This task heavily depends on T108 FoLiA. It also relates to T096 LaMachine for distribution

