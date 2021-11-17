# PaQuUD

**ID**: PAQUUD

**Author:** *Gertjan van Noord*

**Description of the proposed project:**

The PaQu Parse-and-Query website is an online resource for uploading Dutch corpora for automatic parsing and querying
the parsed output using XPath. It is meant to facilitate online access to and interaction with parsed corpora and
manually corrected treebanks.

The Dutch treebanks and the Dutch Alpino parser provide dependency annotation in the CGN/Lassy/Alpino format. This
format is the de-facto standard annotation format for Dutch, but in recent years, a novel standard format for dependency
annotation has become widespread: Universal Dependency. This format is now the standard dependency annotation format,
and treebanks for many languages are available in this format. Consider the listing at
http://universaldependencies.org/.

In the PaQuUd project, we propose to extend the PaQu tool with Universal Dependency annotation. This extension is
possible because it is possible to map the analyses in the CGN/Lassy/Alpino format to the UD format fully automatically.
The script aims at the basic UD2.0 format. For this project, we aim for the newer UD2.1 format, with extensions.

The following tasks are foreseen:

* Design of XML format which extends the alpino_ds format and includes all UD2.1 information.
* Adaptation of the Xquery script which maps the alpino_ds format to the UD2.1 format (including extensions).
* Integration of the new alpino_ds format in PaQu. The integration concerns two important aspects:
* Ability to query aspects of the UD analysis
* Ability to visualize the UD analysis

**Participants**:

* prof. dr. Gertjan van Noord - Principal Investigator
* drs. Peter Kleiweg - scientific programmer
* dr. Gosse Bouma

**Targeted start date**: 2019-1-1

**Targeted end date**: 2019-7-1

## Deliverables

* Deliverable PaQuUd1: Extended Alpino-ds XML format to include all information from the UD2.1 analysis. This deliverable takes the form of a formal specification of the format (DTD) and a short report with explanation and motivation. Date: February 1, 2019

* Deliverable PaQuUd2: Extended script which maps the Alpino-ds XML analyses to UD2.1 analyses, with extensions. This deliverable takes the form of a software package (most probably an Xquery script) with a short report. Date: July 1, 2019.

* Deliverable PaQuUd3: Extension of PaQu which allows both querying and visualization of aspects of the    Universal Dependency annotation. This deliverable takes the form of a software package. Date: July, 2019.


