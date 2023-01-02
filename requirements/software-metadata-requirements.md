# CLARIAH Software Metadata Requirements and Instructions

## Introduction

This document specifies requirements and instructions for software metadata for
CLARIAH software and services. It is aimed at the developers of software and
attempts to provide clear documentation.

The software metadata from all of the sources within CLARIAH is harvested automatically,
and periodically, by [a harvesting
tool](https://github.com/proycon/codemeta-harvester). Subsequently, the
harvested metadata (codemeta) is made available in the tool store, which offers
an API that is in turn used by portals to present the tools.

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”,
“SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be
interpreted as described in [RFC
2119](https://datatracker.ietf.org/doc/html/rfc2119).

## Source Code Metadata Requirements

For all of the mentioned properties it in this section it holds that you *MUST
NOT* use other vocabularies to exclusively express these properties.

### 1. Software metadata *MUST* be kept as close to the source code as possible

The main principle underlying the way we keep our software metadata is that
**metadata is kept at the source and by the maintainers of the software**. This
means that the tool developers themselves are responsible for providing
accurate metadata and that the best place to keep this metadata is *with the
source code* of the software, in a version-controlled repository.

This is in line with current best-practices as most programming language
ecosystems already have their own ways of describing software metadata
alongside the source code. Further details on these best-practises and the
format of the metadata is expressed in other points below.

This also entails that if a third party wants to correct/revise the metadata, this is done via the tool
developers, typically a third part can simply do a pull/merge request on the source repository.

### 2. All tools *MUST* be registered in the Tool Store Registry

Tools MUST be *registered* with the harvester via the [Tool Source
Registry](https://github.com/CLARIAH/tool-discovery/tree/master/source-registry). This simple registry tells the
harvester where to find, for each tool, both the source code repository *and* any service endpoint(s) where the software is
hosted as a service (optional). In order to register your tool, you issue a simple pull request on our git repository as
explained in [these contribution guidelines](https://github.com/CLARIAH/tool-discovery/blob/master/CONTRIBUTING.md).

Note that we make this explicit distinction between *software* and *software as a service*, and we use the more
ambiguous term *tool* to describe either. The *software* metadata is described alongside its source code, the *service*
metadata is provided by a service endpoint and adds some information about a specific deployment of software as a
service. Software services may be served from multiple locations (e.g. the same software may be hosted by multiple
institutes).

When we say '*all tools*' in this context, we distinguish the following three
tiers and do not discriminate based on interface type, intended audience,
producer/provider, or otherwise:

1. Tools built in CLARIAH-PLUS. These *MUST* all be registered and we expect a high level of compliance with regard to these software (metadata) requirements.
2. Tools built in CLARIAH-CORE. These *MUST* all be registered and we expect a fair degree of compliance with regard to these software (metadata) requirements.
3. Tools built in other CLARIAH-related projects. This explicitly includes predecessors like CLARIN-NL but also extends to sister projects that make use of the CLARIAH infrastructure. These *SHOULD* be registered
and we request a certain degree of compliance with regard to our software (metadata) requirements.

### 3. Duplication of metadata *SHOULD* be avoided

We make use of those existing metadata descriptions and convert them
automatically to a unified [CodeMeta](https://codemeta.github.io/)
representation, which is a linked open data vocabulary built on top of
[Schema.org](https://schema.org).

What we want to prevent is that a developer or maintainer has to adapt
the same metadata in multiple places (and multiple paradigms).

### 4. Tool providers *MUST* adhere to the best practices in your programming language ecosystem and specify basic metadata in the way suited for your ecosystem

* For Python this is a ``setup.py``,``setup.cfg`` or ``pyproject.toml`` file
* For Java/Maven this is a ``pom.xml`` file
* For NodeJS/npm this is a ``package.json`` file
* For Rust this is a `cargo.toml` file

Adherence to best practises also entails what has already been started in the [software requirements](software-requirements.md):

* You MUST have a proper `README.md` file in all cases (Point 2 of the [software requirements](software-requirements.md))
* You MUST have `LICENSE.md` or `LICENSE` file in all cases (Point 3 of the [software requirements](software-requirements.md))
* You MUST release the software periodically with clear versions numbers, a git tag, and release notes (Point 4 of the [software requirements](software-requirements.md))

### 5. Tool providers *SHOULD* provide a codemeta.json or codemeta-harvest.json file

[Codemeta](https://codemeta.github.io) is a linked data (structured data) vocabulary on top of
[schema.org](https://schema.org) that is used for describing software metadata. More specifically, it describes a
software project on the source code level. This is the unified representation we use, along with some extensions and
more domain specific vocabulary of our own (explain in later points). Metadata from all other sources (see point 4) is
converted to this representation automatically by the harvester.

You *SHOULD* automatically generate this `codemeta.json` file by running our `codemeta-harvester` yourself. This can be
done as follows (assuming you use docker and are in the root directory of your project's source code):

``
docker run -v $(pwd):/data proycon/codemeta-harvester --regen
``

You *SHOULD* check and possibly edit this `codemeta.json` file after generation, ensuring it is correct and complies to
all the points in these requirements. After that is done you *MUST* add and commit it to the root of your source code
repository. Our harvester will harvest your `codemeta.json` periodically. Tool providers *MUST* therefore ensure the
`codemeta.json` is always kept up-to-date, especially the `version` property will by definition differ each release.
This typically means regenerating and editing/updating it every release. As this may be cumbersome, it is *RECOMMENDED*
to automate the regeneration part if you have a continuous integration/deployment system. However, automating the
editing is more problematic so there is an alternative:

The alternative is that tool providers *MAY* add and commit a `codemeta-harvest.json` instead of a `codemeta.json`. This `codemeta-harvest.json` file contains only the subset of what you want to add/edit on top of the automatically extracted metadata. The only disadvantage is that, unlike `codemeta.json` which is by definition complete, this requires use of our harvester on the side of the user who wants to make actual use of the full metadata.

Though use of the harvester is *RECOMMENDED*, you *MAY* also craft a `codemeta.json` by hand if you know what you are doing, or create one by filling the form of the [codemeta generator](https://codemeta.github.io/codemeta-generator/).
In line with point 3, whenever metadata is incorrect/incomplete, it is *RECOMMENDED* to solve it at the source (point 4)
if possible rather than in the `codemeta.json`. A typical `codemeta.json` file follows JSON-LD syntax and has a structure as shown in the following fairly minimal example:

```json
{
    "@context": [
        "https://doi.org/10.5063/schema/codemeta-2.0",
        "http://schema.org",
        "https://w3id.org/software-types",
        "https://w3id.org/software-iodata"
    ],
    "@id": "https://example.org/mysoftware",
    "@type": "SoftwareSourceCode",
    "identifier": "mysoftware",
    "name": "My Software",
    "description": "My software does nice stuff",
    "codeRepository": "https://github.com/someuser/mysoftware"
}
```

See the [Appendix](#Appendix) for a more elaborate example.

If no `codemeta-json` nor `codemeta-harvest.json` are provided at all, which is *NOT RECOMMENDED*, then our harvester will
construct it on the fly, this implies that the human verification and editing stage is missing and the metadata may be
more prone to being incorrect or incomplete.

### 6. Basic software metadata *MUST* be expressed

The following basic metadata *MUST* be expressed. That means it must be present in the ``codemeta.json`` that our harvester produces when processing your project, either because you provide an explicit `codemeta.json`, `codemeta-harvest.json` yourself (see previous point 5), or because the information is automatically harvestable from other metadata sources in your project. The [Appendix](#Appendix) contains an elaborate `codemeta.json` example that conforms to all these points:

1. The software *MUST* have a name. This is the name for presentation purposes and must be human readable
2. The software *MUST* have a (short) description. 
3. The authors of the software source code *MUST* be expressed. The authors are the main developers of the software.
    * If you're not using `codemeta.json` directly, then a simple text file named `AUTHORS` (at the root of your repository) with one author per line (``Full name <mail@provider.com>``) *MAY* be used.
    * You *SHOULD* use names of individual persons rather than institutions here. Individuals can be tied to institutions via the `affiliation` property.
4. A maintainer *MUST* be expressed. This is the person or persons who maintain the software. (Corollary of point 12 of the [software requirements](software-requirements.md))
    * If you're not using `codemeta.json` directly, then a simple text file named `MAINTAINERS` (at the root of your repository) with one maintainer per line (``Full name <mail@provider.com>``) *MAY* be used.
    * You *SHOULD* use names of individual persons rather than institutions here. Individuals can be tied to institutions via the `affiliation` property.
5. Software *MUST* have a code repository URL. (Corollary of point 1 of the [software requirements](software-requirements.md)). The single `SoftwareSourceCode` class in your `codemeta.json` *MUST* describe exactly one such code repository. 
6. Software *MUST* have a proper README (Corollary of point 2 of the [software requirements](software-requirements.md))
7. Software *MUST* state its license (Corollary of point 3 of the [software requirements](software-requirements.md))
    * If not expressed in 
8. Software *MUST* state its version (Corollary of point 4 of the [software requirements](software-requirements.md))

In addition, the following basic metadata is *RECOMMENDED*:

9. Software source code *SHOULD* link to a continuous integration service that builds the software and runs the software's test (Corollary of point 9 of the [software requirements](software-requirements.md))
10. All contributors *SHOULD* be expressed. Contributors are everyone who contributed to the code base, no matter how minor.
    * Our harvester will automatically extract all contributors from the git history. Additionally, aside from `codemeta.json` or `codemeta-harvest.json`, a simple text file named `CONTRIBUTORS` (at the root of your repository) with one contributor per line (``Full name <mail@provider.com>``) can be used.
    * You *SHOULD* use names of individual persons rather than institutions here. Individuals can be tied to institutions via the `affiliation` property.

The following are *OPTIONAL*:

11. You *MAY* express the programming language(s) used

*Note:* We consider basic metadata to be the metadata properties that codemeta defines or uses, and have grouped those together here. Most of these are typically extracted automatically by our harvester pipeline.

### 7. Development status *MUST* be expressed

The `developmentStatus` property is defined by codemeta and expresses in what stage of development the software is. It
communicates what level of functionality *and* what level of support the user can expect. Codemeta recommends the use of
the [repostatus.org](https://www.repostatus.org/) vocabulary and for CLARIAH that is *REQUIRED*. Simple Assessment
criteria are available on the [repostatus](https://www.repostatus.org) website, along with instructions on how to encode
this information in your own `README.md` as a so-called *badge*. The use of such a badge is *RECOMMENDED*. Once such a
badge is present in your README, our harvester will automatically detect and extract it.

In the `codemeta.json`, this is expressed as follows, for example:

```json
{
    "developmentStatus": "https://www.repostatus.org/#active"
}
```

In addition, we *RECOMMEND* adding a second `developmentStatus` property expressing a technology readiness level, see point 15.

### 8. A producer *SHOULD* be expressed

Please set the `producer` property to the `Organization` that produced the software, i.e. the organization(s) that employ(s)
the developers. Note that this may be distinct from the `provider` of the software as a service! Do not set CLARIAH as
the producer, as that is a project rather than an institute.

Syntax examples for your `codemeta.json`:

```json
    "producer": {
        "@type": "Organization",
        "name": "KNAW Humanities Cluster",
        "url": "https://huc.knaw.nl"
    }
```

This also allows a fair degree of nesting in case you want to express it in more detail:

```json
 "producer": {
        "@type": "Organization",
        "name": "Centre for Language and Speech Technology",
        "url": "https://www.ru.nl/clst",
        "parentOrganization": {
            "@type": "Organization",
            "name": "Centre for Language Studies",
            "url": "https://www.ru.nl/cls",
            "parentOrganization": {
                "name": "Radboud University",
                "@type": "Organization",
                "url": "https://www.ru.nl",
                "location": {
                    "@type": "Place",
                    "name": "Nijmegen"
                }
            }
        }
 }
```
You can keep things shorter and just express an URI, but ideally this should then resolve to some linked data representation using `schema:Organization`:

```json
{
    "producer": "https://huc.knaw.nl"
}
```
### 9. An interface type *SHOULD* be expressed

Software may present various interfaces types for different kinds of use and different audiences. For instance, there are
command-line tools, web-applications, desktop GUI tools, web APIs, software libraries and mobile apps. Such an interface
type *SHOULD* be explicitly expressed in the metadata.

The harvester is smart enough to detect terms such as *"web application"*, *"webservice"*, *"command line application"*
or *"library"* from the `description` property of the metadata, and convert it to a more formal representation,
effectively providing a quick shortcut to expressing interface type.

The `targetProduct` property is used to tie software source code to specific instantiations of the software that are 
the product of the source code, in some fashion. The following example illustrates three types of target products which
are provided by the source code whose metadata is being described:

```json
    "targetProduct": [
        {
            "@type": "CommandLineApplication",
            "name": "My software",
            "executableName": "mysoftware"
        },
        {
            "@type": "SoftwareLibrary",
            "name": "My software",
            "executableName": "mysoftware"
        },
        {
            "@type": "WebApplication",
            "name": "My software",
            "url": "https://example.org/mysoftware",
            "provider": {
                "@type": "Organization",
                "name": "My Organization",
                "url": "https://example.org"
            }
        }
    ],
```

**Note:** This use of `targetProduct` and the specific software interface types is an extension on top of codemeta/schema.org and not in widespread use yet. It is initially proposed in [this issue](https://github.com/codemeta/codemeta/issues/271). The software types that are not in schema.org yet are being defined in [the software types repo](https://github.com/SoftwareUnderstanding/software_types), more specifically in [this JSON-LD file](https://github.com/SoftwareUnderstanding/software_types/blob/main/software-types.jsonld). Most types are subclasses of [schema:SoftwareApplication](https://schema.org/SoftwareApplication). The property `executableName` is also additional vocabulary we created and its use is *RECOMMENDED*, it defines the executable filename (no full path) of the application.

See the section on [service metadata requirements](#service-metadata-requirements) to understand the relation between
software source code and service instances like web applications, web APIs and websites.

### 10. Documentation *SHOULD* be expressed

If there is any kind of documentation available aside from the mandatory
README, then it *SHOULD* be expressed using the ``softwareHelp`` property. 
This is the corollary of point 11 of the [software requirements](software-requirements.md))
A very common scenario is when the documentation is on some external website (in
which case you can use `@type: Website`), for example:

```json
    "softwareHelp": [
        {
            "@id": "https://frognlp.readthedocs.io",
            "@type": "WebSite",
            "name": "Introduction — frog documentation",
            "url": "https://frognlp.readthedocs.io"
        }
    ]
```

For scientific publications, see the next point instead.

### 11. Reference publications *SHOULD* be expressed

If the software can be linked to one or more scholarly publications that
describe it, then this *SHOULD* be done using codemeta's
``referencePublication`` property, which takes a
[schema:ScholarlyArticle](https://schema.org/ScholarlyArticle) as object. This
enables citation of publications related to the software, which may be
preferable in certain circumstances to direct citation of only the software
itself.

Example:

```json
    "referencePublication": {
        "@type": "ScholarlyArticle",
        "sameAs": "https://doi.org/10.1080/non.existant",
        "name": "An efficient memory-based morphosyntactic tagger and parser for Dutch",
        "author": [ "Antal van den Bosch", "Bertjan Busser", "Sander Canisius", "Walter Daelemans" ],
        "pageStart": "99",
        "pageEnd": 114,
        "isPartOf": {
            "@type": "PublicationIssue",
            "datePublished": "2007",
            "name": "Selected Papers of the 17th Computational Linguistics in the Netherlands Meeting",
            "location": "Leuven, Belgium"
        },
        "url": "http://ilk.uvt.nl/downloads/pub/papers/tadpole-final.pdf"
	}
```

You *SHOULD* include a [DOI](https://www.doi.org/index.html) whenever possible, either as ``@id`` or using the `sameAs` property.

### 12. You *MAY* specify screenshots/screencasts and thumbnails using existing vocabulary from schema.org and codemeta.

For links to screenshots or screencasts of the application, use the [screenshot property](https://schema.org/screenshot) with a full URL. The links *MUST* use HTTPS.

```json
{
    "screenshot": "https://example.org/screenshot.jpg"
}
```

For thumbnails with for example the software's logo, use [thumbnailUrl property](https://schema.org/thumbnailUrl):

```json
{
    "thumbnailUrl": "https://example.org/thumbnail.jpg"
}
```

### 13. System requirements *SHOULD* be expressed 

Software does not exist in isolation but runs on certain hardware and is dependent on certain other software.
The metadata should express these via the following properties. You *MAY* use any and *SHOULD* use those that are very relevant to your software's functioning:

* ``runtimePlatform`` - Runtime platform or script interpreter dependencies (for example: Java 8, Python 3.10). Use the property multiple times if specifying multiple platforms.
* ``operatingSystem`` - Operating systems supported (for example: Linux, macOS 10.6, Android, Windows 11). Use the property multiple times if specifying multiple operating systems. You *MUST NOT* add any operating systems that are only supported via virtualisation.
* ``browserRequirements`` - Specifies browser requirements in human-readable text. For example, 'requires HTML5 support'. Used for software that is served as a web application.
* ``permissions`` - Specifies permission requirements on the host OS in human-readable text. For example, 'requires camera access'. Used for software that is served as a web or mobile application.

These schema.org properties are first and foremost meant to be informative to the user rather than machine-actionable. It is up to the software developer to determine how specific to be.

* ``softwareRequirements`` - This property links software source code to other software dependencies (``SoftwareApplication`` instances), that are needed to run the software.

In addition to software requirements, you *MAY* use any of the following properties to express hardware constraints, and *SHOULD* use them if they are important to your software's functioning:

* ``processorRequirements`` - Processor architecture required to run the application (e.g. x86_64). May also state a minimum number of cores.
* ``memoryRequirements``- Minimum memory requirements.
* ``storageRequirements``- Minimum storage requirements (free disk space).

We recognize that such requirements are often hard to formulate and may be very dependent on factor such as input data, parameter selection and the level of concurrency. Descriptions are textual and *MAY* add clarifications.

You use these properties either directly on ``SoftwareSourceCode``, or on specific ``SoftwareApplication`` resources via ``targetProduct``, as explained in Point 9.


Consider the following fictitious example that illustrates all of the above:

```json
{
    "@context": [
        "https://doi.org/10.5063/schema/codemeta-2.0",
        "http://schema.org",
        "https://w3id.org/software-types",
    ],
    "@type": "SoftwareSourceCode",
    "name": "MySpeechRecognizer",
    "codeRepository": "https://github.com/someuser/MySpeechRecognizer",
    ...,
    "operatingSystem": [ "Linux", "BSD", "macOS" ],
    "runtimePlatform": "Python >= 3.6",
    "softwareRequirements": [
        { 
            "@type": "SoftwareLibrary",
            "name": "transformers",
            "producer": {
                "@type": "Organization",
                "name": "Huggingface",
            },
            "version": ">= 4.20",
        },
        { 
            "@type": "SoftwareLibrary",
            "name": "SciPy",
            "version": ">= 1.8",
        }
    ],
    "processorRequirements": "x86_64",
    "memoryRequirements": "1GB",
    "permissions": "Requires microphone access",
    "storageRequirements": "20GB (included models are large)",
    "targetProduct": [
        {
            "@type": "CommandLineApplication",
            "executableName": "transcribe",
            "name": "My Speech Recognition Tool",
        },
    ]
}
```

### 13. Funders *SHOULD* be acknowledged

If the project is funded by CLARIAH-PLUS, it should be expressed as follows in `codemeta.json`/`codemeta-harvest.json`:

```json
    "funding": {
        "@type": "Grant",
        "name": "CLARIAH-PLUS (NWO grant 184.034.023)",
        "funder": {
            "@type": "Organization",
            "name": "NWO", 
            "url": "https://www.nwo.nl"
        }
    }
```

Of course, any additional funders *SHOULD* also be acknowledged in a similar fashion. Here are some predecessors that might require acknowledgement:

* CLARIAH-CORE (NWO grant 184.033.101)
* CLARIN-NL (NWO grant 184.021.003)

## Prescribed extra vocabulary

There are a few additional metadata fields/properties and associated vocabulary
that we as CLARIAH want you to use. These fields are expected by the portal
tools that eventually present your software and they are usually *not
automatically extractable* from existing metadata schemas but need to be
*explicitly* specified by you as the tool developer (in `codemeta.json` or
`codemeta-harvest.json`). We call these *extra* vocabularies because they are
not defined by schema.org or codemeta, but often by us in CLARIAH itself.

### 14.  You *SHOULD* express input/output formats and languages

When your software consumes certain a data type as input and/or produces data
of a certain type. Then this information *SHOULD* be encoded in the metadata in accordance with the [software-iodata](https://github.com/SoftwareUnderstanding/software-iodata) extension to
codemeta/schema.org. This extension defines the `consumesData` and
`producesData` properties. The range of the properties is a
[schema:CreativeWork](https://schema.org/CreativeWork) (or any subclass),
offering a high degree of flexibility and re-use of existing schema.org
properties. This allows expressing content/encoding types (MIME types), but
also natural languages.

It is *RECOMMENDED* to encode this on the `targetProduct` level. Consider a
fictitious speech recognition tool (on the command line) for English, producing
plain text transcriptions:

```json
{
    "@context": [
        "https://doi.org/10.5063/schema/codemeta-2.0",
        "http://schema.org",
        "https://w3id.org/software-types",
        "https://w3id.org/software-iodata"
    ],
    "@type": "SoftwareSourceCode",
    "name": "MySpeechRecognizer",
    "codeRepository": "https://github.com/someuser/MySpeechRecognizer",
    ...,
    "targetProduct": [
        {
            "@type": "CommandLineApplication",
            "executableName": "transcribe",
            "name": "My Speech Recognition Tool",
            "runtimePlatform": "Linux"
            "consumesData": {
                "@type": "AudioObject",
                "encodingFormat": "audio/mp3",
                "inLanguage": {
                     "@id": "https://iso639-3.sil.org/code/eng",
                     "@type": "Language",
                     "name": "English"
                     "identifier": "eng",
                }
            },
            "producesData": {
                "@type": "TextDigitalDocument",
                "encodingFormat": "text/plain",
                "inLanguage": {
                     "@id": "https://iso639-3.sil.org/code/eng",
                     "@type": "Language",
                     "name": "English"
                     "identifier": "eng",
                }
            }
        },
    ]
}
```

Note that the metadata description does not go into detail on what
entrypoints/endpoints are used and is not a substitute for a full API
specification. Multiple input and output types may be specified but their
precisely relation is not captured.

For the data types, the use of the following types available in schema.org is *RECOMMENDED*:

* [AudioObject](https://schema.org/AudioObject)
* [VideoObject](https://schema.org/VideoObject)
* [ImageObject](https://schema.org/ImageObject)
* [3DModel](https://schema.org/3DModel)
* [TextDigitalDocument](https://schema.org/TextDigitalDocument)
* [PresentationDigitalDocument](https://schema.org/PresentationDigitalDocument)
* [SpreadsheetDigitalDocument](https://schema.org/SpreadsheetDigitalDocument)
* [Dataset](https://schema.org/Dataset)


### 15.  You *SHOULD* express a technology readiness level 

The *Technology Readiness Level* (TRL) expresses how mature or ready the
software is, including the technological solution that the software implements.
This is interpreted more from a user-perspective than a developer perspective.
This is expressed using `developmentStatus`, which we have used before with the repostatus vocabulary.
The difference between the two vocabularies is that the repostatus vocabulary places a strong focus on a *maintenance* dimension (which
is fully absent in the TRL) and where software is in its development cycle, the
TRL vocabulary places more emphasis on *maturity* and
*validation* in scientific
settings. 

The Technology Readiness Levels are grouped into four broad stages (1-4) and 10 more
narrowly defined levels (0-9). You *MAY* point to either a stage or one of the
levels. Each stage/level has a badge, it is *RECOMMENDED* to put this badge in your `README.md` (you can copy the markdown from the source of this document), our harvester will automatically detect it then.

* **Planning stage** *(pre-alpha)* - The technology is in an initial planning stage (pre-alpha), no implementation is available yet - `https://w3id.org/research-technology-readiness-levels#Stage1Planning` - ![Technology Readiness Stage 1/4 - The technology is in an initial planning stage (pre-alpha), no implementation is available yet](https://w3id.org/research-technology-readiness-levels/Stage1Planning.svg)
    * *0 - Idea* - Unproven, untested and largely unformulated concept - `https://w3id.org/research-technology-readiness-levels#Level0Idea` - ![Technology Readiness Level 0/9 - Idea - Unproven, untested and largely unformulated concept](https://w3id.org/research-technology-readiness-levels/Level0Idea.svg)
    * *1 - Initial Research* - Basic (scholarly) needs observed and reported - `https://w3id.org/research-technology-readiness-levels#Level1InitialResearch` - ![Technology Readiness Level 1/9 - Initial Research - Basic (scholarly) needs observed and reported](https://w3id.org/research-technology-readiness-levels/Level1InitialResearch.svg)
    * *2 - Concept Formulated* - Initial technology/application's concept has been formulated - `https://w3id.org/research-technology-readiness-levels#Level2ConceptFormulated` - ![Technology Readiness Level 2/9 - Concept Formulated - Initial technology/application's concept has been formulated](https://w3id.org/research-technology-readiness-levels/Level2ConceptFormulated.svg)
* **Proof of Concept stage** *(alpha)* - An initial proof-of-concept implementation of the technology is available (alpha). It is not mature enough for end-users yet. - `https://w3id.org/research-technology-readiness-levels#Stage2ProofOfConcept` - ![Technology Readiness Stage 2/4 - An initial proof-of-concept implementation of the technology is available (alpha). It is not mature enough for end-users yet.](https://w3id.org/research-technology-readiness-levels/Stage2ProofOfConcept.svg)
   *  *3 - Proof of Concept* - Initial Proof-of-concept of key functionality . Concept presented for initial feedback from scholarly users. Not yet validated and not suitable for end-users yet. - `https://w3id.org/research-technology-readiness-levels#Level3ProofOfConcept` - ![Technology Readiness Level 3/9 - Proof of Concept - Initial Proof-of-concept of key functionality . Concept presented for initial feedback from scholarly users. Not yet validated and not suitable for end-users yet.](https://w3id.org/research-technology-readiness-levels/Level3ProofOfConcept.svg)
   *  *4 - Validated Proof of Concept* - Validated Proof-of-concept of key functionality. Technology validated in its own experimental setting (e.g. the lab). Not mature enough for end-users yet.- `https://w3id.org/research-technology-readiness-levels#Level4ProofOfConcept` - ![Technology Readiness Level 4/9 - Validated Proof of Concept - Validated Proof-of-concept of key functionality. Technology validated in its own experimental setting (e.g. the lab). Not mature enough for end-users yet.](https://w3id.org/research-technology-readiness-levels/Level4ValidatedProofOfConcept.svg)
* **Experimental stage** *(beta)* - The technology is implemented and ready for experimental settings (beta), but requires further work and validation - `https://w3id.org/research-technology-readiness-levels#Stage3Experimental` - ![Technology Readiness Stage 3/4 - The technology is implemented and ready for experimental settings (beta), but requires further work and validation](https://w3id.org/research-technology-readiness-levels/Stage3Experimental.svg)
   * *5 - Early Prototype* - Technology validated in target setting (e.g. with potential end-users) - `https://w3id.org/research-technology-readiness-levels#Level5EarlyPrototype` - ![Technology Readiness Level 5/9 - Early Prototype - Technology validated in target setting (e.g. with potential end-users)](https://w3id.org/research-technology-readiness-levels/Level5EarlyPrototype.svg)
   * *6 - Late Prototype* - Technology demonstrated in target setting, end-users adopt it for testing purposes.- `https://w3id.org/research-technology-readiness-levels#Level5LatePrototype` - ![Technology Readiness Level 6/9 - Late Prototype - Technology demonstrated in target setting, end-users adopt it for testing purposes](https://w3id.org/research-technology-readiness-levels/Level6LatePrototype.svg)
   * *7 - Release Candidate* - Technology ready enough and in initial use by end-users in intended scholarly environments. Further validation in progress. - `https://w3id.org/research-technology-readiness-levels#Level7ReleaseCandidate` - ![Technology Readiness Level 7/9 - Release Cancidate - Technology ready enough and in initial use by end-users in intended scholarly environments. Further validation in progress.](https://w3id.org/research-technology-readiness-levels/Level7ReleaseCandidate.svg)
* **Completed stage** *(stable)* - The technology is complete, stable and deployed in production scenarios for end-users - `https://w3id.org/research-technology-readiness-levels#Stage4Complete` - ![Technology Readiness Stage 4/4 - The technology is complete, stable and deployed in production scenarios for end-users](https://w3id.org/research-technology-readiness-levels/Stage4Complete.svg)
   * *8 - Complete* - Technology complete and qualified, released for all end-users in scholarly environments. - `https://w3id.org/research-technology-readiness-levels#Level8Complete` - ![Technology Readiness Level 8/9 - Complete - Technology complete and qualified, released for all end-users in scholarly environments.](https://w3id.org/research-technology-readiness-levels/Level8Complete.svg)
   * *9 - Proven* - Technology complete and proven in practice by real users - `https://w3id.org/research-technology-readiness-levels#Level9Proven` - ![Technology Readiness Level 9/9 - Proven - Technology complete and proven in practise by real users](https://w3id.org/research-technology-readiness-levels/Level9Proven.svg)

This ontology is defined using SKOS and can be found [here](https://w3id.org/research-technology-readiness-level).

You *SHOULD* pick only one of the above URIs and inject it into your codemeta as in the following example, or use the appropriate badge and add it to your `README.md`:

```
{
    "developmentStatus": "https://w3id.org/research-technology-readiness-levels#Stage3Experimental"
}
```

### 16.  You *SHOULD* express a TaDiRAH research activity as category

The *research activity* is expressed using the
[TaDiRaH](https://vocabs.dariah.eu/tadirah) ontology. This is used by the DARIAH project,
adopted by Ineo, and formulated in SKOS. It consists of the following top-level categories:

* [Analyzing](https://vocabs.dariah.eu/tadirah/analyzing)
* [Capturing](https://vocabs.dariah.eu/tadirah/capturing)
* [Creating](https://vocabs.dariah.eu/tadirah/creating)
* [Disseminating](https://vocabs.dariah.eu/tadirah/disseminating)
* [Enriching](https://vocabs.dariah.eu/tadirah/enriching)
* [Interpreting](https://vocabs.dariah.eu/tadirah/interpreting])
* [Storing](https://vocabs.dariah.eu/tadirah/storing)

Each is subdivided into multiple subcategories (and deeper levels). Click the links above and pick from
any of them the ones (multiple allowed) that cover your tool, preferably from
the deeper levels, and add it as a category to your codemeta as follows. You
*MUST* use the exact URI of the TaDiRaH concept here.

```
{
    "applicationCategory": "https://vocabs.dariah.eu/tadirah/enriching"
    "applicationCategory": "https://vocabs.dariah.eu/tadirah/structuralAnalysis"
}
```

You *SHOULD* express at least one category using TaDiRaH and you *MAY* also
express additional categories using any other vocabularies.

### 17.  You *SHOULD* express a research domain as a category

Research domains are also expressed using `applicationCategory` using the [NWO
research fields vocabulary](https://www.nwo.nl/en/nwo-research-fields). A
[formal ontolology (SKOS) is
available](https://github.com/CLARIAH/tool-discovery/blob/master/schemas/nwo-research-fields.jsonld).
When specifying a research domain, you *MUST* specify the URI (starting with
`https://w3id.org/nwo-research-fields#`). The quickest way to find it is by
first picking a category from the NWO site, noting its six-digit number, and
then looking it up in the JSON-LD file and copying the `@id` there. For example
for *Software for humanities* (37.10.00):

```
{
    "applicationCategory": "https://w3id.org/nwo-research-fields#SoftwareForHumanities"
}
```

You *MAY* pick from either the fine-grained categories (each has a six digit
number) or from the top-level categories. The following is just a non-exhaustive excerpt of a
few categories (with URIs) that might be relevant for CLARIAH:

* **Linguistics** - `https://w3id.org/nwo-research-fields#Linguistics` - (Work Package 3)
    * **Phonetics and phonology** - `https://w3id.org/nwo-research-fields#PhoneticsAndPhonology` 
    * **Morphology, grammar and syntax** - `https://w3id.org/nwo-research-fields#MorphologyGrammarAndSyntax`
    * **Computational linguistics and philology** - `https://w3id.org/nwo-research-fields#ComputationalLinguisticsAndPhilology`
    * **Psycholinguistics and neurolinguistics** - `https://w3id.org/nwo-research-fields#PsycholinguisticsAndNeuroLinguistics`
    * **Language teaching and acquisition** - `https://w3id.org/nwo-research-fields#LanguageTeachingAndAcquisition`
* **History** - `https://w3id.org/nwo-research-fields#History` 
* **Philosophy** - `https://w3id.org/nwo-research-fields#Philosophy` 
* **Communication Science** - `https://w3id.org/nwo-research-fields#CommunicationScience` 
* **Computer Science** - `https://w3id.org/nwo-research-fields#ComputerScience` 
    * **Artificial intelligence, expert systems** - `https://w3id.org/nwo-research-fields#ArtificialIntelligenceExpertSystems` 
* **Computers and the Humanities** - `https://w3id.org/nwo-research-fields#ComputersAndTheHumanities` 
    * **Software for the Humanities** - `https://w3id.org/nwo-research-fields#SoftwareForTheHumanities` 
    * **Textual and content analysis** - `https://w3id.org/nwo-research-fields#TextualAndContentAnalysis`  (Work Packages 3 and 6)
    * **Textual and linguistic corpora** - `https://w3id.org/nwo-research-fields#TextualAndLinguisticCorpora` (Work Packages 3 and 6)
    * **Databases for humanities** - `https://w3id.org/nwo-research-fields#DatabasesForHumanities`
    * **Hypertexts and Multimedia** - `https://w3id.org/nwo-research-fields#HypertextsAndMultimedia`
* **Music, theatre, performing arts and media** - `https://w3id.org/nwo-research-fields#MusicTheatrePerformingArtsAndMedia` (Work package 5)
    * **Film, photography and audio-visual media** - `https://w3id.org/nwo-research-fields#FilmPhotographyAndAudioVisualMedia`
    * **Journalism and mass communications** - `https://w3id.org/nwo-research-fields#JournalismAndMassCommunications`
    * **Media studies** - `https://w3id.org/nwo-research-fields#MediaStudies`

You *MAY* specify multiple research domains.

## Service metadata requirements

We have seen that providing metadata for the source code is done using `codemeta.json` (or `codemeta-harvest.json`) in
the source code repository. This is the primary source for metadata. However, for *software as a service* such as web
applications, webservices and possibly even simple web pages, we may want to provide some additional metadata *on top of*
the data already provided alongside the source code.

Most notably, the source code does not know where and when it is deployed, i.e. who hosts it where. The link between the
source code and the service instances comes from the [Tool Source
Registry](https://github.com/CLARIAH/tool-discovery/tree/master/source-registry) (see point 2) and is provided by the tool
producer/provider when registering. It may be that that is already enough information but it is possible to have web
endpoints provide extra metadata.


### 18. Software as a service endpoints *MUST* provide metadata

Software as a service *MUST* provide some metadata through an endpoint, at least a name, description, and provider
(see point 19 of the [software requirements](software-requirements.md)). The metadata needs not be as extensive as provided at the source code level, as by definition each
service is associated with some source code from which it derives most metadata. The registration in the tool source
registry (see point 2) is what links these two.

An endpoint with metadata *MUST* be publicly available without authentication barriers.

Specifying service metadata can be done in a variety of ways, in alignment with existing industry standards:

* Add a `<script type="application/ld+json">` block in your HTML and specify a single resource of one of the following
   `@type`s:
    * `schema:SoftwareApplication`
    * `schema:WebApplication`
    * `schema:WebAPI`
    * `schema:WebSite`
    * `schema:WebPage`
  This is the most explicit form to provide service metadata and the only one that ensures that all metadata ends up in the harvested end-product.
* Register an endpoint that provides an [OpenAPI specification](https://www.openapis.org/), our harvester will extract some metadata (the info block mainly)
* Register a [CLAM](https://proycon.github.io/clam/) webservice, our harvester will extract some metadata.
* Use standard HTML `<meta>` tags to express metadata, as well as a `<title>`. Our harvester will parse and extract these as much as possible.

Some examples, first of all an inline JSON-LD block:

```html
<script type="application/ld+json">
{
    "@context": "http://schema.org/",
    "@type": "WebApplication",
    "name": "My tool",
    "description": "This is a web application",
    "url": "https://example.org/my/tool",
    "provider": {
        "@type": "Organization",
        "name": "My institute"
    }
}
</script>
```

Or using structured data embedded in HTML using [microdata](https://html.spec.whatwg.org/multipage/microdata.html):

```html
<html itemscope itemtype="http://schema.org/WebApplication">
<head>
    <title>My tool</title>
    <meta itemprop="name" content="This is a web application" />
    <meta itemprop="description" content="This is a web application" />
    <meta itemprop="author" content="John Doe" />
    <meta itemprop="provider" content="My institute" />
</head>
```

or using [RDFa](https://www.w3.org/TR/rdfa-primer/):

```html
<html vocab="http://schema.org">
<head>
    <title>My tool</title>
    <meta property="name" content="This is a web application" />
    <meta property="description" content="This is a web application" />
    <meta property="author" content="John Doe" />
    <meta property="provider" content="My institute" />
</head>
```

or plain HTML:

```html
<head>
    <title>My tool</title>
    <meta name="description" content="This is a web application" />
    <meta name="author" content="John Doe" />
</head>
```

As you see, the current codemeta-harvester attempts to be as flexible as possible.


### 19. Software as a service *MUST* specify a provider

Please set the `provider` property to the `Organization` that provides the software, i.e. the institutes that makes it available as a service on their infrastructure. Note that this may be distinct from the `producer` that produces the software!

Syntax is analogous to `producer` as listed before.

### 20. Software as a service *SHOULD* specify extra metadata if it was omitted on the source level

You *MAY*  express a `technologyReadinessLevel` (point 15) and a research
domain (point 17) and research activity (point 16) at the service metadata
level (e.g. as properties on `schema:SoftwareApplication` or any of the
others). Especially for `technologyReadinessLevel` this makes sense as a there
may be service provider specific circumstances (uptime/downtime, security
checks) that have an impact on the Technology Readiness Level.

If for some reason you have not yet expressed this at the source level, then
you *SHOULD* even express these on this service level instead.

## Appendix

### Codemeta JSON-LD Example

This is an example of a codemeta JSON-LD file which you can use as a template or reference:

```json
{
    "@context": [
        "https://doi.org/10.5063/schema/codemeta-2.0",
        "http://schema.org",
        "https://w3id.org/software-types",
        "https://w3id.org/software-iodata",
        "https://w3id.org/research-technology-readiness-levels"
    ],
    "@id": "https://example.org/mysoftware",
    "@type": "SoftwareSourceCode",
    "identifier": "mysoftware",
    "name": "My Software",
    "description": "My software does nice stuff",
    "codeRepository": "https://github.com/someuser/mysoftware",
    "url": "https://example.org/my-software-website",
    "issueTracker": "https://github.com/someuser/mysoftware/issues",
    "license": "https://spdx.org/licenses/GPL-3.0-only",
    "developmentStatus": "https://www.repostatus.org/#active",
    "author": {
        "@type": "Person",
        "givenName": "John",
        "familyName": "Doe"
    },
    "producer": {
        "@type": "Organization",
        "name": "My Organization",
        "url": "https://example.org"
    },
    "maintainer": {
        "@type": "Person",
        "givenName": "John",
        "familyName": "Doe"
    },
    "operatingSystem": [ "Linux", "Windows", "macOS", "BSD" ],
    "processorRequirements": [ "x84_64", "aarch64" ] ,
    "memoryRequirements": "2GB",
    "runtimePlatform": "Python >= 3.6",
    "programmingLanguage": "Python",
    "softwareRequirements": [
        {
            "@type": "SoftwareLibrary",
            "name": "Some required library",
            "version": ">= 2.3"
        },
    ],
    "softwareHelp": [
        {
            "@id": "https://example.readthedocs.io",
            "@type": "WebSite",
            "name": "My example documentation",
            "url": "https://example.readthedocs.io"
        }
    ],
    "targetProduct": [
        {
            "@type": "CommandLineApplication",
            "name": "My software",
            "executableName": "mysoftware"
        },
        {
            "@type": "SoftwareLibrary",
            "name": "My software",
        },
        {
            "@type": "WebApplication",
            "name": "My software",
            "url": "https://example.org/mysoftware",
            "provider": {
                "@type": "Organization",
                "name": "My Organization",
                "url": "https://example.org"
            }
        }
    ],
    "funding": {
        "@type": "Grant",
        "name": "CLARIAH-PLUS (NWO grant 184.034.023)",
        "funder": {
            "@type": "Organization",
            "name": "NWO", 
            "url": "https://www.nwo.nl"
        }
    },
    "dateCreated": "2022-04-29T14:57:10Z+0200",
    "dateModified": "2022-04-29T14:57:10Z+0200"
}
```




