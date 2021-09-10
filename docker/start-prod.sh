#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings.prod

cd /code

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn \
    -w 2 \
    -b 0.0.0.0:8000 \
    core.wsgi:application
