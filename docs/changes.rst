Changelog
=========

0.3.1
-----

* Bugfix for 0.3.0 - handle AttributeError due to short-circuiting behaviour of old-style middleware

0.3.0
-----

* Add support for new Django ``MIDDLEWARE`` setting introduced in Django 1.10.
* Invalidate global variables ``request`` and ``response`` at the end of the
  request/response cycle.
* Removed deprecated ``django_globals.middleware.User``. Use
  ``django_globals.middleware.Global`` instead.

0.2.1
-----

* A special code was added to send ReST version of readme to pypi.

0.2.0
-----

* The middleware now save the user AND the request.
* The ``django_globals.middleware.User`` middleware is replaced by the
  ``django_globals.middleware.Global`` (but it's kept for retro-compatibility with
  a deprecation warning)

0.1.0
-----

* First public release.
