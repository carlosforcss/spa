# -*- coding: utf-8 -*-
# Django
from django.shortcuts import render


def login(request):
    context = {}
    return render(request, "users/login.html", context)
