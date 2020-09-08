# -*- coding: utf-8 -*-
# Django
from django.core.management.base import BaseCommand
# Thirth Parties & Python
# - - -
# Project
from spa.users.models import User

class Command(BaseCommand):

    help = "Create an user"

    def handle(self, *args, **options):
        username = input("Username: ")
        password = input("Password: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        is_superuser = input("Is Superuser? (y/N): ") or ""
        is_staff = input("Is Staff? (y/N): ") or ""

        is_superuser = True if is_superuser.lower() == "y" else False
        is_staff = True if is_staff.lower() == "y" else False

        new_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            is_superuser=is_superuser,
            is_staff=is_staff,
        )
        new_user.set_password(password)
        new_user.save()
