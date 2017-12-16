#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

from django_globals import globals

User = get_user_model()


class TestMiddleware(TestCase):

    def test_request(self):
        self.client.get("/?foo=bar")

        self.assertEqual(dict(globals.request.GET.dict()), {"foo": "bar"})

    def test_user(self):
        user = User.objects.create_user(username='testuser', email='user@example.com', password='top_secret')
        self.client.login(username='testuser', password='top_secret')

        self.client.get("/?foo=bar")
        self.assertEqual(globals.user, user)
