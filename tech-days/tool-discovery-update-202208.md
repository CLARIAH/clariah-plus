# CLARIAH Tool Discovery: Progress update

## Vocabularies (1/2)

Work in collaboration with external party (Daniel Garijo, Universidad Politécnica de Madrid):

* **Software Types vocabulary**: Defines additional software interface types (e.g. `SoftwareLibrary`, `CommandLineApplication`)
* **Software IO Data vocabulary**: Defines `consumesData` and `producesData` properties to tie input/output formats to software metadata.

Formulated in a way that it can be easily merged into codemeta/schema.org with minimal extra vocabulary.

## Vocabularies (2/2)

CLARIAH-specific vocabularies:

* **Technology Readiness Levels** (PR[98](https://github.com/CLARIAH/clariah-plus/issues/98)): Proposed awaiting approval
* Still undecided points (issue [32](https://github.com/CLARIAH/clariah-plus/issues/32)):
    * vocabulary for research subjects/activities (Tadirah?)
    * vocabulary for research domains (NWO?)
    * vocabulary for research phases
    * If no formal ontologies exist yet, they must be created.

## Software Metadata Requirements

Document: https://github.com/CLARIAH/clariah-plus/blob/main/requirements/software-metadata-requirements.md

* Precisely defines what software metadata *MUST*, *SHOULD* or  *MAY* be
  provided and in what the eventual form expressed in codemeta/schema.org
  will be.
* Serves as reference and documentation for any software provider in CLARIAH
* Points are often corollaries of points in the [Software Requirements](https://github.com/CLARIAH/clariah-plus/blob/main/requirements/software-requirements.md)
* Keep in mind that automatic harvesting will already take care of a lot

## Software Stack

* [codemetapy](https://github.com/proycon/codemetapy)
* [codemeta-harvester](https://github.com/proycon/codemeta-harvester)
* [codemeta-server](https://github.com/proycon/codemeta-server)
* [CLARIAH tool discovery & source registry](https://github.com/CLARIAH/tool-discovery)

* Various fixes and improvements
* Signs of community interest; significant contributions from external contributor

## Validation

* Validation schema for software metadata (SHACL), with David de Boer
* Automatic validation upon harvesting
* Automatic **validation report** with feedback on your metadata, formulated according to the Software Metadata Requirements.
* Rating for your metadata (0 to 5 stars), presented in the Tool Store

## Call to Action / Request for Comment

* **ALL** CLARIAH software must be registered in the source registry (very simple procedure). Is yours already?
* Feedback on Software Metadata Requirements much appreciated!
* Contributions in the vocabulary discussions welcome! (issue [32](https://github.com/CLARIAH/clariah-plus/issues/32))
* Second opinions from linked data experts welcome
