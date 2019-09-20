# flake8: NOQA
from .app import *
from allhub.util import ConflictCheck


class Apps(AppMixin, metaclass=ConflictCheck):
    pass
