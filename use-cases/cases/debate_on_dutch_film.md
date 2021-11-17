# Sex, Beer and RomComs: Studying the Debate on Dutch film

## Metadata

* **Status:**  Proposed
* **Type:** Specific
* **Work Package**: WP2/WP3/WP4/WP5/WP6
* **Research Coordinators:**  Julia Noordegraaf (University of Amsterdam, department of Media Studies and CREATE Research program and lab, CLARIAH WP5 leader)
* **Coordinators for CLARIAH:**  Jasmijn Van Gorp, Roeland Ordelman
* **Participating Institutes:** Netherlands Institute for Sound and Vision (Media Suite; DANE), National Library of the Netherlands (Delpher), University of Amsterdam-CREATE (Cinema Context), Meertens Instituut/HuC (PICCL?), IISG & UU? (CoW, Cattle, Druid), Max Planck Institute (ELAN)
* **End-users**: This use case is based on Julia Noordegraaf’s book project on the use of digital data and methods for media historical research, where an analysis of the debate on Dutch film post WWII is the central case study. This use case aims to provide an example of the needs of media scholars and other humanities researchers doing historical research, combining different types of data (structured, text, audiovisual) and using different tools and methods. As such, it aims to provide a cross-WP perspective on the use of the CLARIAH infrastructure.
* **Developers**: For Media Suite: Jaap Blom, DANE: Nanne van Noord, Delpher: WP6?, PICCL: Martin Reynaert?,
CoW/Cattle/Druid: WP4? ELAN: Han?
* **Interest Groups**: Audiovisual processing, Text processing, Annotation, Linked Open Data, Workflows, Curation, User/UI/UX
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

This use case focuses on the longstanding debate on Dutch film. From its emergence in 1896 until today, Dutch fiction films have been heavily criticized for lack of quality, originality or ambition. Dutch films are labelled as ‘the mediocre of the mediocre’, lacking orginal scripts and good dialogue (Dijksterhuis 2019) and containing too much non-functional sex, beer and swearing (Fok.nl 2008). At the same time, over 90% of Dutch adults (over 16) and children (10-15 years) regularly watch Dutch films and of those only 15% express an explicit dislike for them (Scholtens & Verstraeten 2013). This raises the question of how to explain this discrepancy between, on the one hand, the negative image of Dutch film and, on the other, its evident popularity among Dutch audiences.  

An analysis of this discrepancy requires the study of the production (the content of the films themselves and the conditions under which they were produced), distribution (where were the films shown?) and reception (where and how were they seen and discussed?) of Dutch film. The idea is to discover longitudinal patterns in each of these three areas and to try and explain those via more in-depth case studies and contextual knowledge on Dutch cinema culture.

For each of these three dimensions of Dutch cinema culture, different types of data and different tools are required. As such, the use case demonstrates how a media historical researcher, or cultural historians more broadly, might approach the data and tools offered in the CLARIAH infrastructure across the different work packages.


### What is the research about?

This use case is situated in the domain of media studies, in particular the field of film history. It is the central case study in Julia Noordegraaf’s book project on the use of digital data and methods for media historical research. The research question is: ‘How can we explain the discrepancy between the consistently negative reception of Dutch film and its continued popularity among Dutch cinema audiences since 1945?’
Answering this question involves both methods for analyzing film content (such as film form and style analysis) and for analyzing the socio-economic and cultural context of film production, distribution and consumption. As such, the use case also relates to the domains of cultural history and socio-economic history. The language technologies and processing pipelines of linguistics are useful for the extraction of structured data from texts and the analysis of textual content (e.g. sentiment mining of film reviews or online forum discussions); so for linguistics the use case provides an example of how their tooling may be used in another academic discipline.

### What problem is hindering the research?

- The required data are not readily available;
- The available datasets are not in the same format so cannot be linked;
- There is a need for a sustainable and user-friendly triple store and SPARQL endpoint; Druid fulfills this need but is not yet set up for taking in user data of this scale?
- Certain software and services are not yet implemented in the CLARIAH infrastructure yet, hindering their use by non-technically skilled researchers (e.g., DIGIFIL processing pipeline);
- Some services (e.g., ASR, DANE) are not yet compatible with datasets brought in by the researcher (e.g. video data from ripped DVDs);
- There are no clear workflows for each of the steps or tasks, meaning that the researcher has to invent many wheels and is dependent on programming expertise provided by others.

### What is needed to do the research?

The research focuses on three distinct stages, each with its own type of data and tools for analysis:
1. Analysis of distribution of Dutch films 1945-2020 (in cinema theatres)
2. Analysis of reception of Dutch films 1945-2020 (newspapers/journals, RTV, online)
3. Analysis of content of Dutch films 1945-2020 (form and style analysis)

#### Data

1. **Analysis of distribution: extracting structured data on Dutch film screenings**

Distribution is here defined as ‘films shown in cinema theatres’ (for reasons of scope and consistency, television and streaming are left out of this use case). While the Cinema Context database at UvA-CREATE contains a lot of data on dutch cinema culture, including screening data until 1946, structured data on film screenings in Dutch cinemas post 1946 are not readily available. These data can be derived from the film listings in newspapers as accessible via Delpher (OCR of scans of newspaper pages); see under tools. For more contemporary screenings (post 2000), these data can be scraped from online platforms.

For identification a seed list is needed of all Dutch film titles, which is available via [Wikipedia](https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_films_per_decennium) or the [Internet Movie Database](IMDb, https://www.imdb.com).

2. **Analysis of reception: textual data**

For the reception of films, the following sources are relevant:
- Reviews in newspapers (via Delpher, until 1995; more recent data only via licenced Nexis database and in the future via TwiXL project (UvA-ASCoR collection of online news))
- Reviews in film journals (at EYE Film Institute; to which extent digitized?)
- Discussion of Dutch films on radio and television (Audiovisual Collection of RTV programs Netherlands Institute for Sound and Vision, available via the CLARIAH Media Suite: metadata and - where available - ASR transcriptions of spoken language)
- Reviews and debates on online film-related blogs and forums, Twitter and other social media platforms (have to be collected still)

3. **Content: audiovisual data**

The analysis of the content of the films relies on digital copies of Dutch films (presently only Desmet films available via the CLARIAH Media Suite; could be ripped versions of purchased DVDs used by researcher only), ideally enriched with annotations (face/object/motion/pose detection; shot boundary detection; framing analysis; ...) to do form and style analysis at scale.


#### Tools

0. **Corpus building**:

- For the extraction of structured data, we could use the processing pipeline developed in the CLARIAH-funded [DIGIFIL](https://gitlab.com/uvacreate/digifil) project. This allows for:
  - Locating the listings in newspaper: classifying the articles in the corpus as a film listing or other;
  - Parsing the listings: identifying the entities in them (film titles, names of cinemas, screening times, etc.);
  - Linking the film titles: linking extracted titles with entries in external databases such as the Internet Movie Database for identification and adding additional data (e.g., on cast).

- Alternatively, we could test the [PICCL](http://portal.clarin.nl/node/14392) pipeline (see also [GitHub](https://github.com/LanguageMachines/piccl) page) for the same purpose
- [CoW](https://github.com/CLARIAH/COW/wiki) or [Cattle](http://cattle.datalegend.net/) tools for transforming the csv data into rdf for linking the screenings to the film titles (Wikidata & IMDb) and other relevant Linked Open Datasets (e.g., film posters that form visual summaries of the films’ contents; see the HackaLOD 2020 [contribution](https://uvacreate.gitlab.io/cinema-context/cinema-context-rdf/events/hackalod2020/)).
- [Druid](https://druid.datalegend.net/) for storing and querying the linked datasets

1. **Distribution analysis**:
- Statistical analysis of film screening data (R and/or SPSS)
- Visualization software (e.g., [Tableau](https://www.tableau.com/) and/or [QGIS](https://www.qgis.org/en/site/)) for diagrams and maps of film screening data

2. **Reception analysis**:
- Discourse analysis of discussion of Dutch films in newspapers, on RTV and online: sentiment analysis, collocation networks (e.g., of films often cited together), …

3. **Content analysis**:
- [DANE](https://github.com/CLARIAH/DANE) for automatic annotation of Dutch film corpus with various features for ‘distant viewing’ of film style (Arnold & Tilton, 2020) (Arnold et al., 2019);
- [ELAN](https://archive.mpi.nl/tla/elan) for manual annotation of sample set of films, importing the automatically extracted features (such as shot boundary detection);
- Possible qualitative analysis of film posters as visual summary of film content (building on the HackaLOD 2020 ‘[Poster Wall](https://uvacreate.gitlab.io/cinema-context/cinema-context-rdf/events/hackalod2020/)’ project), e.g. supporting selecting samples for manual annotation.



### What software and services are involved?

(if known, what existing software and services are involved, which need to be developed? Please link to the tools if possible and specify whether it can be used as is, needs extra work, needs to be developed from scratch etc.)

- **DIGIFIL**: would need to be implemented in the CLARIAH infrastructure
- **PICCL**: assess if useful for the tasks listed above
- **Druid**: can this be used as the CLARIAH triple store and SPARQL endpoint?


### How to evaluate this?

(How do we evaluate the solution to the problem?)

## References

References to related resources and publications and especially links to related use-cases:

Arnold, Taylor, en Lauren Tilton. 2019. ‘Distant Viewing: Analyzing Large Visual Corpora’. Digital Scholarship in the Humanities. [https://doi.org/10.1093/digitalsh/fqz013](https://doi.org/10.1093/digitalsh/fqz013).

Arnold, Taylor, Lauren Tilton, en Annie Berke. 2019. ‘Visual Style in Two Network Era Sitcoms’. Journal of Cultural Analytics, juli. [https://culturalanalytics.org/article/11045-visual-style-in-two-network-era-sitcoms](https://culturalanalytics.org/article/11045-visual-style-in-two-network-era-sitcoms).

Dijksterhuis, E. (2019). ‘“Te veel romkoms, geen originele scripts en slechte dialogen”:
Enquête onder regisseurs, scenaristen en acteurs toont negatief zelfbeeld.’ Filmkrant, 27 February. [https://filmkrant.nl/nieuws/waar-leggen-we-de-lat/](https://filmkrant.nl/nieuws/waar-leggen-we-de-lat/).

Fok.nl. (2008). ‘De Nederlandse film, trots of beschamend?’ Forum debate, 23 October, [https://forum.fok.nl/topic/1211559](https://forum.fok.nl/topic/1211559).

Scholtens, J., & Verstraeten, P. (2013). Het publiek en de Nederlandse speelfilm: Een verkenning van de nationale markt. Stichting Filmonderzoek en Filmtest. [https://www.filmonderzoek.nl/wp-content/uploads/2013/10/Eindrapport-Het-publiek-en-de-Nederlandse-speelfilm.pdf](https://www.filmonderzoek.nl/wp-content/uploads/2013/10/Eindrapport-Het-publiek-en-de-Nederlandse-speelfilm.pdf).




* [CLARIAH](https://clariah.nl)
