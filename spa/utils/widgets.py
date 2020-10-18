# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django
from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe
# Python & Third Parties
from abc import abstractmethod


class SimpleCustomWidget(Widget):

    template_name : str = None

    def __init__(self, *args, **kwargs):
        if not self.template_name:
            raise Exception("You have to define template_name value")
        super(SimpleCustomWidget, self).__init__(*args, **kwargs)

    @abstractmethod
    def get_context(self, name, value, attrs):
        return {
            'widget': {
                'name': name,
                'is_hidden': self.is_hidden,
                'required': self.is_required,
                'value': self.format_value(value),
                'attrs': self.build_attrs(self.attrs, attrs),
                'template_name': self.template_name,
            },
        }

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)


class TextWidget(SimpleCustomWidget):

    template_name = "utils/widgets/text_widget.html"
    is_password = False

    def __init__(self, *args, **kwargs):
        self.is_password = kwargs.pop("is_password", False)
        super(TextWidget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super(TextWidget, self).get_context(name, value, attrs)
        context["widget"]["is_password"] = self.is_password
        return context
