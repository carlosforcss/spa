# -*- coding: utf-8 -*-
# Djangop
from django import forms
# Project
from spa.management.models import Spa
from spa.utils.widgets import TextWidget


class SpaForm(forms.ModelForm):

    class Meta:
        model = Spa

        fields = (
            "name",
            "address",
        )

        widgets = {
            "name": TextWidget(),
            "address": TextWidget(),
        }
