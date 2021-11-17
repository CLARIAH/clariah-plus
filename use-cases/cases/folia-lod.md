# Interoperability Integrated Text Annotation and Linked Open Data

## Metadata

* **Status:**  Proposed
* **Type:** Generic
* **Work Package**: WP3, WP6
* **Research Coordinators:** Maarten van Gompel
* **Coordinators for CLARIAH:**  (who is coordinating this use case for CLARIAH? If decided)
* **Participating Institutes:** HuC
* **End-users**: (Who is involved as end-user for this use-case? Try to mention name, institute, role/responsibility)
* **Developers**: Maarten van Gompel
* **Interest Groups**: Ann, Text, LoD
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

There is an ongoing a trend towards the use of linked open data in and around CLARIAH and towards decentralised
infrastructures in which annotations and the objects that are being annotated can be distributed widely over
the web, using for instance standards such as [web annotation](https://www.w3.org/TR/annotation-model/).

On the other hand, there have been many years of development going into something that can be seen as largely going in
the opposite direction. [FoLiA](https://proycon.github.io/folia/) takes a very integrated approach where a FoLiA XML
document describes in detail the text (the object of annotation) along with all its (textual and linguistic) annotations. Formats
like TEI, TCF (CLARIN-D) and NAF take a similar approach.

There are advantages and disadvantages to each of the paradigms and their is merit in both.  A decentralised approach
often brings challenges with regard to versioning (annotation and annotation object have be clearly versioned if they
are to remain in sync) and demands a networked infrastucture with annotation storages and query services in place. The
integrated approach suffers from being less flexible to extend with ad-hoc annotations and is less suited for a fully distributed
workflow. It does have the advantage tof being more easily usable in off-line scenarios and providing a complete picture
of the data without querying further sources.

Both approaches require specialised tooling to operate.

FoLiA defines a strictly defined vocabulary of (linguistic and other) annotation types, text structure types and other.
It does leave the actual vocabularies (linguistic categories etc) that are used FOR annotation completely open to the
user to define as Linked Open Data (SKOS in this case), so in this sense there is already a distributed component. There
are also ample other facilities to refer from a FoLiA document to external sources. But still, at its core it proposes a
single document-based, multiple annotation layer paradigm with a certain degree of inspectability if the user were to
simply look at the XML without further tooling.

### What problem is hindering the research?

Researchers need to be as free as possible to move between different ecosystems and use the tooling that is designed for
these ecosystems. There is currently insufficient tooling to convert between these.

### What is needed to do the research?

This use case focuses on FoLiA, which needs to become a first-class citizen in the Linked Open Data world and its
structure defined as Linked Open Data, and by extension, data in FoLiA convertable to RDF, possibly to web annotations
in particular if that is the dominant solution. The reverse also holds true, Linked Open Data using (or mappable to)
FoLiA's ontology, needs to be convertable back to a simple integrated XML document so that the FoLiA-based tooling
developed in CLARIN/CLARIAH can operate on it.

#### Tools

* Data conversion tools have to be written to convert from FoLiA's XML serialisation to a FoLiA RDF representation, and vice
versa, from a FoLiA RDF representation back to the XML serialisation. Web annotations could serve as the underlying
paradigm for the annotations.
* FoLiA's RDF vocabulary needs to be mapped to existing initiatives, especially those used in CLARIAH.

* FoLiA-tools
* untanggle (developed at HuC) could play a role here


## References

Related issues:
* [Generate RDF/OWL ontology of FoLiA](https://github.com/proycon/folia/issues/4)
* [Interoperability with Salt, Pepper and ANNIS](https://github.com/proycon/folia/issues/85)

Related use cases:
* [WP6 Use Case 005 Lossless Text Data Exchange](https://github.com/CLARIAH/usecases/blob/master/cases/wp6-use-case-5-lossless.md)
* [Data format for various linguistically-annotated corpora](folia-corpora.md)
* [Store, share and search web annotations](web-annotation-services.md)

