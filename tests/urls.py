# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url

from .views import simple_view

urlpatterns = [
    url(r'^', simple_view),
]
