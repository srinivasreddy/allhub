from allhub.response import Response


class InvitationMixin:
    def invitations(self, owner, repo):
        url = f"/repos/{owner}/{repo}/invitations"
        self.response = Response(self.get(url), "Invitations")
        return self.response.transform()

    def delete_invitation(self, owner, repo, invitation_id):
        url = f"/repos/{owner}/{repo}/invitations/{invitation_id}"
        self.response = Response(self.get(url), "")
        return self.response.status_code == 204

    def update_invitation(self, owner, repo, invitation_id, permissions):
        url = f"/repos/{owner}/{repo}/invitations/{invitation_id}"
        self.response = Response(
            self.patch(url, params={"permissions": permissions}), "Invitations"
        )
        return self.response.transform()

    def user_repository_invitations(self):
        url = f"/user/repository_invitations"
        self.response = Response(self.get(url), "Invitations")
        return self.response.transform()

    def accept_repository_invitations(self, invitation_id):
        url = f"/user/repository_invitations/{invitation_id}"
        self.response = Response(self.patch(url), "Invitations")
        return self.response.transform()

    def decline_repository_invitations(self, invitation_id):
        url = f"/user/repository_invitations/{invitation_id}"
        self.response = Response(self.delete(url), "Invitations")
        return self.response.status_code == 204
