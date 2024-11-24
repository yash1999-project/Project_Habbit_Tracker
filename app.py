import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    mongodb_uri= os.getenv("MONGODB_URI");
    #client = MongoClient( os.getenv("MONGODB_URI"))
    if not mongodb_uri:
        raise ValueError("MONGODB_URI is not set in the environment variables")

    client = MongoClient(mongodb_uri)
    app.db = client.get_default_database()

    app.register_blueprint(pages)
    return app