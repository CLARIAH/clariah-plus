# ASR for sensitive data

## Metadata

* **Status:**  In Progress
* **Type:** Specific
* **Work Package**: WP3
* **Research Coordinators:**  Henk van den Heuvel, CLST/Radboud  University
* **Coordinators for CLARIAH:**  Henk van den Heuvel, CLST/Radboud  University
* **Participating Institutes:** Clst, Radboud University; University of Utrecht
* **End-users**: Researchers from U Utrecht, depts social sciences, medical faculty, all researchers usig interviews with sensitive recordings
* **Developers**: Henk van den Heuvel, Louis ten Bosch, Maarten van Gompel (RU), Johan Rietveld (UU)
* **Interest Groups**: AV-processing
* **Task IDs**: T031, T227

## Description

Interview data are widely used as research instrument. Fast and accurate transcriptions are a deeply felt need. 
Automatic speech recognition (ASR) can resolve this issue but is not at the stage the it results in transcriptions of sufficient quality. 
Nonetheless, ASR transcriptions can help if users only need to scan the contents of the interview for relevant topics, or as the starting point for more accurate transcriptions. In this use case we will focus on two aspects of an existing speech transcription facility in the CLARIAH infrastructure (https://webservices.cls.ru.nl/oralhistory): 
1.	Technical: What are additional wishes from users regarding quality of transcriptions, textual output and time stamps, speaker information
2.	Confidential: Wat are scenarios to process sensitive speech data, i.e. data with sensitive personal information about e.g. medical or criminal records of people.  


### What is the research about?

CLST at Radboud University has started a project with the University of Utrecht to explore these issues. We have chosen a setup where the webportal (https://webservices.cls.ru.nl/oralhistory) is used in case of non-personal sensitive data, and a more secure route is chosen for (highly) sensitive data by which audio and resulting transcripts are transferred via encrypted channels and the ASR runs behind the walls of the webportal. The procedure involves:
-	Setting up an appropriate data processing agreement
-	With a protocol to treat sensitive data via encrypted transfers
-	Technical: Reporting about quality of the transcriptions and requests for other output options
-	Security: Are both routes needed for security reason or can we convene to the webportal solution for all cases and do we need adaptations of the portal for highly sensitive recordings  


### What problem is hindering the research?

Technical issues regarding quality of the speech recognition and the format of the text output as desired by various researchers, and security issues for sensitive data.

### What is needed to do the research?

A secure solution for transferring and processing the data.

#### Data

Interviews collected at U Utrecht by individual researchers are used for the use case

#### Tools

https://webservices.cls.ru.nl/oralhistory

https://clarin.phonetik.uni-muenchen.de/apps/TranscriptionPortal/ 

### What software and services are involved?

https://webservices.cls.ru.nl/oralhistory

https://clarin.phonetik.uni-muenchen.de/apps/TranscriptionPortal/ 

https://filesender.surf.nl/ 


### How to evaluate this?

User satisfaction (researchers). We will ask the users of the proposed solution how they evaluate the quality of the resulting transcriptions, which improvements they would like in terms of the output of the speech recognizer and the ergonomics of the interface and background service. 

Legal satisfaction (legal advisors of U Utrecht & Radboud University and CLARIN’s CLIC)


## References

References to related resources and publications and especially links to related use-cases:

Van den Heuvel, H. (2020) Crossing the SSH Bridge with Interview Data. Proceedings Workshop LR4SSHOC, at the 12th International Conference on Language Resources and Evaluation (LREC2020).p.42-44. https://lrec2020.lrec-conf.org/media/proceedings/Workshops/Books/LR4SSHOCbook.pdf  (invited contribution)

* [CLARIAH](https://clariah.nl)
