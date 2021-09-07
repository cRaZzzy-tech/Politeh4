from django.forms import inlineformset_factory, Select, NumberInput, formset_factory, CheckboxInput, NullBooleanSelect, \
    TextInput, Textarea
from django import forms

from .models import Files, FilesTbl, Files_gps, FilesTbl_gps, Step_2_doc, Step_2, Place, GPS_doc, GPS

class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

# mymodel.objects.filter(first_name__icontains="Foo", first_name__icontains="Bar")

# class GPSModal(forms.Form):
#     gps_files = forms.ModelMultipleChoiceField(queryset=GPS_doc.objects.all().values_list("file"), label='Файл', blank=True)

class FileModal(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=Step_2_doc.objects.all(), label='Файл', blank=True)

class PlacesModal(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=Place.objects.all(), label='Место', blank=True)

class DateForm1(forms.Form):
    my_date_field = forms.DateField(widget=DateInput, label='Начало')
    my_date_field1 = forms.DateField(widget=DateInput, label='Конец')

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class FilesForm(forms.ModelForm) :
    class Meta :
        model = Files
        fields = ('date', 'place', 'file', 'comment')
        widgets = {'date' : DateInput(), 'comment' : Textarea}

class GPS_docForm(forms.ModelForm) :
    class Meta :
        model = GPS_doc
        fields = ('date', 'place', 'file1', 'file2', 'comment')
        widgets = {'date' : DateInput(), 'comment': Textarea}

class FilesForm_gps(forms.ModelForm) :
    class Meta :
        model = Files
        fields = ('date', 'place', 'file', 'comment')
        widgets = {'date' : DateInput(), 'comment' : Textarea}

class FilesFormGPS(forms.ModelForm) :
    class Meta :
        model = Files_gps
        fields = ('date', 'place', 'file', 'comment')
        widgets = {'date' : DateInput(), 'comment' : Textarea}

FilesFormSet = inlineformset_factory(Files, FilesTbl, form=FilesForm, fields=('name', 'x', 'y', 'z', 'l', 's', 'newline'), extra=1,
                                     widgets={
                                        'name':TextInput(attrs={'class':'name'}),
                                        'x':NumberInput(attrs={'class':'x'}),
                                        'y':NumberInput(attrs={'class':'y'}),
                                        'z':NumberInput(attrs={'class':'z'}),
                                        'l':NumberInput(attrs={'class':'l'}),
                                        's':NumberInput(attrs={'class':'s'}),
                                     })

FilesFormSet_gps_load = inlineformset_factory(Files_gps, FilesTbl_gps, form=FilesForm_gps, fields=('name', 'x', 'y', 'z', 'newline'), extra=1, widgets={
    'name':TextInput(attrs={'class':'name'}),
    'x':NumberInput(attrs={'class':'x'}),
    'y':NumberInput(attrs={'class':'y'}),
    'z':NumberInput(attrs={'class':'z'}),
})

FilesFormSet_step_2 = inlineformset_factory(Step_2_doc,
                                            Step_2,
                                            fields=('name', 'x', 'y', 'z', 's', 'l', 'x2', 'y2', 'z2', 's2', 'l2', 'ox', 'oy', 'oz', 'os', 'ol', 'absolute', 'newline', 'newline2'),
                                            extra = 1,
                                            widgets={
                                                'name' : TextInput(attrs={'class' : 'name'}),
                                                'x' : NumberInput(attrs={'class' : 'x'}),
                                                'y' : NumberInput(attrs={'class' : 'y'}),
                                                'z' : NumberInput(attrs={'class' : 'z'}),
                                                'l' : NumberInput(attrs={'class' : 'l'}),
                                                's' : NumberInput(attrs={'class' : 's'}),
                                                'x2' : NumberInput(attrs={'class' : 'x2'}),
                                                'y2' : NumberInput(attrs={'class' : 'y2'}),
                                                'z2' : NumberInput(attrs={'class' : 'z2'}),
                                                'l2' : NumberInput(attrs={'class' : 'l2'}),
                                                's2' : NumberInput(attrs={'class' : 's2'}),
                                                'ox' : NumberInput(attrs={'class' : 'ox'}),
                                                'oy' : NumberInput(attrs={'class' : 'oy'}),
                                                'oz' : NumberInput(attrs={'class' : 'oz'}),
                                                'ol' : NumberInput(attrs={'class' : 'ol'}),
                                                'os' : NumberInput(attrs={'class' : 'os'}),
                                                'absolute' : NumberInput(attrs={'class' : 'absolute'}),
                                                'newline' : CheckboxInput(attrs={'class' : 'nw'}),
                                                'newline2' : CheckboxInput(attrs={'class' : 'nw2'}),
                                            }
)

FilesFormSet_gps = inlineformset_factory(GPS_doc,
                                            GPS,
                                            fields=('name', 'x', 'y', 'z', 'x2', 'y2', 'z2', 'ox', 'oy', 'oz', 'absolute', 'v'),
                                            extra = 1,
                                            widgets={
                                                'name' : TextInput(attrs={'class' : 'name'}),
                                                'x' : NumberInput(attrs={'class' : 'x'}),
                                                'y' : NumberInput(attrs={'class' : 'y'}),
                                                'z' : NumberInput(attrs={'class' : 'z'}),
                                                'x2' : NumberInput(attrs={'class' : 'x2'}),
                                                'y2' : NumberInput(attrs={'class' : 'y2'}),
                                                'z2' : NumberInput(attrs={'class' : 'z2'}),
                                                'ox' : NumberInput(attrs={'class' : 'ox'}),
                                                'oy' : NumberInput(attrs={'class' : 'oy'}),
                                                'oz' : NumberInput(attrs={'class' : 'oz'}),
                                                'absolute' : NumberInput(attrs={'class' : 'absolute'}),
                                                'v' : NumberInput(attrs={'class' : 'v'}),
                                            }
)

class DateForm1(forms.Form):
    my_date_field = forms.DateField(widget=DateInput, label='Начало')
    my_date_field1 = forms.DateField(widget=DateInput, label='Конец')









