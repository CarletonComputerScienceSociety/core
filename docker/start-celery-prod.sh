#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings.prod

echo "Waiting for database"
# Wait for the database to be ready
python /code/docker/wait.py

cd /code

echo "Starting celery"
celery -A core worker --beat --scheduler django --loglevel=info
