# Corpus-based history of ideas #

## Metadata

* **Status:**  Confirmed with WP6
* **Type:** Specific
* **Work Package**: WP6, WP3
* **Research Coordinators:**  Arianna Betti
* **Coordinators for CLARIAH:**  (who is coordinating this use case for CLARIAH? If decided)
* **Participating Institutes:** University of Amsterdam, INT
* **End-users**: Arianna Betti
* **Developers**: Martin Reynaert, Jan Niestadt, Koen Mertens, Jesse de Does
* **Interest Groups**: Text
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

The use case involved leveraging CLARIAH tools to support the research by the group of the VICI project eIdeas, led by philosopher Arianna Betti.

The work centers around purpose-built corpora consisting of the collected works of a number of specific philosophers: Quine and Russell (English), Bolzano and Kant (German), Wolff (German and Latin), as well as corpora consisting of works from a particular time slot, possibly region, and dedicated to a particular topic (e.g. the 'Mathematical Method in Philosophy' in Prussia in the 18th Century: currently 98 works in German, 96 in (Neo-)Latin, by nearly as many different authors).

The group requires advanced search, exploration and exploitation capabilities for these corpora and future corpora it envisages. 

The CLARIAH infrastructure in the Netherlands offers enticing possibilities towards these ends and these have wholeheartedly been adopted by the group. 
Already in an LREC Workshop 2020 and a COLING 2020 paper, work has been presented on QUINE version 0.5 (an author's name in capitals refers to the corpus, not the author). These are the works of Willard Van Orman Quine (1908–2000), converted from a wide range of diverse publication formats into FoLiA XML, linguistically enriched (lemmatization, POS-tagging, etc.) by Spacy, indexed by BlackLab through INT CLARIAH service Autosearch and now available online in what is essentially WhiteLab (version 3) to just those scholars who have been granted access through the CLARIN login scheme (because of possible copyright restrictions).


### What is the research about?
(cf. https://conceptsinmotion.org/e-ideas/) 

Corpus-based approach to researching the history of ideas, relying on the novel ‘model approach’ to the history of ideas as its theoretical foundation. We draw on philosophy, intellectual history, computational linguistics, artificial intelligence and computer science.

### What problem is hindering the research?

A corpus exploitation environment (autosearch) is used. To facilitate the research, several extensions to the core environment and the ecosystem around it are desirable:

* Although autosearch is not a digital edition tool, enhancements to the default FoLiA indexing and presentation of documents to enable (e.g.) linking to scans of pages and retrieving document context by page number would be paramount for verification purposes
* Easier conversion tools from a simple text+metadata representation in csv to FoLiA
* Retrieval of "semantically" similar documents/paragraphs/sentences. This could be implemented either by 
  * Enriching the data with similarity data before indexing
  * Leveraging existing lucene scoring mechanisms
  * Enable blacklab to take similarity obtained from a remote service or database into account while searching (Related to the WP3 task "Annotation of search results")
 
### What is needed to do the research?

Cf. previous item

#### Data

The collected works of a number of specific philosophers: Quine and Russell (English), Bolzano and Kant (German), Wolff (German and Latin), as well as corpora consisting of works from a particular time slot, possibly region, and dedicated to a particular topic (e.g. the 'Mathematical Method in Philosophy' in Prussia in the 18th Century: currently 98 works in German, 96 in (Neo-)Latin, by nearly as many different authors.

#### Tools

* Autosearch
* Approaches to semantic similarity (BERT-based, classical IR approaches, novel approaches, e.g. KOOPMAN, Rob and WANG, Shenghui (2019) An innovative approach to scalable semantic embedding. Paper presented at: IFLA WLIC 2019 - Athens, Greece - Libraries: dialogue for change in Session S15 - Big Data. In: Data intelligence in libraries: the actual and artificial perspectives, 22-23 August 2019, Frankfurt, Germany. URL: http://library.ifla.org/2747/1/s15-2019-koopman-en.pd
* Enhanced conversion tools in the FoLiA ecosystem
* A multilingual UD pipeline (spacy, ....) enhanced with FoLiA input/output

(if known, describe what tools or functionalities you need to work with the data and do the research. Take the different stadia of the research into account, such as exploration phase, distant reading, close reading, annotating data, publishing, etc. Be as specific as possible)

### What software and services are involved?

* Autosearch
* Spacy
* LaMachine

### How to evaluate this?

Evaluation of enhancements to AutoSearch will be initially conducted iteratively by members of Betti’s team, experts in the thought of Wolff and 18th century philosophy, Kant, Bolzano, Russell, and Quine. It will be guided by a cluster of questions to be designed iteratively, starting with e.g. the following:

* To what extent do the enhancements to AutoSearch support your data-driven research in the history of ideas? 

In particular:

* To what extent does the enhanced AutoSearch enable you to construct a concept-based ground truth in the sense of Betti et al. (2020) for the corpus you are studying?
* How intuitive and helpful is it to use the expert CQL tab? Or do the Advanced search capabilities cover your advanced search needs?
* How often do you resort to the HitPaRank module for retrieving a ranked set of paragraphs containing the same key words? (every time - sometimes - never)
* How would you rank the option of checking the images of the original text you are analysing (absolutely key - useful - moderately useful - not useful at all)
* Do you see yourself publishing a paper in a top-ranked venue in your field relying substantially on AutoSearch’s variety of semantic searches? If your answer is ‘No’, can you explain why?

## References

References to related resources and publications and especially links to related use-cases:

* [CLARIAH](https://clariah.nl)

* Expert Concept-Modeling Ground Truth Construction for Word Embeddings Evaluation in Concept-Focused Domains. Betti, A., Reynaert, M., Ossenkoppele, T., Oortwijn, Y., Salway, A., & Bloem, J. In Proceedings of the 28th International Conference on Computational Linguistics, pages 6690–6702, Barcelona, Spain (Online), December, 2020. International Committee on Computational Linguistics.


