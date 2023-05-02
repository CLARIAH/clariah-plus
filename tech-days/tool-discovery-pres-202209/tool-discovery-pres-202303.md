# CLARIAH Tool Discovery -- The Role of Registries and CLARIAH's development strategy

## Introduction

* We have built a registry that contains **software metadata**
    * Provides essential information for scholars to *find* tools suitable for their needs
    * Can function as the data provider for other portals (e.g. Ineo)
* This registry information for *all tools* developed in CLARIAH
    * Aimed to be *complete*
    * Tools is broad concept and includes all software and software services
* Information **automatically harvested** from the source

## Strategy (1/2)

1. Ensure we always have **up-to-date** and **complete** overview of all tools produced in CLARIAH
    * Developers know best how to describe their software *alongside their source code*; full agency; no man-in-the-middle
    * Periodic and **automatic harvesting** of software metadata *from the source*
    * Accommodate *existing* software metadata practises, map them to a *uniform vocabulary*.
    * Strong requirements to CLARIAH participants to include all their software to guarantee *completeness*

![Harvester and Converter](../tool-discovery-pres-202203/converter.png)

## Strategy (2/2)

2. How to **identify** which tools are suitable for a scholar's needs?
    * To make this decision, metadata must be accurately reflect various aspects of the software.
    * We provide a uniform way of describing this metadata as Linked Open Data (and require this from developers)
    * User must be given the ability to search on arbitrary metadata (e.g. faceted search)
    * Software must comply to certain software requirements ensuring a certain quality. 
    * We can automatically test compliance (to a limited degree) and communicate to the user whether these are met.

## Technologies

* Full linked-open-data; SPARQL endpoint
* Builds upon codemeta and schema.org vocabularies
* Harvester automatically converts from various existing industry-standard vocabularies that are already used in the field
* Extended with some additional vocabularies

## Current state of the project (March 2023)

1. Harvester pipeline, converter and tool store are all ready and operational
    * See <https://tools.clariah.nl>
    * Bug fixes and harvester improvements are always ongoing
    * You should gradually see the quality improve
2. All CLARIAH tool providers are requested to **check** and **improve** their metadata
    * Have you as developer provided sufficient metadata?
    * Are you complying to the guidelines?
    * Has the automatic harvester done a good enough job?
    * Some major CLARIAH tools are missing still or have poor metadata
3. Work on **integration** with portals
    * *CLARIN VLO:* Codemeta to CMDI conversion and inclusion in their OAI harvester
      (Menzo Windhouwer & Meindert Kroese) 
    * *Ineo:* to be requested from the Ineo developers
    * *CLARIN Switchboard*: to investigate & implement
    * *SSHOC Marketplace*: to investigate

## Conclusion

In summary; the role of our registry and our strategy:

1. Ensure software producers need to specify their metadata *only once* and reuse *their* existing sources as much as possible
2. Establish a single well-documented unified vocabulary for our software metadata needs; automatically convert to that from other industry standards
    * Fully embrace Linked Open Data as a standard
    * Use existing initiatives like codemeta and schema.org and build on them
    * Documented in the [Software Metadata Requirements](https://github.com/CLARIAH/clariah-plus/blob/main/requirements/software-metadata-requirements.md).
3. Short automatic update cycles (harvesting at regular intervals) to ensure everything is *up-to-date*
4. Provide an API (SPARQL) for interoperability with other tools (e.g. Ineo)

