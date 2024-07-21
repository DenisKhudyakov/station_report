# Generated by Django 5.0.6 on 2024-07-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("station_report", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="comment",
            field=models.TextField(blank=True, null=True, verbose_name="Комментарий"),
        ),
        migrations.AlterField(
            model_name="section",
            name="is_completed",
            field=models.BooleanField(
                default=False, verbose_name="Скомплектовано? Галочкой отметить"
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="section_name",
            field=models.CharField(max_length=50, verbose_name="Название этапа"),
        ),
        migrations.AlterField(
            model_name="sectiondate",
            name="issue_date_RD",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата выдачи РД"
            ),
        ),
        migrations.AlterField(
            model_name="sectiondate",
            name="issue_date_SZ",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата выдачи СЗ"
            ),
        ),
        migrations.AlterField(
            model_name="station",
            name="station_number",
            field=models.CharField(max_length=50, unique=True, verbose_name="Станция"),
        ),
    ]
