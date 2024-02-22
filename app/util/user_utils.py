from flask import current_app as app, flash
"""
The function `get_or_create_user` retrieves or creates a user in a MongoDB collection based on Auth0
user information.

:param userinfo: The `userinfo` parameter in the `get_or_create_user` function is a dictionary
containing information about the user. It is expected to have at least a key "sub" which represents
the user's Auth0 ID. Other optional keys that may be present in the `userinfo` dictionary include
"email
:return: The function `get_or_create_user` returns the user document retrieved from the database or
created if it doesn't exist. If an error occurs during the process, it returns `None`.
"""
from datetime import datetime
from .db_util import getDB


def get_or_create_user(userinfo):
    # Ensure userid is present; fail if not
    if "sub" not in userinfo:
        app.logger.error("Userinfo does not contain userid (sub).")
        flash("An error occurred during authentication. Please try again.", "error")
        return None

    app.logger.info(
        "Attempting to get or create user with Auth0 ID: %s", userinfo["sub"]
    )  # Log the attempt with the user's Auth0 ID

    try:
        db = getDB()
        users = db.userAccounts
        app.logger.debug(
            "MongoDB Collection: %s", users.name
        )  # Log the name of the collection

        user = users.find_one({"auth0_user_id": userinfo["sub"]})
        app.logger.info("User found: %s", user)

        if not user:
            # If user doesn't exist, create a new document with last login time
            user_data = {
                "auth0_user_id": userinfo["sub"],
                "last_login": datetime.utcnow(),  # Set the current UTC time as last login
                "roles": ["default_user"],
            }

            # Add email and picture if they exist
            if "email" in userinfo:
                user_data["email"] = userinfo["email"]
            if "picture" in userinfo:
                user_data["picture"] = userinfo["picture"]

            insert_result = users.insert_one(user_data)
            app.logger.info("Created new user with ID: %s", insert_result.inserted_id)
            user = user_data
        else:
            # For existing users, update the last login time
            update_data = {"$set": {"last_login": datetime.utcnow()}}
            update_result = users.update_one(
                {"auth0_user_id": userinfo["sub"]},
                update_data,
            )
            app.logger.info(
                "Updated last login for user: %s, Update Result: %s",
                userinfo["sub"],
                update_result.modified_count,
            )
    except Exception as e:
        app.logger.error(
            "Failed to get or create user: %s", e, exc_info=True
        )  # Log the exception details
        flash("An unexpected error occurred while processing your login.", "error")
        return None  # or handle as appropriate for your application

    return user
