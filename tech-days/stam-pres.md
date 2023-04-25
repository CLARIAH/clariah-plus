# STAM: Stand-off Text Annotation Model

## Objective

1. We want to formulate a *simple* but *powerful* base model for text annotation,
   the model provides a foundation to efficiently encode all kinds of annotations on text.

    * *separation from semantics*: We want the base model to be agnostic with regard to vocabulary and annotation paradigm: 
    * *separation from syntax*: We want a simple format (JSON, CSV) to express the model (serialisation), but the model does not depend on any single serialisation.
    * *separation from implementation*: Although we aim for a complete reference implementation, the model itself should be formulated independently in a clear and simple specification.
    * *separation from dependencies*: We want a model that does not depend on further complex models. We do want to support 
      transformations to established models like RDF and W3C Web Annotations.
    * the core model is deliberately kept as minimal as necessary, extras are formulated as *extensions*.

## Objective (2)

2. We want a *reusable* implementation for working with annotations on text.
   On top of this more specific applications can be implemented. It should
   implement a wide variety of operations that are common on stand-off annotated text.

    * We want an *efficient* and *performant* implementation. Let's implement all the core logic once and as well as we can.
    * We do not want any heavy dependencies. The implementation should run on a wide variety of systems and be independent of any wider service infrastructure (including CLARIAH's!): It should not depend on any software services.
    * We want a programming library as well as simple command-line tools for basic operations. 

## Use-cases (1)

* As a researcher, You want a simple model to express annotation on text
    * you want complete freedom to use whatever vocabulary/annotation paradigm you see fit; either existing vocabularies or newly designed ones.
* As a researcher, you want to move from a simpler annotation model to a more formal model like web annotations -  STAM acts as a pivot model
* As a researcher/data scientist - You want to do low-level search on text and annotations without requiring complex infrastructure.
    * you want to find annotations based on relations like overlap, embedding, adjacency etc
    * you want to find annotations based on the content of the annotation
    * you want to find annotations based on text
    * you want to find/convert/compute offset information

## Use-cases (2)

* As a researcher/data scientist, you want to do basic low-level manipulation on text and annotations without requiring complex infrastructure
* As a researcher/data scientist, you want to quickly ingest annotation data from simple JSON, CSV formats.
* As a developer, you want a programming library that you can use to build an application handling stand-off annotation on text.
* As a development team, you don't want to implement similar base logic for annotations over an over again in different applications.
* As CLARIAH WP3, we want to facilitate conversion paths for CLARIAH formats like FoLiA XML and ubiquitous 3rd party formats like TEI, so they can be more comfortably used with other tools in the infrastructure that converge more towards stand-off annotation and linked open data.

## The Model

* An **Annotation** says something about a target that it *selects* and associates (one or more) **AnnotationData**.
* **AnnotationData** consists of a **DataKey** and a **DataValue**.
* The **DataKey** is a field in whatever vocabulary .
* The **DataValue** is typed (string, integer, etc...
* A **TextResource** holds a text.
* An **AnnotationDataSet** holds **DataKeys** and **AnnotationData**, it essentially represents a *vocabulary*. 
* An **AnnotationStore** holds **Annotations**, **AnnotationDataSets**, **TextResources**. It is essentially the *workspace*

The model is set up in such a way that there is as good as no
duplication/redundancy in the representation. Making it space-efficient to
implement.

## Limitations

* Current implementations are memory-based, i.e. scalability is limited to what fits in computer memory.

## Deliverables

**Specification** - <https://github.com/annotation/stam>

**Implementation:**

* *stam-rust*: Programming library for STAM for Rust (=compiles to machine code) - <https://github.com/annotation/stam-rust>
* *stam-python*: Python binding to the Rust library. Offers a slightly higher-level API more accessible for technical researchers - <https://github.com/annotation/stam-python>
* *stam-tools*:  Collection of command-line Interface tools for working with STAM - <https://github.com/annotation/stam-tools>

**Documentation:**

* stam-rust API reference - <https://docs.rs/stam>
* stam-python API reference - <https://stam-python.readthedocs.io>
* STAM Tutorial: Standoff Text Annotation for Pythonistas - An extensive tutorial showing how to work with this Python library, in the form of a Jupyter Notebook. - <https://github.com/annotation/stam-python/blob/master/tutorial.ipynb>
