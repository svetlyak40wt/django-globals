from django_globals import globals

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    # Works perfectly for everyone using MIDDLEWARE_CLASSES
    MiddlewareMixin = object


class Global(MiddlewareMixin):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)

    def process_response(self, request, response):
        # check for attribute before deleting because in some cases (eg Django<1.10-style MIDDLEWARE_CLASSES)
        # process_request may not have been called.
        if hasattr(globals, 'request'):
            del globals.request

        if hasattr(globals, 'user'):
            del globals.user

        return response
