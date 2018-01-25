from django_globals import globals

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)
