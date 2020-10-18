# -*- coding: utf-8 -*-
# Django
from django.urls import path
# Project
from spa.management.views.spas import SpaListView, SpaCreateView


urlpatterns = [
    path("", SpaListView.as_view(), name="spa_list"),
    path("spa/create/", SpaCreateView.as_view(), name="spa_create")
]
