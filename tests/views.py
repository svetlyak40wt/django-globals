from django.http import HttpResponse

from django_globals import globals


def assert_request_view(request):
    """
    View that asserts that the request object is accessible via globals
    :param request:
    :return:
    """
    if globals.request != request:
        raise Exception("Expected request object in globals.request")

    return HttpResponse("<html></html>")


def assert_user_view(request):
    """
    View that asserts that the user object is accessible via globals
    :param request:
    :return:
    """
    if globals.user != request.user:
        raise Exception("Expected user object in globals.user")

    return HttpResponse("<html></html>")
