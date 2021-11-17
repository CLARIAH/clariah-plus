# CLAM: Maintenance & Support

**ID**: T142

**Author:** Maarten van Gompel

**Introduction:**

CLAM is software that is used to develop RESTful webservices and similtaneously offer an web interface for human
end-users. CLAM expects a description of your system and wraps itself around your existing tool, allowing end-users or automated
clients to upload input files to your application, start your application with specific parameters of their choice, and
download and view the output of the application once it is completed. Unlike traditional low-latency webservices, CLAM is optimised
for long-running batch processes.

**What exists:**

CLAM has been in existence and under continuous active development since 2011, previousy funded by CLARIN-NL and
CLARIAH-CORE, and is widely used in CLARIAH.

**What must be adapted / extended / created anew:**

This is an ongoing support and development task that assures:

* Support is offered to all users/developers (both within and beyond CLARIAH) with any questions about CLAM
* Bugfixes and implementation of feature requests
* Further integration with the the CLARIN/CLARIAH infrastructure where there is a demand

**Why important for CLARIAH (scientific impact):** CLAM is used by many NLP webservices in and beyond of CLARIN/CLARIAH

**Targeted/Actual users:** Developers, service providers

**Actual use (quantify!):** Usage of the CLAM webservices hosted in Nijmegen (until September 2020) can be tracked in our [statistical report](https://applejack.science.ru.nl/lamastats/clamstats.html), does not include stats on any CLAM services hosted by other parties (and there are various)

**Lead**: Maarten van Gompel (DI, KNAW)

**Participants**: Maarten van Gompel (DI, KNAW)

**Estimated needed PMs:** 5PM (spread over the entire duration of the CLARIAH-PLUS project) (was 2PM)

**Actually Allocated PMs:** 3PM

## Deliverables

1. ``(T142D1)`` Software: [CLAM](https://github.com/proycon/clam)
    * ``(T142D1.1)`` [Documentation](https://clam.readthedocs.io/)

## Milestones

Due to the ongoing nature of this task, milestones are often defined as the task is ongoing, on the basis of reports from users, and completed in short development cycles. There are therefore no future milestones scheduled yet at this point.

1. ``(T142M1)`` [CLAM v3.0](https://github.com/proycon/clam/milestone/9) - October 2019 **(COMPLETED)** - Features a new modernized web interface with a better end-user experience

## Progress Reports

Detailed progression of this task is logged as part of our [regular progress reports](https://github.com/LanguageMachines/releasereport/tree/master/reports) .

## Changes

Changes with respect to the earlier plan:

* More extensive description and motivation of the task
* Added completed CLAM v3.0 milestone (which was not explicitly planned as such before)
* Since 14 July 2020 - This task has moved from CLST, Radboud University Nijmegen to Digital Infrastructure, Humanities
    Cluster, KNAW


## References

* M. van Gompel (2018). CLAM Documentation. Language and Speech Technoogy Technical Report Series 18-03. Radboud University - https://clam.readthedocs.io
