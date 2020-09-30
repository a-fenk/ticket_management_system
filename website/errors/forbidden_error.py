from django.http import HttpResponseForbidden

default_message = '403. Sorry, You Are Not Allowed to Access This Page.'


def raise_403(custom_message=None):
    return HttpResponseForbidden(custom_message or default_message)
