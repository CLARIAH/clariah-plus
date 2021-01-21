# CLARIN Centre deployment of PICCL

## Metadata

* **Status:**  Completed
* **Type:** Specific
* **Work Package**: WP3
* **Coordinators:** Peter Dekker  (INT), Maarten van Gompel (Radboud)
* **Participating Institutes:** INT, Radboud University
* **End-users**: INT
* **Developers**: Maarten van Gompel (Radboud), Martin Reynaert (UvT)
* **Interest Groups**: DevOps, Text
* **Task IDs**: T098 (LaMachine), PICCL

## Description

### What is the research about?

Not a research project, but rather a deployment project. Aim was to deploy PICCL, which is distributed through LaMachine.

This was the first instance of deployment of LaMachine at a CLARIN centre, and came at a point in time where LaMachine
development was just in a major transition.

### What problem is hindering the research?

At the time, LaMachine was still on version 1 and deployment on the desired distribution (CentOS 7) was not possible
yet. This influenced the development of LaMachine v2, which would be powered by Ansible just like the technology INT was
already using for deployment, and would be made to work with CentOS 7.

### What is needed to do the research?

#### Tools

Needed was CentOS 7 support for LaMachine, CLARIN authentication (was not actually implemented in LaMachine but solved as an
additional middleware layer on top of the deployment)

### What software and services are involved?

* LaMachine
* PICCL

### How to evaluate this?

Some evaluation remarks from the internal report:


> "Code changes in LaMachine and PICCL proved a major challenge for the installation. LaMachine consists of a large
> number of interdependent packages with own versions. With every fresh installation, the latest releases of all
> packages are downloaded. This means that an installation on Tuesday can be different from an installation on
> Wednesday. Although understandable from a development point of view, this provides some difficulties for production
> deployment." [1]

> "The development of LaMachine v2 and deployment of PICCL at the INT overlapped time-wise. Whilst on the one hand
> this caused some delay in deployment, on the other hand it provided an excellent collaboration between the two
> CLARIAH partners and an great testing bed for LaMachine v2 in real-life production scenarios that could not have
> been otherwise accomplished." [1]

> "At first, we tried to directly call the LaMachine Ansible playbook from our own playbook, in order to get more
> transparent error messages during installation. However, as this was not the recommended way of installing
> LaMachine, it resulted in unexpected errors. We reverted to calling the LaMachine bootstrap script from our
> playbook.". [1]

> "In our setup, it is convenient to be able to upgrade LaMachine, if there is a new version of LaMachine, PICCL or
> one of the tools.". [1]

> "During PICCL deployment, we learned several lessons, which we will now summarize, as recommendations for future
> projects. Firstly, we benefited from the use of a configuration management tool (in our case Ansible) to get a
> reproducible installation. Secondly a stable code base of the software which should be installed is needed, for
> example by version pinning. Thirdly, it is important to test the deployment always under the same conditions, to
> prevent errors at later stages. Fourthly, it is good to pay extra attention to fit the hardware to the requirements
> of the application." [1]

## References

References to related resources and publications and especially links to related use-cases:

1. Peter Dekker - Development of PICCL (internal report)
