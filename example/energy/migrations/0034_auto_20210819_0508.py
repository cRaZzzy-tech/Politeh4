# Generated by Django 3.2.5 on 2021-08-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0033_auto_20210818_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_2',
            name='newline',
            field=models.BooleanField(default=False, verbose_name='nw'),
        ),
        migrations.AlterField(
            model_name='step_2',
            name='newline2',
            field=models.BooleanField(default=False, verbose_name='nw2'),
        ),
    ]
