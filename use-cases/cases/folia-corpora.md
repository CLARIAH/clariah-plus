# Data format for various linguistically-annotated corpora

## Metadata

* **Status:**  Complete
* **Type:** Generic
* **Work Package**: WP3
* **Research Coordinators:** (various)
* **Coordinators for CLARIAH:** Maarten van Gompel
* **Participating Institutes:** (various)
* **End-users**: Corpus builders and their users
* **Developers**: Maarten van Gompel, Ko van der Sloot
* **Interest Groups**: Annotation, Text
* **Task IDs**: T108 (FoLiA)

## Description

This use case groups several projects that aimed to deliver a corpus with various kinds of linguistic enrichment, either
achieved automatically by NLP or manually.

### What is the research about?

This use case is an abstraction over several research projects that all needed a way to encode their corpora:

* [SoNaR500]() - A 500 million word reference corpus for contemporary written Dutch, which is delivered in
FoLiA format. Other corpora in which FoLiA is used
* [VU-DNC]() - a 2 million word diachronic corpus for Dutch offering both sentiment annotations and a gold standard for OCR post-correction.
* [DutchSemCor](http://wordpress.let.vupr.nl/dutchsemcor/) - A lexical semantic sense annotated corpus (superset of SoNaR500)
* [Basilex](http://www.basilex.nl) - A corpus consisting of
Dutch texts young children would typically be exposed to; VU-DNC, a 2 million word diachronic corpus for Dutch offering both sentiment annotations and a gold standard for OCR post-correction.
* [Basiscript](https://www.jbe-platform.com/content/journals/10.1075/ijcl.17086.tel) - A corpus of contemporary Dutch texts written by primary school children
* [Nederlab](http://www.nederlab.nl) - Established a search environment for a large number of dutch text collections,
    including historical ones. The project however does not dissemminate the corpus that it compiled due to licensing
    restrictions.
* [Political Mashup](https://www.politicalmashup.nl/) - Parliamentary corpus

### What problem was hindering the research?

These projects needed to encode texts one or more types of linguistic annotation.  Between all these projects there was
quite a diversity in linguistic annotation types that had to be encoded, such as for example Part-of-Speech tags,
lemmas, named entities, dependency relations, semantic roles. To prevent having to encode each using an ad-hoc scheme, a
more general solution was proposed and adopted by these projects.

In addition to encoding linguistic annotation, it was also important for some projects to have a format that can also encode document
structure (paragraphs, sentences, lists, etc) and even text markup.

### What is needed to do the research?

#### Data

* A clear data format specification for linguistic annotation. [FoLiA](https://proycon.github.io/folia) was adopted as a
  solution by these projects. (Note that Political Mashup is a notable exception as they technically did not adopt FoliA but merely embedded
  parts of it in their own format).
  FoLiA provides an integrated XML-based solution. It has its own document-based generic paradigm and strictly defines
  various linguistic and structural annotation types, but leaves definitions of actual linguistic (or other)
  vocabulary up to the user.
  FoLiA is indended as both a corpus storage format and language-resource interchange format between tools and services. It shares certain similarities with initiatives such as TEI, TCF, TiGeR XML, NAF, and various others.
* Formal schemas (RelaxNG)
* Independent vocabularies offered through FoLiA Set Definitions (nowadays SKOS-based).

#### Tools

* Validation tools
* Programming libraries to work with the format
* NLP tools that can handle the format
* Tools for visualisation

### What software and services are involved?

* [FoLiA](https://proycon.github.io/folia) - Format for Linguistic Annotation; data format
* [foliapy](https://github.com/proycon/foliapy) - Python library for working with FoLiA (previously part of [pynlpl](https://github.com/proycon/pynlpl))
* [libfolia](https://github.com/LanguageMachines) - C++ library for working with FoLiA
* [foliatools](https://github.com/proycon/foliatools) - Command-line tools for working with FoLiA (contains validators
    and converters etc)
* [foliautils](https://github.com/LanguageMachines/foliautils) - Another set of command-line tools for working with FoLiA (contains validators
    and converters etc)
* [Ucto](https://languagemachines.github.io/ucto) - Ucto is a tokeniser with built-in FoliA support that has been used
    in several of these projects.
* [Frog](https://languagemachines.github.io/frog) - Frog is an NLP-tool for Dutch that has built-in FoLiA support and
    was used in several of these projects and has probably been a factor in their choice for FoLiA.


## References

Related use cases that use FoLiA:

* [Negation Annotation in Dutch dialogue](negation-annotation-task.md) (WP3, FLAT/FoLiA)
* [Retrodigitization of Text-critical Editions](max-weber.md) (WP3, FoLiA/FLAT/LaMachine)
* [Annotation of spelling correction for CLIN28 Shared Task](clin28sharedtask.md) (WP3, FLAT/FoLiA)
* [Syntactic Movement Annotation](syntactic-movement-annotation.md) (WP3, FoLiA/FLAT)

Publications:

* M. van Gompel (2018) - [FoLiA: Format for Linguistic Annotation - Documentation and Reference Guide](https://folia.readthedocs.io/en/latest/)
* M. van Gompel , M.  Reynaert (2013) — [FoLiA: A practical xml format for linguistic annotation - a descriptive and comparative study](http://clinjournal.org/sites/clinjournal.org/files/05-vanGompel-Reynaert-CLIN2013.pdf) — In: Computational Linguistics in the Netherlands Journal. vol. 3 .
* M.  van Gompel , K.  van der Sloot , M.  Reynaert , A.  Bosch (2017) — [FoLiA in practice: The infrastructure of a linguistic annotation format](http://www.jstor.org/stable/j.ctv3t5qjk.13) — In: CLARIN in the low countries. Ubiquity Press.
* M. Reynaert , I.  Schuurman , V.  Hoste , N.  Oostdijk , M.  Gompel (2012) — [Beyond sonar: Towards the facilitation of large corpus building efforts](http://www.lrec-conf.org/proceedings/lrec2012/pdf/748_Paper.pdf) — In: Proceedings of the eighth international conference on language resources and evaluation (lrec). vol. 8 .
* N. Oostdijk, M. Reynaert, V. Hoste, I. Schuurman (2013) - [The construction of a 500-million-word reference corpus of contemporary written Dutch.](https://link.springer.com/chapter/10.1007/978-3-642-30910-6_13) In: Essential Speech and Language Technology for Dutch: Results by the STEVIN Programme. Chapter 13.
* A. Tellings, M. Hulsbosch, A. Vermeer, A. Van den Bosch (2014). BasiLex: An 11.5 million words corpus of Dutch texts written for children. Computational Linguistics in the Netherlands. 4. 191-208.
* A. Tellings, N. Oostdijk, I. Monster, F. Grootjen, A. van den Bosch - Basiscript: A corpus of contemporary Dutch texts written by primary school children. International Journal of Corpus Linguistics Vol. 23:4 (2018). pp. 494–508. https://doi.org/10.1075/ijcl.17086.tel
* K. Vis (2011) -  Subjectivity in news discourse. A corpus linguistic analysis of informalization. PhD Dissertation, VU Amsterdam.
* P. Vossen , A.  Görög , F.  Laan , M.  Gompel , R.  Izquierdo-Bevia , A.  Bosch (2011) — DutchSemCor: Building a semantically annotated corpus for dutch — In: Electronic lexicography in the 21st century: New applications for new users: Proceedings of eLex 2011, bled, 10-12 november 2011.
