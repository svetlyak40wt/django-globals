from django_globals import globals

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)

    @staticmethod
    def get_user():
        if hasattr(globals, 'user'):
            return globals.user

    @staticmethod
    def get_request():
        if hasattr(globals, 'request'):
            return globals.request

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
