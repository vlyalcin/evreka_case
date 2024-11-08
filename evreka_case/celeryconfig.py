from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evreka_case.settings')
celery_app = Celery("device_data_processing")
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
