#!/bin/sh
python3 manage.py wait_for_database
python3 manage.py migrate
python3 manage.py collectstatic --clear --no-input
gunicorn --workers=4 --bind=0.0.0.0:8000 wsgi:application