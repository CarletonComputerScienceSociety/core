#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings.prod

cd /code

# Wait for the database to be ready
$(python /code/docker/wait.py)

echo "Migrating"
python manage.py migrate

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Starting server"
python manage.py runserver 0.0.0.0:8000

# gunicorn \
#     -w 2 \
#     -b 0.0.0.0:8000 \
#     core.wsgi:application
