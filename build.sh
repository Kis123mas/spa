#!/usr/bin/env bash

# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

#convert static asset files

python manage.py collectstatic --on-input


#Apply any outstanding database migrations
python manage.py migrate