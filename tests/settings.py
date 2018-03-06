# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ei)v0lm793utcpieu%40kyi&#$#l0!(s)(^(=sw^a4tz09fhl)"

APPEND_SLASH = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",

    "django_globals",
]

SITE_ID = 1

MIDDLEWARE_CLASSES_TEMP = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django_globals.middleware.Global',
)

if django.VERSION < (1, 10, 0,):
    # old style
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES_TEMP
else:
    # new style
    MIDDLEWARE = MIDDLEWARE_CLASSES_TEMP
