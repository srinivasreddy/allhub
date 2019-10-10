# flake8: NOQA

from .pull_request import PullRequestMixin, PRSort, PRDirection, PRState
from .review_comments import ReviewCommentsMixin, PRCommentsSort, PRCommentsDirection
from .review_requests import ReviewRequestsMixin
from .reviews import ReviewsMixin
from allhub.util import ConflictCheck


class PullRequestsMixin(
    PullRequestMixin,
    ReviewCommentsMixin,
    ReviewRequestsMixin,
    ReviewsMixin,
    metaclass=ConflictCheck,
):
    pass
