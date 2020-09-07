# -*- coding: utf-8 -*-
# Django
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
# Python & Thirth Parties
# - - -
# Spa
# - - -


class User(AbstractBaseUser):
    USERNAME_FIELD = "username"

    username = models.CharField(max_length=16, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=31, help_text="Contact phone number")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return u"{} {}".format(self.first_name, self.last_name)
