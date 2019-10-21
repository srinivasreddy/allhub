from allhub.response import Response
from enum import Enum

_mime = {"Accept": "application/vnd.github.hellcat-preview+json"}


class CollabPermission(Enum):
    PULL = "pull"
    PUSH = "push"
    ADMIN = "admin"


class CollaboratorsMixin:
    def repo_collaborators(self, owner, repo, affiliation="all"):
        url = "/repos/{owner}/{repo}/collaborators".format(owner=owner, repo=repo)
        self.response = Response(
            self.get(url, params={"affiliation": affiliation}, **_mime), "Collaborators"
        )
        return self.response.transform()

    def is_collaborator(self, owner, repo, username):
        url = "/repos/{owner}/{repo}/collaborators/{username}".format(
            owner=owner, repo=repo, username=username
        )
        self.response = Response(self.get(url, **_mime), "")
        return self.response.status_code == 204

    def user_permission(self, owner, repo, username):
        url = "/repos/{owner}/{repo}/collaborators/{username}/permission".format(
            owner=owner, repo=repo, username=username
        )
        self.response = Response(self.get(url, **_mime), "")
        return self.response.transform()

    def add_user_as_collaborator(
        self, owner, repo, username, permission=CollabPermission.PUSH
    ):
        url = "/repos/{owner}/{repo}/collaborators/{username}".format(
            owner=owner, repo=repo, username=username
        )
        self.response = Response(
            self.put(url, params={"permission": permission.value}, **_mime), "User"
        )
        return self.response.transform()

    def remove_user_as_collaborator(self, owner, repo, username):
        url = "/repos/{owner}/{repo}/collaborators/{username}".format(
            owner=owner, repo=repo, username=username
        )
        self.response = Response(self.delete(url, **_mime), "User")
        return self.response.status_code == 204
