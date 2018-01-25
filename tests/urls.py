# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^assert-request', views.assert_request_view),
    url(r'^assert-user', views.assert_user_view),
]
