# Inventory of Text Processing Tools in CLARIAH

[Back to main page](../README.md)

This document provides an inventory of the annotation text processing tools used in CLARIAH.
We try to be explicit in mentioning both the software, with a link to the source,
as well as hosted services based on that software.

## Natural Language Processing Tools

This is an overview of a variety of NLP tools that are developed within CLARIN/CLARIAH and/or used within CLARIAH.  Some
notable third-party tools are mentioned as well, but a full overview of those is beyond our scope, see for example
https://github.com/keon/awesome-nlp for a good collection.

### Multi-purpose NLP Suites and libraries

Tools in this category perform a wide variety of linguistic enrichments and typically offer (at least) a command-line
interface.

- [Alpino](https://github.com/rug-compling/alpino) - Alpino dependency parser for Dutch. Also does part-of-speech tagging, lemmatisation, tokenisation. It is also made available as a [webservice & web-application](https://webservices-lst.science.ru.nl/alpino) and is available through the web-application  [PaQu](https://github.com/rug-compling/paqu/), for parsing & querying corpora. Status: mature/production
- [Frog](https://languagemachines.github.io/frog/) - An NLP-suite for Dutch (and some variants of historical dutch). Performs part-of-speech tagging, named entity recognition, dependency parsing, shallow parsing and morphological analysis. Tokenisation and sentence segmentation via [ucto](https://languagemachines.github.io/ucto). Full FoLiA import/output support. Status: mature/production; developed in CLARIAH PLUS WP3 and actively mainained. Widely used in the dutch/flemish NLP community and beyond. It is a command-line tool and C++ library, but is also made available as a [webservice & web-application](https://webservices-lst.science.ru.nl/frog) or a [python binding](https://github.com/proycon/python-frog).


The following list contains pipeline systems that integrate a number of tools for specific purposes:

- [VU Reading Machine](https://github.com/cltl/vu-rm-pip3) - An integration of various in-house developed tools for processing Dutch texts and generates high-level semantic interpretations: annotated concepts, entities (people, organisations, places), events and roles, time expressions and opinions. Uses the NAF format.
- [Nederlab Pipeline](https://github.com/proycon/nederlab-pipeline)  - An integration of various tools (most notably
  tei2folia, ucto and Frog) for the linguistic enrichment of historical dutch, as developed in the scope of the Nederlab
  project.

This last list consists of noteworthy mature third-party tools that may or may not be used in CLARIAH, they often also act as libraries:

- [CoreNLP](https://stanfordnlp.github.io/CoreNLP/) - Automatic linguistic annotations for text, including token and sentence boundaries, parts of speech, named entities, numeric and time values, dependency and constituency parses, coreference, sentiment, quote attributions, and relations. (no dutch)
- [Stanza](https://stanfordnlp.github.io/stanza/) - A Python natural language analysis package, featuring pretrained
    neural models for 66 languages, a python binding for CoreNLP.
- [FreeLing](http://nlp.lsi.upc.edu/freeling/) - FreeLing is a tool and C++ library providing language analysis functionalities (morphological analysis, named entity detection, PoS-tagging, parsing, Word Sense Disambiguation, Semantic Role Labelling, etc.) for a variety of languages (English, Spanish, Portuguese, Italian, French, German, Russian, Catalan, Galician, Croatian, Slovene, among others). Usage in CLARIAH unknown.
- [Huggingface Transformers](https://github.com/huggingface/transformers) - Provides state-of-the-art general-purpose architectures (BERT, GPT-2, RoBERTa, XLM, DistilBert, XLNet, T5, CTRL...) for Natural Language Understanding (NLU) and Natural Language Generation (NLG) with over thousands of pretrained models in 100+ languages and deep interoperability between PyTorch & TensorFlow 2.0.
- [SpaCy](https://spacy.io/) - Popular python library for a wide variety of linguistic enrichments in many languages, including part-of-speech tagging, dependency parsing. Many statistical models and pretrained word vectors. We have a [webservice & web-application](https://webservices-lst.science.ru.nl/spacy) in the scope of CLARIAH, which adds FoLiA support.
- [UDPipe](https://github.com/ufal/udpipe) is a trainable pipeline for tokenizing, tagging, lemmatizing and parsing Universal Treebanks and other CoNLL-U files. Primarily written in C++, offers a fast and reliable solution for multilingual NLP processing.


### Tokenisers

- [Ucto](https://github.com/LanguageMachines/ucto) - A regular-expression based tokeniser and sentence segmenter. Supports multiple language including Dutch. Full FoLiA import/output support. Also integrated into Frog and maintained in that context as part of CLARIAH PLUS WP3. It is a command-line tool and C++ library, but it also made available as a [webservice & web-application](https://webservices-lst.science.ru.nl/ucto) or a [python binding](https://github.com/proycon/python-ucto). Status: mature/production.
- Tokenisers are often also part of larger libraries (see *Multi-purpose NLP suites and libraries* above)

### (Named) Entity Recognition

- [entity identification from scratch](https://github.com/cltl/entity-identification-from-scratch) - Entity
  identification for historical documents in Dutch. Developed in CLARIAH.
- [wikiente](https://github.com/proycon/wikiente) - Named entity recogniser (and linker) using [DBPedia Spotlight](https://www.dbpedia-spotlight.org/) (multiple languages), provides FoLiA support.
- NER is often integrated into larger libraries/tools (see *Multi-purpose NLP suites and libraries* above)

### Language Detection

- **FoLiA-langcat**, part of [foliautils](https://github.com/LanguageMachines/foliautils). Wrapper with FoLiA support around [libtextcat](https://www.let.rug.nl/~vannoord/TextCat/) for n-gram-based language detection.
- **folialangid**, part of [foliatools](https://github.com/proycon/foliatools). Wrapper with FoLiA support around [langid](https://github.com/saffsd/langid.py) for language detection.
- **colibri-lang**, part of [Colibri Utils](https://github.com/proycon/colibri-utils). N-gram based language
  identification with FoLiA support.

### Normalisation and OCR post-correction

- **TICCL**, part of [PICCL](https://github.com/LanguageMachines/PICCL) - Performs spelling correction and OCR post-correction (normalisation of spelling variants etc). All the individual modules that make up TICCL are part of the [TicclTools](https://github.com/LanguageMachines/ticcltools) collection. A PICCL [webservice & web-application](https://webservices-lst.science.ru.nl/piccl) is available. Currently not actively developed anymore.

### Spelling Correction

- [gecco](https://github.com/proycon/gecco) - Tool for context-aware spelling correction. Powers
  [valkuil.net](https://valkuil.net) webservice/web-application ([sources](https://github.com/proycon/valkuil-gecco)). Technically not part
  of CLARIN/CLARIAH but developed alongside and sharing common solutions. Currently not actively developed anymore.

### Language Modelling

- [colibri-core](https://github.com/proycon/colibri-core) - A tool and library (C++/Python) for the extraction of
  patterns (n-grams/skipgrams/flexgrams) from text-data in a quick and memory-efficient way. Technically not part
  of CLARIN/CLARIAH but developed alongside and sharing common solutions.

### Machine Translation

- **Oersetter** [webservice source](https://github.com/proycon/oersetter-webservice), [model
  source](https://github.com/proycon/oersetter-models) - A Frisian-Dutch, Dutch-Frisian machine translation system. Developed by Radboud University Nijmegen with Fryske Akademy. [Web-application available](https://taalweb.frl/oersetter). Technically not part
  of CLARIN/CLARIAH but developed alongside and sharing common solutions.

### Text Analytics

- [T-scan](https://github.com/proycon/tscan) - An analysis tool for dutch texts to assess the complexity of the text, computes and extracts text features. Technically not part of CLARIN/CLARIAH but developed alongside and sharing common solutions. [webservice & web-application](https://webservices-lst.science.ru.nl/tscan) available Status: production/mature.
- [Stylene](https://www.clips.uantwerpen.be/cgi-bin/stylenedemo.html) - Analyses dutch writing style. **No source code found!**

