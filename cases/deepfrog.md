# Deep-learning for Dutch text mining

## Metadata

* **Status:**  Proposed
* **Type:** Generic
* **Work Package**: WP3
* **Research Coordinators:** Maarten van Gompel
* **Coordinators for CLARIAH:**  Maarten van Gompel
* **Participating Institutes:** KNAW HuC, Radboud University Nijmegen
* **End-users**: Researchers/developers, specific research is being conducted already by  Tess Dejaeghere and Vincent
    vandeGhinste in the scope of CLARIAH-VL
* **Developers**: Maarten van Gompel
* **Interest Groups**: Text
* **Task IDs**: T139b (Deepfrog)

## Description

This generic use-cases proposes builds upon the [Automatic linguistic enrichment for Dutch texts](frog.md) use-case.
Do note that there is currently no official time or budget allocated for this initiative yet. Nevertheless, we already
got started on it and have a first prototype.

### What is the research about?

The various NLP modules in [Frog](https://languagemachines.github.io/frog) were built on k-NN classifiers, whereas the
current state-of-the art tends to converge to using a variety of neural transformer-based model.

### What problem is hindering the research?

The current Frog may or may not leap behind the current state-of-the-art, whether that is the case is still to be
determined. To research this we propose a next generation Frog which we call
[DeepFrog](https://github.com/proycon/deepfrog) that offers ground for comparison.

### What is needed to do the research?

Frog currently consists of multiple components addressing different kinds of
linguistic enrichment, this will be no different in the proposed DeepFrog.
Initial emphasis will be on:

* Part-of-Speech Annotation
* Lemmatisation
* Named-entity Recognition

This leaves morphological analysis, dependency parsing and shallow parsing for
a later stages>

The aim is to use the same training data for the modules of DeepFrog as has
been used for Frog, in this way, a fair comparison between the two systems can
be drawn. This comparison constitutes the main research objective of this
research; the hypothesis is that by applying state-of-the-art deep learning
techniques we can improve the accuracy for each of our very specific Dutch
linguistic enrichment tasks.

Using the same training data also implies that the same tagsets will be used
(i.e. the CGN tagset for Part of Speech tagging). This provides a necessary
continuity for the possible future adoption of the new tool if it proves
successful, as it can then be a stand-in replacement for the current Frog.

Unlike earlier work on Frog, this project will build an entirely new code base rather than an update the existing Frog
codebase, as such they can live alongside and independently of eachother. The reason for a new codebase is the fact that
we are effectively replacing the very memory-based algorithms that have powered Frog for years with different ones based
on neural networks. A new Python codebase would be more appropriate than the current C++ one in the light of the deep
learning libraries that are available and the need to do rapid prototyping to develop and test the new models. The
performance penalty that comes with the interpreted overhead (Python) can be largely disregarded as the underlying deep
learning libraries that perform the bulk of the work are native implementations anyway.

We will adhere to the same input and output formats as the current Frog: FoLiA
XML input/output, plain text input, and columned output.  The idea is that DeepFrog can act as a more-or-less drop-in
replacement.

#### Data

We will leverage existing pre-trained models for Dutch such as BERTje, Roberta, and fine-tune those on specific NLP
tasks.

#### Tools

We will build on existing third-party libraries such as [transformers library offered by huggingface](https://github.com/huggingface/transformers) and its [port to
Rust](https://github.com/guillaume-be/rust-bert).

[DeepFrog](https://github.com/proycon/deepfrog) will be a command-line tool that integrates the necessary data layers,
but most of the models we train can also be used independently of the tooling we develop and have merit on their own.

### What software and services are involved?

* [transformers library offered by huggingface](https://github.com/huggingface/transformers)
* [rust-bert](https://github.com/guillaume-be/rust-bert) - Rust-port of the former
    * [https://github.com/guillaume-be/rust-tokenizers](https://github.com/guillaume-be/rust-tokenizers)
* [FoLiA](https://proycon.github.io/folia) support via  [libfolia](https://github.com/LanguageMachines/folia) - An
    XML-based data format supporting the various kinds of linguistic annotations Frog provides.
* [NextFlow](https://nextflow.io) - Workflow system for the training pipelines
* [CLAM](https://proycon.github.io/clam) - Used to power the webservice
    [CLAM](https://proycon.github.io/clam))
* [LaMachine](https://proycon.github.io/lamachine) - Use as a distribution/deployment solution.

### How to evaluate this?

A study needs to be done to assess the efficacy of the DeepFrog with Frog. An initiative to this end, using the first
protype we delivered, has already started
in the Flemish CLARIAH with Vincent Vandeghinste and intern Tess Dejaeghere. Further interest from Flanders has also been expressed by Walter
Daelemans.

## References

Related use-cases:

* [Automatic linguistic enrichment for Dutch texts using Frog](frog.md)
* [Data format for linguistically-annotated corpora](cases/folia-corpora.md) (WP3, FoLiA)

Links:

* [DeepFrog](https://github.com/proycon/deepfrog)
