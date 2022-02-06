# Generated by Django 3.1.7 on 2021-08-30 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0020_auto_20210831_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interfacecontrol',
            name='TYPE',
        ),
        migrations.AddField(
            model_name='interfacecontrol',
            name='FOR_WHOM',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='interfacecontrol',
            name='FIELD_NAME',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='input_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 31, 0, 50, 27, 33798)),
        ),
    ]