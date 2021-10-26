# Tool Discovery & Deployment

## Two services

* Discovering tools
* Deploying tools (includes Tools to Data)

Tool is defined in the broadest sense; any software

## Tool Discovery

* **User story**: *As a scholar, I* am looking for tools and want to browse through and search in a registry of available tools *in order to* select the tools I need to further my research.
* **Implementations**: Ineo, CLARIN switchboard, LaMachine portal, CLAPOP
* **Discussion points**:
    * Automatic harvesting of software/service metadata
    * Central forcus on Ineo as CLARIAH-wide solution (including concerns)
    * Collaboration in the CLARIN switchboard

## Tool Deployment/Tools to Data

* **User stories:**
    * *As a scholar*, I want to execute tools on data *in order to* be able to do some specialised analysis/processing on the data. *However*, the data may have restricted access, i.e. I can’t move it to my own computing environment or that of a third party. To facilitate this, the tools need to be *deployed either at my institute or on my local machine*.
    * *As a scholar,* I want to execute tools in my own computing environment (e.g. on my own laptop) in order to work with data which I can’t move to an external computing environment
    * (and some more devops-oriented stories for WP2)
* **Implementations**:
    * Docker containers
    * LaMachine
    * Kubernetes as deployment infrastructure, Helm charts, kubernetes-as-a-service (rancher)
* **Discussion Points**:
    * Infrastructure/software requirements

