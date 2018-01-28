# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestMiddleware(TestCase):
    """
    Since the middleware doesn't preserve its contents after the request
    we rely on views to perform the assertions
    """

    def test_request(self):
        response = self.client.get("/assert-request")

        self.assertEqual(response.status_code, 200)

    def test_anon_user(self):
        self.client.logout()

        response = self.client.get("/assert-user")

        self.assertEqual(response.status_code, 200)

    def test_user(self):
        user = User.objects.create_user(username='testuser', email='user@example.com', password='top_secret')
        self.client.login(username='testuser', password='top_secret')

        response = self.client.get("/assert-user")

        self.assertEqual(response.status_code, 200)
