# flake8: NOQA

from .webhooks import WebHooksMixin
from .repos import ReposMixin
from .traffic import TrafficMixin
from .statuses import StatusMixin
from allhub.util import ConflictCheck


class RepositoryMixin(
    ReposMixin, TrafficMixin, StatusMixin, WebHooksMixin, metaclass=ConflictCheck
):
    pass
