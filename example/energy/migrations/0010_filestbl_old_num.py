# Generated by Django 3.2.5 on 2021-07-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0009_auto_20210713_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestbl',
            name='old_num',
            field=models.IntegerField(default=1, verbose_name='Старый ноиер'),
            preserve_default=False,
        ),
    ]
