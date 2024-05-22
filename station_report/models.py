from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Station(models.Model):
    """Модель станции"""
    station_number = models.CharField(max_length=50, unique=True, verbose_name='station')

    def __str__(self):
        return self.station_number


class Section(models.Model):
    """Модель этапа производства"""
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.station} - {self.section_name}"


class SectionDate(models.Model):
    """Модель дата выдачи СЗ и дата выдачи РД"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    issue_date_SZ = models.DateField(null=True, blank=True)
    issue_date_RD = models.DateField(null=True, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.section} - Dates"
