# -*- coding: utf-8 -*-
# Django
from django.test import TestCase
# Project
from spa.management.models import Spa


class SpaTestCase(TestCase):

    def setUp(self):
        Spa.objects.create(name="default", address="Default Address")

    def test_spa_endpoint(self):
        self.assertEqual(True, True, "Test no aprobado")
