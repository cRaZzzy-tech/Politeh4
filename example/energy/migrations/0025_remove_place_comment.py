# Generated by Django 3.2.5 on 2021-08-12 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0024_place_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='comment',
        ),
    ]
