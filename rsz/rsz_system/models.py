from django.db import models


class Divisiontable(models.Model):
    division = models.CharField(max_length=255, blank=True, null=True)
    officer = models.PositiveIntegerField(blank=True, null=True)
    ensign = models.PositiveIntegerField(blank=True, null=True)
    contract = models.PositiveIntegerField(blank=True, null=True)
    soldier = models.PositiveIntegerField(blank=True, null=True)
    cadet = models.PositiveIntegerField(blank=True, null=True)
    listener = models.PositiveIntegerField(blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)
    s_officer = models.PositiveIntegerField(blank=True, null=True)
    s_ensign = models.PositiveIntegerField(blank=True, null=True)
    s_contract = models.PositiveIntegerField(blank=True, null=True)
    s_soldier = models.PositiveIntegerField(blank=True, null=True)
    s_cadet = models.PositiveIntegerField(blank=True, null=True)
    s_listener = models.PositiveIntegerField(blank=True, null=True)
    s_total = models.PositiveIntegerField(blank=True, null=True)


class Outtable(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    military_rank = models.CharField(max_length=255, blank=True, null=True)
    subdivision = models.CharField(max_length=255, blank=True, null=True)
    whyout = models.CharField(max_length=255, blank=True, null=True)
    numberoforder = models.CharField(max_length=255, blank=True, null=True)
    datestart = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    daterealend = models.DateField(blank=True, null=True)
