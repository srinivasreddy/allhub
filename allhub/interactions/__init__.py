from .org import OrganizationMixin
from .repo import RepoMixin
from allhub.util import ConflictCheck


class InteractionLimitsMixin(OrganizationMixin, RepoMixin, metaclass=ConflictCheck):
    pass
