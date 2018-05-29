import importlib
import os
import sys
from collections import namedtuple

from django.urls import path, include
from django.core.management import ManagementUtility
from sidekick import lazy

from .configuration import NinaConf

NINA_CONF_MODULE = 'nina.global_mods.settings'
NINA_URLS = 'nina.global_mods.urls'
LAST_PROJECT = None

MountedApp = namedtuple('MountedApp', ['app', 'path'])


class Project:
    """
    Instances represent Django projects.
    """

    @lazy
    def settings(self):
        mod = importlib.import_module(NINA_CONF_MODULE)
        conf = NinaConf(self, **extra_config(self))
        mod.__dict__.update(conf.get_settings())
        return mod

    @property
    def urls(self):
        urls = []
        for app, path_ in self.apps:
            if path_ is None:
                urls.extend(app.urls)
            else:
                urls.append(path(path_, include(apps.url)))
        return urls

    def __init__(self):
        self.apps = []
        set_last_project(self)

    def init_project(self):
        """
        Project initialization.
        """
        os.environ['DJANGO_SETTINGS_MODULE'] = NINA_CONF_MODULE
        sys.modules[NINA_CONF_MODULE] = self.settings
        self.init_urls_module()

    def init_urls_module(self):
        mod = importlib.import_module(NINA_URLS)
        mod.urlpatterns[:] = self.urls
        return mod

    def run(self):
        """
        Runs project.
        """
        self.run_command('runserver')

    def run_command(self, command, *args, **kwargs):
        """
        Runs a Django command.
        """
        self.init_project()
        argv = ['nina cmd', command, *map(str, args), *to_argv(**kwargs)]
        utility = ManagementUtility(argv)
        utility.execute()

    def mount(self, app, path=None):
        """
        Mounts app inside project.
        """
        self.apps.append(MountedApp(app, path))

def to_argv(**kwargs):
    args = []
    for k, v in kwargs:
        k = k.replace('_', '-')
        if not k.startswith('-'):
            k = '--' + k
        args.extend([k, str(v)])
    return args


# Last project
def last_project():
    """
    Return the lastly created project.
    """
    return LAST_PROJECT


def set_last_project(project):
    """
    Sets the last project.
    """
    global LAST_PROJECT
    LAST_PROJECT = project


def extra_config(project):
    return {
        'root_urlconf': NINA_URLS,
    }


# Global project instance
project = Project()
run = project.run
