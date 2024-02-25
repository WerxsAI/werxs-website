"""
The function `getDB` attempts to establish a connection to a MongoDB database using the URI provided
in the environment variable "MONGO_URI".
:return: The function `getDB()` is returning a MongoDB database named "werxsai" from the MongoClient
connected to the URI specified in the environment variable "MONGO_URI".
"""
from os import environ as env
import pymongo
import sys

def getDB():

    try:
        URI = env.get("MONGO_URI")
        print(URI)
        client = pymongo.MongoClient(env.get("MONGO_URI"))

    # return a friendly error if a URI error is thrown
    except pymongo.errors.ConfigurationError:
        print(
            "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
        )

    # use a database named "myDatabase"
    db = client.werxsai
    return db