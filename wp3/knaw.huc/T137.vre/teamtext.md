# Team Text and the WP3 VRE Plan

The VRE plan plan as currently proposed did not yet take into account any
significant extra manpower brought by Team Text or anyone else, and is a
project I could complete myself. However, now extra manpower is available, we
can make some enhancements to the plan. I propose a few in this document.

## Delegating existing proposed work

If we indeed have extra hands for this job then that would allow for more to be
accomplished and I suggest we widen the plan rather than attempt to delegate
some of the already proposed implementation work, which is mostly in my code
base and therefore much quicker for me to pick up than for someone new to dive
into or even for me to coordinate. Nevertheless, I start with a small overview
of deliverables (excerpts taken from the plan) that could be delegated to
others if need be:

* **Deliverable Implementation:** [clam#96](https://github.com/proycon/clam/issues/96) - Implement a CLAM forwarder to GreTeL 4 (which supports plain
    text, CHAT, and possibly also FoLiA and TEI by now?). The feasibility of this still requires some investigation.
* **Deliverable Implementation:**  [clam#97](https://github.com/proycon/clam/issues/97)- Implement a CLAM forwarder to PaQu. The feasibility of this still requires some investigation.
* **Deliverable:** ``D2`` - Provide documentation for end-users, preferably and at least in the form of screencast videos demonstrating the various user stories.

## Expanding the plan

It would be more logical to expand the plan and integrate extra tools that Team
Text has expertise on. My perspective on this is limited but I will attempt to
provide some suggestions:

* **MTAS** - This was developed in the scope of Nederlab. The user story that would go with this tool is similar to that of INT's AutoSearch: *The user has a text collection and wants to index and make it searchable*. There are some important questions to consider, though:
    * What is needed for integration in the VRE?
        * A generic indexing pipeline (as a webservice) for FoLiA XML (such as produced by Frog for instance) and possibly some variants of TEI. This can then be connected to various FoLiA-producing tools (Frog, Ucto, Alpino, Piereling, Valkuil, etc).
        * a CLAM forwarder to the MTAS indexing pipeline (possible a new CLAM webservice that wraps the indexing if MTAS does not provide this yet?)
        * Optional but recommended: integration into LaMachine if we want to make this easily distributable (tools to the data) in a single integrated platform with tighter integration between components. The alternative is to keep it as an independent remote service, a specific deployment somewhere and have tools in LaMachine interface with that.
    * What is the overlap between AutoSearch and MTAS? Does MTAS bring much added value?
    * What obstacles are there?
          * The first issue is the maintainership of MTAS considering its main developer left (although he still does a fair amount of maintenance fortunately); does Team Text intend to keep actively supporting, maintaining and developing the software?
          * Considering the huge amount of effort it already takes to index DBNL, how feasible is it to have MTAS and FoLiA indexing as pre-cooked component in a VRE?


* **TextRepo** - This seems to be the current important focus of Team Text. It may be worth investigating what role this could play in a VRE.
    * With what existing CLARIAH WP3 tools could this interact, and in doing so, what actual user problems does it solve?
    * What is needed for integration in the VRE?
        * a CLAM forwarder to TextRepo
        * Possibly: The ability in TextRepo to serialise data and invoke external services?
        * Optional but recommended: integration into LaMachine if we want to make this easily distributable (tools to the data) in a single integrated platform with tighter integration between components. The alternative is to keep it as an independent remote service, a specific deployment somewhere and have tools in LaMachine interface with that.

* **Archiving** - Archiving of results, in a proper and persistant repository (DANS? Zenodo?) or even in temporal cloud storage (S3?) is currently not provided in the VRE plan but could be a possible addition that may be valuable for researchers. With implementation of a CLAM forwarder to some archiving solution we would in one go have this for a wide variety of webservices. Similar additional implementations could be conceived in non-CLAM tools like FLAT.

* **Salvaging some of the initial VRE attempt** - There has gone considerable implementation work into the first VRE attempt, focusing on data management features that are entirely absent from my revised VRE plan. Is it worth and feasible reviving certain components of this? I'm quite skeptical of undertaking or coordinating any centralised data management features, but in the proposed plan does not prohibit such functionality from being added at a certain point.

