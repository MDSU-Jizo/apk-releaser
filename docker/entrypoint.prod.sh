#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


echo "[1/2] >>> Running migrations..."
python manage.py migrate
echo "[1/2] <<< Migration done"

echo "[2/2] >>> Creating super user..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_USERNAME', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | python3 manage.py shell &>/dev/null
echo "[2/2] <<< Super User created"

exec "$@"