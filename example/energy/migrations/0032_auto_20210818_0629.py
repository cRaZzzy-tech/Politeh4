# Generated by Django 3.2.5 on 2021-08-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0031_auto_20210813_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestbl',
            name='newline',
            field=models.BooleanField(default=False, verbose_name='Новая строка'),
        ),
        migrations.AlterField(
            model_name='filestbl',
            name='old_num',
            field=models.IntegerField(verbose_name='Старый номер'),
        ),
    ]
