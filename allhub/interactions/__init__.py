# flake8: NOQA

from .org import OrganizationMixin
from .repo import RepoMixin
from .util import InteractionLimit
from allhub.util import ConflictCheck


class InteractionLimitsMixin(OrganizationMixin, RepoMixin, metaclass=ConflictCheck):
    pass
