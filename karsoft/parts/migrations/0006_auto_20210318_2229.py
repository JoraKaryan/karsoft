# Generated by Django 3.1.7 on 2021-03-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_auto_20210318_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
