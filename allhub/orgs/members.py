from allhub.response import Response
from enum import Enum


class Filter(Enum):
    TWO_FA_DISABLED = "2fa_disabled"
    ALL = "all"


class Role(Enum):
    ALL = "all"
    ADMIN = "admin"
    MEMBER = "member"


class OrgMembersMixin:
    def org_members(self, org, filter=Filter.ALL, role=Role.ALL):
        """
        List all users who are members of an organization. If the authenticated user is also a member
        of this organization then both concealed and public members will be returned.
        :param org:
        :param filter:
        :param role:
        :return:
        """
        url = f"/orgs/{org}/members"
        params = {"filter": filter.value, "role": role.value}
        self.response = Response(self.get(url, params=params), "OrgMembers")
        return self.response.transform()

    def check_org_membership(self, org, username):
        """
        Check if a user is, publicly or privately, a member of the organization.

        Response if requester is an organization member and user is a member
        Status: 204 No Content

        Response if requester is an organization member and user is not a member
        Status: 404 Not Found

        Response if requester is not an organization member and is inquiring about themselves
        Status: 404 Not Found

        Response if requester is not an organization member
        Status: 302 Found

        :param org:
        :param username:
        :return:
        """
        url = f"/orgs/{org}/members/{username}"
        self.response = Response(self.get(url), "")
        if self.response.status_code == 204:
            return True
        elif self.response.status_code in (404, 302):
            return False
        raise ValueError(
            f"check_membership(.....) returned {self.response.status_code}, it should either be 204, 302 or 404."
        )

    def delete_org_member(self, org, username):
        url = f"/orgs/{org}/members/{username}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"delete_org_member(.....) returned {self.response.status_code}, it should be 204."
        )

    def public_org_members(self, org):
        url = f"/orgs/{org}/public_members"
        self.response = Response(self.get(url), "OrgPublicMembers")
        return self.response.transform()

    def check_public_membership(self, org, username):
        url = f"/orgs/{org}/public_members/{username}"
        self.response = Response(self.get(url), "OrgPublicMembers")
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        raise ValueError(
            f"check_public_membership(.....) returned {self.response.status_code}, it should be 204 or 404."
        )

    def publicize_membership(self, org):
        url = f"/orgs/{org}/public_members/{self.username}"
        self.response = Response(self.put(url, **{"Content-Length": "0"}), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"publicize_membership(.....) returned {self.response.status_code}, it should be 204."
        )

    def conceal_membership(self, org):
        url = f"/orgs/{org}/public_members/{self.username}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"conceal_membership(.....) returned {self.response.status_code}, it should be 204."
        )

    def get_org_membership(self, org, username):
        url = f"/orgs/{org}/memberships/{username}"
        self.response = Response(self.get(url), "")
        return self.response.transform()

    def add_or_update_org_membership(self, org, username, role="member"):
        url = f"/orgs/{org}/memberships/{username}"
        params = {"role": role}
        self.response = Response(self.put(url, params=params), "")
        return self.response.transform()

    def remove_org_membership(self, org, username):
        url = f"/orgs/{org}/memberships/{username}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"remove_org_membership(.....) returned {self.response.status_code}, it should be 204."
        )

    def org_invitation_teams(self, org, invitation_id):
        url = f"/orgs/{org}/invitations/{invitation_id}/teams"
        self.response = Response(
            self.get(url, **{"Accept": "application/vnd.github.dazzler-preview+json"}),
            "OrgInvitationTeams",
        )
        return self.response.transform()

    def pending_org_invitations(self, org):
        url = f"/orgs/{org}/invitations"
        self.response = Response(
            self.get(url, **{"Accept": "application/vnd.github.dazzler-preview+json"}),
            "OrgInvitations",
        )
        return self.response.transform()

    def create_org_invitation(
        self, org, team_ids, invitee_id=None, email=None, role="direct_member"
    ):
        url = f"/orgs/{org}/invitations"
        params = {}
        if invitee_id is None and email is None:
            raise ValueError("Either invitee_id or email should be provided.")
        assert isinstance(team_ids, (list, tuple))
        for team_id in team_ids:
            if not isinstance(team_id, int):
                raise ValueError("team_ids should be array of integers.")

        if invitee_id:
            params["invitee_id"] = invitee_id
        if email:
            params["email"] = email
        if team_ids:
            params["team_ids"] = team_ids
        if role:
            params["role"] = role

        self.response = Response(
            self.post(
                url,
                params=params,
                **{"Accept": "application/vnd.github.dazzler-preview+json"},
            ),
            "OrgInvitations",
        )
        return self.response.transform()

    def organization_memberships(self, state=None):
        url = "/user/memberships/orgs"
        params = {}
        if state:
            params["state"] = state
        self.response = Response(self.get(url, params=params), "OrgMemberships")
        return self.response.transform()

    def organization_membership(self, org):
        url = f"/user/memberships/orgs/{org}"
        self.response = Response(self.get(url), "OrgMembership")
        return self.response.transform()

    def edit_organization_membership(self, org, state="active"):
        url = f"/user/memberships/orgs/{org}"
        self.response = Response(
            self.patch(url, params={"state": state}), "OrgMembership"
        )
        return self.response.transform()
