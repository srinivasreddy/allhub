# flake8: NOQA
from .search import (
    Order,
    LabelSort,
    CodeSort,
    CommitSort,
    IssueSort,
    RepoSort,
    UserSort,
    SearchMixin as _SearchMixin,
)

from allhub.util import ConflictCheck


class SearchMixin(_SearchMixin, metaclass=ConflictCheck):
    pass
