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
docker run -v .:/data proycon/codemeta-harvester --regen
``

You *SHOULD* check and possibly edit this `codemeta.json` file after generation, ensuring it is correct and complies to
all the points in these requirements. After that is done you *MUST* add and commit it to the root of your source code
repository. Our harvester will harvest your `codemeta.json` periodically. Tool providers *MUST* therefore ensure the
`codemeta.json` is always kept up-to-date, especially the `version` property will by definition differ each release.
This typically means regenerating and editing/updating it every release. As this may be cumbersome, it is *RECOMMENDED*
to automate the regeneration part if you haved a continuous integration/deployment system. Howeveer, automating the
editing is more problematic so there is an alternative:

The alternative is that tool providers *MAY* add and commit a `codemeta-harvest.json` instead of a `codemeta.json`. This `codemeta-harvest.json` file contains only the subset of what you want to add/edit on top of the automatically extracted metadata. The only disadvantage is that, unlike `codemeta.json` which is by definition complete, this requires use of our harvester on the side of the user who wants to make actual use of the full metadata.

Though use of the harvester is *RECOMMENDED*, you *MAY* also craft a `codemeta.json` by hand if you know what you are doing, or create one by filling the form of the [codemeta generator](https://codemeta.github.io/codemeta-generator/).
In line with point 3, whenever metadata is incorrect/incomplete, it is *RECOMMENDED* to solve it at the source (point 4)
if possible rather than in the `codemeta.json`. A typical `codemeta.json` file follows JSON-LD syntax and has a structure as shown in the following fairly minimal example:

```json
{
    "@context": [
        "https://raw.githubusercontent.com/codemeta/codemeta/2.0/codemeta.jsonld",
        "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/13.0/schemaorgcontext.jsonld",
        "https://w3id.org/software-types"
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

### 6. Development status *MUST* be expressed

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

### 7. A producer *SHOULD* be expressed

Please set the `producer` property to the `Organization` that produced the software, i.e. the organization that employs
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
### 8. An interface type *SHOULD* be expressed

Software may present various interfaces types for different kinds of use and different audiences. For instance, there are
command-line tools, web-applications, desktop GUI tools, web APIs, software libraries and mobile apps. Such an interface
type *SHOULD* be explicitly expressed in the metadata.

The `targetProduct` property is used to tie software source code to specific instantiations of the software that are the
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

**Note:** This use of `targetProduct` and the specific software interface types is an extension on top of codemeta/schema.org and not in widespread use yet. It is initially proposed in [this issue](https://github.com/codemeta/codemeta/issues/271). The software types that are not in schema.org yet are being defined in [the software types repo](https://github.com/SoftwareUnderstanding/software_types), more specifically in [this JSON-LD file](https://github.com/SoftwareUnderstanding/software_types/blob/main/software-types.jsonld). Most types are subclasses of [schema:SoftwareApplication](https://schema.org/SoftwareApplication). The property `executableName` is also additional vocabulary we created and its use is *RECOMMENDED*, it defines the executable as it can be invoked within a certain runtime-context, without any OS-specific extensions (``.exe``,``.dll``,``.so``,``.dylib``).


See the section on [service metadata requirements](#service-metadata-requirements) to understand the relation between
software source code and service instances like web applications, web APIs and websites.

### 9. Extra vocabulary *SHOULD* be expressed for CLARIAH

There are a few additional metadata fields/properties and associated vocabulary that we as CLARIAH want you to use.
These fields are expected by the portal tools that eventually present your software and they are usually not
automatically extractable from existing metadata schemas but need to be explicitly specified by you as the tool
developer (in `codemeta.json` or `codemeta-harvest.json`).

* Research domain, research phase and others... (WIP)
    * **TODO: This is still an [ongoing discussion](https://github.com/CLARIAH/clariah-plus/issues/32)**
* Input/Output formats and languages (WIP)
    * **TODO: This is still an [ongoing discussion](https://github.com/codemeta/codemeta/issues/188)**

### 10. You *MAY* express extra vocabulary from schema.org

For links to screenshots or screencasts of the application, use the [screenshot property](https://schema.org/screenshot) with a full URL.The links *MUST* use HTTPS.

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

## Service metadata requirements

We have seen that providing metadata for the source code is done using `codemeta.json` (or `codemeta-harvest.json`) in
the source code repository. This is the primary source for metadata. However, for *software as a service* such as web
applications, webservices and even possibly even simple web pages, we may want to provide some additional metadata *on
top of* the data already provided alongside the source code.

Most notably, the source code does not know where and when it is deployed, i.e. who hosts it where. The link between the
source code and the service instances comes from the [Tool Source
Registry](https://github.com/CLARIAH/tool-discovery/tree/master/source-registry) (see point 2) and is provided by the tool
producer/provider when registering. It may be that that is already enough information but it is possible have web
endpoints provide extra metadata.

* **TODO: This is still an [ongoing discussion](https://github.com/CLARIAH/clariah-plus/issues/92)**

### 11. Software as a service endpoints *MUST* provide metadata

Software as a service *MUST* provide some metadata through an endpoint, at least a name, description, and provider
(see point 11). The metadata needs not be as extensive as provided at the source code level, as by definition each
service is associated with some source code from which it derives most metadata. The registration in the tool source
registry (see point 2) is what links these two.

An endpoint with metadata *MUST* be publicly available with authentication barriers.

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

Some examples, first of an inline JSON-LD block:

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org/",
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
<html itemscope itemtype="https://schema.org/WebApplication">
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
<html vocab="https://schema.org">
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

### 12.  Provider

Please set the `provider` property to the `Organization` that provides the software, i.e. the institutes that makes is available as a service on their infrastructure. Note that this may be distinct from the `producer` that produces the software!

Syntax is analogous to `producer` as listed before.


## Appendix

### Codemeta JSON-LD Example

This is an example of a codemeta JSON-LD file which you can use as a template or reference:

```json
{
    "@context": [
        "https://raw.githubusercontent.com/codemeta/codemeta/2.0/codemeta.jsonld",
        "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/13.0/schemaorgcontext.jsonld",
        "https://w3id.org/software-types"
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
    "dateCreated": "2022-04-29T14:57:10Z+0200",
    "dateModified": "2022-04-29T14:57:10Z+0200"
}
```





