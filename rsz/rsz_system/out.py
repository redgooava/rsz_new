import datetime as dt
from datetime import datetime as dt_
from datetime import date

from .models import Divisiontable, Outtable
from .collection import listOfMilitaryRanks, listOfReasons, listOfRanks


def out(request):
    divisionList = ''
    fullOutTable = ''
    errorlabel = ''
    try:
        divisionList = getDivisionList(Divisiontable.objects.all())
        add(request)
        delete(request)
        returning(request)
        fullOutTable = table(Outtable.objects.all())
        edit(request)
    except ValueError:
        errorlabel = 'Ошибка в заполнении формы. ' \
                     'Возможно, вы оставили пустое поле или заполнили форму непредусмотренным значением'

    context = {
        'listMilRanks': listOfMilitaryRanks,
        'divisionList': divisionList,
        'listOfReasons': listOfReasons,
        'listRanks': listOfRanks,
        'fullOutTable': fullOutTable,
        'errorlabel': errorlabel,
    }
    return context


def getDivisionList(queryset):
    allData = queryset.values()
    divisionList = []
    for i in allData:
        divisionList.append(i)
    return divisionList


def add(request):
    if request.POST.get('createbutton') is not None:
        copyRequest = Outtable.objects.filter(name=request.POST.get('name'),
                                              whyout=request.POST.get('reason'),
                                              datestart=request.POST.get('datestart'),
                                              dateend=request.POST.get('dateend'),
                                              subdivision=request.POST.get('division'),
                                              numberoforder=request.POST.get('numberoforder'),
                                              rank=request.POST.get('rank'),
                                              military_rank=request.POST.get('mrank')
                                              )
        if len(copyRequest) == 0 and len(request.POST.get('name')) is not 0:
            Outtable.objects.create(name=request.POST.get('name'),
                                    whyout=request.POST.get('reason'),
                                    datestart=request.POST.get('datestart'),
                                    dateend=request.POST.get('dateend'),
                                    subdivision=request.POST.get('division'),
                                    numberoforder=request.POST.get('numberoforder'),
                                    rank=request.POST.get('rank'),
                                    military_rank=request.POST.get('mrank')
                                    )
        else:
            print('----------------')
            print('Не записалось')
            print('----------------')


def delete(request):
    if request.POST.get('deletebutton') is not None:
        delQueryset = Outtable.objects.filter(name__exact=request.POST.get('deletename'),
                                               datestart__exact=request.POST.get('deletestart'))
        delQueryset.delete()


def table(queryset):
    allData = queryset.values()
    resultList = []
    for i in allData:
        resultList.append(i.values())

    listChoosenHuman = []

    for i in resultList:
        listChoosenHuman.append(list(i))

    for i in listChoosenHuman:
        if i[7] is not None:
            i[7] = dt.datetime.date(dt.datetime.strptime(str(list(i)[7]), '%Y-%m-%d')).strftime('%d.%m.%Y')
        if i[8] is not None:
            i[8] = dt.datetime.date(dt.datetime.strptime(str(list(i)[8]), '%Y-%m-%d')).strftime('%d.%m.%Y')
        if i[9] is not None:
            i[9] = dt.datetime.date(dt.datetime.strptime(str(list(i)[9]), '%Y-%m-%d')).strftime('%d.%m.%Y')

    return listChoosenHuman


def returning(request):
    if request.POST.get('realendbutton') is not None:
        returnQueryset = Outtable.objects.filter(name__exact=request.POST.get('realendname'),
                                                 datestart__exact=request.POST.get('realendstart'))
        for i in returnQueryset:
            i.daterealend = request.POST.get('realendend')
            i.save()


def edit(request):
    if request.POST.get('editbutton') is not None:
        editQueryset = Outtable.objects.filter(id__exact=request.POST.get('editid'))
        for i in editQueryset:
            i.name = request.POST.get('editname')
            i.military_rank = request.POST.get('editmrank')
            i.rank = request.POST.get('editrank')
            i.whyout = request.POST.get('editreason')
            i.datestart = request.POST.get('editdatestart')
            i.dateend = request.POST.get('editdateend')
            i.subdivision = request.POST.get('editdivision')
            i.numberoforder = request.POST.get('editnumberoforder')
            i.save()


def search(request):
    queryset1 = Outtable.objects.filter(name__exact=request.POST.get('choosenname', ' '),
                                                 subdivision__exact=request.POST.get('division', ' '),
                                                 datestart__gte=request.POST.get('datestart', date(2022, 1, 1)),
                                                 datestart__lte=request.POST.get('dateend', date(2022, 1, 1)))

    queryset2 = Outtable.objects.filter(name__exact=request.POST.get('choosenname', ' '),
                                                 subdivision__exact=request.POST.get('division', ' '),
                                                 dateend__gte=request.POST.get('datestart', date(2022, 1, 1)),
                                                 dateend__lte=request.POST.get('dateend', date(2022, 1, 1)))

    querysetUnion = queryset1.union(queryset2)

    choosenHuman = table(querysetUnion.values())

    context = {
        'choosenHuman': choosenHuman,
        'divisionList': getDivisionList(Divisiontable.objects.all()),
    }
    return context
