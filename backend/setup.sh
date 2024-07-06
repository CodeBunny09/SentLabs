#!/bin/bash

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate

# Load initial data if any (optional)
# echo "Loading initial data"
# python manage.py loaddata initial_data.json

# Run Django development server
echo "Starting Django development server"
python manage.py runserver 0.0.0.0:8000
