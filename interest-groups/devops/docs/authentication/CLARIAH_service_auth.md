# Add CLARIAH authentication to your service

(...)


The following two Open ID Process Flows are documented in this readme:

1. **Authentication Flow**: User authenticates to your service
2. **Authorization Code Flow**: Your service calls other CLARIAH services **on behalf of authenticated users**

If your service stands on itself, meaning it does not rely on any other external resources for loading/saving data, the **Authentication Flow** is enough and fairly simple to incorporate. 

If however your service or users need to call external APIs after authenticating, the **Authentication Code Flow** needs to be implemented as well. Also your external resources/services/APIs also need to be adapted to make sure they can handle the `access_tokens` provided by the this process flow.

## Considerations

Before going ahead with the implementation, please consider the following:

- Does my service load external resources that require user authentication?
- What institutions are allowed to access my service?
- Are there institutions of which only certain known users are allowed access?

The first consideration was mentioned in the previous section. The remaining two can be addressed by whitelisting/blacklisting institutions and/or individual users within institutions. Examples for this are included further on. TODO ref 

## Prerequisites

The following example implementations require the following:

- Python 3.8 or higher
- [Authlib](https://docs.authlib.org/en/latest/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- Permanent session cookie

In Flask a permanent session cookie can be configured as follows:

```python
# Note: These settings only work if running on HTTPS! (https://github.com/onelogin/python-saml)
SESSION_COOKIE_NAME = "__Host-xlab-mediasuite"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "Lax"

# Note: These settings only work on HTTP (so without a web proxy with a TLS cert)
# SESSION_COOKIE_HTTPONLY = False
# SESSION_COOKIE_PATH = "/"
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SAMESITE = "None"
```

```python
@app.before_request
def make_session_permanent():
    # ensure the session is permanent (to avoid killing the session on browser closing)
    session.permanent = True
    app.logger.info(app.session_interface.get_expiration_time(app, session))
```

# Implementation

For both the Authentication Flow and the Authorization Code Flow an Open ID client needs to be instantiated.

Flask is one of the web servers supported by Authlib and by adding the following keys to your Flask config, the OAuth client can fetch the following settings conveniently:

```python
 # NOTE: a CLIENT ID and SECRET must be requested from the CLARIAH organisation
CLARIAH_CLIENT_ID = "your_service_client_id"
CLARIAH_CLIENT_SECRET = "your_service_client_secret"
```

With these settings in place the client can be instantiated as follows:

```python
from flask import Flask
from authlib.integrations.flask_client import OAuth
from authlib.integrations.base_client.errors import OAuthError  # used in later examples

# basic example of initiating the Flask app
app = Flask(__name__)

auth_server_metadata_url = 'https://CLARIAH_AUTH_SERVER/.well-known/openid-configuration'

# initiate the OIDC (OAuth) client
oauth = OAuth(app)  # pass the Flask app here
oauth.register(
    name="clariah",  # CLARIAH_CLIENT_ID and CLARIAH_CLIENT_SECRET are found this way
    server_metadata_url=auth_server_metadata_url,  # points to CLARIAH SATOSA auth server
    client_kwargs={"scope": "openid email profile"},  # parameters to enforce open ID connect
)
```

If you follow the [auth_server_metadata_url](https://CLARIAH_AUTH_SERVER/.well-known/openid-configuration), you can see how the `register` function obtains all the relevant endpoints required for both the Authentication and Authorization Code Flows.

## Authentication Flow

Let's assume you have configured the following routes in your Flask application:

```python
# add the following routs to your Flask app
app.add_url_rule("/login", view_func=login, methods=["GET"])
app.add_url_rule(
    "/oidc/redirect", view_func=oidc_auth_redirect, methods=["GET"]
)

def login(self):
    redirect_user_to_uri = request.headers.get("Referer") 
    return do_login(oauth, redirect_user_to_uri)

def oidc_auth_redirect(self):
    return oidc_auth_redirect(oauth)
```


The following function shows how the **Authentication Flow** can be triggered. Pass the `oauth` client from the previous code example. 

```python
def do_login(self, oauth, redirect_user_to_uri=None):
    # remember from which page the user started login for redirection later
    session["user_requested_url"] = redirect_user_to_uri 
    redirect_uri = url_for(
        "oidc_auth_redirect", _external=True, _scheme="https"
    )

    # use the Oauth client to start the Authentication Flow
    return oauth.clariah.authorize_redirect(
        redirect_uri=redirect_uri,
        claims=json.dumps(
            {
                "id_token": {
                    "edupersontargetedid": {"essential": True},
                    "schac_home_organisation": {"essential": True},
                    "nickname": {"essential": True},
                    "email": {"essential": True},
                    "eppn": {"essential": True},
                    "idp": {"essential": True},
                },
                "userinfo": {
                    "edupersontargetedid": {"essential": True},
                    "schac_home_organisation": {"essential": True},
                    "nickname": {"essential": True},
                    "email": {"essential": True},
                    "eppn": {"essential": True},
                    "idp": {"essential": True},
                },
            }
        ),
    )
```

When the user authenticates SATOSA calls the configured `redirect_uri`, which is handled by the following function:

TODO clean up this function for this documentation

```python
# called by SATOSA after the user has tried to authenticate at the IdP
def oidc_auth_redirect(self, oauth):
    if not self.__check_openid_server_error(request):
        return self.__redirect_to_login_failed(
            "The login server returned an error preventing a successful login"
        )

    # the user is authenticated, now request an access token for the APIs
    token = None
    try:
        token = oauth.clariah.authorize_access_token()
    except OAuthError:
        logger.exception("Error: could not fetch initial access token")

    if not token:
        return self.__redirect_to_login_failed(
            "The server failed to fullfil your login request"
        )

    if not token.get("access_token", None):
        return self.__redirect_to_login_failed(
            "The server failed to obtain an access token"
        )

    if not token.get("userinfo", None):
        return self.__redirect_to_login_failed(
            "The server failed to obtain any user info"
        )

    # grab the access_token (for APIs) and userinfo (UI, IdP whitelist check)
    access_token = token["access_token"]
    user_info = token["userinfo"]
    refresh_token = token["refresh_token"]
    expires_in = token["expires_in"]
    logger.info("access_token and userinfo found, checking idp whitelist")

    # check if the user's idp is whitelisted
    allowed_idp = get_allowed_user_idp(user_info, self.OIDC_IDP_WHITELIST)
    if not allowed_idp:
        return self.__redirect_to_login_failed(
            "The organisation you are authenticating from is not authorized access to the CLARIAH Media Suite"
        )

    # check if the user is specically whitelisted for a certain institution
    if not check_idp_user_whitelist(
        user_info, allowed_idp, self.OIDC_IDP_USER_WHITELIST
    ):
        return self.__redirect_to_login_failed(
            "You are not allowed to login via CLARIN please ask for dispensation via the CLARIAH project"
        )

    # all is good, make sure the user session is setup & redirect
    session["oidcIsAuthenticated"] = True
    session["access_token"] = access_token
    session["userinfo"] = user_info
    session["refresh_token"] = refresh_token
    session["expires_in"] = expires_in
    session["token_obtained"] = int(time())

    return self.__redirect_to_requested_url()
```



## Authorization Code Flow

Ensure `access_tokens` are refreshed before expiring.

```python
# see https://flask.palletsprojects.com/en/1.1.x/api/ (this will make sessions expire after 31 days)
@app.before_request
def make_session_permanent():
    # ensure the session is permanent (to avoid killing the session on browser closing)
    session.permanent = True
    app.logger.info(app.session_interface.get_expiration_time(app, session))

    # check if the OIDC access_token needs refreshing
    token_refreshed = auth_hub.check_refresh_token()
    app.logger.info(f"New refresh token issued: {token_refreshed}")
```


# Recommended reading

- [auth0.com: Authorization Code Flow](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow)
- [openid.net: Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth)