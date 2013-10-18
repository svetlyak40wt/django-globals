from django_globals import globals, get_current_user

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = get_current_user()


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
