from __future__ import absolute_import, unicode_literals

import os
import ssl
from celery import Celery
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cn_django_test.settings')

redis_url = settings.CELERY_BROKER_URL
app = Celery('cn_django_test', broker=redis_url, result_backend=redis_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.timezone = 'UTC'