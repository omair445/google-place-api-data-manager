import datetime
import json

from bson import json_util

from carpoolyn.utils.google_http_client import get_places_from_google
from carpoolyn.utils.response import success


def process_places(payload, places):
    created_places = []
    for address in payload['predictions']:
        try:
            places.insert_one({
                'address': address['description'],
                'place_id': address['place_id'],
                'reference': address['reference'],
                'predictions': address,
                'created_at': datetime.datetime.utcnow()
            })
            created_places.append(address)
        except Exception as error:
            if error.code == 11000:
                created_places.append(address)
            else:
                raise Exception(error)
        finally:
            pass
    return created_places


def get_places(cursor, places):
    places_doc = []
    response = None
    records = places.find({
        "address": {
            "$regex": cursor,
            "$options": "i"
        }
    }).limit(10)
    for document in records:
        places_doc.append(document['predictions'])
    data = json.loads(json_util.dumps(places_doc))
    if len(data) <= 1:
        data = get_places_from_google(cursor)
        data = process_places(data, places)
    return success('success', data)


def get_cached_places_count(places):
    total_count = places.count_documents({})
    return success('success', {
        "count": total_count
    })
