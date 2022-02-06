# Generated by Django 3.1.7 on 2021-08-30 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0019_auto_20210828_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceControl',
            fields=[
                ('ID', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('PARENTID', models.IntegerField(db_index=True)),
                ('MAPPING', models.CharField(db_index=True, max_length=30)),
                ('SORT', models.IntegerField(blank=True, null=True)),
                ('TYPE', models.CharField(blank=True, max_length=30, null=True)),
                ('TEXT', models.CharField(blank=True, max_length=150, null=True)),
                ('FIELD_NAME', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='reserve',
            name='input_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 31, 0, 43, 39, 563834)),
        ),
    ]
