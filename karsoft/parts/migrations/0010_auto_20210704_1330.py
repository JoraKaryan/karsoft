# Generated by Django 3.1.7 on 2021-07-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0009_reserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='phone',
            field=models.TextField(),
        ),
    ]
