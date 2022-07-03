import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


def get_places_from_google(cursor: str):
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=" + cursor + "&region=pk&key=" + str(
        os.environ.get(
            'FLASK_APP_GOOGLE_PLACES_API_KEY'))

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)
