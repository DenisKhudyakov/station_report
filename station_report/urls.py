from django.urls import path

from station_report.apps import StationReportConfig
from station_report.views import StationReportView, StationReportUpdateView, StationReportDeleteView, StationCreateView

app_name = StationReportConfig.name

urlpatterns = [
    path("", StationReportView.as_view(), name="report_view"),
    path("<int:pk>/", StationReportUpdateView.as_view(), name="station_report_update"),
    path("<int:pk>/delete/", StationReportDeleteView.as_view(), name="station_report_delete"),
    path("create/", StationCreateView.as_view(), name="station_report_create"),
]
