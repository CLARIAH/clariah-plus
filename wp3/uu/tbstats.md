# Treebank Statistics

## Metadata

* **Status:**  In Progress
* **Type:** Specific 
* **Work Package**: WP3
* **Research Coordinators:**  Jan Odijk (UU)
* **Coordinators for CLARIAH:**  Jan Odijk (UU)
* **Participating Institutes:** UiL-OTS, UU
* **End-users**: Jan Odijk, Martin Kroon (UL), all linguists
* **Developers**: UU, DH Lab (Sheean Spoel, Jelte van Boheemen)
* **Interest Groups**: Text Processing, Work Flows .
* **Task IDs**: WP3 T094

## Description

Extend treebank search application so that, e.g. for a dependency triple (d,lab,h ) with a relation lab between a head word h, and a dependent word d. You define a query in terms of  properties (if any)  of h and d that define the dependency that you are interested in
Properties of h and d include: part of speech code, inflectional properties (often encoded in a pos tag), lemma, root/stem, frame.
This query yields a result set. Of this result set one would want to obtain automatically a large number of statistics, e.g.
* absolute and relative frequency of each of the properties of d
* absolute and relative frequency of each of the properties of h
* absolute and relative frequency of each of the combinations of properties of h and d
* frequency of the distance between h and d (in terms of # of words)
* for frequent small distances (<=2,3), frequencies of the properties of each of the intervening words, and frequencies of the  sequences of these properties 
* frequencies of the order of d and h (d<h, d>h)
* for each of the orders, frequencies of the distances
* for each of the orders, frequencies of each the properties of d and h
* for each of the orders and distances, frequencies of each the properties of d and h
* for all adjacent h and d: frequencies of the properties
* frequency of projectivity; frequency of projectivity and other properties
* 	…
*	a list of significant findings within these statistics.
*	statistics of combinations of these properties. Output that can be used in statistical packages for e.g. Multivariate analysis, Principal component analysis etc.
*	generalize this to other classes of frequently needed query types that involve more than just a dependency triple): constructions

### What is the research about?

The tool to generate treebank statistics will accelerate linguistic research, will provide quantitative evidence for or against hypotheses, may suggest new hypotheses
Mainly relevant for linguistics.

### What problem is hindering the research?
A few corpus linguists do similar things, but usually with ad-hoc developed tools.

### What is needed to do the research?


#### Data

Treebanks as currently available

#### Tools

extensions of GrETEL application

### What software and services are involved?

GrETEL. Some initial extensions have been made.

### How to evaluate this?

The number of true generalisations suggested versus 
the number of false generalisations suggested

## References

References to related resources and publications and especially links to related use-cases:


* An initial report is available: Jan Odijk, dec 2020, Treebank Statistics
Interim Report. CLARIAH report, UU.

