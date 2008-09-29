Django-globals
--------------

Django-globals, is a very simple application, that allow to define
a thread specific global variables.

Also, it includes a middleware User, which can be used, to access to
the current user outside a view, when "request" variable is not
defined.

Installation
------------

Download sources, add place `django_globals` somewhere in yours python path.

Next, add `django_globals` to the INSTALLED_APPS and, optionally,
`django_globals.middleware.User` to the MIDDLEWARE_CLASSES.

Now you can make `from django_globals import globals` and access to
the `globals.user` anywhere.
