from nina import *

from django.db import models
from django.conf import settings


class ModelMeta(type(models.Model)):
    def __prepare__(self, *args):
        from django.db import models

        names = vars(models)
        names = {
            k: v 
            for k, v in names.items() 
            if isinstance(v, type) and issubclass(v, models.Field) 
        }
        return names

class Book(models.Model, metaclass=ModelMeta):
    name = CharField(max_length=200)

    class Meta:
        app_label = 'nina'


@route
def index():
    return 'Hello World!'
