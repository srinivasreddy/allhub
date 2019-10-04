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
