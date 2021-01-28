# Nederlab: Automatic Linguistic Enrichment of Historical Dutch

## Metadata

* **Status:**  Completed
* **Type:** Specific
* **Work Package**: WP3/WP6
* **Research Coordinators:**  Katrien DePuydt (INT), Hennie Brugman (KNAW HuC)
* **Participating Institutes:** INT, KNAW HuC, Radboud
* **Developers**: Erik Tjong Kim Sang (KNAW HuC), Maarten van Gompel (RU), Jesse de Does (INT), Erwin Komen (RU)
* **Interest Groups**: Text, Annotation

## Description

The aim of the Nederlab project is to offer a research portal containing a huge collection of various digitised
Dutch documents in various time periods.

Though the project itself is independent of CLARIAH, it uses a variety of CLARIAH tools.

### What is the research about?

The aspect addressed in this use case relates to the automatic linguistic enrichment of historical dutch, with an
initial focus on 17th century dutch.

### What problem is hindering the research?

A main issue was the fact that most NLP tools were trained on contemporary Dutch rather than historical Dutch.
Other major issues related to handling/converting the original TEI documents and getting them into another form so automatic enrichment
could be performed. A third issue was the inaccuracy of metadata.

### What is needed to do the research?

#### Data

The resulting corpora are delivered in the [FoLiA](https://proycon.github.io/folia) format. Various improvements were made to
accommodate the Nederlab results, such as the ability to [associate metadata with sub-parts of a document](https://github.com/proycon/folia/issues/30). The input corpora are largely in TEI format and come from various sources, the KB's DBNL being a notable one.

Tagged historical trainings data with part-of-speech tags and lemmas was an important resource in this research. The Brieven
als Buit corpus and the corpus Rhenen-Mulder were used as a basis here.

The inaccuracy of metadata (time period information) provided to be a problem, especially pertaining to sub-editions, so
a metadata curation effort was undertaken by Katrien DePuydt. Accurate time period information was essential for the
enrichment pipeline to decide what enrichment strategy to apply.

#### Tools

A wide variety of tools were used and [a workflow](https://github.com/proycon/nederlab-pipeline) needed to be
implemented that invokes these tools. There was considerable work needed to handle the initial TEI input so that it was
suitable for further linguistic enrichment; a [tei2folia](https://github.com/proycon/foliatools) converted was developed to this end and continues where earlier efforts like [INT's OpenConvert](https://github.com/INL/OpenConvert) stopped. [Frog](https://languagemachines.github.io/frog) was used as the main engine for linguistic enrichment in the form of Part-of-Speech tagging, lemmatisation and named entity recognition. As Frog only handles contemporary Dutch, new Models were trained for different two different historical time periods.

Initial work by Erik Tjong Kim Sang focussed on a translation step of 17th century dutch to contemporary dutch, so the
contemporary translation could be used for further enrichment with tools (Frog) that only knew contemporary Dutch. This strategy was applied for this time period.

### What software and services are involved?

* [ucto](https://languagemachines.github.io/ucto) for tokenisation.
* [Frog](https://languagemachines.github.io/frog) for PoS-tagging, lemmatisation and Named Entity Recognition for Dutch,
    Middle Dutch, and Early New Dutch (vroegnieuwnederlands)
* [FoLiA-utils](https://github.com/LanguageMachines) for:
    * ``FoLiA-wordtranslate`` - Implements Erik Tjong Kim Sang's word-by-word modernisation method. This is a
        reimplementation of his initial prototype, with some added improvements.
* [Colibri Utils](https://github.com/proycon/colibri-utils) for:
    * ``colibri-lang`` - Language Identification (including models for Middle Dutch and Early new Dutch)
* [FoLiA Tools](https://github.com/proycon/foliatools) for:
    * ``foliavalidator`` - Validation
    * ``foliaupgrade`` - Upgrades to FoLiA v2
    * ``tei2folia`` - Conversion from a subset of TEI to FoLiA.
    * ``foliamerge`` - Merges annotations between two FoLiA documents.
* [wikiente](https://github.com/proycon/wikiente) for Named Entity Recognition and Linking using [DBPedia Spotlight](https://www.dbpedia-spotlight.org). This eventually replaced earlier work called [foliaentity](https://github.com/ErwinKomen/FoliaEntity) by Erwin Komen.


## References

References to related resources and publications and especially links to related use-cases:

* [Nederlab Pipeline](https://github.com/proycon/nederlab-pipeline)
* [Nederlab Portal](https://nederlab.nl)
* [Nederlab Linguistic Enrichment work repositor](https://github.com/INL/nederlab-linguistic-enrichment) (private)

* [The CLIN27 Shared Task: Translating Historical Text to Contemporary Language for Improving Automatic Linguistic Annotation](https://clinjournal.org/clinj/article/view/68/61), by Erik Tjong Kim Sang, Marcel Bollmann, Remko Boschker, Francisco Casacuberta, Feike Dietz, Stefanie Dipper, Miguel Domingo, Rob van der Goot, Marjo van Koppen, Nikola Ljubešiç, Robert Östling, Florian Petran, Eva Pettersson, Yves Scherrer, Marijn Schraagen, Leen Sevens, Jörg Tiedemann, Tom Vanallemeersch and Kalliopi Zervanou. In: Computational Linguistics in the Netherlands Journal, volume 7, pages 53-64, 2017, ISSN 2211-4009.
* [Nederlab: Towards a Single Portal and Research Environment for Diachronic Dutch Text Corpora](https://ifarm.nl/erikt/papers/lrec2016nederlab.pdf), by Hennie Brugman, Martin Reynaert, Nicoline van der Sijs, René van Stipriaan, Erik Tjong Kim Sang and Antal van den Bosch. Proceedings of LREC 2016, Tenth International Conference on Language Resources and Evaluation, ELRA, Portoroz, Slovenia, pages 1277-1281, 2016, ISBN 978-2-9517408-9-1.
* [Improving Part-of-Speech Tagging of Historical Text by First Translating to Modern Text](https://ifarm.nl/erikt/papers/chdh2016.pdf), by Erik Tjong Kim Sang. 2nd IFIP International Workshop on Computational History and Data-Driven Humanities, editors: Bozic, Mendel-Gleason, Debruyne and O'Sullivan, Springer Verlag, 2016, ISBN 978-3-319-46223-3, doi:10.1007/978-3-319-46224-0.
* [Verwerking van achttiende-eeuws Nederlands met Frog](https://ifarm.nl/erikt/papers/2014edbo.pdf), by Erik Tjong Kim Sang. Internal Report, Meertens Institute, Amsterdam, The Netherlands, 13 February 2014.

