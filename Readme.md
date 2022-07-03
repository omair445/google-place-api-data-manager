## Google Places API Data Manager
[![Python application](https://github.com/omair445/google-place-api-data-manager/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/omair445/google-place-api-data-manager/actions/workflows/python-app.yml)
### Dependencies:
1) venv
2) mongodb
3) Python 3.9.13
4) Docker

## Install python and venv
```bash
apt-get install python3-pip python3-dev python3-venv
```
Above line is for Linux Ubuntu. It may vary for your OS

## Create and activate venv
```bash
python3 -m venv venv
source venv/bin/activate
```
### How to Setup ?
#### Fire up the docker container for Mongo DB
```cd docker && docker-compose up```

#### Boot Flask Application
```bash start_app_server.sh```


#### Post: http://127.0.0.1:5000/api/places
#### JSON Body:
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

#### GET: http://127.0.0.1:5000/api/places
#### Expected Response Body:
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

### Setup Gunicorn as Service ?
```
sudo nano /etc/systemd/system/gunicorn.service
```

### Paste the following
```mysql
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/google-place-api-data-manager
ExecStart=bash start_app_server.sh

[Install]
WantedBy=multi-user.target
```

### Start the Service
```mysql
sudo systemctl start gunicorn
```

### Enable the service
```mysql
sudo systemctl enable gunicorn
```

### Nginx Reverse Proxy
#### Install Nginx and edit the following file 
```mysql
nano /etc/nginx/sites-available/default
```
#### Then paste the following block
```mysql

server {
  server_name               xxxxxx.xxxxx.xxxxx;
  listen                    80;
  location / {
    proxy_pass              http://localhost:4400;
    proxy_set_header        Host $host;
  }
}

```

#### Login To mongo db container and connect to mongo shell using and then create unique index for places collection
```mysql
mongo -u root -p root
```
