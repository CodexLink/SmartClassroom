# Generated by Django 3.0.3 on 2020-02-09 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCControlSystem', '0003_auto_20200209_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='Classroom_Status',
            field=models.CharField(choices=[('Operational', 'Operational'), ('In-Use', 'In-Use'), ('Opened', 'Opened'), ('Closed', 'Closed'), ('Non-Operational', 'Non-Operational')], default=('Operational', 'Operational'), help_text='Status Indication of the classroom. Required', max_length=15, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(15)], verbose_name='Classroom Instructure Status'),
        ),
    ]