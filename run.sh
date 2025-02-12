#!/bin/bash

# db init in the project
flask db init

# first migration
flask db migrate -m "initial migration"

# Upgrade database
flask db upgrade

gunicorn app:app --bind 0.0.0.0:5000
