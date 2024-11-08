
from .tasks import process_device_data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DeviceData
from .serializers import DeviceDataSerializer
from django.utils.dateparse import parse_datetime

class DeviceDataView(APIView):
    def post(self, request):
        serializer = DeviceDataSerializer(data=request.data)
        if serializer.is_valid():
            process_device_data.delay(serializer.validated_data)
            return Response({"status": "Data has been queued"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDataRangeView(APIView):
    def get(self, request):
        device_id = request.query_params.get("device_id")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        # Validate parameters
        if not device_id or not start_date or not end_date:
            return Response({"error": "device_id, start_date, and end_date are required parameters."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
        except ValueError:
            return Response({"error": "Invalid date format. Use ISO 8601 format."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Fetch data in the specified range
        data = DeviceData.objects.filter(
            device_id=device_id,
            timestamp__range=(start_date, end_date)
        )
        serializer = DeviceDataSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeviceDataLatestView(APIView):
    def get(self, request, device_id):
        # Fetch the latest record for the specified device_id
        latest_data = DeviceData.objects.filter(device_id=device_id).order_by('-timestamp').first()

        if not latest_data:
            return Response({"error": "No data found for the specified device_id."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeviceDataSerializer(latest_data)
        return Response(serializer.data, status=status.HTTP_200_OK)