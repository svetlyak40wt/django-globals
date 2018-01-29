Django-globals
--------------

[![changelog](http://allmychanges.com/p/python/django-globals/badge)](http://allmychanges.com/p/python/django-globals/)

Django-globals is a very simple application, that allow you to define
thread specific global variables.

It includes a middleware Global, which can be used to access to
the current request and user, which is useful outside of a view when the "request" variable is not
defined.

## Installation


Install using pip

```
   pip install django_globals
```

## Configuration


In your project's `settings.py`, add `django_globals.middleware.Global` to `MIDDLEWARE`
(or `MIDDLEWARE_CLASSES` on Django < 1.10).

## Usage


Now you can use `from django_globals import globals` and access to
the `globals.request` and `globals.user` from anywhere.

## Help

For more information see the documentation at:

https://django-globals.readthedocs.io/

If you have questions or have trouble using the app please file a bug report
at:

https://github.com/svetlyak40wt/django-globals/issues
