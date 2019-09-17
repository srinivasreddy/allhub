# flake8: NOQA
from .gist import GistMixin as _GistMixin
from .gist_comments import GistCommentsMixin


class GistMixin(_GistMixin, GistCommentsMixin):
    pass
