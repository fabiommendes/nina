import argparse
import os
import sys

import markdown as md
from markupsafe import Markup

import nina
from nina import __version__, settings

has_run = False


def run():
    """
    Starts web server.
    """

    global has_run
    has_run = True

    if len(sys.argv) == 1:
        ensure_migrations()
        return runserver()

    # Start parser
    parser = argparse.ArgumentParser('miniserver')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    parser.add_argument('command', help='Command')
    args = parser.parse_args()

    # Execute command
    if args.command == 'sync':
        from nina.manage import main
        main(['miniserver', 'makemigrations'])
        main(['miniserver', 'migrate'])
    elif args.command == 'run':
        return runserver()
    else:
        raise SystemExit('invalid command: %s' % args.command)


def markdown(data):
    return Markup(md.markdown(data))


def ensure_migrations():
    """
    Examine models and check if any migrations are necessary.
    """


def runserver():
    """
    Runs Django's runserver command.
    """

    from nina.manage import main
    main(['miniserver', 'runserver'])


def load_miniserver_app_from_file(path):
    namespace = vars(nina)
    namespace['__file__'] = os.path.abspath(path)
    namespace['__module__'] = '__main__'
    namespace['run'] = lambda: None
    settings.file = path

    with open(path) as F:
        source = F.read()
        exec(source, namespace)

    if len(sys.argv) == 2 or len(sys.argv) == 3 and sys.argv[2] == 'run':
        runserver()
    del sys.argv[0]
    run()