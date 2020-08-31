# Inventory of Annotation Models, Formats, Converters used in CLARIAH

[Back to main page](./README.md)

This document provides an inventory of the annotation models, paradigms, formats and converters used in CLARIAH. Eventually, we aim to create recommendations based on this inventory.

## Annotation Models

### Generic Annotation Models

- [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/): this model connects the Interest Group on Annotation with the Interest Group on Linked Open Data.

### Text Annotation Models

- [TEI](https://tei-c.org) (**Text Encoding Initiative**) -  An international and widely used encoding method for
    machine-readable text, chiefly in the humanities, social sciences and linguistics. Used by various CLARIAH partners.
    Maintained by the TEI Consortium.
- [FoLiA](https://proycon.github.io/folia/) (**Format for Linguistic Annotation**) - A generic paradigm and XML-based format for encoding linguistic annotation on text, aimed at the storage and exchange of linguistically annotated documents. The goal is to deliver a practical format with rich tooling infrastructure. Used by various CLARIAH partners, various dutch corpora, and actively developed/maintained in WP3.
- [TCF](https://weblicht.sfs.uni-tuebingen.de/weblichtwiki/index.php/The_TCF_Format) (**Text Corpus Format**) - An XML-data
    exchange format for [Weblicht](https://weblicht.sfs.uni-tuebingen.de/), intended mostly as an internal processing format. Was developed in the scope of CLARIN-D. Current use within CLARIAH unknown, may be relevant for interoperability with Weblicht.
- [NAF](https://github.com/newsreader/NAF) (**NLP Annotation Format**) -  NAF is a stand-off, multilayered annotation schema for representing linguistic annotations. It is developed at the VU Amsterdam and partners and stems from the Newsreader and Kyoto projects. It is used mainly by various linguistic processing pipelines developed at the VU.
- [Alpino XML](https://www.let.rug.nl/~vannoord/trees/) - An XML-based treebank format used by the tool Alpino, developed at Rijksuniversiteit Groningen and
    used by various CLARIAH partners and the LASSY corpus.
- [CONLL-U](https://universaldependencies.org/format.html) - A simple plain-text column based format for a limited
    amount of linguistic annotation. The format (or any of its dialects) is widely used internationally and popular in conferences and shared tasks, mostly due to its simplicity.
- [Salt](https://corpus-tools.org/salt/) - A graph-based, tagset-independent and theory-neutral meta model (and API) for storing, manipulating, and representing nearly all types of linguistic data. This model is of a more generic nature that the aforementioned models. It was developed an intermediate model for conversion and manipulation of linguistic data in a tool called [Pepper](https://corpus-tools.org/pepper/).
- [LAF](https://www.cs.vassar.edu/~ide/papers/ide-romary-clergerie.pdf) (**Linguistic Annotation Framework**) -  A abstract meta-model for annotation interchange and merging developed in ISO TC37
    SC4, and its GraF (Graph Annotation Format) serialisation. Usage within CLARIAH unclear (less immediate practical
    implications), may possibly influence some theoretical foundations?
- [TigerXML](https://www.ims.uni-stuttgart.de/documents/ressourcen/werkzeuge/tigersearch/doc/html/TigerXML.html) (Treebank encoding format). Probably not used in CLARIAH?
- [PaulaXML](https://github.com/korpling/paula-xml) (Potsdamer AUstauschformat Linguistischer Annotationen). Probably not used in CLARIAH?
- [ALTO](https://www.loc.gov/standards/alto/) (Analyzed Layout and Text Object) - An XML-based format developed for the description of text OCR and layout information of pages for digitized material. Used in CLARIAH WP3.
- [hOCR](http://kba.cloud/hocr-spec/1.2/) (Analyzed Layout and Text Object) - XHTML-based data representation for formatted text obtained from optical character recognition. Used by software such as Tesseract and used in CLARIAH WP3.

### Audiovisual Annotation Models

- [ELAN](https://archive.mpi.nl/tla/elan)

## Converters

### Text Annotation Conversion

- alpino→folia: [alpino2folia (foliatools)](https://github.com/proycon/foliatools), integrated into [piereling](https://github.com/proycon/piereling) webservice. Information loss: Minimal to None
- alto→folia: [FoLiA-alto (foliautils)](https://github.com/LanguageMachines/foliautils), integrated into [piereling](https://github.com/proycon/piereling) webservice. Information loss: unknown.
- alto→tei: [OpenConvert](https://github.com/INL/OpenConvert). Information loss: unknown
- conll→folia: [conllu2folia (foliatools)](https://github.com/proycon/foliatools), integrated into [piereling](https://github.com/proycon/piereling) webservice. Information loss: None
- conll→salt: [Pepper](https://corpus-tools.org/pepper/).
- hocr→folia: [FoLiA-hocr (foliautils)](https://github.com/LanguageMachines/foliautils), integrated into [piereling](https://github.com/proycon/piereling) webservice.
- folia→naf: [folia2naf (NAFFoLiAPy)](https://github.com/cltl/NaFFoLiAPy)). Information loss: considerable, converter is
- folia→salt: [folia2salt (foliatools)](https://github.com/proycon/foliatools)
- folia→tei: [OpenConvert](https://github.com/INL/OpenConvert). Information loss: considerable
- graf→salt: [Pepper](https://corpus-tools.org/pepper/).
- naf→folia [naf2folia (NAFFoLiAPy)](https://github.com/cltl/NaFFoLiAPy)). Information loss: not all layers are
    implemented yet, but converter is usable to for the various layers that are. Converter is currently not actively
    maintained.
- paula→salt: [Pepper](https://corpus-tools.org/pepper/).
- salt→graf: [Pepper](https://corpus-tools.org/pepper/).
- salt→tcf: [Pepper](https://corpus-tools.org/pepper/).
- salt→tei: [Pepper](https://corpus-tools.org/pepper/).
- salt→paula: [Pepper](https://corpus-tools.org/pepper/).
- tei→folia:
    * [tei2folia (foliatools)](https://github.com/proycon/foliatools), integrated into [piereling](https://github.com/proycon/piereling) webservice. Supports a notable subset of TEI P5.
        * *Information loss*: The converter will only work for a certain subset of TEI, mostly equivalent to TEI Lite, and may fail on others. Though a lot of TEI elements are supported there is also still a lot that is not covered by the converter due to the vastness of TEI. There will be comments in the output for anything that could not be converted properly.
    * [OpenConvert](https://github.com/INL/OpenConvert) (the above tei2folia implemention is derived from initial work on this and supersedes it)
- tcf→salt: [Pepper](https://corpus-tools.org/pepper/).
- tiger→salt: [Pepper](https://corpus-tools.org/pepper/).
- tei→salt: [Pepper](https://corpus-tools.org/pepper/). Information loss: supports only a subset of TEI.

### Text Conversion

The conversion of text mark-up and structure from and to presentional formats that do not have a deeper annotation
dimension are considered out of scope for this interest group. This includes formats such as plain text, reStructuredText,
Markdown, Word, OpenOffice, PDF, LaTeX, docbook, HTML, EPUB. There is, however, work in this area in WP3 in tools/services
such as [piereling](https://github.com/proycon/piereling) (FoLiA-centric) and [OpenConvert](https://github.com/INL/OpenConvert) (TEI-centric).

## Annotation Storage

### Web Annotation Servers

- [Elucidate](https://github.com/dlcs/elucidate-server)
- [Scholarly Web Annotation Server](https://github.com/CLARIAH/scholarly-web-annotation-server)

