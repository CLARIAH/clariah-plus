## CLARIAH FAIR Tool Discovery integration with SSH Open Marketplace

## Introduction

This is a subtask of the [CLARIAH FAIR Tool Discovery](fair-tool-discovery.md) track
that aims to periodically and automatically publish (a subset of) the
(automatically) gathered software metadata, published (as codemeta) in our
[tool registry](https://tools.clariah.nl), to the [SSH Open
Marketplace](https://marketplace.sshopencloud.eu).

The aim is to *automatically and without human intervention* make available to
a wider research community the latest up to date versions of CLARIAH tools. By
connecting to the SSH Open Marketplace, we also seek to connect CLARIAH to the
wider European Infrastructure. This all is of course on the condition that they
too are open to this collaboration and ingesting our software metadata.

## Planning

1. Preliminary investigation of:
    * SSH Open Marketplace contacts and determine interest in collaboration
    * [SSH Open Marketplace API](https://marketplace.sshopencloud.eu/about/api-documentation)
    * Reusability of available tooling developed for other conversion pipelines (Ineo, VLO)
    * rough time estimate: 20 hours
2. Implementation of conversion pipeline that fetches results from our tool registry, converts the representations (including vocabulary where appropriate) and does API calls to push the data to the SSH Open Marketplace API.
    * rough time estimate: 125 hours
3. Deployment of the conversion pipeline on the CLARIAH cluster, will run periodically and automatically
    * rough time estimate: 5 hours

This should be completed before the end of the extension of the CLARIAH project
(june 2024?) by [Maarten van Gompel](https://proycon.anaproy.nl) (KNAW Humanities Cluster).

## Deliverables

* **software + documentation**:  Conversion pipeline (corresponds with point 2 of the planning)
* Our software metadata accessible in the SSH Open Marketplace

## Challenges & Limitations

* Not all tools in our tool registry are mature enough to be published in the marketplace, I propose
  we simply adhere to the same automated criteria as we do for VLO and Ineo: a metadata validation rating of 3/5 or more, 
  a development status ([repostatus](https://www.repostatus.org/)) that is not 'concept','wip','suspended', 'unsupported' or 'abandoned' and/or a technology readiness level of  7 of higher.
* We will need some technical contact(s) at SSHOC Marketplace to obtain the necessary access keys and to help with questions that may arise. One of the challenges is that our pipeline will do frequent updates to previously created records.
* Certain tools already appear in the SSHOC Marketplace as they seem to be harvested by other means (most notably via CLARIN), some mechanism may be required to resolve such clashes.
* This task covers only the tool registry, not the data registry.
* This task does not make use of the [Rich User Content](https://github.com/CLARIAH/ineo-content) we use for Ineo, but only of the tool metadata itself.
