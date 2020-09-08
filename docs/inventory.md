# Inventory of Text Processing Tools in CLARIAH

[Back to main page](../README.md)

This document provides an inventory of the annotation text processing tools used in CLARIAH.
We try to be explicit in mentioning both the software, as well as hosted services based on that software.

## Natural Language Processing Tools

This is an overview of a variety of NLP tools that are developed within CLARIN/CLARIAH and/or used within CLARIAH.  Some
notable third-party tools are mentioned as well, but a full overview of those is beyond our scope, see for example
https://github.com/keon/awesome-nlp for a good collection.

### Multi-purpose NLP Suites and libraries

Tools in this category perform a wide variety of linguistic enrichments and typically offer (at least) a command-line
interface.

- [Alpino](https://github.com/rug-compling/alpino) - Alpino dependency parser for Dutch. Also does part-of-speech tagging, lemmatisation, tokenisation. It is also made available as a [webservice](https://webservices-lst.science.ru.nl/alpino) and is available through the web-application  [PaQu](https://github.com/rug-compling/paqu/), for parsing & querying corpora.
- [Frog](https://languagemachines.github.io/frog/) - An NLP-suite for Dutch (and some variants of historical dutch). Performs part-of-speech tagging, named entity recognition, dependency parsing, shallow parsing and morphological analysis. Tokenisation and sentence segmentation via [ucto](https://languagemachines.github.io/ucto). Full FoLiA import/output support. Developed in CLARIAH PLUS WP3 and actively mainained. Widely used in the dutch/flemish NLP community and beyond. It is a command-line tool and C++ library, but is also made available as a [webservice](https://webservices-lst.science.ru.nl/frog) or a [python binding](https://github.com/proycon/python-frog).

The following are noteworthy third-party tools that may or may not be used in CLARIAH, they often also act as libraries:

- [CoreNLP](https://stanfordnlp.github.io/CoreNLP/) - Automatich linguistic annotations for text, including token and sentence boundaries, parts of speech, named entities, numeric and time values, dependency and constituency parses, coreference, sentiment, quote attributions, and relations. (no dutch)
- [FreeLing](http://nlp.lsi.upc.edu/freeling/) - FreeLing is a tool and C++ library providing language analysis functionalities (morphological analysis, named entity detection, PoS-tagging, parsing, Word Sense Disambiguation, Semantic Role Labelling, etc.) for a variety of languages (English, Spanish, Portuguese, Italian, French, German, Russian, Catalan, Galician, Croatian, Slovene, among others). Usage in CLARIAH unknown.
- [Huggingface Transformers](https://github.com/huggingface/transformers) - Provides state-of-the-art general-purpose architectures (BERT, GPT-2, RoBERTa, XLM, DistilBert, XLNet, T5, CTRL...) for Natural Language Understanding (NLU) and Natural Language Generation (NLG) with over thousands of pretrained models in 100+ languages and deep interoperability between PyTorch & TensorFlow 2.0.
- [SpaCy](https://spacy.io/) - Popular python library for a wide variety of linguistic enrichments in many languages, including part-of-speech tagging, dependency parsing. Many statistical models and pretrained word vectors. We have a [webservice](https://webservices-lst.science.ru.nl/spacy) in the scope of CLARIAH, which adds FoLiA support.
- [UDPipe](https://github.com/ufal/udpipe) is a trainable pipeline for tokenizing, tagging, lemmatizing and parsing Universal Treebanks and other CoNLL-U files. Primarily written in C++, offers a fast and reliable solution for multilingual NLP processing.


### Tokenisers

- [Ucto](https://github.com/LanguageMachines/ucto) - A regular-expression based tokeniser and sentence segmenter. Supports multiple language including Dutch. Full FoLiA import/output support. Also integrated into Frog and maintained in that context as part of CLARIAH PLUS WP3. It is a command-line tool and C++ library, but it also made available as a [webservice](https://webservices-lst.science.ru.nl/ucto) or a [python binding](https://github.com/proycon/python-ucto).
- Tokenisers are often also part of larger libraries (see *NLP Suites and Libraries* above)

### Language Detection

- **FoLiA-langcat**, part of [foliautils](https://github.com/LanguageMachines/foliautils). Wrapper with FoLiA support around [libtextcat](https://www.let.rug.nl/~vannoord/TextCat/) for n-gram-based language detection.
- **folialangid**, part of [foliatools](https://github.com/proycon/foliatools). Wrapper with FoLiA support around [langid](https://github.com/saffsd/langid.py) for language detection.

### Normalisation and OCR post-correction

- **TICCL**, part of [PICCL](https://github.com/LanguageMachines/PICCL) - Performs spelling correction and OCR post-correction (normalisation of spelling variants etc). All the individual modules that make up TICCL are part of the [TicclTools](https://github.com/LanguageMachines/ticcltools) collection,
