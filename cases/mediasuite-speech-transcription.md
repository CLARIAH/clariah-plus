# Speech transcription of audiovisual data

## Metadata

* **Status:**  In Progress
* **Type:** Generic
* **Work Package**: WP5/WP3
* **Research Coordinators:**  Jasmijn van Gorp
* **Coordinators for CLARIAH:**  Roeland Ordelman
* **Participating Institutes:** Netherlands Institute for Sound and Vision, Radboud Universiteit Nijmegen, Meertens Instituut, Universiteit Twente
* **End-users**: (Who is involved as end-user for this use-case? Try to mention name, institute, role/responsibility)
* **Developers**: Jaap Blom, Maarten van Gompel, Nanne van Noord, Martijn van de Donk, Willem Melder
* **Interest Groups**: Audiovisual Processing, DevOps
* **Task IDs**: (zero or more task IDs if this is addressed in existing CLARIAH-PLUS tasks)

## Description

A variety of scholarly research questions require what is sometimes called "semantic access": being able to track down which items (AV documents) in a collection are "about" a certain topic or mention specific keywords related to the topic. Ideally, also where in the document exactly these keywords are mentioned or topics discussed. Evidently this is especially the case with longer documents and large to very large AV data sets, such as the NISV archive, Oral History collections at DANS, or spoken word collections at Meertens Institute.      

For audiovisual data (radio & television broadcasts, oral history collections, spoken word collections), descriptive metadata that can be used for this type of fine-grained searching is typically sparse. Certain collections come with data that could be used  such as subtitles for the hearing impaired (recent television broadcasts) or manually generated speech transcripts (e.g., in context of Oral History). However, these data are either not used in the search system or are lacking time-codes to link directly to the AV document it relates to.  

In short and in general, researchers require improved search functionality on a semantic level of AV documents that is time-based or segment based. Following the model of scholarly primitives of Unsworth 2000, this use case is typically part of the "Discovering", "Annotating" and "Comparing" primitives of scholarly practice. Based on Palmer et al. 2009, this relates to the activities of "Searching" and "Collecting".  

(Unsworth 2000 Unsworth, J. Scholarly Primitives: what methods do humanities researchers have in common, and how might our tools reflect this? Symposium on Humanities Computing: formal methods, experimental practice sponsored by King's College, London, 13 May 2000.)

(Palmer et al. 2009 Palmer, C.L., L.C. Teffeau and C.M. Pirmann. Scholarly Information Practices in the Online Environment: Themes from the Literature and Implications for Library Service Development. 2009.)

### What is the research about?

The two initial use cases addressed in this context in CLARIAH are Media Studies and Oral History. However, the described use scenario is relevant to many other research domains, from psychology to linguistics.

### What problem is hindering the research?

To facilitate fine-grained access (e.g., time-based searching) to audiovisual data, speech in AV data can be decoded into text by applying automatic speech recognition technology (speech-to-text). However, commercial or available open-source systems for automatic speech recognition have serious limitations for use in scholarly research: they are expensive, lack quality that is required for the heterogeneous (Dutch) data scholars (in general) are interested in, are hard to use without technical know-how, cannot be easily applied to large collections, etc.    

When speech transcripts such as subtitles or manually generated transcripts are available, the problem is that these are often not aligned to the timings of speech in the AV documents (e.g., where a specific word is mentioned). 

### What is needed to do the research?


#### Data

(if known, describe the data that are needed for the intended research, be as specific as possible)

#### Tools

(if known, describe what tools or functionalities you need to work with the data and do the research. Take the different stadia of the research into account, such as exploration phase, distant reading, close reading, annotating data, publishing, etc. Be as specific as possible)

### What software and services are involved?

(if known, what existing software and services are involved, which need to be developed? Please link to the tools if possible and specify whether it can be used as is, needs extra work, needs to be developed from scratch etc.)

### How to evaluate this?

(How do we evaluate the solution to the problem?)

## References

References to related resources and publications and especially links to related use-cases:

* [CLARIAH](https://clariah.nl)
