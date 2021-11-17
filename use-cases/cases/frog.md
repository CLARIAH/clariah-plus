# Automatic linguistic enrichment for Dutch texts using Frog

## Metadata

* **Status:**  Completed
* **Type:** Generic
* **Work Package**: WP3
* **Coordinators for CLARIAH:** Maarten van Gompel
* **Participating Institutes:** KNAW HuC ,  Radboud University Nijmegen (in the past: Tilburg University)
* **End-users**: Researchers
* **Developers**: Maarten van Gompel (current maintainer), Ko van der Sloot (former lead developer, now retired), Antal
    van den Bosch, Peter Berck, Bertjan Busser, Walter Daelemans
* **Interest Groups**: Text
* **Task IDs**: T139 (Frog), T108 (FoLiA)

## Description

This is a generic use case, generalising over a variety of possible research projects that focus on text mining for
Dutch.

In this use case we focus on one particular solution that has been developed in the scope of CLARIN-NL and CLARIAH:
[Frog](https://languagesmachines.github.io/frog), an NLP-suite for Dutch that integrates various modules for different
kinds of linguistic annotation:

* Tokenizer (through [ucto](https://languagemachines.github.io/ucto))
* Multi-word units
* Lemmatizer
* Morphological Analyzer
* Part-of-Speech Tagger
* Named Entity Recogniser
* Phrase Chunker (Shallow parsing)
* Dependency Parser

Most of the modules are based on memory-based learning (k-NN based techniques) and are the culmination of over two
decades of work by various partners, containing the output of multiple research projects. It can be contrasted to some
of the more state-of-the-art deep learning techniques that have gained ground in recent years. Frog was and remains a
widely used tool for many researchers.

### What is the research about?

Researchers often want to enrich texts with linguistic features such as Part-of-Speech tags, lemmas, dependency
relations, named entities, etc.. These often provide useful features for text mining or as preprocessing towards further
ends.

### What is needed to do the research?

#### Tools

Frog (as well as ucto) is a command-line tool. To make it accessible to a wider audience we have:

* Integrated a low-latency daemon mode (TCP)
* Made available a [Python binding](https://github.com/proycon/python-frog) (also [one for
    ucto](https://github.com/proycon/python-ucto)
* Made it available as [a webservice](https://webservices.cls.ru.nl/frog) that lends itself to further integration with
    the CLARIAH infrastructure. Note however most users prefer to access this tool using the lower interfaces.

#### Data

* Various memory-based models have been trained. The tokeniser is rule-based.
    * There are also some PoS and lemma models for historical dutch from two time periods, developed in the scope of the
        Nederlab project.
* A rich data format was needed to represent all the possible annotations. The XML-based format [FoLiA](https://proycon.github.io/folia) was
    adopted to this and Frog (and ucto) supports reading and writing this format and adding the necessary annotation
    layers where requested.
* In addition to FoLiA, output in a simple tab-seperated-format is supported, but there is
  some information loss when this is chosen.
* Recent versions of Frog also an extra JSON-output mode.

### What software and services are involved?

* [Frog](https://languagemachines.github.io/frog) - CLI tool and C++ library
    * [frogdata](https://github.com/LanguageMachines/frogdata) - The trained models/data files
* [Ucto](https://languagemachines.github.io/ucto) - The tokeniser (standalone CLI tool and C++ library)
    * [uctodata](https://github.com/LanguageMachines/uctodata) - Rule-based tokenisation rules for several languages
* [Mbt](https://languagemachines.github.io/mbt) - Memory-based tagger (C++)
    * [Timbl](https://languagemachines.github.io/timbl) - A k-NN memory-based learning toolkit (C++)
* [FoLiA](https://proycon.github.io/folia) support via  [libfolia](https://github.com/LanguageMachines/folia) - An
    XML-based data format supporting the various kinds of linguistic annotations Frog provides.
* [CLAM](https://proycon.github.io/clam) - Used to power the webservice
    [CLAM](https://proycon.github.io/clam))
* [Toad](https://github.com/LanguageMachines/toad) - This is a separate set of tools that can be used to train new
    models for Frog.
* [LaMachine](https://proycon.github.io/lamachine) - Because Frog is complex software with many dependencies that may be
    non-trivial to install for many users, all that is necessary to run and deploy it is bundled in LaMachine, a meta-distribution of
    various NLP tools. LaMachine is a courtesy to the user here, not a dependency for Frog.

## References


Related use-cases:

* [Data format for linguistically-annotated corpora](cases/folia-corpora.md) (WP3, FoLiA)
* [Tools to the data: Text Mining for Health Inspection](cases/text-mining-for-health-inspection.md) (WP3, LaMachine/Frog)
* [Research Environment for Workshop: Cataloguing of Textual Cultural Heritage
    Objects](cases/cataloguing-of-textual-cultural-heritage-objects.md) (WP3, LaMachine)
* [Retrodigitization of Text-critical Editions](cases/max-weber.md) (WP3, FoLiA/FLAT/LaMachine)
* [Nederlab: Automatic Linguistic Enrichment of Historical Dutch](cases/nederlab-enrichment.md) (WP3/WP6, Frog/FoLiA)
* [Quickly building webservices with CLAM](cases/clam-webservice.md) (WP3, CLAM)

Relevant publications:

* K.  van der Sloot , I.  Hendrickx , M.  van Gompel , A.  van den Bosch , W.  Daelemans (2018) — [Frog, a natural language processing suite for dutch. Reference Guide](https://frognlp.readthedocs.io/en/latest/) — Language and Speech Technology Technical Report Series 18-02. Radboud University. Nijmegen, The Netherlands.

