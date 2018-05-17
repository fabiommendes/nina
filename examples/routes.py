from nina import *


@route('/')
def index():
    return 'Hello World!'


@route('<name>/')
def hello_name(name):
    return 'Hello %s!' % name
