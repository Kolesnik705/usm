#!/bin/sh

set -ev

python app/service/mongo_data_creator.py
uvicorn --host 0.0.0.0 --port 8110 --factory app.app:create_app