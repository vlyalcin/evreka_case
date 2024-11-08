from django.contrib import admin
from django.urls import path
from .views import DeviceDataView, DeviceDataRangeView, DeviceDataLatestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', DeviceDataView.as_view(), name='data-ingest'),
    path('data/range/', DeviceDataRangeView.as_view(), name='data-range'),
    path('data/latest/<str:device_id>/', DeviceDataLatestView.as_view(), name='data-latest')
]
