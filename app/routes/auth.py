"""
The code defines Flask routes for authentication with Auth0, including login, callback, and logout
functionality.

:param app: The code you provided is setting up OAuth authentication using Auth0 in a Flask
application. Here's a breakdown of the key components:
"""
from flask import Blueprint, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from os import environ as env
from urllib.parse import urlencode, quote_plus
from app.util.user_utils import get_or_create_user

# Initialize Blueprint
auth_bp = Blueprint("auth_bp", __name__)

# Setup OAuth
oauth = OAuth()


def setup_oauth(app):
    oauth.init_app(app)
    oauth.register(
        "auth0",
        client_id=env.get("AUTH0_CLIENT_ID"),
        client_secret=env.get("AUTH0_CLIENT_SECRET"),
        client_kwargs={"scope": "openid profile email"},
        server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
    )


# Auth routes


@auth_bp.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("auth_bp.callback", _external=True)
    )


import requests


@auth_bp.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    userinfo_response = requests.get(
        f'https://{env.get("AUTH0_DOMAIN")}/userinfo',
        headers={"Authorization": f'Bearer {token["access_token"]}'},
    )

    if userinfo_response.ok:
        userinfo = userinfo_response.json()
        # Process userinfo as needed
    else:
        # Handle error
        print("Failed to fetch userinfo")

    session["user"] = token  # or use userinfo for session
    get_or_create_user(userinfo)
    return redirect("/")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("public.home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )
