# flake8: NOQA

from .branches import BranchMixin
from .webhooks import WebHooksMixin
from .repos import ReposMixin
from .traffic import TrafficMixin
from .statuses import StatusMixin
from .downloads import DownloadMixin
from .deploy_keys import DeployKeysMixin
from .forks import ForkMixin
from .deployments import DeploymentMixin
from .contents import ContentsMixin
from allhub.util import ConflictCheck


class RepositoryMixin(
    BranchMixin,
    ContentsMixin,
    DeploymentMixin,
    DeployKeysMixin,
    ReposMixin,
    ForkMixin,
    TrafficMixin,
    StatusMixin,
    WebHooksMixin,
    DownloadMixin,
    metaclass=ConflictCheck,
):
    pass
