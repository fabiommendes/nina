import sys
import copy
from sidekick import property, delegate_to, placeholder as _

from .router import Router

LAST_APP = None


class App:
    """
    Represents a Django application.
    """

    urls = delegate_to('router')
    route = delegate_to('router')

    def __init__(self, name=None, path=None):
        if name is None:
            self.name = sys._getframe(2).f_globals['__name__']
        self.router = Router()
        self.path = path
        set_last_app(self)


def last_app():
    """
    Return the lastly created app instance.
    """
    return LAST_APP


def set_last_app(app):
    """
    Register the last app.
    """
    global LAST_APP
    LAST_APP = app


# Global app instance
default_app = App(__name__)
route = default_app.route
