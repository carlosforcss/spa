# -*- coding: utf-8 -*-
# Django
# - - -
# Third Paties
from rest_framework import serializers
# Project
from spa.users.models import User


class SingUpSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate(data):
        return data

    @staticmethod
    def create(validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone"
        )
