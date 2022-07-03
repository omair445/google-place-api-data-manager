from flask import Flask, request

from carpoolyn.controllers.places_controller import *
from carpoolyn.utils.mongo_client import init

app = Flask(__name__)
places = init().places


@app.route('/api/places/count', methods=['GET'])
def get_places_count():
    return get_cached_places_count(places)


@app.route('/api/places', methods=['GET'])
def pull_places():
    return get_places(request.values.get('cursor'), places)
