from django.shortcuts import render
from django.views.generic import ListView

from station_report.models import Station, Section, SectionDate


def home(request):
    return render(request, "station_report/start_page.html")


class StationReportView(ListView):
    template_name = "station_report/report.html"
    model = Station

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_stations = []

        stations = Station.objects.all()
        for station in stations:
            data_structure = {
                "station": station,
                "sections": {
                    "КМ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                    "ТХ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                    "ЭОМ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                            "start_work_date": None, "comment": None, "complate_date": None},
                    "ЭОМшк": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                              "start_work_date": None, "comment": None, "complate_date": None},
                    "АК": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                    "АКшк": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                             "start_work_date": None, "comment": None, "complate_date": None},
                    "ОВ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                },
            }

            for section in Section.objects.filter(station=station):
                section_data = data_structure["sections"].get(section.section_name)
                if section_data:
                    section_data["section_name"] = section.section_name
                    section_data["is_completed"] = section.is_completed
                    section_data["comment"] = section.comment
                    section_data["start_work_date"] = section.start_work_date
                    section_data["complate_date"] = section.complate_date
                    for section_date in SectionDate.objects.filter(section=section):
                        if section_date.issue_date_SZ:
                            section_data["issue_date_SZ"].append(section_date.issue_date_SZ)
                        if section_date.issue_date_RD:
                            section_data["issue_date_RD"].append(section_date.issue_date_RD)

            data_stations.append(data_structure)

        context["stations"] = data_stations
        return context


class TestView(ListView):
    template_name = "station_report/main.html"
    model = Station

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_stations = []

        stations = Station.objects.all()
        for station in stations:
            data_structure = {
                "station": station,
                "sections": {
                    "КМ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                    "ТХ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                    "ЭОМ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                            "start_work_date": None, "comment": None, "complate_date": None},
                    "ЭОМшк": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                              "start_work_date": None, "comment": None, "complate_date": None},
                    "АК": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                    "АКшк": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                             "start_work_date": None, "comment": None, "complate_date": None},
                    "ОВ": {"section_name": None, "issue_date_SZ": [], "issue_date_RD": [], "is_completed": None,
                           "start_work_date": None, "comment": None, "complate_date": None},
                },
            }

            for section in Section.objects.filter(station=station):
                section_data = data_structure["sections"].get(section.section_name)
                if section_data:
                    section_data["section_name"] = section.section_name
                    section_data["is_completed"] = section.is_completed
                    section_data["comment"] = section.comment
                    section_data["start_work_date"] = section.start_work_date
                    section_data["complate_date"] = section.complate_date
                    for section_date in SectionDate.objects.filter(section=section):
                        if section_date.issue_date_SZ:
                            section_data["issue_date_SZ"].append(section_date.issue_date_SZ)
                        if section_date.issue_date_RD:
                            section_data["issue_date_RD"].append(section_date.issue_date_RD)

            data_stations.append(data_structure)

        context["stations"] = data_stations
        return context