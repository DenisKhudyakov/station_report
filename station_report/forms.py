from django import forms

from station_report.models import Station, Section, SectionDate

from django.forms import inlineformset_factory


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = "__all__"


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_name', 'is_completed', 'comment', 'start_work_date', 'complate_date']

class SectionDateForm(forms.ModelForm):
    class Meta:
        model = SectionDate
        fields = ['issue_date_SZ', 'issue_date_RD']


SectionFormSet = inlineformset_factory(Station, Section, form=SectionForm, extra=1, can_delete=True)
SectionDateFormSet = inlineformset_factory(Section, SectionDate, form=SectionDateForm, extra=1, can_delete=True)
