# Historical research on media-events across heterogenous broadcast datasets with linked and missing data

## Metadata

* **Status:**  In Progress
* **Type:** Generic
* **Work Package**: WP5
* **Research Coordinators:**  Alexander Badenoch, Jasper Keijzer
* **Coordinators for CLARIAH:**  Jasmijn Van Gorp, Roeland Ordelman
* **Participating Institutes:** UU, NISV, and KB for omroepgidsen
* **End-users**: Media historians, NISV, KB, educators, journalists
* **Developers**: NISV
* **Interest Groups**: Audiovisual processing, Text processing, Annotation, Linked Open Data, IG Uncertainty and reliability
* **Task IDs**:

## Description

Media historians need a variety of contextual datasets to conduct research, such as broadcast magazines (programme guides), viewing and listening rates, streamed content, and newspapers.

In our case study, we will look into programming strategies of Dutch public broadcast radio and television in relation to specific events.

We do this in five phases:

- Phase 1: determining the event such as nature disasters (Tchernobyl), societal crisis (oil crisis) or planned events (moon landing, Our World, Eurovision Song Competition)

- Phase 2: finding the broadcasts of the (live) event

- Phase 3: collecting automatically all structured data information on the broadcast. This requires probably a linked data through the title of the broadcast, the event and the related persons in all different heterogeneous collections.

- Phase 4: analysing the links between the broadcast, conduct data and tool criticism, and detect the anomalies in the data

- Phase 5: visualizing certain links and visualizing missing data (gaps, conflicting data, uncertainty in data, …)


### What is the research about?

Research on media events is key in many media historical research projects. Historians need to gather different type of sources to document the event.

In this particular case we will investigate the role of disrupting events in media history, by focusing on programming and viewing/listening data, which both show programming strategies as well as reflecting audience reactions.

Computationally, we will look into the potential of linking heterogeneous broadcast collections and linked data on the one hand, and visualization of missing data across different datasets on the other hand.


### What problem is hindering the research?

The different datasets are not yet linked. The datasets need to be linked by programme title.

Challenges of the quality of the digitized data:
1. The dataset of OCR’d viewing and listening rate reports has some unclear and missing data

2. The OCR of broadcast magazines is sometimes unclear and ambiguous.

We do not have yet a Jupyter Notebook for visualizations in place for broadcast magazines or viewing and listening rates..

### What is needed to do the research?

- Set up a pilot study on linking the NISV broadcasts archive with the broadcast magazines and the viewing reports to link them through programme titles

- Have visualization libraries for structured data in place in the Jupyter Notebooks

- Have research done on visualisations of digitized heritage collections, with a focus on missing data visualisations.


#### Data

- Broadcast magazines (1930s-current)
- Viewing and listening rates (1930s-current)
- Broadcasts
- Delpher newspapers: tv and radio programming schedules, broadcast magazines 1930s-1950s


#### Tools

- Media Suite Jupyter Notebook
- Media Suite Resource Viewer
- Media Suite Workspace


### What software and services are involved?

A Jupyter Notebook
Automatic links between NISV datasets


### How to evaluate this?

(How do we evaluate the solution to the problem?)

## References

References to related resources and publications and especially links to related use-cases:

On media events and programming:
* Dayan D. & Katz E. Media Events: The Live Broadcasting of History (Harvard UP 1992)
* Scannell, P Radio Television and Modern Life (Blackwell 1996)

Interesting parallels to BBC programme guides (genome) and mass observation data: [https://www.bbc.co.uk/historyofthebbc/100-voices/radio-reinvented/listening-to-radio](https://www.bbc.co.uk/historyofthebbc/100-voices/radio-reinvented/listening-to-radio)
