from flask import flash
from flask import current_app as app
from .db_util import getDB
from app.models.UserModel import (
    UserModel,
)  # Ensure this import path matches your project structure


def get_or_create_user(userinfo):
    if "sub" not in userinfo:
        app.logger.error("Userinfo does not contain userid (sub).")
        flash("An error occurred during authentication. Please try again.", "error")
        return None

    app.logger.info(
        "Attempting to get or create user with Auth0 ID: %s", userinfo["sub"]
    )

    try:
        db = getDB()
        user_model = UserModel(db)
        user = user_model.find_user(userinfo["sub"])

        if not user:
            user = user_model.create_user(userinfo)
        else:
            user_model.update_user_last_login(userinfo["sub"])

    except Exception as e:
        app.logger.error("Failed to get or create user: %s", e, exc_info=True)
        flash("An unexpected error occurred while processing your login.", "error")
        return None

    return user
