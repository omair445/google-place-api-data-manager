## Google Places API Data Manager
[![Places API Gateway](https://github.com/omair445/google-place-api-data-manager/actions/workflows/python-app.yml/badge.svg)](https://github.com/omair445/google-place-api-data-manager/actions/workflows/python-app.yml)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/37a9c542a3a3bc15a262?action=collection%2Fimport)
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


#### GET: http://127.0.0.1:5000/api/places?cursor=Southville
#### Expected Response Body:
```json
{
    "data": [
        {
            "description": "Southville Solutions, Service Road, Block R1 Block R 1 Phase 2 Johar Town, Lahore",
            "matched_substrings": [
                {
                    "length": 14,
                    "offset": 0
                }
            ],
            "place_id": "ChIJj8LWbe0BGTkRHDRZ3UQ5HEM",
            "reference": "ChIJj8LWbe0BGTkRHDRZ3UQ5HEM",
            "structured_formatting": {
                "main_text": "Southville Solutions",
                "main_text_matched_substrings": [
                    {
                        "length": 14,
                        "offset": 0
                    }
                ],
                "secondary_text": "Service Road, Block R1 Block R 1 Phase 2 Johar Town, Lahore"
            },
            "terms": [
                {
                    "offset": 0,
                    "value": "Southville Solutions"
                },
                {
                    "offset": 22,
                    "value": "Service Road"
                },
                {
                    "offset": 36,
                    "value": "Block R1"
                },
                {
                    "offset": 45,
                    "value": "Block R 1"
                },
                {
                    "offset": 55,
                    "value": "Phase 2"
                },
                {
                    "offset": 63,
                    "value": "Johar Town"
                },
                {
                    "offset": 75,
                    "value": "Lahore"
                }
            ],
            "types": [
                "point_of_interest",
                "establishment"
            ]
        }
    ],
    "message": "success",
    "status": true,
    "status_code": 200,
    "total_count": 1
}
```

#### Login To mongo db container and connect to mongo shell using and then create unique index for places collection
```mysql
mongo -u root -p root
```

#### Create UNIQUE Index for Places table against *address* field
```mysql
db.places.createIndex( { "place_id": 1 }, { unique: true } )
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
