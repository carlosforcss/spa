# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework.serializers import ModelSerializer
# Project
from spa.management.models import Spa


class SpaSerializer(ModelSerializer):

    class Meta:
        model = Spa
        fields = ("id", "name", "address")