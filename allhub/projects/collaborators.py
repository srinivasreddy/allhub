from allhub.response import Response
from enum import Enum

_project_accept_header = "application/vnd.github.inertia-preview+json"


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
        url = f"/projects/{project_id}/collaborators"
        params = [("collaborators", collaborators.value)]
        self.response = Response(
            self.get(url, params=params, **{"Accept": _project_accept_header}),
            "Collaborators",
        )

        return self.response.transform()

    def review_permission_level(self, project_id, username):
        url = f"/projects/{project_id}/collaborators/{username}/permission"
        self.response = Response(
            self.get(url, **{"Accept": _project_accept_header}), "Permission"
        )

        return self.response.transform()

    def add_user_collaborator(self, project_id, username, permission=Permission.WRITE):
        url = f"/projects/{project_id}/collaborators/{username}"
        params = [("permission", permission.value)]
        self.response = Response(
            self.put(url, params=params, **{"Accept": _project_accept_header}), ""
        )

        return self.response.status_code == 204

    def delete_user_collaborator(self, project_id, username):
        url = f"/projects/{project_id}/collaborators/{username}"
        self.response = Response(
            self.delete(url, **{"Accept": _project_accept_header}), ""
        )

        return self.response.status_code == 204
