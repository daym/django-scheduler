# Generated by Django 4.1.7 on 2023-03-25 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0017_delete_category_calendar_color_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ['name'], 'verbose_name': 'calendar', 'verbose_name_plural': 'calendars'},
        ),
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='name'),
        ),
    ]
