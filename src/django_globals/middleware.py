from django_globals import globals

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)

    def process_response(self, request, response):
        del globals.request
        del globals.user
        return response

# retrocompatibility
class User(Global):
    def __init__(self, *args, **kwargs):
        import warnings
        warnings.warn(
            'The `django_globals.middleware.User` middleware is deprecated, you should use `django_globals.middleware.Global`',
            DeprecationWarning,
            stacklevel=2
        )
        super(User, self).__init__(*args, **kwargs)
