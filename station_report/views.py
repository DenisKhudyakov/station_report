from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from station_report.models import Station, Section, SectionDate


def home(request):
    return render(request, 'station_report/start_page.html')


class StationReportView(ListView):
    template_name = 'station_report/report.html'
    model = Station

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        stations = Station.objects.all()
        for station in stations:
            sections = Section.objects.filter(station=station)
            section_data = SectionDate.objects.filter(section__in=sections)
            context['stations'] = stations
            context['sections'] = sections
            context['section_data'] = section_data
        return context
