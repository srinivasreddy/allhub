# flake8: NOQA
from .app import AppMixin

# from .events import *
from .permission import AppPermission
from allhub.util import ConflictCheck

from allhub.apps.installations import InstallationMixin


class AppsMixin(AppMixin, InstallationMixin, metaclass=ConflictCheck):
    pass
