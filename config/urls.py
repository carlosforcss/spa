# -*- coding: utf-8 -*-
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# Project
from spa.users.views import  LoginView
from spa.management.views.spas import SpaListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view()),
    path("", SpaListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
