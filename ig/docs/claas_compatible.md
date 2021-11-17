# CLaaS Compatible
> Jauco Noordzij

CLaaS is a concept that deals with three problem domains:

1. How can the Clariah project ensure that an institution can host (part of) its software? And moreover: how can the institution integrate that software with the institute’s own, unique, data?
1. How can the Clariah software components become an integrated whole? How can we allow the user to seamlessly switch from one component to the next?
1. How can we balance the overhead of integration and quality with the need to improve, innovate and try new things?

## Making software CLaaS compatible

The CLaaS concept proposes to handle these problems using the following techniques:
1. To ensure that the software can be hosted by people who are not the developers
    1. the released artifacts of the software components should be in a standardised format. This is not just the binary, but also the ways that the binary interacts with the host system. So that someone who is not the original programmer is able to 
        1. launch it in a server environment
        1. “contain” the software, i.e. run it under non-root privileges in a container environment, behind a proxy that blocks most outgoing connections etc.
        1. monitor whether it is still running 
        1. inject a full data-store that is created by other tools than the software itself
        1. monitor it’s “health”, i.e. offset memory usage against expected values, monitor response times etc.
    2. Furthermore, someone other than the original developer should be able to provide fixes to the original software (given enough dedication and knowledge of the target domain and software platform). That means that they should have access to
        1. An environment without outside dependencies that allows them to recreate the build artifacts from the changed source code.
    3. Finally, most software is integrated in the real world using processes and procedures (i.e. for creating new users, cleaning up resources). The software release should contain documentation on
        1. What procedures the host organisation should put into place to successfully operate the software and how the technical side of the operations should be performed (i.e. what file needs to be created, where, in what format)
2. To allow the software components to integrate we need to make sure that they
    1. have a standardised way of sending (or fetching) their data to other components based so that the data in a piece of software is interchangeable with other CLaaS software that matches or overlaps in terms of functionality.
    1. Fulfill a unique niche in the infrastructure. It is clear for the user when to use which service.
    1. Are able to interact with each other on behalf of the user and are therefore able to have the user delegate authorization to them
3. The above two techniques will make the development process more costly. Therefore within CLaaS we balance the lifetime and usage of the software to the degree of integration that is being required of it. Simply put, a component that is being used by many others and/or that is kept online for multiple years will need to adhere more rigorously to points 1 and 2 then a small experiment. 

We take a proactive stance here. If the software does not score high on the above points it is terminated sooner and it will be served in such a way that not many tools can depend on it.

These points are rather handwavy. The Interest Groups were formed to elaborate them and make them concrete. In the IG providers and users collaborate to reach a level where the standard achieves these goals, while still being practical.


### Operationalization

Being “CLaaS compatible” therefore means that the first a judgement is made where the software is placed on the axis from “very experimental” to “very fundamental”. This is a decision by the CLARIAH board that is made based on information on the technical fit of the software within the infrastructure (as provided by the technical board) and the impact that it can have on the user’s work (as provided by the work packages 3 - 6). 

Based on that decision the software receives either requirements on quality and stability or requirements on “unstability”. Here we are talking about the "right to exist" of the applications and to what extent we think it is good that the application violates our own rules and what measures we take to limit its impact. If you remember the presentation, we say that an experiment does not have to adhere to any standards at all, but that it does not remain in the air as a service after the experiment has ended (and that only the buildbase + code + paper is published and is archived). Or that it is best to write a piece of software that does exactly the same as another existing piece of software, but that evaluation criteria and an evaluation moment are planned in which it is determined with which service the CLARIAH project will continue.

## Making institutes CLaaS compatible
