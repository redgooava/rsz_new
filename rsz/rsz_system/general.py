import datetime as dt

from datetime import datetime
from .models import Divisiontable
from .actions import rankIsOut, reasonOfOut


def general(request):
    errorlabel = ''
    generalTable = None
    generalDate = None
    try:
        add(request)
        edit(request)
        delete(request)
        generalTable, gDate = table(request, Divisiontable.objects.values())
        generalDate = dt.datetime.strptime(str(gDate), '%Y-%m-%d').strftime('%d.%m.%Y')
    except ValueError as e:
        errorlabel = 'Ошибка в заполнении формы. ' \
                     'Возможно, вы оставили пустое поле или заполнили форму непредусмотренным значением'
        generalDate = ''
        print('Ошибка в заполнении формы. '
              'Возможно, вы оставили пустое поле или заполнили форму непредусмотренным значением')
    context = {
        'generalTable': generalTable,
        'generalDate': generalDate,
        'errorlabel': errorlabel,
    }
    return context


def table(request, queryset):
    date = None
    if request.POST.get('date') is None:
        date = dt.date.today()
    else:
        date = request.POST.get('date')

    generalTable = []

    for i in queryset:
        generalTable.append(i.values())

    for i in range(len(generalTable)):
        generalTable[i] = list(generalTable[i])
        generalTable[i].append(generalTable[i][9] - rankIsOut(generalTable[i][1], 'Оф', date))
        generalTable[i].append(generalTable[i][10] - rankIsOut(generalTable[i][1], 'Пр', date))
        generalTable[i].append(generalTable[i][11] - rankIsOut(generalTable[i][1], 'К/с', date))
        generalTable[i].append(generalTable[i][12] - rankIsOut(generalTable[i][1], 'С/с', date))
        generalTable[i].append(generalTable[i][13] - rankIsOut(generalTable[i][1], 'К-ты', date))
        generalTable[i].append(generalTable[i][14] - rankIsOut(generalTable[i][1], 'Сл', date))
        generalTable[i].append(generalTable[i][16] + generalTable[i][17] + generalTable[i][18] +
                               generalTable[i][19] + generalTable[i][20] + generalTable[i][21])
        generalTable[i].append(reasonOfOut(generalTable[i][1], 'Отпуск', date))
        generalTable[i].append(reasonOfOut(generalTable[i][1], 'Стационарное лечение', date))
        generalTable[i].append(reasonOfOut(generalTable[i][1], 'Амбулаторное лечение', date))
        generalTable[i].append(reasonOfOut(generalTable[i][1], 'Наряд', date))
        generalTable[i].append(reasonOfOut(generalTable[i][1], 'Командировка', date))
        generalTable[i].append(generalTable[i][23] + generalTable[i][24] +
                               generalTable[i][25] + generalTable[i][26] + generalTable[i][27])
    return generalTable, date


def search(request, queryset):
    date = None
    if request.POST.get('date') is None:
        date = dt.date.today()
    else:
        date = request.POST.get('date')
    generalTable = []

    if len(queryset) != 0:
        for i in queryset:
            generalTable.append(i.values())

        for i in range(len(generalTable)):
            generalTable[i] = list(generalTable[i])
            generalTable[i].append(generalTable[i][9] - rankIsOut(generalTable[i][1], 'Оф', date))
            generalTable[i].append(generalTable[i][10] - rankIsOut(generalTable[i][1], 'Пр', date))
            generalTable[i].append(generalTable[i][11] - rankIsOut(generalTable[i][1], 'К/с', date))
            generalTable[i].append(generalTable[i][12] - rankIsOut(generalTable[i][1], 'С/с', date))
            generalTable[i].append(generalTable[i][13] - rankIsOut(generalTable[i][1], 'К-ты', date))
            generalTable[i].append(generalTable[i][14] - rankIsOut(generalTable[i][1], 'Сл', date))
            generalTable[i].append(generalTable[i][16] + generalTable[i][17] + generalTable[i][18] +
                                   generalTable[i][19] + generalTable[i][20] + generalTable[i][21])
            generalTable[i].append(reasonOfOut(generalTable[i][1], 'Отпуск', date))
            generalTable[i].append(reasonOfOut(generalTable[i][1], 'Стационарное лечение', date))
            generalTable[i].append(reasonOfOut(generalTable[i][1], 'Амбулаторное лечение', date))
            generalTable[i].append(reasonOfOut(generalTable[i][1], 'Наряд', date))
            generalTable[i].append(reasonOfOut(generalTable[i][1], 'Командировка', date))
            generalTable[i].append(generalTable[i][23] + generalTable[i][24] +
                                   generalTable[i][25] + generalTable[i][26] + generalTable[i][27])
    else:
        generalTable = None

    context = {
        'choosenTable': generalTable,
    }

    return context


def add(request):
    if request.POST.get('addbutton') is not None:
        copyRequest = Divisiontable.objects.filter(division=request.POST.get('addname'))
        if len(copyRequest) == 0:
            Divisiontable.objects.create(division=request.POST.get('addname'),
                                         officer=request.POST.get('addofficer'),
                                         ensign=request.POST.get('addensign'),
                                         contract=request.POST.get('addcontract'),
                                         soldier=request.POST.get('addsoldier'),
                                         cadet=request.POST.get('addcadet'),
                                         listener=request.POST.get('addlistener'),
                                         total=request.POST.get('addtotal'),
                                         s_officer=request.POST.get('addsofficer'),
                                         s_ensign=request.POST.get('addsensign'),
                                         s_contract=request.POST.get('addscontract'),
                                         s_soldier=request.POST.get('addssoldier'),
                                         s_cadet=request.POST.get('addscadet'),
                                         s_listener=request.POST.get('addslistener'),
                                         s_total=request.POST.get('addstotal'),
                                         )
        else:
            print('----------------')
            print('Не записалось')
            print('----------------')


def edit(request):
    if request.POST.get('editbutton') is not None:
        editQueryset = Divisiontable.objects.filter(id__exact=request.POST.get('editid'))
        for i in editQueryset:
            i.division = request.POST.get('editname')
            i.officer = request.POST.get('editofficer')
            i.ensign = request.POST.get('editensign')
            i.contract = request.POST.get('editcontract')
            i.soldier = request.POST.get('editsoldier')
            i.cadet = request.POST.get('editcadet')
            i.listener = request.POST.get('editlistener')
            i.total = request.POST.get('edittotal')
            i.s_officer = request.POST.get('editsofficer')
            i.s_ensign = request.POST.get('editsensign')
            i.s_contract = request.POST.get('editscontract')
            i.s_soldier = request.POST.get('editssoldier')
            i.s_cadet = request.POST.get('editscadet')
            i.s_listener = request.POST.get('editslistener')
            i.s_total = request.POST.get('editstotal')
            i.save()


def delete(request):
    if request.POST.get('deletebutton') is not None:
        delQueryset = Divisiontable.objects.filter(id__exact=request.POST.get('deleteid'))
        delQueryset.delete()


def main(request):
    generalTable, gDate = table(request, Divisiontable.objects.values())
    generalDate = dt.datetime.strptime(str(gDate), '%Y-%m-%d').strftime('%d.%m.%Y')
    context = {
        'generalTable': generalTable,
        'generalDate': generalDate,
    }
    return context
