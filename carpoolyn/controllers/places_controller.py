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


def get_places(cursor, places, counters):
    places_doc = []
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
        data = get_places_from_google(cursor, counters)
        data = process_places(data, places)
    else:
        count_values = counters.find_one({
            'key': 'CACHED_PLACE_API_CALL_COUNT'
        })
        if count_values:
            counters.update_one({
                '_id': count_values['_id']
            }, {
                '$set': {
                    'key': 'CACHED_PLACE_API_CALL_COUNT',
                    'value': count_values['value'] + 1
                }
            }, upsert=False)
        else:
            counters.insert_one({
                'key': 'CACHED_PLACE_API_CALL_COUNT',
                'value': 1
            })

    return success('success', data)


def get_cached_places_count(places, counters):
    total_count = places.count_documents({})
    place_api_counters = counters.find_one({
        'key': 'PLACE_API_CALL_COUNT'
    })
    cached_place_api_counters = counters.find_one({
        'key': 'CACHED_PLACE_API_CALL_COUNT'
    })
    return success('success', {
        "total_cached_records": total_count,
        "place_api_google_count": place_api_counters["value"],
        "cached_place_api_count": cached_place_api_counters["value"]
    })
