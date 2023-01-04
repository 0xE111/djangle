#!/bin/sh
python manage.py wait_for_database
python manage.py migrate
python manage.py collectstatic --clear --no-input
gunicorn --workers=4 --bind=0.0.0.0:8000 wsgi:application