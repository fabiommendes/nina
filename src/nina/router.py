class Route:
    """
    Represents a route.

    Route is a view + url + optional transformations to the view function.
    """

    def __init__(self, view, path, login=False, perms=None, regex=False):
        self.path = path
        self.view = view

    def as_path(self):
        """
        Return path as a Django path.
        """
        raise NotImplementedError

    def view_function(self):
        """
        Return view as a Django-compatible view function.
        """
        return self.view


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
            route = Route(path, func, **kwargs)
            self.routes.append(route)
            func.nina_route = route
            return func

        return decorator
