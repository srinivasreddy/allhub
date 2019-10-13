from allhub.response import Response
from enum import Enum


class ProjectState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    ALL = "all"


_project_accept_header = "application/vnd.github.inertia-preview+json"


class ProjectMixin:
    def repo_projects(self, owner, repo, state=ProjectState.OPEN):
        url = "/repos/{owner}/{repo}/projects".format(owner=owner, repo=repo)
        params = [("state", state.value)]
        self.response = Response(
            self.get(url, params=params, **{"Accept": _project_accept_header}),
            "RepoProjects",
        )

        return self.response.transform()

    def org_projects(self, org, state=ProjectState.OPEN):
        url = "/orgs/{org}/projects".format(org=org)
        params = [("state", state.value)]
        self.response = Response(
            self.get(url, params=params, **{"Accept": _project_accept_header}),
            "OrgProjects",
        )
        return self.response.transform()

    def user_projects(self, username, state=ProjectState.OPEN):
        url = "/users/{username}/projects".format(username=username)
        params = [("state", state.value)]
        self.response = Response(
            self.get(url, params=params, **{"Accept": _project_accept_header}),
            "UserProjects",
        )
        return self.response.transform()

    def project(self, project_id):
        url = "/projects/{project_id}".format(project_id=project_id)
        self.response = Response(
            self.get(url, **{"Accept": _project_accept_header}), "Project"
        )
        return self.response.transform()

    def create_owner_project(self, owner, repo, name, body=None):
        url = "/repos/{owner}/{repo}/projects".format(owner=owner, repo=repo)
        params = [("name", name), ("body", body)]
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "Project",
        )
        return self.response.transform()

    def create_org_project(self, org, name, body=None):
        url = "/orgs/{org}/projects".format(org=org)
        params = [("name", name), ("body", body)]
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "OrgProject",
        )
        return self.response.transform()

    def create_user_project(self, name, body=None):
        url = "/user/projects"
        params = [("name", name), ("body", body)]
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "UserProject",
        )
        return self.response.transform()

    def update_project(
        self, project_id, name, body, state, organization_permission, private
    ):
        assert state in ("open", "closed")
        assert isinstance(private, bool)
        assert organization_permission in ("read", "write", "admin", "none")
        url = "/projects/{project_id}".format(project_id=project_id)
        params = [
            ("name", name),
            ("body", body),
            ("state", state),
            ("organization_permission", organization_permission),
            ("private", private),
        ]
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _project_accept_header}),
            "Project",
        )
        return self.response.transform()

    def delete_project(self, project_id):
        url = "/projects/{project_id}".format(project_id=project_id)
        self.response = Response(
            self.delete(url, **{"Accept": _project_accept_header}), "Project"
        )
        return self.response.status_code == 204
