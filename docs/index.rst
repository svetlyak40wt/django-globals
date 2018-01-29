Django Globals - Thread specific global variables
=================================================

Django-globals is a very simple application, that allow you to define
thread specific global variables.

It includes a middleware Global, which can be used to access to
the current request and user, which is useful outside of a view when the "request" variable is not
defined.

Installation
------------

Install using pip::

   pip install django_globals


Configuration
-------------

In your project's ``settings.py``, add ``django_globals.middleware.Global`` to ``MIDDLEWARE``
(or ``MIDDLEWARE_CLASSES`` on Django < 1.10).  eg::

   MIDDLEWARE = (
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',

       'django_globals.middleware.Global',
   )


Usage
-----

Now you can use ``from django_globals import globals`` and access to
the ``globals.request`` and ``globals.user`` from anywhere.


.. toctree::
   :maxdepth: 2

   changes



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
