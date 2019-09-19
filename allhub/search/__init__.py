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


class SearchMixin(_SearchMixin):
    pass
