from allhub.response import Response


class InvitationMixin:
    def invitations(self, owner, repo):
        url = "/repos/{owner}/{repo}/invitations".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "Invitations")
        return self.response.transform()

    def delete_invitation(self, owner, repo, invitation_id):
        url = "/repos/{owner}/{repo}/invitations/{invitation_id}".format(
            owner=owner, repo=repo, invitation_id=invitation_id
        )
        self.response = Response(self.get(url), "")
        return self.response.status_code == 204

    def update_invitation(self, owner, repo, invitation_id, permissions):
        url = "/repos/{owner}/{repo}/invitations/{invitation_id}".format(
            owner=owner, repo=repo, invitation_id=invitation_id
        )
        self.response = Response(
            self.patch(url, params={"permissions": permissions}), "Invitations"
        )
        return self.response.transform()

    def user_repository_invitations(self):
        url = "/user/repository_invitations"
        self.response = Response(self.get(url), "Invitations")
        return self.response.transform()

    def accept_repository_invitations(self, invitation_id):
        url = "/user/repository_invitations/{invitation_id}".format(
            invitation_id=invitation_id
        )
        self.response = Response(self.patch(url), "Invitations")
        return self.response.transform()

    def decline_repository_invitations(self, invitation_id):
        url = "/user/repository_invitations/{invitation_id}".format(
            invitation_id=invitation_id
        )
        self.response = Response(self.delete(url), "Invitations")
        return self.response.status_code == 204
