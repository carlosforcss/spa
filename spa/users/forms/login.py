# -*- coding: utf-8 -*-
# Django
from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
# Python & Thirth Parties
# - - -
# Project
from spa.users.models import User
from spa.utils.widgets import TextWidget


class LoginForm(forms.Form):

    username = forms.CharField(max_length=16, widget=TextWidget(is_password=True))
    password = forms.CharField(widget=TextWidget)

    def clean(self):
        data = super(LoginForm, self).clean()
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Wrong username or password")

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong username or password")

        return data

    def get_user(self):
        user = get_object_or_404(User, username=self.cleaned_data.get("username"))
        return user

