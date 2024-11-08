from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone

class DeviceDataTests(APITestCase):
    def setUp(self):
        self.device_data_url = reverse('data-ingest')

    def test_insert_device_data(self):
        device_data_payload = {
            "device_id": "test_device_123",
            "timestamp": timezone.now().isoformat(),
            "location": {"lat": 41.0082, "lon": 28.9784},
            "speed": 55.0
        }

        response = self.client.post(self.device_data_url, data=device_data_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data["status"], "Data has been queued")