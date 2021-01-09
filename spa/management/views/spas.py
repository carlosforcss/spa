# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Third Parties
from rest_framework.viewsets import ModelViewSet
# Project
from spa.management.models import Spa
from spa.management.forms import SpaForm
from spa.management.serializers.spas import SpaSerializer


class SpaListView(LoginRequiredMixin, ListView):

    model = Spa
    form = SpaForm
    template_name = "management/spa/list.html"


class SpaCreateView(LoginRequiredMixin, CreateView):

    model = Spa
    form = SpaForm
    fields = ("name", "address")
    template_name = "management/spa/create.html"
    success_url = reverse_lazy('management:spa_list')


class SpaViewSet(ModelViewSet):

    queryset = Spa.objects.all()
    serializer_class = SpaSerializer
