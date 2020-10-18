# -*- coding: utf-8 -*-
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# Project
from spa.users.views import  LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view()),
    path("", include(("spa.management.urls", "spa.management"), namespace="management")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
