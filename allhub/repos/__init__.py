# flake8: NOQA

from .branches import BranchMixin
from .webhooks import WebHooksMixin
from .repos import (
    ReposMixin,
    RepoAffiliation,
    RepoDirection,
    RepoSort,
    RepoType,
    RepoVisibility,
)
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
from .community import CommunityMixin
from .collabs import CollaboratorsMixin, CollabPermission
from .commits import CommitMixin
from .comments import CommentsMixin
from allhub.util import ConflictCheck


class RepositoryMixin(
    BranchMixin,
    CollaboratorsMixin,
    ContentsMixin,
    CommentsMixin,
    DeploymentMixin,
    DeployKeysMixin,
    InvitationMixin,
    ReposMixin,
    ForkMixin,
    MergingMixin,
    CommitMixin,
    TrafficMixin,
    StatusMixin,
    WebHooksMixin,
    DownloadMixin,
    StatisticsMixin,
    ReleaseMixin,
    CommunityMixin,
    PagesSiteMixin,
    metaclass=ConflictCheck,
):
    pass
