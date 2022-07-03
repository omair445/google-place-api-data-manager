import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


def get_places_from_google(cursor: str, counters):
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=" + cursor + "&region=pak&strictbounds=true&radius=2430000&location=31.458114624023438,74.27582133657911&key=" + str(
        os.environ.get(
            'FLASK_APP_GOOGLE_PLACES_API_KEY'))

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    count_values = counters.find_one({
        'key': 'PLACE_API_CALL_COUNT'
    })
    if count_values:
        counters.update_one({
            '_id': count_values['_id']
        }, {
            '$set': {
                'key': 'PLACE_API_CALL_COUNT',
                'value': count_values['value'] + 1
            }
        }, upsert=False)
    else:
        counters.insert_one({
            'key': 'PLACE_API_CALL_COUNT',
            'value': 1
        })

    return json.loads(response.text)
