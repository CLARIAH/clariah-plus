# Tools to the data: Text Mining for Health Inspection

## Metadata

* **Status:**  Completed
* **Type:** Specific
* **Work Package**: WP3
* **Coordinators:**  Iris Hendrickx (Radboud University)
* **Participating Institutes:** Radboud University, Dutch Health Inspectorate
* **End-users**: Dutch Health Inspectorate
* **Developers**: Iris Hendrickx (Radboud), Maarten van Gompel (Radboud)
* **Interest Groups**: DevOps, Text
* **Task IDs**: T098 (LaMachine), T139 (Frog)

## Description

### What is the research about?

Citation from M. van Gompel & I. Hendrickx (2018):

> We participated in a small Dutch national project titled “Text mining for Inspection: an exploratory study on automatic
> analysis of health care complaints” led by IQhealthcare42, the scientific centre for healthcare quality of RadboudUMC
> hospital. This project took place at the Dutch Health Inspectorate and aimed to apply text mining techniques to health
> care complaints that have been registered at the national contact point for health care (Landelijk Meldpunt Zorg).
>
> We investigated the usefulness of text mining to categorise and cluster complaints, to automatically determine the
> severity of incoming complaints, to extract patterns and to identify risk cases. This project turned out to be a good
> test case of the applicability and usefulness of LaMachine as a standalone research environment. As the complaint data
> is highly sensitive, it could not leave the secure servers of the health inspectorate and was stored in an environment
> without internet access. We needed to bring the software to the data via a shared folder

### What problem is hindering the research?

The tools needed to be brought to a secure non-networked environment, on-site, because of the sensitive nature of the
data that had to be worked with.

The main functionality to bring the full environment to the data was already present with LaMachine, but the ability to have a shared
dataspace between the host and VM was insufficiently developed prior to this project.

### What is needed to do the research?

#### Tools

LaMachine was used as the solution to bring the tools to the data. Better integration between host and VM, with regards
to shared data space, was implemented.

### What software and services are involved?

* LaMachine
* Frog

### How to evaluate this?

The researcher has succesfully used the research environment in a restricted network-less environment in which she was
only offered a Windows machine, and processed privacy-sensitive data on-site with various tools.

## References

References to related resources and publications and especially links to related use-cases:

*  M. van Gompel & I. Hendrickx (2018). LaMachine: A meta-distribution for NLP software. CLARIN Annual Conference 2018.

