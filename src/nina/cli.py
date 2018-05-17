import click
from sidekick import import_later

last_app = import_later('nina.app:last_app')


@click.group()
def main():
    pass


@main.command()
@click.argument('file', type=click.Path())
def run(file):
    """
    Runs the given nina app.
    """
    import nina

    with open(file) as F:
        source = F.read()
    mod = compile(source, file, 'exec')
    exec(mod, {})

    nina.project.mount(last_app())
    nina.project.run()


if __name__ == '__main__':
    main()
