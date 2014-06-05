# -*- coding: utf-8 -*-

from django.contrib.auth.backends import ModelBackend

from .models import CustomModel


class CustomModelBackend(ModelBackend):

    def authenticate(self, username=None):
        try:
            return CustomModel.objects.get(username=username)
        except CustomModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomModel.objects.get(pk=user_id)
        except CustomModel.DoesNotExist:
            return None
