## Google Places API Data Manager

###Environments:
1) venv
2) mongodb
3) Python 3.9.13
4) Docker

### How to Setup ?
#### Fire up the docker container for Mongo DB
```cd docker && docker-compose up```

#### Install dependencies
```pip install -r requirements.txt```

#### Boot Flask Application
```flask run```


#####Post: http://127.0.0.1:5000/api/places
#####JSON Body:
```python
{
   "a":[
      {
         "a":"ChIJ2QeB5YMEGTkRYiR-zGy-OsI",
         "b":[
            "LOCALITY",
            "POLITICAL",
            "GEOCODE"
         ],
         "c":"Islamabad, Pakistan",
         "d":"Islamabad",
         "e":"Pakistan",
         "f":[
            {
               "a":0,
               "b":1
            }
         ],
         "g":[
            {
               "a":0,
               "b":1
            }
         ]
      }
   ]
}
```

#####GET: http://127.0.0.1:5000/api/places
#####Expected Response Body:
```json
{
    "data": [
        {
            "_id": {
                "$oid": "62bf5bf99a8fffcaef884664"
            },
            "address": "Allama Iqbal International Airport, Airport Road, Cantt, Lahore, Pakistan",
            "created_at": {
                "$date": "2022-07-01T20:41:29.609Z"
            },
            "latitude": "00.00.00.00",
            "longitude": "00.00.00.00",
            "object": {
                "a": "ChIJ5z8s8n0PGTkRA2uqQNr_140",
                "b": [
                    "AIRPORT",
                    "POINT_OF_INTEREST",
                    "ESTABLISHMENT"
                ],
                "c": "Allama Iqbal International Airport, Airport Road, Cantt, Lahore, Pakistan",
                "d": "Allama Iqbal International Airport",
                "e": "Airport Road, Cantt, Lahore, Pakistan",
                "f": [
                    {
                        "a": 1,
                        "b": 1
                    }
                ],
                "g": [
                    {
                        "a": 1,
                        "b": 1
                    }
                ]
            },
            "place_name": "Allama Iqbal International Airport",
            "short_place_name": "Airport Road, Cantt, Lahore, Pakistan"
        },
        {
            "_id": {
                "$oid": "62bf5bf99a8fffcaef884663"
            },
            "address": "Lahore Ring Road, Block A Bankers Town, Lahore, Pakistan",
            "created_at": {
                "$date": "2022-07-01T20:41:29.601Z"
            },
            "latitude": "00.00.00.00",
            "longitude": "00.00.00.00",
            "object": {
                "a": "EjhMYWhvcmUgUmluZyBSb2FkLCBCbG9jayBBIEJhbmtlcnMgVG93biwgTGFob3JlLCBQYWtpc3RhbiIuKiwKFAoSCfv99br-Ghk5EbxxaFKLYwD2EhQKEgnnUTbEJAYZORH5qn_a3NcIQQ",
                "b": [
                    "ROUTE",
                    "GEOCODE"
                ],
                "c": "Lahore Ring Road, Block A Bankers Town, Lahore, Pakistan",
                "d": "Lahore Ring Road",
                "e": "Block A Bankers Town, Lahore, Pakistan",
                "f": [
                    {
                        "a": 0,
                        "b": 1
                    }
                ],
                "g": [
                    {
                        "a": 0,
                        "b": 1
                    }
                ]
            },
            "place_name": "Lahore Ring Road",
            "short_place_name": "Block A Bankers Town, Lahore, Pakistan"
        },
        {
            "_id": {
                "$oid": "62bf5bf99a8fffcaef884661"
            },
            "address": "Lahore, Pakistan",
            "created_at": {
                "$date": "2022-07-01T20:41:29.589Z"
            },
            "latitude": "00.00.00.00",
            "longitude": "00.00.00.00",
            "object": {
                "a": "ChIJ2QeB5YMEGTkRYiR-zGy-OsI",
                "b": [
                    "LOCALITY",
                    "POLITICAL",
                    "GEOCODE"
                ],
                "c": "Lahore, Pakistan",
                "d": "Lahore",
                "e": "Pakistan",
                "f": [
                    {
                        "a": 0,
                        "b": 1
                    }
                ],
                "g": [
                    {
                        "a": 0,
                        "b": 1
                    }
                ]
            },
            "place_name": "Lahore",
            "short_place_name": "Pakistan"
        },
        {
            "_id": {
                "$oid": "62bf5bf99a8fffcaef884665"
            },
            "address": "Liberty Market Gulberg III, Lahore, Pakistan",
            "created_at": {
                "$date": "2022-07-01T20:41:29.617Z"
            },
            "latitude": "00.00.00.00",
            "longitude": "00.00.00.00",
            "object": {
                "a": "ChIJMxiU-FoEGTkRFmrGF09fudY",
                "b": [
                    "SUBLOCALITY_LEVEL_2",
                    "SUBLOCALITY",
                    "POLITICAL",
                    "GEOCODE"
                ],
                "c": "Liberty Market Gulberg III, Lahore, Pakistan",
                "d": "Liberty Market Gulberg III",
                "e": "Lahore, Pakistan",
                "f": [
                    {
                        "a": 0,
                        "b": 1
                    }
                ],
                "g": [
                    {
                        "a": 0,
                        "b": 1
                    }
                ]
            },
            "place_name": "Liberty Market Gulberg III",
            "short_place_name": "Lahore, Pakistan"
        }
    ],
    "message": "success",
    "status": true,
    "status_code": 200,
    "total_count": 4
}
```

#### Create UNIQUE Index for Places table against *address* field
```mysql
db.places.createIndex( { "address": 1 }, { unique: true } )
```


#### Environment Variables (.env)
```mysql
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_MONGO_PASSWORD=root
FLASK_MONGO_USERNAME=root
FLASK_MONGO_PORT=27017
FLASK_MONGO_HOST=localhost

```
