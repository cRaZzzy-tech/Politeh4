from django.contrib import admin

from .models import *

# Register your models here.
class Files_form(admin.ModelAdmin):
    list_display = ('date', 'place', 'file')

class Place_form(admin.ModelAdmin) :
    list_display = ('name',)


admin.site.register(Files, Files_form)
admin.site.register(Place, Place_form)