from flask import Blueprint, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from os import environ as env
from urllib.parse import urlencode, quote_plus

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
# 👆 We're continuing from the steps above. Append this to your server.py file.


@auth_bp.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("auth_bp.callback", _external=True)
    )


@auth_bp.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
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
                "returnTo": url_for("public.index", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )
