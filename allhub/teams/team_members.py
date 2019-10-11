from enum import Enum
from allhub.response import Response

_mime = "application/vnd.github.hellcat-preview+json"


class TeamMemberRole(Enum):
    MEMBER = "member"
    MAINTAINER = "maintainer"
    ALL = "all"


# NOTE: Not covering the deprecated APIs for team membership(s)


class TeamMembersMixin:
    def team_members(self, team_id, role=TeamMemberRole.ALL):
        url = f"/teams/{team_id}/members"
        self.response = Response(
            self.get(url, params={"role": role.value}, **{"Accept": _mime}),
            "TeamMembers",
        )
        return self.response.transform()

    def team_membership(self, team_id, username):
        url = f"/teams/{team_id}/memberships/{username}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamMembership")
        return self.response.transform()

    def add_update_team_membership(self, team_id, username, role=TeamMemberRole.MEMBER):
        url = f"/teams/{team_id}/memberships/{username}"
        self.response = Response(
            self.put(url, params={"role": role.value}, **{"Accept": _mime}),
            "TeamMembership",
        )
        return self.response.transform()

    def delete_team_membership(self, team_id, username):
        url = f"/teams/{team_id}/memberships/{username}"
        self.response = Response(
            self.delete(url, **{"Accept": _mime}), "TeamMembership"
        )
        return self.response.status_code == 204

    def pending_team_invitations(self, team_id):
        _mime = "application/vnd.github.dazzler-preview+json"
        url = f"/teams/{team_id}/invitations"
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamInvitations")
        return self.response.transform()
