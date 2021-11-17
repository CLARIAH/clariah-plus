# Providing Language and Speech webservices at CLST (Radboud University, Nijmegen)

## Metadata

* **Status:**  In Progress
* **Type:** Specific
* **Work Package**: WP2, WP3, WP5
* **Coordinators:** Henk van den Heuvel, Maarten van Gompel
* **Participating Institutes:** CLST (Radboud University, Nijmegen), Stichting Open Spraaktechnologie
* **End-users**: Researchers
* **Developers**: Maarten van Gompel
* **Interest Groups**:  DevOps, Text Processing, Audiovisual Processing
* **Task IDs**: T018 (New CLARIN Centre CLST Nijmegen), T098 (LaMachine), T142 (CLAM)

## Description

This use case concerns making available a wide variety of language & speech webservices developed within CLARIAH, its
predecessors and other projects. The Centre for Language and Speech Technology (CLST) at Radboud University provides
infrastructure in the form of various webservices. These are available through https://webservices.cls.ru.nl

In order to build webservices for individual tools, we mostly use [CLAM](https://proycon.github.io/clam). This offers
both a RESTful web API as well as a web interface for human end users. CLAM is optimised for batch processing and less
suitable for low-latency services, although we do use it for many speech recognizers as well (wrapping
[kaldi](https://kaldi-asr.org).

All our webservices and all their dependencies are in turn are deployed through
[LaMachine](https://proycon.github.io/LaMachine). This ensures a certain amount of integration and inter-connectivity
between webservices. It also offers a single [portal](https://webservices.cls.ru.nl) to provide access to all the
services.

### What problems are addressed in this use-case?

The problems that we solved in this use case are:

* How to quickly create both webservices and provide a generic web user interface for the end-user?
    * We use [CLAM](https://proycon.github.io/clam) as a solution to this, this is a generic solution that works for
        many use-cases
* How to deploy the webservices for production use?
    * We use [LaMachine](https://proycon.github.io/lamachine) as a solution to this, this is a generic solution that
        works for many use-cases.
    * LaMachine with all desired webservices is deployed as a single LXC container on a single high-end server (512GB RAM, 64 cores)
* How to dynamically build a portal based on software metadata where users can browse and access the services?
    * We use [codemeta](https://codemeta.github.io) to record software metadata for all tools included in LaMachine. The
        software metadata is kept as close to the source or providing repository as possible and automatically
        converted where needed.
    * [LaMachine](https://proycon.github.io/lamachine) gathers the software metadata of all software installed within
        it and discloses it as a single registry (just one big JSON-LD graph file)
    * [Labirinto](https://github.com/proycon/labirinto) dynamically provides a simple portal page on the basis of this collected
        metadata registry. It offers a very limited form of faceted search.
    * We include also links to certain services that are external to the LaMachine installation and not managed by it
* How to track service use/popularity?
    * LaMachine incorporates a [simple and public analytics solution](https://webservices.cls.ru.nl/lamastats/) that
      was custom-built.

Open problems are:

* We are currently still running our own non-federated authentication scheme. This is sub-optimal and work is being done
  to eventually move to the federated authentication infrastructure.
* Our scalability is limited, we are running on one dedicated high-end server on a first-come-first-serve basis with a fair use policy. In practise, this proves quite sufficient.

### What software and services are involved?

* [CLAM](https://proycon.github.io/clam) - A framework to build webservices
* [LaMachine](https://proycon.github.io/lamachine) - The deployment solution
    * [Linux Containers](https://linuxcontainers.org/) - The specific form of our deployment
    * [Ansible](https://ansible.org/) - The main tool that powers LaMachine
* [Labirinto](https://github.com/proycon/labirinto) - The portal software integrated into LaMachine
* [Lamastats](https://github.com/proycon/lamastats) - The custom analytics solution integrated into LaMachine

The individual services we offer build on a wide variety of tools, various of them developed in the scope of CLARIAH. A full
overview of those is beyond the scope of this use case.

### What hardware is involved?

A single high-end server with 512GB RAM and 32x AMD EPYC 7452 32-Core Processor (64x hyperthreaded) and a service
contract with the science faculty's departement of [Computer & Communicatiezaken](http://cncz.science.ru.nl/).

## References

References to related resources and publications and especially links to related use-cases:

* [CLARIAH Task T018: New CLARIN Centre CLST Nijmegen](https://github.com/LanguageMachines/clariah-plus-tasks/blob/master/clst/T018.CLARIN-Centre-CLST.md)
* [Language and Speech Tools](https://webservice.cls.ru.nl) (the webservice portal)


