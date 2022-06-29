from django.shortcuts import render

from . import out, general
from .models import Divisiontable


def v_general(request):
    context = general.general(request)
    return render(request, 'rsz_system/general.html', context)


def v_out(request):
    context = out.out(request)
    return render(request, 'rsz_system/out.html', context)


def v_general_main(request):
    context = general.main(request)
    return render(request, 'rsz_system/general_main.html', context)


def v_out_search(request):
    context = out.search(request)
    return render(request, 'rsz_system/search_out.html', context)


def v_general_search(request):
    context = general.search(request,
                             Divisiontable.objects.filter(division__exact=request.POST.get('choosendivision')).values())
    return render(request, 'rsz_system/search_general.html', context)


def about(request):
    return render(request, 'rsz_system/about.html')
