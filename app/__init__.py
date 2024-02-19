from flask import Flask
from dotenv import load_dotenv
from os import environ as env

# Ensure all your route imports are correct
from .routes.public import public_bp
from .routes.admin import admin_bp
from .routes.realtor import realtor_bp
from .routes.auth import auth_bp, setup_oauth


# Base configuration class
class Config:
    SECRET_KEY = "your_secret_key_here"
    # Add more configurations here as needed


# Testing configuration class inherits from base configuration
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Example for SQLAlchemy
    WTF_CSRF_ENABLED = False  # Useful for form testing


def create_app(config_class=Config):
    app = Flask(__name__)
    app.secret_key = env.get("APP_SECRET_KEY")
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(realtor_bp)

    # Additional initialization here if necessary

    return app
