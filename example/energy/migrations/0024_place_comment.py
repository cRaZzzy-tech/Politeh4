# Generated by Django 3.2.5 on 2021-08-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0023_auto_20210730_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='comment',
            field=models.CharField(default=' ', max_length=500, null=True, verbose_name='Комментарий'),
        ),
    ]
