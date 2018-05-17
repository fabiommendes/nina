``nina`` is a Django-based microframework that can be used to quickly create
small web applications. Nina is based on Django, but it is extremely simplified
and requires no boilerplate. The goal is to provide a nice environment for
quick projects, hackatons and teaching programming with web-based technology.

Hello World
===========

Our first application

.. code-block:: python

    # hello.py

    from nina import *

    @route('/')
    def index():
        return 'Hello World!'

From the terminal, just run:

    $ nina run hello.py


Installation instructions
=========================

nina can be installed using pip::

    $ python3 -m pip install nina

This command will fetch the archive and its dependencies from the internet and
install them.

If you cloned the repository and want to start a local development, execute::

    $ python setup.py develop

(in both cases, add the --user flag to perform a local install)


Basic concepts
==============



