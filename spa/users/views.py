# -*- coding: utf-8 -*-
# Django
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth import login
# Python & Thirth Parties
# - - -
# Project
from spa.users.forms import LoginForm


class LoginView(View):

    template = "users/login.html"
    form_class= LoginForm

    def get_context(self, request):
        context : dict = {"form": self.form_class()}
        if request.POST:
            context["form"] = self.form_class(request.POST)
        return context

    def get(self, request):
        context : dict = self.get_context(request)
        return render(request, self.template, context)

    def post(self, request):
        context = self.get_context(request)
        form = context.get('form')
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template, context)
