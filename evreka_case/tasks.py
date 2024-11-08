from .celeryconfig import celery_app
from .models import DeviceData

@celery_app.task
def process_device_data(data):
    DeviceData.objects.create(**data)
