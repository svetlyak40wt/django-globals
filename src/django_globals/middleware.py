from django_globals import globals

class Global(object):
    def process_request(self, request):
        globals.request = request
        if hasattr(request, 'user'):
            globals.user = request.user

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
