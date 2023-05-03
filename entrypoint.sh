#!/bin/sh

#while [ ! -f /app/db/db.sqlite3 ] || [ ! -w /app/db/db.sqlite3 ]; do
#  sleep 1
#done

python manage.py makemigrations
python manage.py migrate

exec "$@"
