from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Место', null=True)

    def __str__(self):
        return str(self.name)

class Files(models.Model):
    date = models.DateField(verbose_name='Дата:', null=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место', null=True)
    file = models.FileField(verbose_name='Файл', upload_to='data/', default=None)
    read = models.BooleanField(verbose_name='Прочитан', default=False)
    comment = models.CharField(max_length=500, verbose_name='Комментарий', null=True, default=' ')

    def __str__(self):
        return str(self.pk+' '+self.place+' '+self.date)

class FilesTbl(models.Model):
    parent = models.ForeignKey('Files', on_delete=models.CASCADE, verbose_name='Родитель')
    x = models.FloatField(verbose_name='x', null=True)
    y = models.FloatField(verbose_name='y', null=True)
    z = models.FloatField(verbose_name='z', null=True)
    s = models.FloatField(verbose_name='S', null=True)
    l = models.FloatField(verbose_name='L', null=True)
    name = models.CharField(max_length=100, verbose_name='Обозначение')
    old_num = models.IntegerField(verbose_name='Старый номер')
    newline = models.BooleanField(verbose_name='Новая строка', default=False)

    def __str__(self):
        return str(self.name)

class Files_gps(models.Model):
    date = models.DateField(verbose_name='Дата:', null=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место', null=True)
    file = models.FileField(verbose_name='Файл', upload_to='data/', default=None)
    read = models.BooleanField(verbose_name='Прочитан', default=False)
    comment = models.CharField(max_length=500, verbose_name='Комментарий', null=True, default=' ')

    def __str__(self):
        return str(self.pk+' '+self.place+' '+self.date)

class FilesTbl_gps(models.Model):
    parent = models.ForeignKey('Files_gps', on_delete=models.CASCADE, verbose_name='Родитель')
    x = models.FloatField(verbose_name='x', null=True)
    y = models.FloatField(verbose_name='y', null=True)
    z = models.FloatField(verbose_name='z', null=True)
    name = models.CharField(max_length=100, verbose_name='Обозначение')
    newline = models.BooleanField(verbose_name='Новая строка', default=False)

    def __str__(self):
        return str(self.name)

class GPS(models.Model):
    parent = models.ForeignKey('GPS_doc', on_delete=models.CASCADE, verbose_name='Родитель')
    name = models.CharField(max_length=100, verbose_name='Имя', null=True, default=' ')
    x = models.FloatField(verbose_name='x', null=True)
    y = models.FloatField(verbose_name='y', null=True)
    z = models.FloatField(verbose_name='z', null=True)
    x2 = models.FloatField(verbose_name='x2', null=True)
    y2 = models.FloatField(verbose_name='y2', null=True)
    z2 = models.FloatField(verbose_name='z2', null=True)
    ox = models.FloatField(verbose_name='ox', null=True, default=0)
    oy = models.FloatField(verbose_name='oy', null=True, default=0)
    oz = models.FloatField(verbose_name='oz', null=True, default=0)
    absolute = models.FloatField(verbose_name='absolute', null=True, default=0)
    v = models.FloatField(verbose_name='v', null=True, default=0)
    newline = models.BooleanField(verbose_name='Новая строка', default=False)

class GPS_doc(models.Model):
    date = models.DateField(verbose_name='Дата:', null=True)
    date1 = models.DateField(verbose_name='Дата1:', null=True)
    date2 = models.DateField(verbose_name='Дата2:', null=True)
    place = place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место', null=True)
    file1 = models.FileField(max_length=300, upload_to='data/', verbose_name='Файл', null=True, default=' ')
    file2 = models.FileField(max_length=300, upload_to='data/', verbose_name='Файл', null=True, default=' ')
    comment = models.CharField(max_length=300, verbose_name='Комментарий', null=True, default=' ')
    read = models.BooleanField(verbose_name='Прочитан', default=False)

class Step_2(models.Model):
    parent = models.ForeignKey('Step_2_doc', on_delete=models.CASCADE, verbose_name='Родитель')
    name = models.CharField(max_length=100, verbose_name='Имя', null=True, default=' ')
    x = models.FloatField(verbose_name='x', null=True)
    y = models.FloatField(verbose_name='y', null=True)
    z = models.FloatField(verbose_name='z', null=True)
    s = models.FloatField(verbose_name='S', null=True)
    l = models.FloatField(verbose_name='L', null=True)
    newline = models.BooleanField(verbose_name='nl', default=False)
    x2 = models.FloatField(verbose_name='x2', null=True)
    y2 = models.FloatField(verbose_name='y2', null=True)
    z2 = models.FloatField(verbose_name='z2', null=True)
    s2 = models.FloatField(verbose_name='S2', null=True)
    l2 = models.FloatField(verbose_name='L2', null=True)
    newline2 = models.BooleanField(verbose_name='nl2', default=False)
    ox = models.FloatField(verbose_name='ox', null=True)
    oy = models.FloatField(verbose_name='oy', null=True)
    oz = models.FloatField(verbose_name='oz', null=True)
    ol = models.FloatField(verbose_name='ol', null=True)
    os = models.FloatField(verbose_name='os', null=True)
    absolute = models.FloatField(verbose_name='absolute', null=True)
    newline = models.BooleanField(verbose_name='nw', default=False)
    newline2 = models.BooleanField(verbose_name='nw2', default=False)

class Step_2_doc(models.Model):
    date = models.DateField(verbose_name='Дата:', null=True)
    file1 = models.CharField(max_length=300, verbose_name='Файл1', null=True, default=' ')
    file2 = models.CharField(max_length=300, verbose_name='Файл2', null=True, default=' ')
    comment = models.CharField(max_length=300, verbose_name='Комментарий', null=True, default=' ')





