"""Useful functions that can be reused by different applications."""

import django.http
from django.core.urlresolvers import reverse


def check_auth(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return django.http.HttpResponseRedirect(reverse('admin:index'))
        return func(request, *args, **kwargs)
    return wrapper


def check_sadmin(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return django.http.HttpResponseForbidden(
                "Only superuser can access this url!")
        return func(request, *args, **kwargs)
    return wrapper
