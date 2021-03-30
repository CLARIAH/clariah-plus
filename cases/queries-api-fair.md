# grlc -> sparql queries as api and with metadata

## Metadata

* **Status:**  Completed, but underused by CLARIAH!
* **Type:** Generic
* **Work Package**: WP4, useful to WP2, WP5, perhaps WP6
* **Research Coordinators:**
* **Coordinators for CLARIAH:**  Richard Zijdeman
* **Participating Institutes:** VU, UU
* **End-users**: Anybody writing sparql queries, or anybody in need of an API, who doesn't write sparql queries
* **Developers**: Albert Merono-Penuela (ex-CLARIAH), Carlos Rodrigues Martinez (eScience center)
* **Interest Groups**: IG-vocabs/modeling, IG-findability
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description
The use case is two fold. One is that sparql is yet another query language for developers. By providing sparql queries as api's, developers can more easily incorporate them in their software.
The other part of the use case is about historians. For them to learn sparql, having examples is crucial. More over, when not entirely up to task, sharing a sparql query via a decent place (rather than mail) is important to get help from experts (e.g. via Stackoverflow). Finally, in scientific communication, the retrieval of data (e.g. via a sparql query) is a necessity. for them grlc allows user to store sparql queries on git, allows others to adopt and adapt them and make them findable via the grlc meta-data tags provided for sparql queries.

### What is the research about?
The research questions can really be from any domain even outside CLARIAH. The repo where we store (some of) the queries, can be found [here](https://github.com/clariah/wp4-queries).

### What problem is hindering the research?
- sparql being a rather new query language is new to both developers and researchers;
- sparql queries are not Findable, Accessible (often hard coded in an application), Interoperable and Reusable.

### What is needed to do the research?
- grlc.io (developed in CLARIAH CORE) helps to solve these issues. What is still need to is to make grlc.io sustainable software (e.g. make it a CLAAS service)

#### Data
- any data that one can write queries. Note that grlc is not just for SPARQL.

#### Tools
grlc can be used in the phase of data exploration, as well as in publishing the final research queries (slices of the data used for analysis).

### What software and services are involved?
[http://grlc.io](http://grlc.io/)
[grlc github repo](https://github.com/clariah/grlc/)

### How to evaluate this?
This use case has been solved when you can:
- name the institute that is responsible for maintaing the grlc software;
- other WP's than WP4 use grlc for (SPARQL) queries.

## References
https://zenodo.org/badge/latestdoi/46131212

References to related resources and publications and especially links to related use-cases:
* [WP4-queries](https://github.com/clariah/wp4-queries)
* [CLARIAH](https://clariah.nl)
