# Exploring Dialect2Keyword

## Metadata

* **Status:**  Proposed
* **Type:** Specific
* **Work Package**: WP3
* **Research Coordinators:**  Prof. Nicoline van der Sijs, Dr Henk van den Heuvel, Prof. Jos Swanenberg
* **Coordinators for CLARIAH:**  ??
* **Participating Institutes:** INT, Radboud University, U Tilburg
* **End-users**: Transcription volunteers at INT & Erfgoed 
* **Developers**: Humanities Lab, Radboud University
* **Interest Groups**: Annotation; Curation
* **Task IDs**:T008

## Description

Both for semantics and interoperability of (digital) dialect dictionaries it is of paramount interest that dialect entries are coupled to appropriate keywords. 
In T008 of CLARIAH-PLUS CLST at Radboud University develops a webtool that automatically converts dialect entries into keywords. 
A first version of this tool offers two estimates of a keyword. 
The first estimate is based on minimizing edit distances moving from the dialect entry to (existing) keywords and trained on Saxon dialects in the Netherlands; 
the second estimate is based on a phonetisaurus WFST approach and trained on available training material from various dialects all over the Netherlands as included in the eWND.  

This version of the tool is now available at https://dialect2keyword.cls.ru.nl/ 

Volunteers at INT and Erfgoed Brabant will use the tool and give feedback for improvements. Also volunteers involved in WALD (Woordenboek Achterhoekse en Liemers dialecten) will evaluate the tool.


### What is the research about?

The project concerns linguistics, in particular dialectology and lexicography. 
The research question is: how can researchers bypass the diverse spelling conventions for the various existing dialect forms, 
and is it possible to develop a tool, using machine learning, that semi-automatically adds the standard Dutch forms? 
This tool could be used for the dialectwebsite eWND: http://ewnd.ivdnt.org/boeken/ and for enriching and opening up existing dialect surveys. 

In the eWND a growing number of old and modern dialect dictionaries are presented. 
The aim of the eWND is to make as many dialect dictionaries as possible digitally available and searchable, 
so that linguists can consult all important Dutch dialect dictionaries at one central point. 
The many dialect dictionaries that have been compiled from the nineteenth century onwards usually only describe the vocabulary of a particular place, 
sometimes of a somewhat larger region, but they never cover the entire Dutch-speaking area. The eWND will eventually do that: 
within the eWND all existing dictionaries will be linked to one large network, and the node for this is the Standard Dutch form that is added to each dialect lemma. 
The resulting network provides an easy overview of the spread of dialect words, sounds, conjugations, and inflections (such as plurals and diminutives) over the Dutch language
area. Via the eWND it is possible to compare the language use from different regions. 
The fact that the eWND contains both old and new dialect dictionaries also reveals changes that dialects have undergone over time. 
To do this, the researcher does not need to have knowledge on the (ever changing) spelling conventions of the various dialects, 
but s/he can find the relevant information though the Standard Dutch forms.


### What problem is hindering the research?

Up till now the Standard Dutch forms were added by hand by trainees or volunteers, resulting in a golden standard. 
Connecting dialect entries is a tedious and laborious task for volunteers. 
They would be helped with a tool that speeds up their work. Ideally, perfect keyword attribution is done automatically, 
but the quality of automatically generated keywords is not sufficient for unsupervised use. Therefore, volunteers will be helped with a tool that 

*	Is web-based and does not require any installation
*	Has easy upload and download facilities 
*	Comes up with meaningful suggestions for keywords
*	Allows easy copy/paste and editing facilities for suggested keywords


### What is needed to do the research?
As part of T008 CLST has developed a first version of such a tool (see above). This tool will now be evaluated by volunteers working on keyword attribution with respect to

*	Quality of the proposed keywords
*	User transparency
*	Efficiency
*	The result when used for non-Saxon dialects

Volunteers will be engaged to evaluate the tool as part of their tasks in ongoing keyword annotation projects running at INT and Erfgoed Brabant, and for WALD.

#### Data

To make the tool more generic, it will be adjusted to other, non-Saxon dialects, specifically to dialects spoken in Brabant, Utrecht and Holland. Therefore, volunteers will test the tool on the one hand for new Saxon dialects (specifically from the WALD, together with Erfgoedcentrum Doetinchem), and one the other hand with non-Saxon dialects, in collaboration with Erfgoed Brabant and erfgoedvrijwlliger.nl. For this test, new data (new dialect dictionaries) will be made available for the volunteers, and the volunteers will add Standard Dutch forms, using the tool. The results will be added to eWND for all researchers to use, and be available in open access.

#### Tools

https://dialect2keyword.cls.ru.nl/ 

### What software and services are involved?

https://dialect2keyword.cls.ru.nl/ 

### How to evaluate this?

Satisfaction of the end users (volunteers) and their supervisors in an iterative process of evaluation and tool improvement. 

## References

References to related resources and publications and especially links to related use-cases:

Hout, R. van, Sijs, N. van der, Komen, E., Heuvel, H. van den (2018) A Fast and Flexible Webinterface for Dialect Research in the Low Countries. In Proceedings LREC 2018, Miyazaki, 7-10 May 2018, pp. 3617-3621.

