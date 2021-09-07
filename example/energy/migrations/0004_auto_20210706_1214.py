# Generated by Django 3.2.5 on 2021-07-06 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0003_files_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestbl',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Обозначение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='comment',
            field=models.CharField(default=' ', max_length=500, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='files',
            name='file_path',
            field=models.CharField(default='no path', max_length=500, null=True, verbose_name='Путь к файлу'),
        ),
        migrations.AlterField(
            model_name='files',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='energy.place', verbose_name='Место'),
        ),
    ]