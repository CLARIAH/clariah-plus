# CMDI support at DANS Datastation
 
## Metadata
* **Status**: In progress
* **Type:** Specific
* **Work Package:** WP3
* **Coordinators:** Jerry de Vries (DANS)
* **Participating Institutes:** Data Archiving and Networked Services (DANS)
* **End-user:** Researchers searching for CLARIN datasets at the DANS datastation
* **Developers:** Vyacheslav Tykhonov (DANS)
* **Interestgroup:** Preservation
 
## Description
 
### What is the research about?
Exposing of CMDI metadata via a DANS service, by extracting metadata from stored CMDI files, transform it to a custom set of metadata and add the metadata to a newly to develop DANS Datastation. It can make the CLARIN data stored at DANS more visible at the Discovery Service of the Datastation. In order to archive this, Dataverse should be extended with CMDI metadata schema consisting of components with explicit semantics for the interoperability. As a final result, Dataverse instances should deliver a harvestable CLARIN metadata, which will be interoperable with CLARIN discovery services.
 
### What problem is hindering the research?
There is no core set of CMDI metadata fields defined yet as different CLARIN centers using their own CMDI metadata schema. The main goal is to build a pipeline to extract all metadata fields from CMDI files archived at DANS-EASY and automatically transform this metadata to the defined core set of CMDI metadata, and ingest as datasets in Dataverse. Every metadata field should be a part of some CMDI Component and linked to the CMDI Component Registry. Dataverse export functionality has to be extended with possibility to export deposited metadata back to CMDI format following the original specification. 

Another important problem – the use of FAIR controlled vocabularies for existing CMDI records. DANS is going to extend CMDI processing pipeline with some prediction mechanism making recommendations about possible controlled vocabularies and ontologies that could be used by data managers to improve the quality of CMDI metadata records. 
 
### What is needed to do the research?
CLARIN community should make an agreement of the Core set of CMDI metadata, to be added to the DANS Datastation metadata schema and linked manually to the CMDI Component Registry. DANS is working on the pipeline development to extract all metadata elements from the stored CMDI files at DANS-EASY and map them to the core set of metadata fields, and ingest to Dataverse. To make the ingestion process more consistent, transparent and reliable, Apache Airflow framework will be used to monitor every single step in the metadata conversion and ingest. We are also planning to use Semantic Bot to find and confirm semantic mappings in RML, and apply RMLMapper to convert CMDI datasets to RDF.
 
### Data
CMDI metadata files stored at DANS-EASY archive.
 
### Tools
ETL pipeline for extracting and transforming CMDI metadata fields will reuse the functionality of the Dataverse DDI Converter tool (python) with customized XSLT mappings. Semantic Bot (python), a Semi-Automatic Mapping Tool, will be used to generate RDF mappings for CMDI fields. Apache Airflow (python) framework in the part of the architecture to support all workflows, SKOSMOS python module used to query terms from controlled vocabularies. 
 
### What software and services are involved?
DANS data station API, using the to be developed pipeline for CMDI metadata extraction and transformation. SKOSMOS APIs and NDE's Network of Terms GraphQL endpoint will be used to make appropriate controlled vocabularies recommendations for the terms extracted from CMDI fields. All those fields should be linked to CMDI Component Registry in the CMDI metadata schema. 
Apache Superset will be used to visualize all relations between CMDI fields and external ontologies.
 
### How to evaluate this?
Export Dataverse datasets back to CMDI format and compare all fields with originally archived CMDI files. The quality of the created datasets could be automatically checked using F-UJI assestment tool. 
 
### References
* [Adding CMDI support in Dataverse (presentation)](https://www.slideshare.net/vty/clarin-cmdi-support-in-dataverse)
* [Clariah Tech Day: Controlled Vocabularies and Ontologies in Dataverse](https://www.slideshare.net/vty/clariah-tech-day-controlled-vocabularies-and-ontologies-in-dataverse) 
* [CMDI Component Registry](https://catalog.clarin.eu/ds/ComponentRegistry/#/)
* [BeFAIR networked services infrastructure](http://github.com/CoronaWhy/befair/)
* [Apache Airflow](https://airflow.apache.org)
* [Apache Superset](https://superset.apache.org)
* [SKOSMOS framework](http://skosmos.org)
* [Semantic Bot](https://github.com/opendatasoft/semantic-bot)
* [Dataverse DDI Converter tool](http://github.com/IQSS/dataverse-ddi-converter-tool)
* [Metadata & CMDI CLARIN Component Metadata Infrastructure](https://www.clarin.nl/sites/default/files/MetadataEnCMDI.pptx)
* [F-UJI, FAIRsFAIR Research Data Object Assessment Service](https://github.com/pangaea-data-publisher/fuji)
* [Web API for the RMLMapper](http://github.com/RMLio/rmlmapper-webapi-js/)

