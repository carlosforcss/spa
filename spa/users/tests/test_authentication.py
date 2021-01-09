# -*- coding: utf-8 -*-
# Django
from django.test import TestCase
from django.test import Client
# Project
from spa.users.models import User


class LoginTestCase(TestCase):

    client = None

    def setUp(self):
        User.objects.create_user(
            username="root",
            password="root",
            first_name="Carlos",
            last_name="Sanchez",
            email="me@test.com",
            phone="421 232 23 12",
            is_staff=True,
            is_superuser=True,
        )
        self.client = Client()

    def test_right_credentials(self):
        response = self.client.post("/get_token/", data=dict(username="root", password="root"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data.get('token'))

    def test_wrong_credentials(self):
        response = self.client.post("/get_token/", data=dict(username="root", password="wrong"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('token'), None)


class SingUpTestCase(TestCase):

    default_data = {}
    client = Client()

    def setUp(self):
        self.default_data = dict(
            username="root",
            first_name="Carlos",
            last_name="Sanchez",
            email="me@test.com",
            phone="614 234 21 23",
        )

    def test_create_user(self):
        response = self.client.post("/sing_up/", data=self.default_data)
        new_user = User.objects.filter(**self.default_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(new_user.exists())

    def test_worse_data(self):
        User.objects.create_user(**self.default_data)
        response = self.client.post("/sing_up/", data=self.default_data)
        self.assertEqual(response.status_code, 400)
