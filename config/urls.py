# -*- coding: utf-8 -*-
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# Third Parties
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
# Project
from spa.users.views import LoginView, sing_up
from spa.management.views import SpaViewSet


router = routers.DefaultRouter()
router.register("spa", SpaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view()),
    path("api/", include(router.urls)),
    path("get_token/", auth_views.obtain_auth_token),
    path("sing_up/", sing_up),
    path("", include(("spa.management.urls", "spa.management"), namespace="management")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
