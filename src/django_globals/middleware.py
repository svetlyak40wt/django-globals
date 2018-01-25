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
        del globals.request
        del globals.user
        return response
