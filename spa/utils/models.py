# -*- coding: utf-8 -*-
# Django
from django.db import models


class CommonModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'created_on'
        ordering = ['-created_on']
