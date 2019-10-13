from allhub.response import Response

_mime = ", ".join(
    [
        "application/vnd.github.inertia-preview+json",
        "application/vnd.github.hellcat-preview+json",
    ]
)


class TeamMembersMixin:
    def org_teams(self, org):
        url = "/orgs/{org}/teams".format(org=org)
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgTeams")
        return self.response.transform()

    def org_team(self, team_id):
        url = "/teams/{team_id}/".format(team_id=team_id)
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgTeam")
        return self.response.transform()

    def org_team_by_name(self, org, team_slug):
        url = "/orgs/{org}/teams/{team_slug}".format(org=org, team_slug=team_slug)
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgTeam")
        return self.response.transform()

    def create_team_in_org(
        self,
        org,
        name,
        description,
        maintainers,
        repo_names,
        privacy,
        permission,
        parent_team_id,
    ):
        params = {
            "name": name,
            "description": description,
            "maintainers": maintainers,
            "permission": permission,
            "privacy": privacy,
            "repo_names": repo_names,
            "parent_team_id": parent_team_id,
        }
        url = "/orgs/{org}/teams".format(org=org)
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "OrgTeam"
        )
        return self.response.transform()

    def edit_team_in_org(
        self, team_id, name, description, privacy, permission, parent_team_id
    ):
        params = {
            "name": name,
            "description": description,
            "permission": permission,
            "privacy": privacy,
            "parent_team_id": parent_team_id,
        }
        url = "/teams/{team_id}".format(team_id=team_id)
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "OrgTeam"
        )
        return self.response.transform()

    def delete_team_in_org(self, team_id):
        url = "/teams/{team_id}".format(team_id=team_id)
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204

    def child_teams_in_team(self, team_id):
        url = "/teams/{team_id}/teams".format(team_id=team_id)
        self.response = Response(self.get(url, **{"Accept": _mime}), "ChildTeams")
        return self.response.transform()

    def team_repos(self, team_id):
        url = "/teams/{team_id}/repos".format(team_id=team_id)
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamRepos")
        return self.response.transform()

    def team_manage_repo(self, owner, repo, team_id):
        url = "/teams/{team_id}/repos/{owner}/{repo}".format(
            team_id=team_id, owner=owner, repo=repo
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204

    def add_update_team_repo(self, owner, repo, team_id, permission):
        url = "/teams/{team_id}/repos/{owner}/{repo}".format(
            team_id=team_id, owner=owner, repo=repo
        )
        self.response = Response(
            self.put(url, params={"permission": permission}, **{"Accept": _mime}), ""
        )
        return self.response.status_code == 204

    def remove_team_repo(self, owner, repo, team_id):
        url = "/teams/{team_id}/repos/{owner}/{repo}".format(
            team_id=team_id, owner=owner, repo=repo
        )
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204

    def user_teams(self):
        url = "/user/teams"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Teams")
        return self.response.transform()

    def team_projects(self, team_id):
        url = "/teams/{team_id}/projects".format(team_id=team_id)
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamProjects")
        return self.response.transform()

    def review_team_project(self, team_id, project_id):
        url = "/teams/{team_id}/projects/{project_id}".format(
            team_id=team_id, project_id=project_id
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamProject")
        return self.response.transform()

    def add_update_team_project(self, team_id, project_id, permission):
        url = "/teams/{team_id}/projects/{project_id}".format(
            team_id=team_id, project_id=project_id
        )
        self.response = Response(
            self.put(
                url,
                params={"permission": permission},
                **{"Accept": _mime, "Content-Length": "0"},
            ),
            "TeamProject",
        )
        return self.response.status_code == 204

    def remove_team_project(self, team_id, project_id):
        url = "/teams/{team_id}/projects/{project_id}".format(
            team_id=team_id, project_id=project_id
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
