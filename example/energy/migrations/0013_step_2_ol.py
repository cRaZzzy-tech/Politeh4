# Generated by Django 3.2.5 on 2021-07-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0012_auto_20210717_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='step_2',
            name='ol',
            field=models.FloatField(null=True, verbose_name='ol'),
        ),
    ]
