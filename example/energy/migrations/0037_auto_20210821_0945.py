# Generated by Django 3.2.5 on 2021-08-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0036_auto_20210821_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestbl_gps',
            name='newline',
            field=models.BooleanField(default=False, verbose_name='Новая строка'),
        ),
        migrations.AlterField(
            model_name='gps_doc',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата:'),
        ),
    ]
