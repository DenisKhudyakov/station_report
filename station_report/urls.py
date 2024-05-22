from django.urls import path

from station_report.apps import StationReportConfig
from station_report.views import home

app_name = StationReportConfig.name

urlpatterns = [
    path('', home, name='home'),
]