# flake8: NOQA

from .project import ProjectMixin as _ProjectMixin
from allhub.util import ConflictCheck


class ProjectsMixin(_ProjectMixin, metaclass=ConflictCheck):
    pass
