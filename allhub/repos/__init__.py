# flake8: NOQA

from .webhooks import WebHooksMixin
from .repos import ReposMixin
from allhub.util import ConflictCheck


class RepositoryMixin(ReposMixin, WebHooksMixin, metaclass=ConflictCheck):
    pass
