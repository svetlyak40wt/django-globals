import threading
globals = threading.local()


# Setting placeholders for `request` and `user`
# globals to allow calling them outside Django
# context or w/o globals middleware.
if not hasattr(globals, 'request'):
    globals.request = None
    globals.user = None

    globals.get_current_user = get_current_user
