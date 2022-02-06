# Generated by Django 3.1.7 on 2021-07-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0008_auto_20210318_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('ReserveID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]
