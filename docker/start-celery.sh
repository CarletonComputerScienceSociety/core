#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings.dev

cd /code

celery -A core worker --beat --scheduler django --loglevel=info
