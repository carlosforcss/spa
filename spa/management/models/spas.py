# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django
from django.db import models
# Python & Third Parties
# - - -
# Project
from spa.utils.models import CommonModel


class Spa(CommonModel):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{}".format(self.name)
