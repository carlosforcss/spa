# -*- coding: utf-8 -*-
# Django
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
# Python & Thirth Parties
# - - -
# Spa
from spa.utils.models import CommonModel


class User(CommonModel, AbstractBaseUser):
    USERNAME_FIELD = "username"

    username = models.CharField(max_length=16, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=31, help_text="Contact phone number")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    def has_perm(self, permission_name : str):
        if self.is_superuser or self.is_staff:
            return True
        return False

    def has_module_perms(self, module : str):
        if self.is_superuser or self.is_staff:
            return True
        return False

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return u"{} {}".format(self.first_name, self.last_name)
