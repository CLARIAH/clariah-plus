# Computer vision annotations 'n' enrichments of audiovisual data

## Metadata

* **Status:**  In Progress
* **Type:** Generic
* **Work Package**: WP5
* **Research Coordinators:**  Roeland Ordelman, Nanne van Noord
* **Coordinators for CLARIAH:**  Nanne van Noord
* **Participating Institutes:** NISV, UvA
* **End-users**: Christian Olesen (UvA/UU), Jasmijn van Gorp (UU), Julia Noordegraaf (UvA) [Links to use cases will follow]
* **Developers**: Nanne van Noord
* **Interest Groups**: Audiovisual processing, Devops, Workflows
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

### What is the research about?

Media Studies and DH scholars work with and rely on audiovisual colections for research, however the sheer size of these collections makes them difficult to navigate and explore. Progress in audiovisual processing tools, such as Computer Vision and [ASR](https://github.com/CLARIAH/usecases/blob/master/cases/mediasuite-speech-transcription.md) offer the promise of unlocking AV collections. Yet, the availability of these tools to scholars, or their integration into collections remains limited.

This use case is concerned with developing and deploying Computer Vision algorithms via [DANE](https://github.com/CLARIAH/DANE), such that they can be applied to the collections available in the Mediasuite. 

### What problem is hindering the research?

The three main challenges for this research are:

1. *Data access*: Although infrastructures are in place for users to be able to view AV content, for automated access this is not the case for all collections. Unified (and high-speed) access to AV content would improve ease for applying CV tools.
2. *Access to results*: Providing access to the results of AV tools such that users can effectively and efficiently use them is not always trivial. A large amount of results can be turned into standard (textual) metadata (i.e., labels and confidences produced by a classification algorithm), but CV tools are also capable of producing non-textual results (e.g., segmentation maps, keypoints, bounding boxes, feature vectors). Determining at what level of granularity these rich results need to be stored, and how users can be provided with access is still an open problem.
3. *Tool selection*: Despite the ability of CV tools to process data at speeds much greater than humans, the amount of data to contend with is still massive. Figuring out which tools to apply to what data to have the maximum impact, while using the available compute resources most efficiently is an open problem.

### What software and services are involved?

The main backbone for this use case is [DANE](https://github.com/CLARIAH/DANE), which was developed specifically for this use case. Beyond that there are a variety of open-source frameworks and tools used for specific CV analyses, as well as GPU compute infrastructure.

### How to evaluate this?

A good solution to this use case will enable and empower 'downstream' uses (and use cases), as such the evaluation is to be performed through those.

## References

* [DANE](https://github.com/CLARIAH/DANE)
* [DANE-server](https://github.com/CLARIAH/DANE-server)
* [DANE documentation](https://dane.readthedocs.io)
* N. van Noord, C. Olesen, R. Ordelman, and J. Noordegraaf, ‘Automatic Annotations and Enrichments for Audiovisual Archives’, 2021, pp. 633–640.
