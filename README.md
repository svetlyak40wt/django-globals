Django-globals
--------------

[![changelog](http://allmychanges.com/p/python/django-globals/badge)](http://allmychanges.com/p/python/django-globals/)

Django-globals, is a very simple application, that allow to define
a thread specific global variables.

Also, it includes a middleware Global, which can be used, to access to
the current request and user outside a view, when "request" variable is not
defined.

Installation
------------

Install `django_globals` using pip.

Next, add `django_globals` to the INSTALLED_APPS and
`django_globals.middleware.Global` to the `MIDDLEWARE` setting.

Now you can make `from django_globals import globals` and access to
the `globals.request` and `globals.user` from anywhere.
