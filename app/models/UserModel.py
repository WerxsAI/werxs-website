# The `UserModel` class in Python defines methods for interacting with a user collection in a
# database, including finding users, creating users, and updating user last login information.
from datetime import datetime
from flask import current_app as app


class UserModel:
    def __init__(self, db):
        self.collection = db.userAccounts

    def find_user(self, auth0_user_id):
        return self.collection.find_one({"auth0_user_id": auth0_user_id})

    def create_user(self, userinfo):
        user_data = {
            "auth0_user_id": userinfo["sub"],
            "last_login": datetime.utcnow(),
            "roles": ["default_user"],
        }
        if "email" in userinfo:
            user_data["email"] = userinfo["email"]
        if "picture" in userinfo:
            user_data["picture"] = userinfo["picture"]

        result = self.collection.insert_one(user_data)
        app.logger.info("Created new user with ID: %s", result.inserted_id)
        return user_data

    def update_user_last_login(self, auth0_user_id):
        result = self.collection.update_one(
            {"auth0_user_id": auth0_user_id},
            {"$set": {"last_login": datetime.utcnow()}},
        )
        app.logger.info(
            "Updated last login for user: %s, Update Result: %s",
            auth0_user_id,
            result.modified_count,
        )
