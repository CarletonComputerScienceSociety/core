#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings.prod

cd /code

# Wait for the database to be ready
echo "Waiting for database"
python /code/docker/wait.py

echo "Migrating"
python manage.py migrate

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Starting server"
gunicorn \
    -w 3 \
    -b 0.0.0.0:8000 \
    core.wsgi:application
