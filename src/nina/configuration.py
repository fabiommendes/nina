from boogie.configurations import DjangoConf, env


class NinaConf(DjangoConf):
    """
    Base class for nina configurations.
    """

    DATABASE_DEFAULT = env('sqlite:///db.sqlite3', type='db_url')

    def __init__(self, project, **kwargs):
        super().__init__(**kwargs)
        self._project = project
