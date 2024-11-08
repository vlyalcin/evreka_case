from django.db import models

class DeviceData(models.Model):
    device_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    location = models.JSONField()  # {"lat": float, "lon": float}
    speed = models.FloatField(null=True, blank=True)
