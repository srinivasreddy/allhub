# flake8: NOQA
from .team_discussion_comments import (
    TeamDiscussionCommentDirection,
    TeamDiscussionCommentsMixin,
)
from .team_discussions import TeamDiscussionsMixin
from .team_members import TeamMemberRole, TeamMembersMixin
from .team_sync import TeamSyncMixin
from .teams import TeamMembersMixin
from allhub.util import ConflictCheck


class TeamsMixin(
    TeamSyncMixin,
    TeamMembersMixin,
    TeamDiscussionsMixin,
    TeamDiscussionCommentsMixin,
    metaclass=ConflictCheck,
):
    pass
