export DJANGO_SETTINGS_MODULE=core.settings.prod

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000