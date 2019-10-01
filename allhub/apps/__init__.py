# flake8: NOQA
from .app import *
from .events import *
from .permission import *
from allhub.util import ConflictCheck
from allhub.apps.installations import InstallationMixin


class Apps(AppMixin, InstallationMixin, metaclass=ConflictCheck):
    pass
