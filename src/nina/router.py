from nina.global_mods.urls import urlpatterns
from django.urls import path
from django.http import HttpResponse

class Route:
    """
    Represents a route.

    Route is a view + url + optional transformations to the view function.
    """

    def __init__(self, view, path, login=False, perms=None, regex=False):
        self.path = path
        self.view = view

    def as_path(self):
        return path(self.path, self.view_function())

    def view_function(self):
        """
        Return view as a Django-compatible view function.
        """
        def compatible_view(request, *args, **kwargs):
            result = self.view(*args, **kwargs)
            return HttpResponse(result)

        return compatible_view


class Router:
    """
    A router aggregates several routes.
    """

    @property
    def urls(self):
        return [route.as_path() for route in self.routes]

    def __init__(self):
        self.routes = []

    def route(self, path, **kwargs):
        """
        Decorator that creates a route from a view function.
        """

        def decorator(func):
            route = Route(func, path, **kwargs)
            self.routes.append(route)
            func.nina_route = route
            return func

        return decorator
