from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from station_report.forms import StationForm, SectionFormSet
from station_report.models import Station, Section


class StationReportView(ListView):
    """Основной контроллер отображения отчета"""

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
                    "КМ": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
                    "ТХ": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
                    "ЭОМ": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
                    "ЭОМшк": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
                    "АК": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
                    "АКшк": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
                    "ОВ": {
                        "section_name": None,
                        "issue_date_SZ": [],
                        "issue_date_RD": [],
                        "is_completed": None,
                        "start_work_date": None,
                        "comment": None,
                        "complate_date": None,
                    },
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
                    section_data["issue_date_SZ"] = section.issue_date_SZ
                    section_data["issue_date_RD"] = section.issue_date_RD

            data_stations.append(data_structure)

        context["stations"] = data_stations
        return context


class StationReportUpdateView(UpdateView):
    """Обновление отчет по станции"""

    model = Station
    form_class = StationForm
    success_url = reverse_lazy("report:report_view")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            section_formset = SectionFormSet(self.request.POST, instance=self.object)
        else:
            section_formset = SectionFormSet(instance=self.object)
        data['section_formset'] = section_formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        section_formset = context['section_formset']
        self.object = form.save()

        if section_formset.is_valid():
            self.object = form.save()
            section_formset.instance = self.object
            section_formset.save()
        else:
            print('Ошибка в section_formset:', section_formset.errors)
            return self.form_invalid(form)

        return super().form_valid(form)


class StationReportDeleteView(DeleteView):
    """Удаление отчета по станции"""

    model = Station
    success_url = reverse_lazy("report:report_view")


class StationCreateView(CreateView):
    """Создание отчета по станции"""

    model = Station
    form_class = StationForm
    success_url = reverse_lazy("report:report_view")
    template_name = "station_report/station_create.html"

    def form_valid(self, form):
        self.object = form.save()

        section_names = ['КМ', 'ТХ', 'ЭОМ', 'ЭОМшк', 'АК', 'АКшк', 'ОВ']

        for name in section_names:
            section = Section.objects.create(
                station=self.object,
                section_name=name
            )

        return super().form_valid(form)

