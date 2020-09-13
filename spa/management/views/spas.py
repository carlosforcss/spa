# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Project
from spa.management.models import Spa
from spa.management.forms import SpaForm


class SpaListView( LoginRequiredMixin, ListView):

    model = Spa
    form = SpaForm
    template_name = "management/spa/list.html"
