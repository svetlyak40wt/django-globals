from django_globals import globals

class User:
    def process_request(self, request):
        globals.user = request.user
