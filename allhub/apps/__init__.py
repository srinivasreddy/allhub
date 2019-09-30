# flake8: NOQA
from .app import *
from .events import *
from .permission import *
from allhub.util import ConflictCheck


class Apps(AppMixin, metaclass=ConflictCheck):
    pass
