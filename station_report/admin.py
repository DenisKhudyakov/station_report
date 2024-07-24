from django.contrib import admin

from station_report import models


@admin.register(models.Station)
class StationAdmin(admin.ModelAdmin):
    fields = ("station_number",)


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    fields = (
        "station",
        "section_name",
        "is_completed",
        "comment",
        "start_work_date",
        "complate_date",
    )

