# CoW: Csv On the Web

## Metadata

* **Status:**  Completed
* **Type:** Specific
* **Work Package**: WP4
* **Participating Institutes:** International Institute of Social History (IISG) and Vrije Universiteit Amsterdam (VU)
* **Coordinators:**  Richard Zijdeman (IISG)
* **Developers**: Albert Meroño Peñuela, Roderick van de Weerdt, Melvin Roest
* **End-users**: The software is designed for the so called ‘digital’ historian: e.g. someone with basic command line skills.
* **Interest Groups**: IG-LOD, IG-Curation, and Worflows
<!-- * **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks) -->

## Description

### What is the research about?
Historians often use tabular data as input for their analyses. These dataset often reside on local machines, which hinders the reproducibility and replicability of research, as well as preventing to link their dataset to other useful data. This package is a comprehensive command-line utility for batch conversion of multiple datasets expressed in CSV.
### What problem is hindering the research?
Trough Linked Data conversion CoW aims to enhance the workflow of historical research - and other research working with tabular data - by facilitating the sharing, standardization, and interlinking of datasets (and queries).

Its technical features are:

- Expressive [CSVW-compatible](https://www.w3.org/ns/csvw) schemas based on the [Jinja](https://github.com/pallets/jinja) template engine;
- highly efficient implementation leveraging multithreaded and multicore architectures;
- available as a pythonic [CLI tool](https://github.com/CLARIAH/COW#cli) and [library](https://github.com/CLARIAH/COW#library);
- supports Python 3


<!-- ### What is needed to do the research?

(How can we go about solving this problem?) -->

#### Data

Any CSV dataset is required as input, preferably using UTF-8 encoding.

#### Tools

* [COW source code and documentation](https://github.com/CLARIAH/COW)
* [COW technical documentation](https://csvw-converter.readthedocs.io/en/latest/)

<!-- (if known, describe what tools or functionalities you need to work with the data and do the research. Take the different stadia of the research into account, such as exploration phase, distant reading, close reading, annotating data, publishing, etc. Be as specific as possible) -->

### What software and services are involved?

- Python 3

<!-- ### How to evaluate this?

(How do we evaluate the solution to the problem?) -->

## References

References to related resources and publications and especially links to related use-cases:

* [Rinke Hoekstra, Albert Meroño-Peñuela, Auke Rijpma, Richard Zijdeman, Ashkan Ashkpour, Kathrin Dentler, Ivo Zandhuis, Laurens Rietveld, The dataLegend ecosystem for historical statistics, Journal of Web Semantics, Volume 50 (2018),pp. 49-61](https://doi.org/10.1016/j.websem.2018.03.001)
