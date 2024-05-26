from django.urls import path

from station_report.apps import StationReportConfig
from station_report.views import home, StationReportView

app_name = StationReportConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('report_view/', StationReportView.as_view(), name='report_view'),
]