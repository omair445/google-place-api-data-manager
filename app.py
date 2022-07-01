import json

import pymongo as pymongo
from flask import Flask, request
from carpoolyn.controllers.places_controller import *
from carpoolyn.utils.mongo_client import init

app = Flask(__name__)
places = init().places
# places.create_index([('address', pymongo.ASCENDING)])


@app.route('/api/places', methods=['POST'])
def save_places():
    return process_places(json.loads(request.data), places)


@app.route('/api/places', methods=['GET'])
def pull_places():
    return get_places(request.values.get('cursor'), places)


# if __name__ == '__main__':
#     app.run(load_dotenv=True)
