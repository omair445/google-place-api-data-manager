import datetime
import json
from bson import json_util

from carpoolyn.utils.response import success


def process_places(payload, places):
    for address in payload['a']:
        try:
            places.insert_one({
                'address': address['c'],
                'place_name': address['d'],
                'short_place_name': address['e'],
                'latitude': "00.00.00.00",
                'longitude': "00.00.00.00",
                'object': address,
                'created_at': datetime.datetime.utcnow()
            })
        except Exception:
            pass

    return success('Places Saved')


def get_places(cursor, places):
    places_doc = []
    cursor = places.find({
        "address": {
            "$regex": cursor,
            "$options": "i"
        }
    })
    for document in cursor:
        places_doc.append(document)
    response = json.loads(json_util.dumps(places_doc))
    return success('success', response)
