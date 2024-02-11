from flask import Flask
from .routes.public import public_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(public_bp)

    return app
