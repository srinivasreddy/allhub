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
from .invitations import InvitationMixin
from .merging import MergingMixin
from .releases import ReleaseMixin
from .statistics import StatisticsMixin
from .pages import PagesSiteMixin
from allhub.util import ConflictCheck


class RepositoryMixin(
    BranchMixin,
    ContentsMixin,
    DeploymentMixin,
    DeployKeysMixin,
    InvitationMixin,
    ReposMixin,
    ForkMixin,
    MergingMixin,
    TrafficMixin,
    StatusMixin,
    WebHooksMixin,
    DownloadMixin,
    StatisticsMixin,
    ReleaseMixin,
    PagesSiteMixin,
    metaclass=ConflictCheck,
):
    pass
