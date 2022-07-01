import os

from pymongo import MongoClient


def init():
    client = MongoClient(os.environ.get('FLASK_MONGO_HOST'), int(os.environ.get('FLASK_MONGO_PORT')), username=os.environ.get('FLASK_MONGO_USERNAME'), password=os.environ.get('FLASK_MONGO_PASSWORD'))
    return client.flask_db
