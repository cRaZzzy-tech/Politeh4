# Generated by Django 3.2.5 on 2021-08-21 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0034_auto_20210819_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gps_doc',
            name='date2',
        ),
    ]
