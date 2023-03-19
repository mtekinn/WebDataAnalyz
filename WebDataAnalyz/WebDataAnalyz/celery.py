from pathlib import Path
from celery import Celery

# set the default Django settings module for the 'celery' program.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebDataAnalyz.settings")

app = Celery("WebDataAnalyz")

# Using a string here means the worker will not have to
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: [str(app_config.parent.name) for app_config in Path().glob("*/tasks.py")])
