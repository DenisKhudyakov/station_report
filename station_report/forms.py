from django import forms

from station_report.models import Station, Section

from django.forms import inlineformset_factory


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = "__all__"


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


SectionFormSet = inlineformset_factory(Station, Section, form=SectionForm, extra=0, can_delete=True)
