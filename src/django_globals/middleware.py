from django_globals import globals

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)

    def process_response(self, request, response):
        del globals.request
        del globals.user
        return response
