from flask import Blueprint, redirect, url_for, session, render_template
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
@auth_bp.route("/login")
def login():
    redirect_uri = url_for("auth_bp.callback", _external=True)
    return oauth.auth0.authorize_redirect(redirect_uri=redirect_uri)


@auth_bp.route("/callback", methods=["GET", "POST"])
def callback():
    # Your callback logic here
    pass


@auth_bp.route("/logout")
def logout():
    # Your logout logic here
    pass
