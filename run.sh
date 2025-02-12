#!/bin/bash

# Run your first command (e.g., flask db init)
flask db init

# Run your second command (e.g., another command)
flask db migrate -m "initial migration"

# Run your third command (e.g., yet another command)
flask db upgrade

gunicorn app:app --bind 0.0.0.0:5000