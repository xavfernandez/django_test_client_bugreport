# -*- coding: utf-8 -*-

from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY
from django.test import TestCase

from .models import CustomModel

class CustomTestCase(TestCase):

    def test_logout_fail(self):
        CustomModel.objects.create(username='test')
        print "Login: ", self.client.login(username='test')
        print "SESSION_KEY: ", self.client.session[SESSION_KEY]
        print "BACKEND_SESSION_KEY: ", self.client.session[BACKEND_SESSION_KEY]
        print "Logout", self.client.logout()
