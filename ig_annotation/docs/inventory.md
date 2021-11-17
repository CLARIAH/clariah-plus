# Inventory of Annotation Models, Formats, Converters used in CLARIAH

[Back to main page](../README.md)

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
- [Praat TextGrids](https://www.fon.hum.uva.nl/praat/)

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

### Protocols

There are various protocols for storing, retrieving and querying annotation services:

- [Web Annotation Protocol](https://www.w3.org/TR/annotation-protocol/) - a minimal standard for storing and retrieving Web Annotations.
- [Distributed Text Services](https://distributed-text-services.github.io/specifications/) - a specification that defines an API for working with collections of text as machine-actionable data. This specification is under active development and is mainly relevant for CLARIAH Work Package 6 when used in combination with Web Annotation, as it addresses the need for semantic targeting (see [Annotation needs](./annotation-needs.md)) and using the [Scholarly Web Annotation Client](https://github.com/CLARIAH/scholarly-web-annotation-client).
- [International Image Interoperability Framework](https://iiif.io) - a set of API specifications for [delivering](https://iiif.io/api/search/1.0/), [presenting](https://iiif.io/api/presentation/3.0/) and [searching](https://iiif.io/api/search/1.0/) images.

## Annotation Storage

### Web Annotation Servers

- [Elucidate](https://github.com/dlcs/elucidate-server) - this server extends the Web Annotation Protocol mentioned above, to support authenticion, user management and querying of Web Annotations.
- [Scholarly Web Annotation Server](https://github.com/CLARIAH/scholarly-web-annotation-server) - similar to Elucidate, it extends the WA Protocol.

### Format-specific servers

- [FoLiA Document Server](https://github.com/proycon/foliadocserve) - Back-end for
    [FLAT](https://github.com/proycon/flat), operates directly on FoLiA XML files through an in-memory representation. Actively developed/maintained in WP3.

## Annotation Tools

All tools in this section focus on human-mediated annotation, not automatic annotation:

### Text Annotation Tools

- [FLAT](https://github.com/proycon/FLAT) (FoLiA Linguistic Annotation Tool) - Web-based annotation environment for
    linguistic annotation. Document-centric, builds on the FoLiA format and aims to support manual annotation for all annotation
    types supported by FoLiA. Actively developed/maintained in WP3 and used in various projects.
- [CoBaLT](https://github.com/INL/COBALT/) (IMPACT Corpus Based Lexicon Tool) - Keyword-in-Context style annotation of tokens (e.g. lemmatisation and pos-tagging). Web-based and with TEI import/export.
- [WebAnno](https://webanno.github.io/webanno/) - a general purpose web-based annotation tool for a wide range of linguistic annotations.  Usage in CLARIAH unknown, but offered as a service by other national CLARIN projects (CLARIN-D, FIN-CLARIN, CLARIN:el).
- [INCEpTION](https://inception-project.github.io) - similar to WebAnno, it is used at least in CLARIAH WP6
- [BRAT](http://http://brat.nlplab.org/) (Brat rapid annotation tool) - A web-based tool for text annotation. Use in CLARIAH unknown, but this tool is very popular in the field.

### Audiovisual Annotation Tools

- [CLARIAH MediaSuite](https://mediasuite.clariah.nl) - a platform for searching, viewing and annotating audiovisual materials from a range of collections, including the Radio and Television broadcast collections at the Netherlands Institute for Sound and Vision.
- [ELAN](https://archive.mpi.nl/tla/elan)
- [Praat](https://www.fon.hum.uva.nl/praat/)
- [EXMARaLDA](https://exmaralda.org)
- [Advene](https://www.advene.org)
- [VIAN](https://blog.filmcolors.org/2018/03/08/vian/)
- [FrameTrail](https://frametrail.org)
- [Semantic Annotation Tool](http://www.johnpbell.com/the-semantic-annotation-tool/)

### Vocabulary Services for Manual Annotation

- [GTAA](https://labs.beeldengeluid.nl/dataset/5520ccca-2c8e-11e6-a743-005056a71e3a)
- [Onomy](https://onomy.org)

## Annotation Search

The following tools allow the user to search/query annotations in resources, the focus is on searching in large amounts
of data.

### Text Annotation Search

- [Blacklab](https://github.com/INL/Blacklab) - A corpus retrieval engine built on top of Apache Lucene. This is a
    back-end system upon which multiple front-ends can run. It is actively maintained and used.
    - [Corpus Frontend](https://github.com/INL/corpus-frontend) - A corpus search application that works with BlackLab Server, used at INT for CHN, Letters as Loot, and AutoSearch.
    - [Whitelab](https://github.com/Taalmonsters/WhiteLab2.0) - A web-based front-end for the search and exploration of large corpora with linguistic annotations, developed in the scope of CLARIN's OpenSoNaR project, but no longer maintained. (there is also an older [Whitelab 1](https://github.com/TiCCSoftware/WhiteLab) version, an entirely different codebase, which is deprecated)
- [MTAS](https://github.com/matthijsbrouwer/mtas) (Multi Tier Annotation Search) - An annotation search system built on Lucene & Solr, developed for the [Nederlab](https://www.nederlab.nl) project. It was initially developed at the Meertens institute but the lead/sole developer left in 2018, he is still maintaining the software (as time allows).
- [GreTeL](https://github.com/UUDigitalHumanitieslab/gretel) (Greedy Extraction of Trees for Empirical Linguistics) - A
    web-based search engine for the exploitation of syntactically generated corpora aka treebanks.
    Actively developed in CLARIAH WP3. GreTeL 4 is a fork of earlier work (GreTeL 3): https://github.com/CCL-KULeuven/gretel/
- [PaQu](https://github.com/rug-compling/paqu) (Parse & Query) - A web-based tool to query treebanks (it also has a
    major parse compononent for automatic enrichment using Alpino but that is out of scope for this interest group).
- [ANNIS](ANNotation of Information Structure) (ANNotation of Information Structure) - A web-based search and visualization architecture for complex multilevel linguistic corpora with diverse types of annotation. Usage in CLARIAH unknown.


