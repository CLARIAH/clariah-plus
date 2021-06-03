# Use cases for the Virtual Research Environment

## Introduction

In this document we collect actual specific use cases for the proposed Virtual Research
Environment. Which researchers require what specific functionality to conduct
their research?

Generic use-cases are already part of the [VRE plan](plan.md) and described as *user stories*.

## Template

* **Researcher names & affiliations:**
* **Research question/project:** (short description)
* **What functionality is desired and currently missing?**
* **What tools/services are used in this project?**
* **Is this in the scope of the VRE project?**
* **What needs to be implemented?**
* **How can we evaluate this?**
* **References (issue/ticket link, publications):**

The first questions are mostly for the researchers to fill, please provide the text in italics if it's a direct quote from the user.

## Open Use Cases

These are use cases that are still open:

## Rejected Use Cases

These are use cases that are have been rejected because they are either to big for the VRE scope, or too small and
should be dealt with by upstream projects instead.

## Satisfied Use Cases

These is a selection of notable use cases that are already satisfied:

### Tools to the data: Text Mining for Health Inspection

* **Researcher names & affiliations:** Iris Hendrickx, Radboud University
* **Research question/project:**
*"We participated in a small Dutch national project titled “Text mining for Inspection: an exploratory
study on automatic analysis of health care complaints” led by IQhealthcare42, the scientific centre for
healthcare quality of RadboudUMC hospital. This project took place at the Dutch Health Inspectorate
and aimed to apply text mining techniques to health care complaints that have been registered at the
national contact point for health care (Landelijk Meldpunt Zorg) We investigated the usefulness of
text mining to categorise and cluster complaints, to automatically determine the severity of incoming
complaints, to extract patterns and to identify risk cases. This project turned out to be a good test case of
the applicability and usefulness of LaMachine as a standalone research environment. As the complaint
data is highly sensitive, it could not leave the secure servers of the health inspectorate and was stored in
an environment without internet access. We needed to bring the software to the data via a shared folder"* [1]
* **What functionality was desired and was missing?** The main functionality to bring the full environment was already present, but
the ability to have a shared dataspace between the host and VM was insufficiently developed prior to this project.
* **What tools/services are used in this project?** *"We used many of the available tools in LaMachine within this project: Frog for linguistic annotation of the textual content of the complaint and the scikit-learn Python package for classification, T-scan for
feature extraction in the form of text characteristics and colibri-core for n-gram analysis."* [1]
* **Is this in the scope of the VRE project?** yes, bringing tools to the data fits the scope.
* **What needed to be implemented?** Better integration between host and VM, with regards to shared data space.
* **How has this been evaluated?** The researcher has succesfully used the research environment in a restricted
    network-less environment in which she was only offered a Windows machine, and processed privacy-sensitive data
    on-site with various tools.
* **References (issue/ticket link, publications):**
    * **[1]** M. van Gompel & I. Hendrickx (2018). LaMachine: A meta-distribution for NLP software. CLARIN Annual Conference 2018.


### Research Environment for Workshop: Cataloguing of Textual Cultural Heritage Objects

* **Researcher names & affiliations:** Iris Hendrickx, Radboud University
* **Research question/project:** *"The ICT-Research Platform Netherlands and NWO organise a yearly one-week workshop ‘ICT with
Industry’ to stimulate collaboration between industry and academia. The industrial partner provides
a problem and a team of researchers from different backgrounds and universities collaborate to come
up with solutions. We participated in the 2019 edition on the case study by the Dutch Royal Library
who wanted to investigate automatic methods for cataloguing of textual cultural heritage objects, in this
particular case a large collection of digital dissertations."* [1]
* **What functionality was desired and was missing?** None, LaMachine was taken as an out-of-the-box solution.
* **What tools/services are used in this project?** Various *"common scientific data-related packages"* [1].
* **Is this in the scope of the VRE project?** yes, offering a common research enviroment for workshop participants fits
    the scope
* **What needed to be implemented?** Nothing
* **How has this been evaluated?** *"LaMachine offered a convenient platform for a range of different explorations and
experiments in
the area of NLP and text mining. However, for some situations LaMachine, or rather Linux in general, was not a good fit
for the audience of the workshop: for team members who did not have experience with a non-Windows environment, LaMachine
was not a suitable or useful tool. The limit of LaMachine was also reached for members who wanted to use desktop text
editors with a graphical user interface as this is not offered by LaMachine. Moreover, we did not manage to get
X-forwarding working in the Ubuntu Linux VM and after a few attempts the team gave up on resolving this issue due to
time pressure.  This, also demonstrates that fine-tuning the configuration of certain aspects of LaMachine, but
especially beyond LaMachine, is beyond the reach of a data scientist without system administration skills. This
certainly also applies also to the installation as a whole in the SURFsara context, which involved things like the
partitioning, formatting and mounting of (virtual) drives and setting up user accounts on the shared VM, all of which
require some system administration skills and are too context-specific to be within the scope of LaMachine. LaMachine
was convenient and speeded up writing code as the most common scientific data-related packages are already present in
LaMachine."* [1]
* **References (issue/ticket link, publications):**
   * **[1]** M. van Gompel & I. Hendrickx (2018). LaMachine: A meta-distribution for NLP software. CLARIN Annual Conference 2018.

### CLARIN Centre deployment of PICCL

* **Researcher names & affiliations:** Peter Dekker, INT
* **Research question/project:** Not a research project, but rather a deployment project. Aim was to deploy PICCL, which
    is distributed through LaMachine.
* **What functionality is desired and currently missing?** At the time, LaMachine was still on version 1 and deployment
    on the desired distribution (CentOS 7) was not possible yet. This influenced the development of LaMachine v2, which would be powered by Ansible just like the technology INT was already using for deployment, and would be made to work with CentOS 7.
* **What tools/services are used in this project?** PICCL
* **Is this in the scope of the VRE project?** yes, deployment of services to a CLARIN centre is in scope, even though
    it concerns just a single service (with a complex underlying workflow)
* **What needs to be implemented?** CentOS 7 support, CLARIN authentication (was not actually implemented in LaMachine but solved as an additional middleware layer on top of the deployment)
* **How can we evaluate this?** Some evaluation remarks:
    * *"Code changes in LaMachine and PICCL proved a major challenge for the installation. LaMachine consists of a large number of interdependent packages with own versions. With every fresh installation, the latest releases of all packages are downloaded. This means that an installation on Tuesday can be different from an installation on Wednesday. Although understandable from a development point of view, this provides some difficulties for production deployment."* [1]
    * "The development of LaMachine v2 and deployment of PICCL at the INT overlapped time-wise. Whilst on the one hand this caused some delay in deployment, on the other hand it provided an excellent collaboration between the two CLARIAH partners and an great testing bed for LaMachine v2 in real-life production scenarios that could not have been otherwise accomplished." [1]
    * *"At first, we tried to directly call the LaMachine Ansible playbook from our own playbook, in order to get more transparent error messages during installation. However, as this was not the recommended way of installing LaMachine, it resulted in unexpected errors. We reverted to calling the LaMachine bootstrap script from our playbook."*. [1]
    * *"In our setup, it is convenient to be able to upgrade LaMachine, if there is a new version of LaMachine, PICCL or one of the tools."*. [1]
    * *"During PICCL deployment, we learned several lessons, which we will now summarize, as recommendations for future projects. Firstly, we benefited from the use of a configuration management tool (in our case Ansible) to get a reproducible installation. Secondly a stable code base of the software which should be installed is needed, for example by version pinning. Thirdly, it is important to test the deployment always under the same conditions, to prevent errors at later stages. Fourthly, it is good to pay extra attention to fit the hardware to the requirements of the application."* [1]
* **References (issue/ticket link, publications):**
    * **[1]** Peter Dekker - Development of PICCL (internal report)
