import threading
globals = threading.local()


def get_current_user():
    """
    Lazy request.user getter method.
    """
    return getattr(globals.request, 'user', None)

# Setting placeholders for `request` and `user`
# globals to allow calling them outside Django
# context or w/o globals middleware.
if not hasattr(globals, 'request'):
    globals.request = None
    globals.user = None
