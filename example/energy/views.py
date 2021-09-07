from datetime import datetime as dt
from math import sqrt

import xlwt

from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
import cmath
# import tablib
from django.db.models import Q

from .forms import FilesForm
from .models import FilesTbl, Files, Step_2_doc, Step_2, Place, Files_gps, FilesTbl_gps, GPS_doc, GPS

def sitemap(request):
    # if request.method == 'POST':
    print('i am here!')
    print(request)

    return render(request, 'energy/sitemap.html' )

def xls(request, pk):
    file = Files.objects.get(pk=pk)
    xxxx = 'Tahe #'+str(file.pk)+' '+str(file.date)+'.xls'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+xxxx

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tahe')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'x', 'y', 'z', 's', 'l']

    for col_num in range(len(columns)) :
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = FilesTbl.objects.filter(parent=pk).values_list('name', 'x', 'y', 'z', 's', 'l')
    for row in rows :
        row_num += 1
        for col_num in range(len(row)) :
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def xls_tahe(request,pk):
    file = Step_2_doc.objects.get(pk=pk)
    xxxx = 'finaltahe #'+str(file.pk)+' '+str(file.date)+'.xls'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+xxxx

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tahe')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'x', 'y', 'z', 's', 'l', 'x2', 'y2', 'z2', 's2', 'l2', 'ox', 'ox', 'oz', 'os', 'ol', 'absolute']

    for col_num in range(len(columns)) :
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Step_2.objects.filter(parent=pk).values_list('name', 'x', 'y', 'z', 's', 'l', 'x2', 'y2', 'z2', 's2', 'l2', 'ox', 'ox', 'oz', 'os', 'ol', 'absolute')
    for row in rows :
        row_num += 1
        for col_num in range(len(row)) :
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def xls_gps_final(request, pk):
    file = GPS_doc.objects.get(pk=pk)
    xxxx = 'GPS_final file #'+str(file.pk)+' '+str(file.date)+'.xls'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+xxxx

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('GPS_file')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'x', 'y', 'z', 'x2', 'y2', 'z2', 'ox', 'oy', 'oz', 'absolute', 'v']

    for col_num in range(len(columns)) :
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = GPS.objects.filter(parent=pk).values_list('name', 'x', 'y', 'z', 'x2', 'y2', 'z2', 'ox', 'oy', 'oz', 'absolute', 'v')
    for row in rows :
        row_num += 1
        for col_num in range(len(row)) :
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def xls_gps(request, pk):
    file = Files_gps.objects.get(pk=pk)
    xxxx = 'GPS file #'+str(file.pk)+' '+str(file.date)+'.xls'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+xxxx

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('GPS_file')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'x', 'y', 'z']

    for col_num in range(len(columns)) :
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = FilesTbl_gps.objects.filter(parent=pk).values_list('name', 'x', 'y', 'z')
    for row in rows :
        row_num += 1
        for col_num in range(len(row)) :
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def xls_gps_reserve(request, pk):
    file = Files_gps.objects.get(pk=pk)
    xxxx = 'GPS file #'+str(file.pk)+' '+str(file.date)+'.xls'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+xxxx

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('GPS_file')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'x', 'y', 'z', 'x2', 'y2', 'z2', 'ox', 'ox', 'oz', 'absolute', 'v']

    for col_num in range(len(columns)) :
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = GPS.objects.filter(parent=pk).values_list('name', 'x', 'y', 'z', 'x2', 'y2', 'z2', 'ox', 'ox', 'oz', 'absolute', 'v')
    for row in rows :
        row_num += 1
        for col_num in range(len(row)) :
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def load_files_new(request):

    bbb = FilesTbl.objects.filter(parent=1)
    bbb.delete()
    i = 0
    lst = []
    first_s = 0
    second_s = 0
    third_s = 0
    with open('energy/april.txt', "r") as file :
        print('пробуем читать')
        for line in file :
            print(i,')',line)
            i+=1
            first_num = str(line).find(',')
            # first = line[:first_num]
            fle = line[first_num+1:]
            second_num = str(fle).find(',')
            # second = fle[:second_num]
            fle = fle[second_num+1:]
            third_num = str(fle).find(',')
            # third = fle[:third_num]
            fle = fle[third_num + 1 :]
            fourth_num = str(fle).find(',')
            fourth = fle[:fourth_num]
            # # lst.append({'name':first, 'x':second, 'y':third, 'z':fourth})
            # i+=1
            # if i == 1:
            #     FilesTbl.objects.create(
            #         parent=Files.objects.get(id=1),
            #         x=second,
            #         y=third,
            #         z=fourth,
            #         name=first,
            #         secondary_x=0,
            #         secondary_y=0,
            #         secondary_z=0
            #     )
            # else:
            #     j = 0
            #     if int(str(second)[:second.find('.')]) == last_x and int(str(third)[:third.find('.')]) == last_y:
            #         # j += 1
            #         print('попадаю сюда!',int(str(second)[:second.find('.')]))
            #         lst.append([first, second, third, fourth, 0, 0, 0])
            #         FilesTbl.objects.create(
            #             parent=Files.objects.get(id=1),
            #             x=second,
            #             y=third,
            #             z=fourth,
            #             name = first,
            #             secondary_x = 0,
            #             secondary_y = 0,
            #             secondary_z = 0
            #         )
            #     else:
            #         # print('попадаю сюда!!!! оу')
            #         # lst.append([first, second, third, fourth, 0, 0, 0])
            #         print(lst)
            #         for line in lst:
            #
            #             print(j,'_')
            #             first_s = first_s + float(line[1])
            #             second_s = second_s + float(line[2])
            #             third_s = third_s + float(line[3])
            #
            #         kol = len(lst)
            #         print(kol)
            #         first_s = first_s / j
            #         second_s = second_s / j
            #         third_s = third_s / j
            #
            #         FilesTbl.objects.create(
            #             parent=Files.objects.get(id=1),
            #             x=second,
            #             y=third,
            #             z=fourth,
            #             name = first,
            #             secondary_x = first_s,
            #             secondary_y = second_s,
            #             secondary_z = third_s
            #         )
            #         lst = []
            #         # lst.append([first, second, third, fourth, first_s, second_s, third_s])

            # last_x = int(str(second)[:second.find('.')])
            # last_y = int(str(third)[:third.find('.')])
            # print('________',i,'_________')
            # last_z = int(str(fourth)[:fourth.find('.')])
            # print(int(str(second)[:second.find('.')]), int(str(third)[:third.find('.')]))
            # if i > 0:
            #     if int(second)
            #
            #
            #     last_x =
            #     last_y =

            # FilesTbl.objects.create(
            #     parent=Files.objects.get(id=1),
            #     x=second,
            #     y=third,
            #     z=fourth,
            #     name = first
            # )
        # print(lst, type(lst))

        # lst = lst.append(d)
            # print(line, end="")
    # print(lst)
    read_form = FilesForm()
    context = {'form': read_form}
    return render(request, 'energy/load_files.html', context)

def load_files(request):
    if 'newsletter_sub' in request.POST:
        # print('i 4to')
        file = PlaceForm(request.POST)
        print(file)
        if file.is_valid():
            file.save()
        else:
            print('Форма нового места не валидна')
            print(file.errors)
    if 'place' in request.POST:
        place = Place.objects.get(pk=request.POST['places'])
        docs = Files.objects.filter(place=place).order_by('-date')
        read_form = FilesForm()
        location = PlaceForm()
        places_modal = PlacesModal()
        period = DateForm1
        context = {'form' : read_form, 'docs' : docs, 'location' : location, 'places_modal' : places_modal,
                   'period' : period}
        return render(request, 'energy/load_files.html', context)
    if 'place_clear' in request.POST:
        print(request.POST)
    if 'period' in request.POST:
        dates = DateForm1(request.POST)
        if dates.is_valid() :
            docs = Files.objects.filter(
                date__range=[dates.cleaned_data['my_date_field'], dates.cleaned_data['my_date_field1']]).order_by(
                '-date')
            read_form = FilesForm()
            location = PlaceForm()
            places_modal = PlacesModal()
            period = DateForm1
            context = {'form': read_form, 'docs': docs, 'location':location, 'places_modal':places_modal, 'period':period}
            return render(request, 'energy/load_files.html', context)
    #     file = FilesForm(request.POST)
    #     print(request.POST)
    #     if file.is_valid():
    #         print('Форма файла валидна')
    #     else:
    #         print('Форма не валидна')
    #         print(file.errors)
        # Files.objects.create(
        #     date=request.POST.get('date'),
        #     place=Place.objects.get(pk=int(request.POST.get('place'))),
        #     comment=request.POST.get('comment'),
        #     file = request.POST.get('file'),
        #     read = False
        # )
        # if file.is_valid():
        #     file.save()
            # return redirect('energy:profile_bb_change', pk=pk)
    docs = Files.objects.all().order_by('-date')
    read_form = FilesForm()
    location = PlaceForm()
    places_modal = PlacesModal()
    period = DateForm1
    context = {'form': read_form, 'docs': docs, 'location':location, 'places_modal':places_modal, 'period':period}
    return render(request, 'energy/load_files.html', context)

def load_gps(request):
    if 'clear_period' in request.POST:
        print(request.POST)
    if 'newsletter_sub' in request.POST:
        print('пробуем')
        dates = DateForm1(request.POST)
        if dates.is_valid() :
            docs = Files_gps.objects.filter(
                date__range=[dates.cleaned_data['my_date_field'], dates.cleaned_data['my_date_field1']]).order_by(
                '-date')
            read_form = PlacesModal()
            files = FileModal()
            contractor = DateForm1()
            context = {'docs' : docs, 'files' : files, 'contractor' : contractor, 'form': read_form}
            return render(request, 'energy/load_gps.html', context)
    if 'place' in request.POST:
        place = Place.objects.get(pk=request.POST['places'])
        docs = Files_gps.objects.filter(place=place)
        read_form = PlacesModal()
        files = FileModal()
        contractor = DateForm1()
        context = {'docs' : docs, 'files' : files, 'contractor' : contractor, 'form' : read_form}
        return render(request, 'energy/load_gps.html', context)
    if 'place_clear' in request.POST:
        print(request.POST)
    docs = Files_gps.objects.all().order_by('-date')
    read_form = PlacesModal()
    files = FileModal()
    contractor = DateForm1()
    context = {'docs': docs, 'files': files, 'contractor': contractor, 'form': read_form}
    return render(request, 'energy/load_gps.html', context)

def search(request, pk):
    if "apply" in request.POST:
        i = 0
        lst_bool = False
        final_lst = []
        lst = []
        for line in request.POST:
            if i > 5:
                if line[len(line)-4:] == 'name' and lst_bool:
                    final_lst.append(lst)
                    lst = []
                lst.append(request.POST[line])
                if not lst_bool:
                    lst_bool = True
            i += 1

        fileTbl = FilesTbl.objects.filter(parent=pk)
        fileTbl.delete()
        i = 0
        for line in final_lst:
            if i == 0:
                FilesTbl.objects.create(
                    parent=Files.objects.get(pk=pk),
                    x=line[1],
                    y=line[2],
                    z=line[3],
                    name=line[0],
                    l = 0,
                    s = 0,
                    old_num=0
                )
                last_x = float(line[1])
                last_y = float(line[2])
                first_x = float(line[1])
                first_y = float(line[2])
            else:
                nums1 = (last_y - float(line[2])) ** 2
                nums2 = (last_x - float(line[1])) ** 2
                num3 = nums1 + nums2
                num4 = cmath.sqrt(num3)
                num5 = str(num4)[:str(num4).find('.')+3]
                # print('num3',num3,'num4',num4)
                num5 = str(num4)[1 :str(num4).find('.') + 5]
                numl1 = (first_y - float(line[2])) ** 2
                numl2 = (first_x - float(line[1])) ** 2
                numl3 = numl1 + numl2
                numl4 = cmath.sqrt(numl3)
                numl5 = str(numl4)[1 :int(str(numl4).find('.') + 3)]
                print(num4, num5, str(numl4)[1 :int(str(numl4).find('.') + 3)])

                last_x = float(line[1])
                last_y = float(line[2])
                # print(num4, num5)
                # if 'newline' in str(line[0]):

                FilesTbl.objects.create(
                    parent=Files.objects.get(pk=pk),
                    x=line[1],
                    y=line[2],
                    z=line[3],
                    name=line[0],
                    l = numl5,
                    s = num5,
                    old_num=0
                )
            i += 1
            # print(line)

    if 'correct' in request.POST:
        print('correct')
        i = 0
        fileTbl = FilesTbl.objects.filter(parent=pk)
        fileTbl.delete()
        lst_bool = False
        lst = []
        final_lst = []
        # for line in request.POST:
        #     print(line, request.POST[line])
        print(len(request.POST))
        for line in request.POST:
            i += 1
            if i > 6:
                if line[len(line)-4:] == 'name' and lst_bool:
                    # print(line, request.POST[line])
                    final_lst.append(lst)
                    lst = []
                    # if request.POST[line] == '':
                    #     continue

                lst.append(request.POST[line])

                if not lst_bool :
                    lst_bool = True

        for line in final_lst:
            # print(line[0])
            if str(line[0])[len(line[0]) - 7 :] == 'newline':
                line[0] = str(line[0])[:-7]
                FilesTbl.objects.create(
                    parent=Files.objects.get(pk=pk),
                    x=line[1],
                    y=line[2],
                    z=line[3],
                    name=line[0],
                    l=line[4],
                    s=line[5],
                    old_num=0,
                    newline = 1
                )
            else:
                FilesTbl.objects.create(
                    parent=Files.objects.get(pk=pk),
                    x=line[1],
                    y=line[2],
                    z=line[3],
                    name=line[0],
                    l=line[4],
                    s=line[5],
                    old_num=0
                )
        x = FilesTbl.objects.filter(parent=Files.objects.get(pk=pk))
        for line in x:
            if line.name =='':
                line.delete()

    file = Files.objects.get(pk=pk)
    fileTbl = FilesTbl.objects.filter(parent=pk)
    formset = FilesFormSet(instance=file)
    context = {'file' : file, 'fileTbl' : fileTbl, 'formset': formset}
    return render(request, 'energy/search_files.html', context)

def search_gps_load(request, pk):
    if request.POST:
        print('пишем документ')
        # for line in request.POST:
        #     print(line, request.POST[line])
        i = 0
        lst_bool = False
        final_lst = []
        lst = []
        for line in request.POST:
            # if line[len(line) - 4 :] == 'name':
            #     print(i, line, request.POST[line])
            if i > 5:
                if line[len(line)-4:] == 'name' and lst_bool:
                    # print(request.POST[line])
                    if request.POST[line] == '':
                        final_lst.append(lst)
                        continue
                    final_lst.append(lst)
                    print(lst)
                    lst = []
                lst.append(request.POST[line])
                if not lst_bool:
                    lst_bool = True
            i += 1
        #
        # for line in final_lst:
        #     print(line)

        fileTbl_gps = FilesTbl_gps.objects.filter(parent=pk)
        fileTbl_gps.delete()
        for line in final_lst:
            if line[0][len(line[0])-7:] == 'newline':
                line[0] = line[0][:len(line[0])-7]
                FilesTbl_gps.objects.create(
                    parent=Files_gps.objects.get(pk=pk),
                    x=line[1],
                    y=line[2],
                    z=line[3],
                    name=line[0],
                    newline = True
                )
            else:
                FilesTbl_gps.objects.create(
                    parent=Files_gps.objects.get(pk=pk),
                    x=line[1],
                    y=line[2],
                    z=line[3],
                    name=line[0]
                )

    # print('pk =', pk)
    file = Files_gps.objects.get(pk=pk)
    print(type(file))
    fileTbl = FilesTbl_gps.objects.filter(parent=pk)
    # for line in fileTbl:
    #     print(line.name, line.x, line.y, line.z, line.x2, line.y2, line.z2)
    formset = FilesFormSet_gps_load(instance=file)
    # print(formset)
    context = {'file' : file, 'fileTbl' : fileTbl, 'formset': formset}
    return render(request, 'energy/search_gps_load.html', context)

def search_gps(request, pk):
    if request.POST:
        print('пишем документ')
        # for line in request.POST:
        #     print(line, request.POST[line])
        i = 0
        lst_bool = False
        final_lst = []
        lst = []
        for line in request.POST:
            if i > 5:
                if line[len(line)-4:] == 'name' and lst_bool:
                    final_lst.append(lst)
                    lst = []
                lst.append(request.POST[line])
                if not lst_bool:
                    lst_bool = True
            i += 1

        fileTbl_gps = GPS.objects.filter(parent=pk)
        fileTbl_gps.delete()
        file = GPS_doc.objects.get(pk=pk)
        if file.date > file.date2 :
            dates = file.date - file.date2
        else :
            dates = file.date2 - file.date
        for line in final_lst:
            # print(line)
            ox = (round(float(line[4]), 3)-round(float(line[1]), 3))*1000
            oy = (round(float(line[5]), 3)-round(float(line[2]), 3))*1000
            oz = (round(float(line[6]), 3)-round(float(line[3]), 3))*1000
            absolute = round(sqrt(ox ** 2 + oy ** 2 + oz ** 2),3)
            v = round(absolute / dates.days,3)
            GPS.objects.create(
                parent = file,
                x = line[1],
                y = line[2],
                z = line[3],
                x2 = line[4],
                y2 = line[5],
                z2 = line[6],
                ox = ox,
                oy = oy,
                oz = oz,
                absolute = absolute,
                v = v,
                name= line[0],
            )
    file = GPS_doc.objects.get(pk=pk)
    fileTbl = GPS.objects.filter(parent=pk)
    formset = FilesFormSet_gps(instance=file)
    context = {'file' : file, 'fileTbl' : fileTbl, 'formset': formset}
    return render(request, 'energy/search_gps.html', context)

def search_tahe(request, pk):

    def func(last_num, num):
        if int(num)==0:
            return last_num
        else:
            return num

    if 'correct' in request.POST:
        print('почти готов сохраняться')
        i = 1
        lst_bool = False
        final_lst = []
        lst = []

        for line in request.POST:
            if i>6:
                print(i, line, request.POST[line])

            if i > 6:
                # print(line, request.POST[line])
                # if i == 1:
                #     lst_bool = True
                if line[len(line)-4:] == 'name' and lst_bool:
                # if line[len(line) - 4 :] == 'name' :
                    print(line, request.POST[line])
                    #begin
                    # print(str(request.POST[line])[:7], request.POST[line])
                    # end
                    # print(str(request.POST[line])[len(str(request.POST[line]))-7:], request.POST[line])
                    # print(str(request.POST[line])[:len(str(request.POST[line]))-8], request.POST[line])
                    # if str(request.POST[line])[7:] == 'newline' and str(request.POST[line])[:len(str(request.POST[line]))-7] == 'newline':
                    #     print(line[0])
                    # elif str(request.POST[line])[7:] == 'newline':
                    #     print(line[0], 'str(request.POST[line])[8:]')
                    # elif str(request.POST[line])[:len(str(request.POST[line]))-7] == 'newline':
                    #     print(request.POST[line], 'str(request.POST[line])[:len(str(request.POST[line]))-8]')
                    final_lst.append(lst)
                    lst = []
                lst.append(request.POST[line])
                if not lst_bool:
                    lst_bool = True
            i += 1

        # for line in final_lst:
        #     print(line)

        prnt = Step_2_doc.objects.get(pk=pk)
        step2 = Step_2.objects.filter(parent=pk)
        step2.delete()
        for line in final_lst:

            # print(line)
            try:
                if line[0] == '':
                    continue
                Step_2.objects.create(
                    parent= prnt,
                    name = line[0],
                    x = line[1],
                    y = line[2],
                    z = line[3],
                    l = 0,
                    s = 0,
                    x2 = line[6],
                    y2 = line[7],
                    z2 = line[8],
                    l2 = 0,
                    s2 = 0,
                    ox = 0,
                    oy = 0,
                    oz = 0,
                    ol = 0,
                    os = 0,
                    absolute = 0,
                )
            except:
                print('trouble here',line)

        i = 0
        step2 = Step_2.objects.filter(parent=pk)
        for line in step2:

            if i == 0:
                lastx = line.x
                a = lastx
                lasty = line.y
                lastz = line.z
                lastx2 = line.x2
                lasty2 = line.y2
                lastz2 = line.z2
                firstx = line.x
                firsty = line.y
                firstx2 = line.x2
                firsty2 = line.y2
                # last = line
            else:

                # print(lasty, line.y, lastx, line.x)
                print((lasty - line.y)**2)
                line.s = round(sqrt(((lasty - line.y)**2)+((lastx - line.x)**2)),3)
                line.s2 = round(sqrt((lasty2 - line.y2) ** 2 + (lastx2 - line.x2) ** 2),3)
                line.l = round(sqrt(((firsty - line.y)**2)+((firstx - line.x)**2)),3)
                line.l2 = round(sqrt((firsty2 - line.y2) ** 2 + (firstx2 - line.x2) ** 2),3)

                if line.x == 0:
                    line.s = 0
                    line.l = 0
                if line.x2 == 0:
                    line.s2 = 0
                    line.l2 = 0

                line.save()

                if line.name[:7] == 'newline':
                    lastx = line.x
                    lasty = line.y
                    lastz = line.z
                    lastx2 = line.x2
                    lasty2 = line.y2
                    lastz2 = line.z2
                    line.name = line.name[7:]
                    line.l = 0
                    line.s = 0
                    line.l2 = 0
                    line.s2 = 0
                    line.newline = True
                    line.save()
                if line.name[len(line.name)-7:] == 'newline':
                    lastx = line.x
                    lasty = line.y
                    lastz = line.z
                    lastx2 = line.x2
                    lasty2 = line.y2
                    lastz2 = line.z2
                    line.name = line.name[:len(line.name)-7]
                    line.l2 = 0
                    line.s2 = 0
                    line.l = 0
                    line.s = 0
                    line.newline2 = True
                    line.save()

                print(lastx, )
                line.ox = round((line.x2 - line.x) * 1000, 3)
                line.oy = round((line.y2 - line.y) * 1000, 3)
                line.oz = round((line.z2 - line.z) * 1000, 3)
                line.ol = round((line.l2 - line.l) * 1000, 3)
                line.os = round((line.s2 - line.s) * 1000, 3)
                line.absolute = round(sqrt(line.oz ** 2 + line.ol ** 2),3)
                line.save()

                lastx = func(lastx, line.x)
                lasty = func(lasty, line.y)
                lastz = func(lastz, line.z)
                lastx2 = func(lastx2, line.x2)
                lasty2 = func(lasty2, line.y2)
                lastz2 = func(lastz2, line.z2)
            i+=1




        # i = 0
        # for line in final_lst:
        #     linex = float(line[1])
        #     liney = float(line[2])
        #     linex2 = float(line[6])
        #     liney2 = float(line[7])
        #     if i == 0:
        #         line[4] = 0
        #         line[5] = 0
        #         line[9] = 0
        #         line[10] = 0
        #         last_x = 0
        #         last_y = 0
        #         last_x1 = 0
        #         last_y1 = 0
        #         first_x = line[1]
        #         first_y = line[2]
        #         first_x1 = line[6]
        #         first_y1 = line[7]
        #     else:
        #         # L
        #         line[4] = round(sqrt((float(last_y) - liney) ** 2 + (float(last_x) - linex) ** 2), 3)
        #         # S
        #         line[5] = round(sqrt((float(first_y) - liney) ** 2 + (float(first_x) - linex) ** 2), 3)
        #         # L2
        #         line[9] = round(sqrt((float(last_y1) - liney2) ** 2 + (float(last_x1) - linex2) ** 2), 3)
        #         # S2
        #         line[10] = round(sqrt((float(first_y1) - liney2) ** 2 + (float(first_x1) - linex2) ** 2), 3)
        #
        #         if str(line[0])[:7] == 'newline' and str(line[0])[len(line[0])-7:] == 'newline':
        #             line[0] = str(line[0])[7:]
        #             line[0] = str(line[0])[:len(line[0])-7]
        #             line.append('1','1')
        #             #L
        #             line[5] = 0
        #             #S
        #             line[4] = 0
        #             #L2
        #             line[9] = 0
        #             #S2
        #             line[10] = 0
        #         elif str(line[0])[:7] == 'newline':
        #             print('popadayu nachalo')
        #             line[0] = line[0][7:]
        #             #L
        #             line[5] = 0
        #             #S
        #             line[4] = 0
        #             line.append('1','0')
        #         elif str(line[0])[len(line[0])-7:] == 'newline':
        #             print('popadayu konec')
        #             line[0] = line[0][:len(line[0])-7]
        #             line.append('0','2')
        #             #L2
        #             line[9] = 0
        #             #S2
        #             line[10] = 0
        #
        #     #считаю треугольнички
        #
        #     last_x = func(line[1],last_x)
        #     last_y = func(line[2], last_y)
        #     last_x1 = func(line[6], last_x1)
        #     last_y1 = func(line[7], last_y1)
        #     i += 1
        # for line in final_lst:
        #     print(line)







        # for line in final_lst:
        #     print(line)

        # prnt = Step_2_doc.objects.get(pk=pk)
        # step2 = Step_2.objects.filter(parent=pk)
        # step2.delete()
        # for line in final_lst:
        #
        #     # print(line)
        #     try:
        #         Step_2.objects.create(
        #             parent= prnt,
        #             name = line[0],
        #             x = line[1],
        #             y = line[2],
        #             z = line[3],
        #             l = line[4],
        #             s = line[5],
        #             x2 = line[6],
        #             y2 = line[7],
        #             z2 = line[8],
        #             l2 = line[9],
        #             s2 = line[10],
        #             ox = line[11],
        #             oy = line[12],
        #             oz = line[13],
        #             ol = line[14],
        #             os = line[15],
        #             absolute = line[16],
        #         )
        #     except:
        #         print('trouble here',line)

    file = Step_2_doc.objects.get(pk=pk)
    files = Step_2.objects.filter(parent=pk)
    formset = FilesFormSet_step_2(instance=file)
    # print(formset)
    context = {'file': file, 'files':files, 'formset':formset}
    return render(request, 'energy/search_files_tahe.html', context)

def remove_gpsfile(request, pk):
    doc = Files_gps.objects.get(pk=pk)
    doctb = FilesTbl_gps.objects.filter(parent=pk)
    doctb.delete()
    doc.delete()
    return redirect('energy:load_gps')

def remove_gps(request, pk):
    doc = GPS_doc.objects.get(pk=pk)
    doctb = GPS.objects.filter(parent=pk)
    doctb.delete()
    doc.delete()
    return redirect('energy:gps')

def remove_tahe(request, pk):
    doc = Step_2_doc.objects.get(pk=pk)
    doctb = Step_2.objects.filter(parent=pk)
    doctb.delete()
    doc.delete()
    return redirect('energy:tahe')

def remove(request, pk):
    doc = Files.objects.get(pk=pk)
    doctb = FilesTbl.objects.filter(parent=pk)

    doctb.delete()
    doc.delete()
    return redirect('energy:load_files')

def step_1_gps(request, pk):
    parent = Files_gps.objects.get(pk=pk)
    parent.read = True
    parent.save()
    # i = 0
    # if parent.date > parent.date2:
    #     dates = parent.date-parent.date2
    # else:
    #     dates = parent.date2 - parent.date

    # print(dates.days, type(dates))
    # bbb = FilesTbl_gps.objects.filter(parent=pk)
    # bbb.delete()
    # bb = GPS_doc.objects.create(
    #     date = dt.now(),
    #     file1 = file.file,
    #     comment = ' ',
    # )

    bbb = FilesTbl_gps.objects.filter(parent=pk)
    bbb.delete()

    with open('static/media/'+str(parent.file), "r") as file :
        for line in file :
            # i+=1
            first_num = str(line).find(',')
            first = line[:first_num]
            fle = line[first_num+1:]
            second_num = str(fle).find(',')
            second = float(fle[:second_num])
            fle = fle[second_num+1:]
            third_num = str(fle).find(',')
            third = float(fle[:third_num])
            fle = fle[third_num + 1 :]
            fourth_num = str(fle).find(',')
            fourth = float(fle[:fourth_num])
            # fle = fle[fourth_num + 1 :]
            # five_num = str(fle).find(',')
            # five = float(fle[:five_num])
            # fle = fle[five_num + 1 :]
            # six_num = str(fle).find(',')
            # six = float(fle[:six_num])
            # fle = fle[six_num + 1 :]
            # seven_num = str(fle).find(',')
            # seven = float(fle[:seven_num])
            # ox = (round(five, 3)-round(second, 3))*1000
            # oy = (round(six, 3)-round(third, 3))*1000
            # oz = (round(seven, 3)-round(fourth, 3))*1000
            # absolute = round(sqrt(ox ** 2 + oy ** 2 + oz ** 2),3)
            # v = round(absolute / dates.days,3)
            FilesTbl_gps.objects.create(
                parent = parent,
                x = round(second, 3),
                y = round(third, 3),
                z = round(fourth, 3),
                name= first,
            )
    return redirect('energy:load_gps')

def step_1(request, pk):

    def func(num):
        if num < 0:
            return -num
        else:
            return num

    file = Files.objects.get(pk=pk)


    file.read = True


    file.save()
    i = 0
    lst=[]
    lst_names = []
    final = []
    bbb = FilesTbl.objects.filter(parent=pk)
    bbb.delete()
    tt = str(file.file)
    test = []
    with open('static/media/'+tt, "r") as file :
        # print(file)
        for line in file:
            frfr = True
            i += 1
            first_num = str(line).find(',')
            first = line[:first_num]
            fle = line[first_num+1:]
            second_num = str(fle).find(',')
            second = float(fle[:second_num])
            fle = fle[second_num+1:]
            third_num = str(fle).find(',')
            third = float(fle[:third_num])
            fle = fle[third_num + 1 :]
            fourth_num = str(fle).find(',')
            fourth = float(fle[:fourth_num])
            j = 0
            max = 0
            test.append(first)
            if max < i :
                max = i
            with open('static/media/' + tt, "r") as file2 :
                for line2 in file2:
                    # print(i, "_", j)
                    j += 1
                    if i < j or (i != 1 and j == max):
                        first_num = str(line2).find(',')
                        first2 = line2[:first_num]
                        if not first2 in lst_names:
                            fle = line2[first_num + 1 :]
                            second_num = str(fle).find(',')
                            second2 = float(fle[:second_num])
                            fle = fle[second_num + 1 :]
                            third_num = str(fle).find(',')
                            third2 = float(fle[:third_num])
                            fle = fle[third_num + 1 :]
                            fourth_num = str(fle).find(',')
                            fourth2 = float(fle[:fourth_num])

                            frs = func(second-second2)
                            if frs < 0.5:
                                sec = func(third-third2)
                                if sec < 0.5:
                                    thr = func(fourth-fourth2)
                                    if thr < 0.5:
                                        itog = frs + sec + thr
                                        if itog < 0.51:
                                            lst_names.append(first2)
                                            if frfr:
                                                lst.append([first, second, third, fourth])
                                                frfr = False
                                            lst.append([first2, second2, third2, fourth2])
            if len(lst) > 0:
                final.append(lst)
                lst = []

    # n = 0
    for line in final:
        n = 0
        x = 0
        y = 0
        z = 0
        for linne in line:
            x += linne[1]
            y += linne[2]
            z += linne[3]
            n += 1
        FilesTbl.objects.create(
            parent=Files.objects.get(pk=pk),
            x=round(x/n, 3),
            y=round(y/n, 3),
            z=round(z/n, 3),
            name=line[0][0],
            old_num = 90
        )

    step_1 = FilesTbl.objects.filter(parent=pk)
    print('длина списка ', len(step_1))

    i = -1
    lst = []
    for line in step_1:
        i += 1
        result = FilesTbl.objects.get(pk=line.id)

        if i == 0:
            print('i=0, first_x = ',line.x,', first_y = ',line.y)
            prev_y = line.y
            prev_x = line.x
            first_y = line.y
            first_x = line.x
            result = FilesTbl.objects.get(pk=line.id)
            result.s = 0
            result.l = 0
            result.save()
            continue
        else:
            # print('попадаю')
            num1 = (prev_y-line.y)**2
            num2 = (prev_x-line.x)**2
            num3 = num1 + num2
            num4 = cmath.sqrt(num3)
            num5 = float(str(num4)[1:str(num4).find('.')+8])
            num5 = round(num5,3)

            numl1 = (first_y-line.y)**2
            print('numl1 = ',first_y,'-',line.y,'=',numl1)
            numl2 = (first_x-line.x)**2
            print('numl2 = ', first_x, '-', line.x, '=', numl2)
            numl3 = numl1 + numl2
            print('numl3 = ', numl1, '+', numl2, '=', numl1)
            numl4 = cmath.sqrt(numl3)
            print('numl4 =',numl4)
            numl5 = float(str(numl4)[1:str(numl4).find('.')+8])
            numl5 = round(numl5,3)
            print('numl5 = ',numl5)
            print()

            result = FilesTbl.objects.get(pk=line.id)
            result.s = num5
            result.l = numl5
            result.save()
            numl1 = 0
            numl2 = 0
            numl3 = 0
            numl4 = 0
            numl5 = 0
        prev_y = line.y
        prev_x = line.x

    return redirect('energy:load_files')

def tahe_copy(request, pk):
    bb = get_object_or_404(Step_2_doc, pk=pk)
    bbb = Step_2.objects.filter(parent=pk)
    bb.pk = None
    bb.save()
    if bbb:
        for line in bbb:
            line.pk = None
            line.parent = bb
            line.save()
    return redirect('energy:tahe')

def gpsfile_copy(request, pk):
    bb = get_object_or_404(Files_gps, pk=pk)
    bbb = FilesTbl_gps.objects.filter(parent=pk)
    bb.pk = None
    bb.save()
    if bbb:
        for line in bbb:
            line.pk = None
            line.parent = bb
            line.save()
    return redirect('energy:load_gps')

def step1_copy(request, pk):
    bb = get_object_or_404(Files, pk=pk)
    bbb = FilesTbl.objects.filter(parent=pk)
    bb.pk = None
    bb.save()
    if bbb:
        for line in bbb:
            line.pk = None
            line.parent = bb
            line.save()
    return redirect('energy:load_files')

def gps_copy(request, pk):
    bb = get_object_or_404(GPS_doc, pk=pk)
    bbb = GPS.objects.filter(parent=pk)
    bb.pk = None
    bb.save()
    if bbb:
        for line in bbb:
            line.pk = None
            line.parent = bb
            line.save()
    return redirect('energy:gps')

def step_2(request, pk):
    docs = Files.objects.filter(read=True)
    bb = Files.objects.get(pk=pk)
    form_1 = FilesForm(instance=bb)
    form_2 = FilesForm()
    # formset = FilesFormSet_step_2(instance=pk)
    context = {'form1': form_1, 'form2': form_2, 'bb': bb, 'docs': docs}
    return render(request, 'energy/step_2.html', context)

def step_gps(request, pk):
    bb = Files_gps.objects.get(pk=pk)
    docs = Files_gps.objects.filter(read=True).filter(place=bb.place)
    form_1 = GPS_docForm(instance=bb)
    form_2 = GPS_docForm()
    context = {'form1': form_1, 'form2': form_2, 'bb': bb, 'docs': docs}
    return render(request, 'energy/step_gps.html', context)

class CreatePostView(CreateView): # новый
    model = Files
    form_class = FilesForm
    template_name = 'energy/post.html'
    success_url = reverse_lazy('energy:load_files')

class CreateGPSPostView(CreateView): # новый
    model = Files_gps
    form_class = FilesFormGPS
    template_name = 'energy/post_gps.html'
    success_url = reverse_lazy('energy:load_gps')

class HomePageView(ListView):
    model = Files
    template_name = 'sitemap.html'

def gps(request):
    docs = GPS_doc.objects.all().order_by('-date')
    # test = docs.values("file")
    # files = GPS_doc.objects.all().file
    if 'newsletter_sub' in request.POST :
        date1 = request.POST.get('my_date_field')
        date2 = request.POST.get('my_date_field1')
        # print(date1, date2)
        docs = GPS_doc.objects.filter(date__range=(date1, date2)).order_by('-date')
    # if 'file_modal' in request.POST:
    #     print('попадаю')
    #     x = request.POST.get('places')
    #     xx = GPS_doc.objects.get(pk=x).file
    #     xxx = GPS_doc.objects.filter(file=xx)
    #
    #     print(xx)
    # read_form = Step2Form()
    # files = GPS_doc.objects.all()
    # gps_file = GPSModal()
    gps_file = GPS_doc.objects.all().values_list("file1")
    contractor = DateForm1()
    context = {'docs': docs, 'contractor': contractor, 'gps_file':gps_file}
    return render(request, 'energy/gps.html', context)

def tahe(request):
    # Item.objects.filter(Q(creator=owner) | Q(moderated=False))
    docs = Step_2_doc.objects.all()
    if 'newsletter_sub' in request.POST :
        date1 = request.POST.get('my_date_field')
        date2 = request.POST.get('my_date_field1')
        docs = Step_2_doc.objects.filter(date__range=(date1, date2))
    # files = Step_2_doc.objects.all()
    # lst = []
    # for line in files:
    #     if not line.file1 in lst:
    #         lst.append(line.file1)
    #     if not line.file2 in lst:
    #         lst.append(line.file2)
    files = FileModal()
    contractor = DateForm1()
    context = {'docs': docs, 'contractor': contractor, 'files': files}
    return render(request, 'energy/tahe.html', context)

def step2_ajax_1(h, h1, h3):
    print('imhere')
    f = 0
    ff = 0
    lst1 = []
    x = h1[0].name
    try :
        x = int(str(x)[len(x) - 3 :])
        print(x)
        print(len(h))
        for i in range(0, len(h)) :
            if i == 0 :
                last_a = int(str(h[i].name)[len(h[i].name) - 3 :])
                continue
            if min(last_a, x) > min(last_a, int(str(h[i].name)[len(h[i].name) - 3 :])) :
                if f == 0 :
                    lst1.append(['null', h[i - 1].name])
                lst1.append(['null', h[i].name])
                if f == 0:
                    lst1.append([h3, h3])
                    f += 1
            else :
                # if ff == 0 :
                #     lst1.append([h1[i].name, 'null'])
                #     ff += 1
                # lst1.append([h[i].name, 'null'])
                lst1.append(['null', h[i - 1].name])
            last_a = int(str(h[i].name)[len(h[i].name) - 3 :])
        # for u in range (i,len(h)):
        #     i = 0
        #     lst1 = []
        #     for line1 in h :
        #         i += 1
        #         j = 0
        #         for line2 in h1 :
        #             j += 1
        #             if line1.name == line2.name :
        #                 lst1.append(line1.name, line2.name)
        return lst1
    except :
        pass

def ajax_gps(request):
    print('ajax_gps')
    first = request.GET.get('first')
    second = request.GET.get('second')
    comment = request.GET.get('comment')
    date1 = Files_gps.objects.get(pk=first).date
    date2 = Files_gps.objects.get(pk=second).date
    date2 = Files_gps.objects.get(pk=second).date
    date = date2 - date1
    print('наша разница дат равна ', date)

    print(type(date), date)
    if str(date) != '0:00:00':
        date = int(str(date)[:str(date).find(' ')])
    else:
        date = 1
    print('отбросив пробел наша разница дат равна ',date)
    file1 = Files_gps.objects.get(pk=first).file
    file2 = Files_gps.objects.get(pk=second).file
    file1_date = Files_gps.objects.get(pk=first).date
    file2_date = Files_gps.objects.get(pk=second).date
    doc1 = FilesTbl_gps.objects.filter(parent=first)
    doc2 = FilesTbl_gps.objects.filter(parent=second)
    comment = request.GET.get('comment')
    print(len(doc1), len(doc2))

    def is_newline(a,b):
        if a:
            return a
        elif b:
            return b
        else:
            return False

    def func(num):
        if num < 0:
            return -num
        else:
            return num
    lasti = 0
    lastj = 0
    lst2 = []
    lst3 = []
    names_lst = []
    lst_new = []
    for i in range(0,len(doc1)):
        for j in range(0,len(doc2)):
            if doc2[j].name not in names_lst :
                x = func(doc1[i].x - doc2[j].x)
                y = func(doc1[i].y - doc2[j].y)
                z = func(doc1[i].z - doc2[j].z)
                itog = x+y+z
                if itog < 0.51:
                    names_lst.append(doc2[j].name)
                    for ii in range(lasti, i):
                        if doc1[i].name != doc1[ii].name:
                            lst2.append([doc1[ii].name, 0])
                    for jj in range(lastj, j):
                        if doc2[jj].name not in names_lst :
                            if doc2[j].name != doc2[jj].name :
                                lst2.append([doc2[jj].name, 1])
                    if len(lst2)>0:
                        lst3.append(sorted(lst2, reverse = True))
                    lst2 = []
                    newline = is_newline(doc1[i].newline, doc1[j].newline)
                    lst3.append([doc1[i].name,
                                 doc1[i].x,
                                 doc1[i].y,
                                 doc1[i].z,
                                 doc2[j].name,
                                 doc2[j].x,
                                 doc2[j].y,
                                 doc2[j].z,
                                 round((doc2[j].x-doc1[i].x)*1000,3),
                                 round((doc2[j].y-doc1[i].y)*1000,3),
                                 round((doc2[j].z-doc1[i].z)*1000,3),
                                 round(sqrt(((doc2[j].x-doc1[i].x)*1000)**2 + ((doc2[j].y-doc1[i].y)*1000)**2 + ((doc2[j].z-doc1[i].z)*1000)**2), 3),
                                 round(sqrt(((doc2[j].x-doc1[i].x)*1000)**2 + ((doc2[j].y-doc1[i].y)*1000)**2 + ((doc2[j].z-doc1[i].z)*1000)**2) / date, 3),
                                 newline
                                 ])
                    # test = sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2)
                    # print(test, type(test))
                    # print(doc1[i].name, doc1[i].x, doc1[i].y, doc2[j].name, doc2[j].x, doc2[j].y)
                    lasti = i+1
                    lastj = j+1
                    break

    print(len(lst3))
    for line in lst3:
        if type(line[0]) is list:
            pass
            for ln in line:
                if ln[1] == 0:
                    # print(ln[0])
                    obj = FilesTbl_gps.objects.filter(name=ln[0]).filter(parent=first)
                    lst_new.append([obj[0].name,
                                    obj[0].x,
                                    obj[0].y,
                                    obj[0].z,
                                    0,
                                    0,
                                    0,
                                    0,
                                    round((0 - obj[0].x) * 1000, 3),
                                    round((0 - obj[0].y) * 1000, 3),
                                    round((0 - obj[0].z) * 1000, 3),
                                    round(sqrt(((0 - obj[0].x) * 1000) ** 2 + ((0 - obj[0].y) * 1000) ** 2 + ((0 - obj[0].z) * 1000) ** 2), 3),
                                    round(sqrt(((0 - obj[0].x) * 1000) ** 2 + ((0 - obj[0].y) * 1000) ** 2 + ((0 - obj[0].z) * 1000) ** 2) / date, 3),
                                    obj[0].newline
                                    ])
                else:
                    obj = FilesTbl_gps.objects.filter(name=ln[0]).filter(parent=second)
                    if obj[0].name not in names_lst:
                        lst_new.append([0,
                                        0,
                                        0,
                                        0,
                                        obj[0].name,
                                        obj[0].x,
                                        obj[0].y,
                                        obj[0].z,
                                        round((obj[0].x-0)*1000, 3),
                                        round((obj[0].y-0)*1000,3),
                                        round((obj[0].z-0)*1000,3),
                                        round(sqrt(((obj[0].x-0)*1000) ** 2 + ((obj[0].y-0)*1000) ** 2 + ((obj[0].z-0)*1000) ** 2), 3),
                                        round(sqrt(((obj[0].x-0)*1000) ** 2 + ((obj[0].y-0)*1000) ** 2 + ((obj[0].z-0)*1000) ** 2) / date, 3),
                                        obj[0].newline
                                        ])
        else:
            lst_new.append(line)
    i = 0
    for line in lst_new:
        i += 1
        print(i,'|  ', line)

    #
    bb = GPS_doc.objects.filter(file1=file1).filter(file2=file2)
    if bb:
        bbb = GPS.objects.filter(parent = bb[0].pk)
        bbb.delete()
        bb.delete()

    bb = GPS_doc.objects.create(
        date = dt.now(),
        date1 = file1_date,
        date2 = file2_date,
        file1 = file1,
        file2 = file2,
        comment = comment
    )
    for line in lst_new:
        if line[0] == 0:
            name = line[4]
        else:
            name = line[0]
        GPS.objects.create(
            parent = bb,
            name = name,
            x = line[1],
            y = line[2],
            z = line[3],
            x2 = line[5],
            y2 = line[6],
            z2 = line[7],
            ox = line[8],
            oy = line[9],
            oz = line[10],
            absolute = line[11],
            v = line[12],
            newline = line[13]
        )

    # lasti = 0
    # lastj = 0
    # lst2 = []
    # lst3 = []
    # lst_new = []
    # names_lst = []
    # date1 = Files_gps.objects.get(pk=first).date
    # date2 = Files_gps.objects.get(pk=second).date
    #
    # # date = dt.strptime(date1, '%Y-%m-%d').date()
    # # print(date1, type(date1), date2, type(date2))
    # date2 = Files_gps.objects.get(pk=second).date
    # for i in range(0,len(doc1)-1):
    #     for j in range(0,len(doc2)-1):
    #         if round(doc1[i].x,1) == round(doc2[j].x,1) \
    #                 and round(doc1[i].y,1) == round(doc2[j].y,1) \
    #                 and round(doc1[i].z,1) == round(doc2[j].z,1):
    #             names_lst.append(doc2[j].name)
    #             lst3.append(doc1[i].name)
    #             # for ii in range(lasti, i):
    #             #     # if doc1[ii].name not in names_lst:
    #             #     if doc1[i].name != doc1[ii].name:
    #             #         lst2.append([doc1[ii].name, 0])
    #             # for jj in range(lastj, j):
    #             #     if doc2[jj].name not in names_lst :
    #             #         if doc2[j].name != doc2[jj].name :
    #             #             lst2.append([doc2[jj].name, 1])
    #             # if len(lst2)>0:
    #             #     lst3.append(sorted(lst2, reverse = True))
    #             # lst2 = []
    #
    # # for line in lst3:
    # # print(len(lst3))
    #
    # #             date = date2 - date1
    # #             date = int(str(date)[:str(date).find(' ')])
    # #             # print(int(str(date)[:str(date).find(' ')]))
    # #             lst3.append([doc1[i].name,
    # #                          doc1[i].x,
    # #                          doc1[i].y,
    # #                          doc1[i].z,
    # #                          '',#doc1[i].l,
    # #                          '',# doc1[i].s,
    # #                          doc2[j].name,
    # #                          doc2[j].x,
    # #                          doc2[j].y,
    # #                          doc2[j].z,
    # #                          '',#doc2[j].l,
    # #                          '',# doc2[j].s,
    # #                          round((doc2[j].x-doc1[i].x)*1000,4),
    # #                          '',
    # #                          round((doc2[j].y-doc1[i].y)*1000,4),
    # #                          round((doc2[j].z-doc1[i].z)*1000,4),
    # #                          round((doc2[j].z - doc1[i].z) * 1000, 4),
    # #                          '',# round((doc2[j].l-doc1[i].l)*1000,4),
    # #                          '',# round((doc2[j].s-doc1[i].s)*1000,4),
    # #                          '',# round(sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2), 4),
    # #                          ''])# round(sqrt(((doc2[j].z - doc1[i].z) * 1000) ** 2 + ((doc2[j].l - doc1[i].l) * 1000) ** 2)/date, 4)])
    # #             lasti = i+1
    # #             lastj = j+1
    # #             break
    # # for line in lst3:
    # #     if type(line[0]) is list:
    # #         for ln in line:
    # #             if ln[1] == 0:
    # #                 # print(ln[0])
    # #                 obj = FilesTbl_gps.objects.filter(name=ln[0]).filter(parent=first)
    # #                 lst_new.append([obj[0].name,
    # #                                 obj[0].x,
    # #                                 obj[0].y,
    # #                                 obj[0].z,
    # #                                 # '',# obj[0].l,                           # 4
    # #                                 # '',# obj[0].s,                           # 5
    # #                                 0,
    # #                                 0,
    # #                                 0,
    # #                                 0,
    # #                                 '',# 0,                                  #10
    # #                                 '',# 0,                                  #11
    # #                                 round((0 - obj[0].x) * 1000, 4),
    # #                                 '',             #9
    # #                                 round((0 - obj[0].y) * 1000, 4),
    # #                                 round((0 - obj[0].z) * 1000, 4),
    # #                                 '',# round((0 - obj[0].l) * 1000, 4),    #16
    # #                                 '',# round((0 - obj[0].s) * 1000, 4),    #17
    # #                                 '',
    # #                                 '',
    # #                                 ''])#round(sqrt(((0 - obj[0].z) * 1000) ** 2 + ((0 - obj[0].l) * 1000) ** 2), 4)])#19
    # #             else:
    # #                 obj = FilesTbl_gps.objects.filter(name=ln[0]).filter(parent=second)
    # #                 lst_new.append([0,
    # #                                 0,
    # #                                 0,
    # #                                 0,
    # #                                 # '',# 4
    # #                                 # '', # 5
    # #                                 obj[0].name,
    # #                                 obj[0].x,
    # #                                 obj[0].y,
    # #                                 obj[0].z,
    # #                                 '',#10
    # #                                 '',#11
    # #                                 round((obj[0].x-0)*1000,4),
    # #                                 '',
    # #                                 round((obj[0].y-0)*1000,4),
    # #                                 round((obj[0].z-0)*1000,4),
    # #                                 '',#16
    # #                                 '',#17
    # #                                 '',#18
    # #                                 '',
    # #                                 ''])#round(sqrt(((obj[0].z-0)*1000)**2 + ((obj[0].l-0)*1000)**2), 4)])
    # #     else:
    # #         lst_new.append(line)
    # #
    # # bb = GPS_doc.objects.filter(file1=file1).filter(file2=file2)
    # # if bb:
    # #     bbb = FilesTbl.objects.filter(parent = bb[0].pk)
    # #     bbb.delete()
    # #     bb.delete()
    # #
    # # bb = GPS_doc.objects.create(
    # #     date = dt.now(),
    # #     file1 = file1,
    # #     file2 = file2,
    # #     comment = comment
    # # )
    # # for line in lst_new:
    # #     print(line[5])
    # #     if line[0] == 0:
    # #         name = line[6]
    # #     else:
    # #         name = line[0]
    # #     GPS.objects.create(
    # #         parent= bb,
    # #         name = name,
    # #         x = line[1],
    # #         y = line[2],
    # #         z = line[3],
    # #         # l = line[4],
    # #         # s = line[5],
    # #         x2 = line[5],
    # #         y2 = line[6],
    # #         z2 = line[7],
    # #         # l2 = line[10],
    # #         # s2 = line[11],
    # #         ox = line[10],
    # #         oy = line[12],
    # #         oz = line[13],
    # #         # ol = line[16],
    # #         # os = line[17],
    # #         v = 0,
    # #         absolute = 0
    # #     )

    return render(request, 'energy/ajax_step2.html', {'lst':lst_new})


def ajax_step2(request):
    print('ajax_step2')
    def func(num):
        if num < 0:
            return -num
        else:
            return num
    first = request.GET.get('first')
    second = request.GET.get('second')
    comment = request.GET.get('comment')
    file1 = Files.objects.get(pk=first).file
    file2 = Files.objects.get(pk=second).file
    doc1 = FilesTbl.objects.filter(parent=first)
    doc2 = FilesTbl.objects.filter(parent=second)
    # y = dict(doc1)
    # for line in doc1:
    #     print(line.name)
    lasti = 0
    lastj = 0
    lst2 = []
    lst3 = []
    names_lst = []
    lst_new = []
    print(len(doc1))
    for i in range(0,len(doc1)):
        for j in range(0,len(doc2)):
            x = func(doc1[i].x - doc2[j].x)
            y = func(doc1[i].y - doc2[j].y)
            z = func(doc1[i].z - doc2[j].z)
            itog = x+y+z
            if itog < 0.51:
            # if round(doc1[i].x,1) == round(doc2[j].x,1) \
            #         and round(doc1[i].y,1) == round(doc2[j].y,1) \
            #         and round(doc1[i].z,1) == round(doc2[j].z,1):
                names_lst.append(doc2[j].name)
                for ii in range(lasti, i):
                    # if doc1[ii].name not in names_lst:
                    if doc1[i].name != doc1[ii].name:
                        lst2.append([doc1[ii].name, 0])
                for jj in range(lastj, j):
                    if doc2[jj].name not in names_lst :
                        if doc2[j].name != doc2[jj].name :
                            lst2.append([doc2[jj].name, 1])
                    # print(doc1[ii].name, doc1[ii].old_num, ii)


                # names_lst.append(doc2[jj].name)


                #     for jj in range(lastj, j):
                #
                #         print(doc2[jj].name, doc2[jj].old_num, jj)
                #         if str(doc1[ii].name)[len(doc1[ii].name)-3:] > str(doc2[jj].name)[len(doc2[jj].name)-3:]:
                #             print(doc1[ii].name)
                #         else:
                #             print(doc2[jj].name)
                # print(sorted(lst2, reverse = True))

                if len(lst2)>0:
                    lst3.append(sorted(lst2, reverse = True))
                lst2 = []
                lst3.append([doc1[i].name,
                             doc1[i].x,
                             doc1[i].y,
                             doc1[i].z,
                             doc1[i].l,
                             doc1[i].s,
                             doc2[j].name,
                             doc2[j].x,
                             doc2[j].y,
                             doc2[j].z,
                             doc2[j].l,
                             doc2[j].s,
                             round((doc2[j].x-doc1[i].x)*1000,3),
                             '',
                             round((doc2[j].y-doc1[i].y)*1000,3),
                             round((doc2[j].z-doc1[i].z)*1000,3),
                             round((doc2[j].l-doc1[i].l)*1000,3),
                             round((doc2[j].s-doc1[i].s)*1000,3),
                             round(sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2), 3),
                             doc1[i].newline,
                             doc2[j].newline
                             ])
                # test = sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2)
                # print(test, type(test))
                # print(doc1[i].name, doc1[i].x, doc1[i].y, doc2[j].name, doc2[j].x, doc2[j].y)
                lasti = i+1
                lastj = j+1
                break

    print(len(lst3))
    for line in lst3:
        if type(line[0]) is list:
            pass
            for ln in line:
                if ln[1] == 0:
                    # print(ln[0])
                    obj = FilesTbl.objects.filter(name=ln[0]).filter(parent=first)
                    lst_new.append([obj[0].name,
                                    obj[0].x,
                                    obj[0].y,
                                    obj[0].z,
                                    obj[0].l,
                                    obj[0].s,
                                    0,
                                    0,
                                    0,
                                    0,
                                    0,
                                    0,
                                    round((0 - obj[0].x) * 1000, 3),
                                    '',
                                    round((0 - obj[0].y) * 1000, 3),
                                    round((0 - obj[0].z) * 1000, 3),
                                    round((0 - obj[0].l) * 1000, 3),
                                    round((0 - obj[0].s) * 1000, 3),
                                    round(sqrt(((0-doc1[i].z)*1000)**2 + ((0-doc1[i].l)*1000)**2), 3),
                                    obj[0].newline,
                                    0
                                    ])
                else:
                    obj = FilesTbl.objects.filter(name=ln[0]).filter(parent=second)
                    if obj[0].name not in names_lst:
                        lst_new.append([0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        obj[0].name,
                                        obj[0].x,
                                        obj[0].y,
                                        obj[0].z,
                                        obj[0].l,
                                        obj[0].s,
                                        round((obj[0].x-0)*1000, 3),
                                        '',
                                        round((obj[0].y-0)*1000,3),
                                        round((obj[0].z-0)*1000,3),
                                        round((obj[0].l-0)*1000,3),
                                        round((obj[0].s-0)*1000,3),
                                        round(sqrt(((doc2[j].z-0)*1000)**2 + ((doc2[j].l-0)*1000)**2), 3),
                                        0,
                                        obj[0].newline
                                        ])
        else:
            lst_new.append(line)
    i = 0
    for line in lst_new:
        i += 1
        print(i,'|  ', line)

    #
    bb = Step_2_doc.objects.filter(file1=file1).filter(file2=file2)
    if bb:
        bbb = FilesTbl.objects.filter(parent = bb[0].pk)
        bbb.delete()
        bb.delete()

    bb = Step_2_doc.objects.create(
        date = dt.now(),
        file1 = file1,
        file2 = file2,
        comment = comment
    )
    for line in lst_new:
        if line[0] == 0:
            name = line[6]
        else:
            name = line[0]
        Step_2.objects.create(
            parent= bb,
            name = name,
            x = line[1],
            y = line[2],
            z = line[3],
            l = line[4],
            s = line[5],
            x2 = line[7],
            y2 = line[8],
            z2 = line[9],
            l2 = line[10],
            s2 = line[11],
            ox = line[12],
            oy = line[14],
            oz = line[15],
            ol = line[16],
            os = line[17],
            absolute = line[18],
            newline = line[19],
            newline2 = line[20]
        )

    return render(request, 'energy/ajax_step2.html', {'lst':lst_new})


#
# def ajax_step2(request):
#     print('ajax_step2')
#
#     def func(num):
#         if num < 0:
#             return -num
#         else:
#             return num
#
#     first = request.GET.get('first')
#     second = request.GET.get('second')
#     comment = request.GET.get('comment')
#     file1 = Files.objects.get(pk=first).file
#     file2 = Files.objects.get(pk=second).file
#     doc1 = FilesTbl.objects.filter(parent=first)
#     doc2 = FilesTbl.objects.filter(parent=second)
#     # i = 1
#     # for line in doc1:
#     #     print(i, '|', line.name)
#     #     i += 1
#     # y = dict(doc1)
#     # for line in doc1:
#     #     print(line.name)
#     lasti = 0
#     lastj = 0
#     lst2 = []
#     lst3 = []
#     names_lst = []
#     lst_new = []
#     for i in range(0,len(doc1)):
#         for j in range(0,len(doc2)):
#             x = func(doc1[i].x - doc2[j].x)
#             y = func(doc1[i].y - doc2[j].y)
#             z = func(doc1[i].z - doc2[j].z)
#             itog = x+y+z
#             if itog < 0.51:
#             # if round(doc1[i].x,1) == round(doc2[j].x,1) \
#             #         and round(doc1[i].y,1) == round(doc2[j].y,1) \
#             #         and round(doc1[i].z,1) == round(doc2[j].z,1):
#             #     names_lst.append(doc2[j].name)
#             #     print(doc1[i].name, doc2[j].name)
#                 for ii in range(lasti, i):
#                     # if doc1[ii].name not in names_lst:
#                     if doc1[i].name != doc1[ii].name:
#                         lst2.append([doc1[ii].name, 0])
#                 for jj in range(lastj, j):
#                     # if doc2[jj].name not in names_lst :
#                         if doc2[j].name != doc2[jj].name :
#                             lst2.append([doc2[jj].name, 1])
#                 #     # print(doc1[ii].name, doc1[ii].old_num, ii)
#             lasti = i + 1
#             lastj = j + 1
#             break
#
#
#     #             # names_lst.append(doc2[jj].name)
#     #
#     #
#     #             #     for jj in range(lastj, j):
#     #             #
#     #             #         print(doc2[jj].name, doc2[jj].old_num, jj)
#     #             #         if str(doc1[ii].name)[len(doc1[ii].name)-3:] > str(doc2[jj].name)[len(doc2[jj].name)-3:]:
#     #             #             print(doc1[ii].name)
#     #             #         else:
#     #             #             print(doc2[jj].name)
#     #             # print(sorted(lst2, reverse = True))
#     #
#                 if len(lst2)>0:
#                     # for line in sorted(lst2, reverse = True):
#                     #     print(line)
#                     lst3.append(sorted(lst2, reverse = True))
#                 else:
#                     lst3.append(lst2)
#                 lst2 = []
#                 lst3.append([doc1[i].name,
#                              doc1[i].x,
#                              doc1[i].y,
#                              doc1[i].z,
#                              doc1[i].l,
#                              doc1[i].s,
#                              doc2[j].name,
#                              doc2[j].x,
#                              doc2[j].y,
#                              doc2[j].z,
#                              doc2[j].l,
#                              doc2[j].s,
#                              round((doc2[j].x-doc1[i].x)*1000,3),
#                              '',
#                              round((doc2[j].y-doc1[i].y)*1000,3),
#                              round((doc2[j].z-doc1[i].z)*1000,3),
#                              round((doc2[j].l-doc1[i].l)*1000,3),
#                              round((doc2[j].s-doc1[i].s)*1000,3),
#                              round(sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2), 3),
#                              doc1[i].newline,
#                              doc2[j].newline])
#     print('длина', len(lst3))
#     for line in lst3:
#         print(line)
#     #             # test = sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2)
#     #             # print(test, type(test))
#     #             # print(doc1[i].name, doc1[i].x, doc1[i].y, doc2[j].name, doc2[j].x, doc2[j].y)
#     #             lasti = i+1
#     #             lastj = j+1
#     #             break
#     # print('-----')
#     # # for line in lst3:
#     # #     print(line)
#     # # print('-----')
#     # for line in lst3:
#     #
#     #     if type(line[0]) is list:
#     #         for ln in line:
#     #             if ln[1] == 0:
#     #                 # print(ln[0])
#     #                 obj = FilesTbl.objects.filter(name=ln[0]).filter(parent=first)
#     #                 lst_new.append([obj[0].name,
#     #                                 obj[0].x,
#     #                                 obj[0].y,
#     #                                 obj[0].z,
#     #                                 obj[0].l,
#     #                                 obj[0].s,
#     #                                 0,
#     #                                 0,
#     #                                 0,
#     #                                 0,
#     #                                 0,
#     #                                 0,
#     #                                 round((0 - obj[0].x) * 1000, 3),
#     #                                 '',
#     #                                 round((0 - obj[0].y) * 1000, 3),
#     #                                 round((0 - obj[0].z) * 1000, 3),
#     #                                 round((0 - obj[0].l) * 1000, 3),
#     #                                 round((0 - obj[0].s) * 1000, 3),
#     #                                 round(sqrt(((0 - obj[0].z) * 1000) ** 2 + ((0 - obj[0].l) * 1000) ** 2), 3),
#     #                                 obj[0].newline,
#     #                                 false])
#     #             else:
#     #                 obj = FilesTbl.objects.filter(name=ln[0]).filter(parent=second)
#     #                 if obj[0].name not in names_lst:
#     #                     lst_new.append([0,
#     #                                     0,
#     #                                     0,
#     #                                     0,
#     #                                     0,
#     #                                     0,
#     #                                     obj[0].name,
#     #                                     obj[0].x, obj[0].y,
#     #                                     obj[0].z, obj[0].l,
#     #                                     obj[0].s, round((obj[0].x-0)*1000, 3),
#     #                                     '',
#     #                                     round((obj[0].y-0)*1000,3),
#     #                                     round((obj[0].z-0)*1000,3),
#     #                                     round((obj[0].l-0)*1000,3),
#     #                                     round((obj[0].s-0)*1000,3),
#     #                                     round(sqrt(((obj[0].z-0)*1000)**2 + ((obj[0].l-0)*1000)**2), 3),
#     #                                     false,
#     #                                     obj[0].newline])
#     #     else:
#     #         lst_new.append(line)
#     #
#     # bb = Step_2_doc.objects.filter(file1=file1).filter(file2=file2)
#     # if bb:
#     #     bbb = FilesTbl.objects.filter(parent = bb[0].pk)
#     #     bbb.delete()
#     #     bb.delete()
#     #
#     # bb = Step_2_doc.objects.create(
#     #     date = dt.now(),
#     #     file1 = file1,
#     #     file2 = file2,
#     #     comment = comment
#     # )
#     # for line in lst_new:
#     #     if line[0] == 0:
#     #         name = line[6]
#     #     else:
#     #         name = line[0]
#     #     Step_2.objects.create(
#     #         parent= bb,
#     #         name = name,
#     #         x = line[1],
#     #         y = line[2],
#     #         z = line[3],
#     #         l = line[4],
#     #         s = line[5],
#     #         x2 = line[7],
#     #         y2 = line[8],
#     #         z2 = line[9],
#     #         l2 = line[10],
#     #         s2 = line[11],
#     #         ox = line[12],
#     #         oy = line[14],
#     #         oz = line[15],
#     #         ol = line[16],
#     #         os = line[17],
#     #         absolute = line[18],
#     #         newline = line[19],
#     #         newline2 = line[20]
#     #     )
#
#     return render(request, 'energy/ajax_step2.html', {'lst':lst_new})


# def ajax_gps(request):
#     print('ajax_gps')
#     first = request.GET.get('first')
#     second = request.GET.get('second')
#     comment = request.GET.get('comment')
#     file1 = Files_gps.objects.get(pk=first).file
#     file2 = Files_gps.objects.get(pk=second).file
#     doc1 = FilesTbl_gps.objects.filter(parent=first)
#     doc2 = FilesTbl_gps.objects.filter(parent=second)
#     print(len(doc1), len(doc2))
#     lasti = 0
#     lastj = 0
#     lst2 = []
#     lst3 = []
#     lst_new = []
#     date1 = Files_gps.objects.get(pk=first).date
#     date2 = Files_gps.objects.get(pk=second).date
#
#     # date = dt.strptime(date1, '%Y-%m-%d').date()
#     # print(date1, type(date1), date2, type(date2))
#     date2 = Files_gps.objects.get(pk=second).date
#     for i in range(0,len(doc1)-1):
#         for j in range(0,len(doc2)-1):
#             if doc1[i].name == doc2[j].name:
#                 for ii in range(lasti, i):
#                     lst2.append([doc1[ii].name, 0])
#                 for jj in range(lastj, j):
#                     lst2.append([doc2[jj].name, 1])
#                 if len(lst2)>0:
#                     lst3.append(sorted(lst2, reverse = True))
#                 lst2 = []
#                 # print(type(file2.date), file2.date)
#
#                 date = date2 - date1
#                 date = int(str(date)[:str(date).find(' ')])
#                 # print(int(str(date)[:str(date).find(' ')]))
#                 lst3.append([doc1[i].name,
#                              doc1[i].x,
#                              doc1[i].y,
#                              doc1[i].z,
#                              '',#doc1[i].l,
#                              '',# doc1[i].s,
#                              doc2[j].name,
#                              doc2[j].x,
#                              doc2[j].y,
#                              doc2[j].z,
#                              '',#doc2[j].l,
#                              '',# doc2[j].s,
#                              round((doc2[j].x-doc1[i].x)*1000,4),
#                              '',
#                              round((doc2[j].y-doc1[i].y)*1000,4),
#                              round((doc2[j].z-doc1[i].z)*1000,4),
#                              round((doc2[j].z - doc1[i].z) * 1000, 4),
#                              '',# round((doc2[j].l-doc1[i].l)*1000,4),
#                              '',# round((doc2[j].s-doc1[i].s)*1000,4),
#                              '',# round(sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2), 4),
#                              ''])# round(sqrt(((doc2[j].z - doc1[i].z) * 1000) ** 2 + ((doc2[j].l - doc1[i].l) * 1000) ** 2)/date, 4)])
#                 lasti = i+1
#                 lastj = j+1
#                 break
#     for line in lst3:
#         if type(line[0]) is list:
#             for ln in line:
#                 if ln[1] == 0:
#                     # print(ln[0])
#                     obj = FilesTbl_gps.objects.filter(name=ln[0]).filter(parent=first)
#                     lst_new.append([obj[0].name,
#                                     obj[0].x,
#                                     obj[0].y,
#                                     obj[0].z,
#                                     # '',# obj[0].l,                           # 4
#                                     # '',# obj[0].s,                           # 5
#                                     0,
#                                     0,
#                                     0,
#                                     0,
#                                     '',# 0,                                  #10
#                                     '',# 0,                                  #11
#                                     round((0 - obj[0].x) * 1000, 4),
#                                     '',             #9
#                                     round((0 - obj[0].y) * 1000, 4),
#                                     round((0 - obj[0].z) * 1000, 4),
#                                     '',# round((0 - obj[0].l) * 1000, 4),    #16
#                                     '',# round((0 - obj[0].s) * 1000, 4),    #17
#                                     '',
#                                     '',
#                                     ''])#round(sqrt(((0 - obj[0].z) * 1000) ** 2 + ((0 - obj[0].l) * 1000) ** 2), 4)])#19
#                 else:
#                     obj = FilesTbl_gps.objects.filter(name=ln[0]).filter(parent=second)
#                     lst_new.append([0,
#                                     0,
#                                     0,
#                                     0,
#                                     # '',# 4
#                                     # '', # 5
#                                     obj[0].name,
#                                     obj[0].x,
#                                     obj[0].y,
#                                     obj[0].z,
#                                     '',#10
#                                     '',#11
#                                     round((obj[0].x-0)*1000,4),
#                                     '',
#                                     round((obj[0].y-0)*1000,4),
#                                     round((obj[0].z-0)*1000,4),
#                                     '',#16
#                                     '',#17
#                                     '',#18
#                                     '',
#                                     ''])#round(sqrt(((obj[0].z-0)*1000)**2 + ((obj[0].l-0)*1000)**2), 4)])
#         else:
#             lst_new.append(line)
#
#     bb = GPS_doc.objects.filter(file1=file1).filter(file2=file2)
#     if bb:
#         bbb = FilesTbl.objects.filter(parent = bb[0].pk)
#         bbb.delete()
#         bb.delete()
#
#     bb = GPS_doc.objects.create(
#         date = dt.now(),
#         file1 = file1,
#         file2 = file2,
#         comment = comment
#     )
#     for line in lst_new:
#         print(line[5])
#         if line[0] == 0:
#             name = line[6]
#         else:
#             name = line[0]
#         GPS.objects.create(
#             parent= bb,
#             name = name,
#             x = line[1],
#             y = line[2],
#             z = line[3],
#             # l = line[4],
#             # s = line[5],
#             x2 = line[5],
#             y2 = line[6],
#             z2 = line[7],
#             # l2 = line[10],
#             # s2 = line[11],
#             ox = line[10],
#             oy = line[12],
#             oz = line[13],
#             # ol = line[16],
#             # os = line[17],
#             v = 0,
#             absolute = 0
#         )
#     return render(request, 'energy/ajax_step2.html', {'lst':lst_new})
#
# def ajax_step2(request):
#     print('ajax_step2')
#     first = request.GET.get('first')
#     second = request.GET.get('second')
#     comment = request.GET.get('comment')
#     file1 = Files.objects.get(pk=first).file
#     file2 = Files.objects.get(pk=second).file
#     doc1 = FilesTbl.objects.filter(parent=first)
#     doc2 = FilesTbl.objects.filter(parent=second)
#     # print(len(doc1), len(doc2))
#     lasti = 0
#     lastj = 0
#     lst2 = []
#     lst3 = []
#     lst_new = []
#     for i in range(0,len(doc1)-1):
#         for j in range(0,len(doc2)-1):
#             if doc1[i].name == doc2[j].name:
#                 for ii in range(lasti, i):
#                     lst2.append([doc1[ii].name, 0])
#                 for jj in range(lastj, j):
#                     lst2.append([doc2[jj].name, 1])
#                     # print(doc1[ii].name, doc1[ii].old_num, ii)
#                     # for jj in range(lastj, j):
#                         # print(doc2[jj].name, doc2[jj].old_num, jj)
#                         # if str(doc1[ii].name)[len(doc1[ii].name)-3:] > str(doc2[jj].name)[len(doc2[jj].name)-3:]:
#                         #     print(doc1[ii].name)
#                         # else:
#                         #     print(doc2[jj].name)
#                 # print(sorted(lst2, reverse = True))
#                 if len(lst2)>0:
#                     # for line in sorted(lst2, reverse = True):
#                     #     print(line)
#                     lst3.append(sorted(lst2, reverse = True))
#                 lst2 = []
#                 lst3.append([doc1[i].name, doc1[i].x, doc1[i].y, doc1[i].z, doc1[i].l, doc1[i].s, doc2[j].name, doc2[j].x, doc2[j].y, doc2[j].z, doc2[j].l, doc2[j].s, round((doc2[j].x-doc1[i].x)*1000,4), '', round((doc2[j].y-doc1[i].y)*1000,4), round((doc2[j].z-doc1[i].z)*1000,4), round((doc2[j].l-doc1[i].l)*1000,4), round((doc2[j].s-doc1[i].s)*1000,4), round(sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2), 4)])
#                 # test = sqrt(((doc2[j].z-doc1[i].z)*1000)**2 + ((doc2[j].l-doc1[i].l)*1000)**2)
#                 # print(test, type(test))
#                 # print(doc1[i].name, doc1[i].x, doc1[i].y, doc2[j].name, doc2[j].x, doc2[j].y)
#                 lasti = i+1
#                 lastj = j+1
#                 break
#     # for line in lst3:
#     #     print(line)
#     #     print('-----')
#     for line in lst3:
#         if type(line[0]) is list:
#             for ln in line:
#                 if ln[1] == 0:
#                     # print(ln[0])
#                     obj = FilesTbl.objects.filter(name=ln[0]).filter(parent=first)
#                     lst_new.append([obj[0].name, obj[0].x, obj[0].y, obj[0].z, obj[0].l, obj[0].s, 0, 0, 0, 0, 0, 0,
#                                     round((0 - obj[0].x) * 1000, 4), '', round((0 - obj[0].y) * 1000, 4),
#                                     round((0 - obj[0].z) * 1000, 4), round((0 - obj[0].l) * 1000, 4),
#                                     round((0 - obj[0].s) * 1000, 4),
#                                     round(sqrt(((0 - obj[0].z) * 1000) ** 2 + ((0 - obj[0].l) * 1000) ** 2), 4)])
#                 else:
#                     obj = FilesTbl.objects.filter(name=ln[0]).filter(parent=second)
#                     lst_new.append([0, 0, 0, 0, 0, 0, obj[0].name, obj[0].x, obj[0].y, obj[0].z, obj[0].l, obj[0].s, round((obj[0].x-0)*1000,4), '', round((obj[0].y-0)*1000,4), round((obj[0].z-0)*1000,4), round((obj[0].l-0)*1000,4), round((obj[0].s-0)*1000,4), round(sqrt(((obj[0].z-0)*1000)**2 + ((obj[0].l-0)*1000)**2), 4)])
#         else:
#             lst_new.append(line)
#
#     bb = Step_2_doc.objects.filter(file1=file1).filter(file2=file2)
#     if bb:
#         bbb = FilesTbl.objects.filter(parent = bb[0].pk)
#         bbb.delete()
#         bb.delete()
#
#     bb = Step_2_doc.objects.create(
#         date = dt.now(),
#         file1 = file1,
#         file2 = file2,
#         comment = comment
#     )
#     for line in lst_new:
#         if line[0] == 0:
#             name = line[6]
#         else:
#             name = line[0]
#         Step_2.objects.create(
#             parent= bb,
#             name = name,
#             x = line[1],
#             y = line[2],
#             z = line[3],
#             l = line[4],
#             s = line[5],
#             x2 = line[7],
#             y2 = line[8],
#             z2 = line[9],
#             l2 = line[10],
#             s2 = line[11],
#             ox = line[12],
#             oy = line[14],
#             oz = line[15],
#             ol = line[16],
#             os = line[17],
#             absolute = line[18]
#         )
#     #     print(line)
#     # print(file1, file2)
#
#     # i = 0
#     # final = []
#     # d1=0
#     # d2=0
#     # while True:
#     #     try:
#     #         if doc1[i+d1].name == doc2[i+d2].name:
#     #             final.append(doc1[i+d1], doc2[i+d2])
#     #             print(d1, d2)
#     #             print(doc1[i + d1], doc2[i + d2])
#     #         else:
#     #             try:
#     #
#     #                 # for j in range(1, 5):
#     #                 #     print('--',i,'--',doc1[i].name, doc2[i].name)
#     #                 #     print(doc1[i].name, doc2[i+j].name)
#     #                 #     print(doc1[i+j].name, doc2[i].name)
#     #                 #     # if doc1[i+d1].name == doc2[i+j+d2].name:
#     #                 #     #     final.append(doc1[i+d1], doc2[i+j+d2])
#     #                 #     #     print(d1, d2)
#     #                 #     #     d2 += 1
#     #                 #     #     print(doc1[i+d1], doc2[i+j+d2])
#     #                 #     # elif doc1[i+j+d1].name == doc2[i+d2].name:
#     #                 #     #     final.append(doc1[i+j+d1], doc2[i+d2])
#     #                 #     #     d1 += 1
#     #                 #     #     print(d1, d2)
#     #             except:
#     #                 break
#     #     except:
#     #        break
#     #     i += 1
#
#     # i = 0
#     # k = False
#     # test = dict()
#     # lst1 = []
#     # lst_full = []
#     # for line1 in doc1:
#     #     i += 1
#     #     j = 0
#     #     for line2 in doc2:
#     #         j += 1
#     #         if line1.name==line2.name:
#     #             test[line1.name] = [line1.name, line2.name, i, j]
#     #             lst_full.append([line1.name, line2.name, i, j])
#     #             if not k:
#     #                 h3 = line1.name
#     #                 h = doc1[:i-1]
#     #                 h1 = doc2[:j-1]
#     #                 k = True
#     #                 continue
#     #
#     #     # if k:
#     #     #     break
#     #
#     # if len(h)==1 or len(h1)==1:
#     #
#     #     if len(h1)==1:
#     #         lst1 = step2_ajax_1(h,h1, h3)
#     #     else:
#     #         lst1 = step2_ajax_1(h1, h, h3)
#     # ggg = lst1[len(lst1)-1]
#     # print('000', ggg)
#     #
#     #
#     # last_line = 0
#     # last_line_2 = 0
#     # for line in lst_full:
#     #     print()
#     #     print('--------', line[3] - 1)
#     #     for y in range(last_line,line[2]-1):
#     #         for yy in range(last_line_2, line[3] - 1) :
#     #             if int(str(doc1[y].name)[len(doc1[y].name)-3:]) > int(str(doc2[yy].name)[len(doc2[yy].name)-3:]):
#     #                 print(['', doc1[y].name])
#     #             else:
#     #                 print([doc2[yy].name, ''])
#     #             last_line_2 = yy + 1
#     #             continue
#     #         if k :
#     #             continue
#     #             k = False
#     #         print([doc1[y].name, ''])
#     #         #
#     #         last_line = y+1
#     #         # continue
#     #     if k:
#     #         # continue
#     #         k = False
#     #
#     #
#     #
#     #     print('------------------')
#
#         # pass
#
#
#     # for line in lst_full:
#     #     print(i, line[2])
#     #     if line[2] > i:
#     #         lst1.append(['676767','9090'])
#
#
#     # if len(h) > len(h1):
#
#     # print(lst1)
#
#     # for line in test:
#     #     print(test[line])
#     return render(request, 'energy/ajax_step2.html', {'lst':lst_new})






