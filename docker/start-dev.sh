export DJANGO_SETTINGS_MODULE=core.settings.dev

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
celery -A core worker -l info