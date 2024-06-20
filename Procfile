web: gunicorn cn_django_test.wsgi:application --log-level=debug
celery: celery -A cn_django_test worker -l info