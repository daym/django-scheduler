# Generated by Django 4.1.7 on 2023-03-22 11:15

from django.db import migrations, models
import django.db.models.deletion
#from django.utils.translation import gettext_lazy as _

def insert_initial_records(apps, schema_editor):
        RuleParam = apps.get_model('schedule', 'RuleParam')
        RuleParamVariant = apps.get_model('schedule', 'RuleParamVariant')
        def ins(name, display_string, easy_variants=[], complicated_variants=[]):
            dummy = _(display_string) # dummy so translation is picked up
            param = RuleParam(name=name, display_string=display_string)
            param.save()
            for easy_variant in easy_variants:
                variant = RuleParamVariant(param=param, value=easy_variant, value_display_string=str(easy_variant))
                variant.save()
            for value, value_display_string in complicated_variants:
                variant = RuleParamVariant(param=param, value=value, value_display_string=value_display_string)
                variant.save()
            param.save()
        ins('bysetpos', 'instance', range(-366, 367)) # display_string translated by view
        ins('bymonth', 'every month of', complicated_variants=[(1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'), (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC')])
        ins('bymonthday', 'every monthday of', range(1, 32))
        ins('byyearday', 'every yearday of', range(1, 367))
        ins('byweekno', 'every week of', range(1, 53))
        ins('byweekday', 'every weekday of', complicated_variants=[(0, 'MO'), (1, 'TU'), (2, 'WE'), (3, 'TH'), (4, 'FR'), (5, 'SA'), (6, 'SU')])
        ins('byhour', 'every hour of', range(0, 24))
        ins('byminute', 'every minute of', range(0, 60))
        ins('bysecond', 'every second of', range(0, 61))
        ins('byeaster', 'around easter by days', range(-366, 367))


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_use_autofields_for_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='name')),
                ('display_string', models.CharField(max_length=32, unique=True, verbose_name='display string')),
            ],
        ),
        migrations.CreateModel(
            name='RuleParamVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='value')),
                ('value_display_string', models.CharField(max_length=32, verbose_name='value display string')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant_set', to='schedule.ruleparam', verbose_name='Possible value')),
            ],
        ),
        migrations.AddIndex(
            model_name='ruleparam',
            index=models.Index(fields=['name'], name='schedule_ru_name_dfef45_idx'),
        ),
        migrations.AddField(
            model_name='rule',
            name='repeats',
            field=models.ManyToManyField(to='schedule.ruleparamvariant'),
        ),
        migrations.AddIndex(
            model_name='ruleparamvariant',
            index=models.Index(fields=['param'], name='schedule_ru_param_i_e6ad15_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='ruleparamvariant',
            unique_together={('param', 'value')},
        ),
        migrations.RunPython(insert_initial_records),
    ]
