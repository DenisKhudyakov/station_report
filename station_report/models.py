from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Station(models.Model):
    """Модель станции"""
    station_number = models.CharField(max_length=50, unique=True, verbose_name='station')

    def __str__(self):
        return self.station_number


class Section(models.Model):
    """Модель этапа производства"""
    station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name='этапы производства')
    section_name = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.station} - {self.section_name}"


class SectionDate(models.Model):
    """Модель дата выдачи СЗ и дата выдачи РД"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='дата выдачи СЗ и дата выдачи РД')
    issue_date_SZ = models.DateField(**NULLABLE)
    issue_date_RD = models.DateField(**NULLABLE)
    comment = models.TextField(**NULLABLE)

    def __str__(self):
        return f"{self.section} - Dates"
