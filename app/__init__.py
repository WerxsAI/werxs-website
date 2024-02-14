from flask import Flask
from .routes.public import public_bp
from .routes.admin import admin_hp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_hp)

    return app
