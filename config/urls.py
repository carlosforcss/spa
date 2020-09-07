# -*- coding: utf-8 -*-
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# Project
from spa.users.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
