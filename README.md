# CLARIAH Interest Group on Workflows

This repository is intended to organize the work, output and documentation of the CLARIAH Interest Group (IG) on
Workflows.

## Introduction

WP2 works to facilitate modular distributed workflows that bring together components
developed within and outside of CLARIAH to facilitate the different steps of research
processes. Workflows used in WP3, WP4, WP5 and WP6 contain potential
components at all levels. This Interest Group has a strong connection to IG 1
(DevOps), which focuses on toolchains that support workflows.

### Defining workflows

We can define a worfklow as connection of two or more sofware components (in a directed acyclic graph) for a specific
purpose.  We can make a distinction between fully automated workflows, which is the main focus of this group, and those
that require user-interaction.

Possible characteristics of workflow systems (not all need apply):

- **Scheduling**: Determining which sequence of tasks leads to the desired end result
- **Execution**: Execution of tasks, possibly with automatic parallellisation/abstraction
    - Abstraction of pipeline logic from execution layer: local execution, computing cluster, cloud platform
- **Monitoring**: Real-time monitoring of a running workflow and ability to inspect logs on failure
- **Correction**: Ability to resume the workflow after failure and manual intervention; and/or automated fallbacks
- **Reproducibility**: Given the same input, the workflow should ideally produce the same output every time
    - This requires solutions for software deployment and versioning and is mostly in the realm of the DevOps Interest Group.
    - Handling of provenance data
- **Discovery**: automated discovery of possible workflows
- **Interaction**: Human intervention (steering/inspection/visualisation) in at specific points in a workflow
- **Specification**: How are the workflow specified? (e.g. in what language(s)). The specification can be very specific (e.g a shell script on one extreme of the spectrum) or can be completely abstracted from the executioner (Common Workflow Language (CWL) on the other end of the spectrum).

There are various paradigms for workflow systems and very layers of complexity, a simple shell script or Makefile can already be
considered a basic form of a workflow.

- **goal oriented** (GNU Make, luigi, snakemake, Airflow)
- **procedural** (shell scripts)
- **data-flow oriented** (Nextflow, SciPipe)

We can also make a distinction on the nature of the software components that are connected; are those local components
(local processes) or remote networked components (webservices).

## Aims and scope of the Interest Group

The aims of the IG on Workflows are:

- Foster discussion and knowledge sharing regarding research workflows/pipelines
- Develop and share best practices for setting up workflows, recommend solutions
    - Different audiences may require different solutions
- Create an inventory of existing workflow solutions in CLARIAH
- Determine which CLARIAH tools can or should be connected into a larger workflow and for which there is an actual need from the research community; coordinate such solutions
- Promote interoperability between CLARIAH tools
    - More attention for underlying standards and protocols; focus should first and foremost be on clear specifications of input and output data and communicatin protocols. Tools need a common ground to communicate, if this does not exist then higher-level workflow orchestration is pointless.
    - This details of these are mostly in the scope of the other interest groups on Annotation, Text, Audio/Video, Linked Data.

## Communication

We use the following communication channel:

- [slack](clariah-workspace.slack.com) (if you don't have access yet, please contact one of the coordinators)

## Tasks

Unclear, to be defined still!

## Group Members

(Group coordinator is not yet clear)

- Daan Broeder (KNAW Humanities Cluster)
- Maarten van Gompel (KNAW Humanities Cluster)
- Jauco Noordzij (KNAW Humanities Cluster)
- Jaap Blom (Netherlands Institute for Sound and Vision)
- Hennie Brugman (KNAW Humanities Cluster)
- Martijn van de Donk (Netherlands Institute for Sound and Vision)
- Roeland Ordelman (Netherlands Institute for Sound and Vision)
- Joe Raad (VU Amsterdam)
- Adam Belloum (eScience Center)

The group is open to new members.
