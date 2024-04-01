#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "[1/3] >>> Running migrations..."
python manage.py migrate
echo "[1/3] <<< Migration done"

echo "[2/3] >>> Creating super user..."
# shellcheck disable=SC2039
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_USERNAME', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | python3 manage.py shell &>/dev/null
echo "[2/3] <<< Super User created"

echo "[3/3] >>> Starting server in development..."
python manage.py runserver 0.0.0.0:8000
echo "[3/3] <<< Server started"