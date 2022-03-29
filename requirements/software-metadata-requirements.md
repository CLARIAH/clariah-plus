# CLARIAH Software Metadata Requirements and Instructions

## Introduction

This document specifies requirements and instructions for software metadata for
CLARIAH software and services. It is aimed at the developers of software and
attempts to provide clear documentation.

The main principle underlying the way we keep our software metadata is that
**metadata is kept at the source and by the source of the software**. This
means that the tool developers themselves are responsible for providing
accurate metadata and that the best place to keep this metadata is *with the
source code* of the software, in a version-controlled repository.

This is in line with current best-practices as most programming language
ecosystems already have their own ways of describing software metadata
alongside the source code. Our second principle is to **avoid any duplication**
so we make use of those existing metadata descriptions and convert them
automatically to a unified [codemeta](https://codemeta.github.io/)
representation, which is a linked open data vocabulary built on top of
[schema.org](https://schema.org).

The metadata from all of the sources within CLARIAH is harvested automatically,
and periodically, by [a harvesting
tool](https://github.com/proycon/codemeta-harvester). Subsequently, the
harvested metadata (codemeta) is made available in the tool store, which offers
an API that is in turn used by portals to present the tools.

Tools need to be *registered* with the harvester, we have a [Tool Source
Registry](https://github.com/CLARIAH/tool-discovery/tree/master/source-registry)
that tells the harvester where to find, for each tool, both the source code
repository *and* service endpoint where the software is hosted as a service
(optional). Note that we make this explicit distinction between *software*
and *software as a service*. The *software* metadata is described alongside its
source code, the *service* metadata is provided by a service endpoint and adds
some information about a specific deployment of software as a service. Software
services may be served from multiple locations (e.g. the same software may be
hosted by multiple institutes).

## Registering software/services in the Tool Source Registry.

The [Tool Source Registry](https://github.com/CLARIAH/tool-discovery/tree/master/source-registry)
is the input for the harvester, it merely tells the harvester where to look for metadata and does not contains actual metadata itself. Each tool is described by a simple yaml configuration file that lists:

* A single source code repository where the source code of the tool lives. This must be  *git* repository that is publicly accessible (in line with the CLARIAH Software Requirements).
  Note that you can specify only one repository here, choose the one that is representative for the software as a whole. Any other underlying software qualifies as a dependency and should be specified
  as part of the metadata itself, not the tool source registry. If any dependencies have standalone potential and you want to include them in the tool store as well, make a seperate yaml configuration file for each.
* Zero or more service endpoints, i.e. URLs where the tool can be accessed as a service. This may be a web application or some other form of webservice. Rather than enumerate service endpoints individually, this should be pointed to a URL that provides itself provides a specification of endpoints, for example a URL serving a [OpenAPI](https://www.openapis.org/) specification.

To add your yaml configuration, clone the [repository holding the tool source registry](https://github.com/CLARIAH/tool-discovery/), make your changes, and do a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

## Source code metadata

Metadata for your software should be provided alongside the source code as follows:

1. Adhere to the best practices in your programming language ecosystem and specify basic metadata in the way suited for your ecosystem.
    * For Python this is a ``setup.py`` or ``pyproject.toml`` file
    * For Java/Maven this is a ``pom.xml`` file
    * For NodeJS/npm this is a ``package.json`` file
    * Have a proper `README.md` file in all cases
    * Have a proper `LICENSE.md` or `LICENSE` file in all cases
    * All releases of your software should be accompanied with a git tag corresponding to the version number of the release. The harvester will always checkout the highest git tag (i.e. the latest version number) and harvest that instead of the git head of your master/main branch. The main/master branch will only be used as a fall-back in case you have no released versions at all yet.
2. Run the `codemeta-harvester` on your project, it will attempts to automatically extract and convert metadata and produces a ``codemeta.json``
    * **TODO: add instructions on how to run this**
3. Check whether the resulting `codemeta.json` is accurate (minor edits are expected) and commit it to the root of your repository. If this file is present, this will be the authoritative source of metadata and the harvester will not look further.
    * Alternatively, you can commit a ``codemeta-harvest.json`` file instead which only contains only the subset of what you want to add/edit on top of the automatically extracted metadata. In this case our harvester automatically runs step 2 for you on each run.
    * Though use of the harvester is strongly recommmended, you can also craft a `codemeta.json` by hand if you know what you are doing, or create one by filling the form of the [codemeta generator](https://codemeta.github.io/codemeta-generator/).
4. Amend your `codemeta.json` or `codemeta-harvest.json` with CLARIAH-specific vocabulary as described in the next section.

If you use `codemeta.json`, you must take care to update it whenever you do a release, the `version` field changes each time by definition. If you use `codemeta-harvest.json` then you can separate out the parts that are less prone to changes.

The harvester will attempt to do some validation on your metadata and will reject the metadata in case of blatant errors such as invalid JSON, important missing keys, mismatching versions (git tag vs version in the codemeta file).

## Required properties and additional vocabulary

There are a few additional metadata fields/properties and associated vocabulary
that we as CLARIAH want you to use. These fields are expected by the portal
tools that eventually present your software and they are usually not
automatically extractable from existing metadata schemas but need to be
explicitly specified by you as the tool developer.

### Development Status

The `developmentStatus` property is defined by codemeta and expresses in what stage of development the software is. It communicates what level of functionality *and* what level of support the user can expect. Codemeta recommends the use of the [repostatus.org](https://www.repostatus.org/) vocabulary and we make that a hard requirement for CLARIAH. Simple assessment criteria are available on the [repostatus](https://www.repostatus.org) website, along with instructions on how to encode this information in your own `README.md` as a so-called *badge*. Once such a badge is present in your README, our harvester will automatically detect and extract it.

Of course you don't have to use the badge but can also just set it directly in your codemeta.json like for example:

```json
{
    "developmentStatus": "https://www.repostatus.org/#active"
}
```

### Producer

Please set the `producer` property to the `Organization` that produced the software. Note that this may be distinct from the `provider` of the software as a service!

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

### Research domain, research phase and others... (WIP)

* **TODO: This is still an [ongoing discussion](https://github.com/CLARIAH/clariah-plus/issues/32)**

### Input/Output formats and languages (WIP)

* **TODO: This is still an [ongoing discussion](https://github.com/codemeta/codemeta/issues/188)**

### Interface Types (WIP)

* **TODO: This is still an [ongoing discussion](https://github.com/codemeta/codemeta/issues/271)**

### Other recommended vocabulary

For links to screenshots or screencasts of the application, use the [screenshot property](https://schema.org/screenshot) with a full URL:

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

## Service metadata

We have seen that providing metadata for the source code is done using `codemeta.json` in the source code repository. This is the primary source for metadata. However, for *software as a service* such as web applications, webservices and even possibly even simple web pages, we may want to provide some additional metadata *on top of* the data already provided alongside the source code.

Most notably, the source code does not know where and when it is deployed, i.e. who hosts it where. The link between the source code and the service instances comes from the [Tool Source Registry](https://github.com/CLARIAH/tool-discovery/tree/master/source-registry) and is provided by the tool producer/provider when registering. It may be that that is already enough information but it is possible have web endpoints provide extra metadata.


* **TODO: This is still an [ongoing discussion](https://github.com/CLARIAH/clariah-plus/issues/92)**

### Provider

Please set the `provider` property to the `Organization` that provides the software, i.e. the institutes that makes is available as a service on their infrastructure. Note that this may be distinct from the `producer` that produces the software!

Syntax is analogous to `producer` as listed before.







