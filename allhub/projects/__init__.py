# flake8: NOQA

from .project import ProjectState, ProjectMixin as _ProjectMixin
from .cards import *
from .collaborators import *
from .columns import *

from allhub.util import ConflictCheck


class ProjectsMixin(
    _ProjectMixin, CardsMixin, CollaboratorsMixin, ColumnsMixin, metaclass=ConflictCheck
):
    pass
