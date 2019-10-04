from allhub.response import Response


class OutsideCollabMixin:
    def outside_collaborators(self, org, filter="all"):
        url = f"/orgs/{org}/outside_collaborators"
        params = {"filter": filter}
        self.response = Response(self.get(url, params=params), "OutsideCollaborators")
        return self.response.transform()

    def delete_outside_collaborator(self, org, username):
        url = f"/orgs/{org}/outside_collaborators/{username}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"delete_outside_collaborator(.....) returned {self.response.status_code}, instead of 204."
        )

    def convert_member_to_outside_collaborator(self, org, username):
        """
        When an organization member is converted to an outside collaborator, they'll only have access
        to the repositories that their current team membership allows. The user will no longer be a
        member of the organization.

        Response
        Status: 204 No Content

        Response if user is not a member of the organization
        Status: 403 Forbidden

        Response if user is the last owner of the organization
        Status: 403 Forbidden

        :param org:
        :param username:
        :return:
        """
        url = f"/orgs/{org}/outside_collaborators/{username}"
        self.response = Response(self.put(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"convert_member_to_outside_collaborator(.....) returned {self.response.status_code}, instead of 204."
        )
