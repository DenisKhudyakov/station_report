from django.urls import path

from station_report.apps import StationReportConfig
from station_report.views import StationReportView

app_name = StationReportConfig.name

urlpatterns = [
    path("", StationReportView.as_view(), name="report_view"),
]
