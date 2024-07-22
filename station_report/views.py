from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from station_report.forms import StationForm, SectionFormSet, SectionDateFormSet
from station_report.models import Station, Section, SectionDate


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
                    for section_date in SectionDate.objects.filter(section=section):
                        if section_date.issue_date_SZ:
                            section_data["issue_date_SZ"].append(
                                section_date.issue_date_SZ
                            )
                        if section_date.issue_date_RD:
                            section_data["issue_date_RD"].append(
                                section_date.issue_date_RD
                            )

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
            section_date_formsets = [
                SectionDateFormSet(self.request.POST, instance=section)
                for section in self.object.section_set.all()
            ]
        else:
            section_formset = SectionFormSet(instance=self.object)
            section_date_formsets = [
                SectionDateFormSet(instance=section)
                for section in self.object.section_set.all()
            ]
        data['section_formset'] = section_formset
        data['section_date_formsets'] = section_date_formsets
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        section_formset = context['section_formset']
        section_date_formsets = context['section_date_formsets']
        self.object = form.save()

        if section_formset.is_valid():
            self.object = form.save()
            section_formset.instance = self.object
            section_formset.save()
        else:
            print('Ошибка в section_formset:', section_formset.errors)
            return self.form_invalid(form)

        for section_date_formset in section_date_formsets:
            if section_date_formset.is_valid():
                section_date_formset.instance = self.object
                section_date_formset.save()
            else:
                print('Ошибка в section_date_formset:', section_date_formset.errors)
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
            SectionDate.objects.create(
                section=section
            )

        return super().form_valid(form)

