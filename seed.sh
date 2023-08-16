#!/bin/bash

poetry run python manage.py loaddata seed/0001_categories.json
# poetry run python manage.py loaddata seed/0002_users.json
