# Connect service to CLARIAH/CLARIN authentication

This article is mostly useful for CLARIAH application developers who would like to provide a login mechanism that enable members of the CLARIAH/CLARIN community to access their application or service.

## Some context

The CLARIAH community, comprised of mainly acedemic institutes and universities, shares a common Identity Provider (IdP), required for user authentication, via the CLARIN organisation. This way CLARIAH can enable login functionality for CLARIAH services

This CLARIN IdP is connected to the CLARIAH authentication system (SATOSA) and enables CLARIAH services, such as LaMachine and the [Media Suite](https://mediasuite.clariah.nl) to provide a login functionality for (all) members/organisations connected via the CLARIN IdP. (TODO a bit terrible phrasing, fix later)


# How to connect your service

The protocol used to communicate with the CLARIAH authentication is [OpenID Connect](https://openid.net/developers/specs/) or in short: OIDC.

More specifically: currently all communication with the authentication server must follow the [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth)

## Step 1: Register your service domain name

Before being able to implement the desired OIDC communication flow, it is necessary to register a domain the authentication server can access on the web. It's probably best to setup two domains: one for testing and one for production.

Contact the [Humanties Cluster](https://huc.knaw.nl/) to obtain the necessary `client ID` and `client secret` for each of these domains.

## Step 2: Implement the Authorization Code Flow

TODO examples from the media suite.