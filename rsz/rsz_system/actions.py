import datetime

from .models import Outtable


def rankIsOut(division, rank, date):
    querysetFiltered = Outtable.objects.filter(
        subdivision__exact=division, rank__exact=rank,
        datestart__lte=date, dateend__gt=date, daterealend__exact=None)
    return len(querysetFiltered)


def reasonOfOut(division, whyout, date):
    querysetFiltered = Outtable.objects.filter(
        subdivision__exact=division, whyout__exact=whyout,
        datestart__lte=date, dateend__gt=date, daterealend__exact=None)
    return len(querysetFiltered)
