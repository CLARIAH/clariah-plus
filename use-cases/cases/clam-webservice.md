# Quickly building webservices with CLAM

## Metadata

* **Status:**  Complete
* **Type:** Generic
* **Work Package**: WP3
* **Coordinators for CLARIAH:** Maarten van Gompel
* **Participating Institutes:** KNAW (previously Radboud University and before that Tilburg University)
* **End-users**: Service developers
* **Developers**: Maarten van Gompel
* **Interest Groups**: DevOps, Workflows
* **Task IDs**: T142 (CLAM)

## Description

Researchers in NLP regularly develop tools that perform certain data processing tasks. These are often written in
scripting languages like Python, possibly leveraging NLP/deep-learning libraries, and are invoked by the end-user
through the command line. This requires some technical knowledge on the part of the end-user.

CLARIN and CLARIAH aim to make tools more accessible, as services. We focus on researchers in the Humanities who do not always
have a technical background. To make tools accessible requires some expertise on the part of the service developer,
especially when integration into the larger CLARIAH infrastructure is concerned (RESTful APIs, federated authentication
etc).

### What was the hindering problem?

Researchers and developers do not always have the skills or the time to set up a RESTful interface or build a
web-application front-end for their tool.

Another issue is that certain processing data tasks are long-running tasks done in batches,  and can not be done in quick
low-latency responses. A solution is needed that is optimised for such batch processing.

### What is needed?

#### Tools

A framework to build RESTful webservices and a web-interface front-end.

### What software and services are involved?

We developed [CLAM](https://proycon.github.io/clam) to solve this issue. It takes a wrapping approach where the service
developer writes a service specification (input, output, parameters) and a wrapper script that acts as the layer between
CLAM and whatever underlying tool is to be invoked.

CLAM is written in Python and offers an API for clients (to communicate with CLAM webservices) and for wrapper scripts,
but you can write your wrapper script in any language you like.

The goal is two kill two birds with one stone: provide both a generic web-interface for human-end user, as well as a
RESTful API for automated clients.

### What was the research about?

CLAM was initially conceived in the scope of the CLARIN-NL TICCLops project, and has ever since been used to provide many
CLARIN/CLARIAH services.

## References

Related use cases:

* [Providing Language and Speech webservices at CLST (Radboud University, Nijmegen)](clst-webservices.md) (WP3, CLAM/LaMachine)

Publications:

* M.  van Gompel (2018) — [CLAM documentation](https://clam.readthedocs.io/en/latest/) — Language and Speech Technology Technical Report Series 18-03. Radboud University. Nijmegen, The Netherlands.
* M.  van Gompel , M.  Reynaert (2014) — [CLAM: Quickly deploy nlp command-line tools on the web](http://aclweb.org/anthology/C14-2016) — In: Proceedings of coling 2014, the 25th international conference on computational linguistics: System demonstrations. Dublin City University; Association for Computational Linguistics. Dublin, Ireland.
* Marc  Kemps-Snijders , Ineke  Schuurman , Walter  Daelemans , Kris  Demuynck , Brecht  Desplanques , Véronique  Hoste , Marijn  Huijbregts , Jean-Pierre  Martens , Hans  Paulussen , Joris  Pelemans , Martin  Reynaert , Vincent  Vandeghinste , Antalvan den  Bosch , Henk van den Heuvel , Maarten van Gompel , Gertjan  Noord , Patrick  Wambacq (2017) — TTNWW to the rescue: No need to know how to handle tools and resources — In: CLARIN in the low countries. Ubiquity Press.
