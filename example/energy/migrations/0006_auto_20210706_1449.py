# Generated by Django 3.2.5 on 2021-07-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0005_auto_20210706_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestbl',
            name='secondary_x',
            field=models.FloatField(null=True, verbose_name='sec_x'),
        ),
        migrations.AlterField(
            model_name='filestbl',
            name='secondary_y',
            field=models.FloatField(null=True, verbose_name='sec_y'),
        ),
        migrations.AlterField(
            model_name='filestbl',
            name='secondary_z',
            field=models.FloatField(null=True, verbose_name='sec_z'),
        ),
    ]
