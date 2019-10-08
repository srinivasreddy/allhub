from allhub.response import Response

_mime = "application/vnd.github.hellcat-preview+json"


class CollaboratorsMixin:
    def repo_collaborators(self, owner, repo, affiliation="all"):
        url = f"/repos/{owner}/{repo}/collaborators"
        self.response = Response(
            self.get(url, params={"affiliation": affiliation}, **{"Accept": _mime}),
            "Collaborators",
        )
        return self.response.transform()

    def is_collaborator(self, owner, repo, username):
        url = f"/repos/{owner}/{repo}/collaborators/{username}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204

    def user_permission(self, owner, repo, username):
        url = f"/repos/{owner}/{repo}/collaborators/{username}/permission"
        self.response = Response(self.get(url, **{"Accept": _mime}), "")
        return self.response.transform()

    def add_user_as_collaborator(self, owner, repo, username, permission):
        url = f"/repos/{owner}/{repo}/collaborators/{username}"
        self.response = Response(
            self.put(url, params={"permission": permission}, **{"Accept": _mime}),
            "User",
        )

    def remove_user_as_collaborator(self, owner, repo, username):
        url = f"/repos/{owner}/{repo}/collaborators/{username}"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "User")
        return self.response.status_code == 204
