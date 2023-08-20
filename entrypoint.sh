poetry run python manage.py migrate --no-input

poetry run python manage.py compilemessages

poetry run python manage.py collectstatic --no-input

./seed.sh

poetry run gunicorn --pythonpath ./ --bind 0.0.0.0:8000 product_management.asgi:application -k uvicorn.workers.UvicornWorker
