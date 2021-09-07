# Generated by Django 3.2.5 on 2021-08-23 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0037_auto_20210821_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gps_doc',
            old_name='file',
            new_name='file1',
        ),
        migrations.AddField(
            model_name='gps',
            name='absolute',
            field=models.FloatField(default=0, null=True, verbose_name='absolute'),
        ),
        migrations.AddField(
            model_name='gps',
            name='newline',
            field=models.BooleanField(default=False, verbose_name='Новая строка'),
        ),
        migrations.AddField(
            model_name='gps',
            name='ox',
            field=models.FloatField(default=0, null=True, verbose_name='ox'),
        ),
        migrations.AddField(
            model_name='gps',
            name='oy',
            field=models.FloatField(default=0, null=True, verbose_name='oy'),
        ),
        migrations.AddField(
            model_name='gps',
            name='oz',
            field=models.FloatField(default=0, null=True, verbose_name='oz'),
        ),
        migrations.AddField(
            model_name='gps',
            name='v',
            field=models.FloatField(default=0, null=True, verbose_name='v'),
        ),
        migrations.AddField(
            model_name='gps',
            name='x2',
            field=models.FloatField(null=True, verbose_name='x2'),
        ),
        migrations.AddField(
            model_name='gps',
            name='y2',
            field=models.FloatField(null=True, verbose_name='y2'),
        ),
        migrations.AddField(
            model_name='gps',
            name='z2',
            field=models.FloatField(null=True, verbose_name='z2'),
        ),
        migrations.AddField(
            model_name='gps_doc',
            name='file2',
            field=models.FileField(default=' ', max_length=300, null=True, upload_to='data/', verbose_name='Файл'),
        ),
    ]