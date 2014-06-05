# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import models as auth_models


class CustomModel(auth_models.AbstractBaseUser, models.Model):

    USERNAME_FIELD = 'username'

    username = models.CharField('username', max_length=64)

