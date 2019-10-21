from allhub.response import Response
from enum import Enum

_accept_header = {"Accept": "application/vnd.github.inertia-preview+json"}


class Collaborators(Enum):
    OUTSIDE = "outside"
    DIRECT = "direct"
    ALL = "all"


class Permission(Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"


class CollaboratorsMixin:
    def project_collaborators(self, project_id, collaborators=Collaborators.ALL):
        """
        Lists the collaborators for an organization project.
        """
        url = "/projects/{project_id}/collaborators".format(project_id=project_id)
        params = {"collaborators": collaborators.value}
        self.response = Response(
            self.get(url, params=params, **_accept_header), "Collaborators"
        )

        return self.response.transform()

    def review_permission_level(self, project_id, username):
        url = "/projects/{project_id}/collaborators/{username}/permission".format(
            project_id=project_id, username=username
        )
        self.response = Response(self.get(url, **_accept_header), "Permission")

        return self.response.transform()

    def add_user_collaborator(self, project_id, username, permission=Permission.WRITE):
        url = "/projects/{project_id}/collaborators/{username}".format(
            project_id=project_id, username=username
        )
        params = {"permission": permission.value}
        self.response = Response(self.put(url, params=params, **_accept_header), "")

        return self.response.status_code == 204

    def delete_user_collaborator(self, project_id, username):
        url = "/projects/{project_id}/collaborators/{username}".format(
            project_id=project_id, username=username
        )
        self.response = Response(self.delete(url, **_accept_header), "")

        return self.response.status_code == 204
