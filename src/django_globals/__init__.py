import threading


class DjangoGlobal(threading.local):
    user = None
    request = None

    def __init__(self, *args, **kwargs):
        super(DjangoGlobal, self).__init__(*args, **kwargs)


globals = DjangoGlobal()
