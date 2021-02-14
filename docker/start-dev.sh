#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings.dev

cd /code

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
celery -A core worker -l info
