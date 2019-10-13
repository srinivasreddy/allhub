from allhub.response import Response
from .permission import AppPermission

_app_mime_type = "application/vnd.github.machine-man-preview+json"


class AppMixin:
    def app(self, app_slug):
        """Get a single GitHub App"""
        url = "/apps/{app_slug}".format(app_slug=app_slug)
        self.response = Response(self.get(url, **{"Accept": _app_mime_type}), "App")
        return self.response.transform()

    def auth_app(self):
        """Get the authenticated GitHub App"""
        self._app_token_check(self)
        url = "/app"
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "App",
        )
        return self.response.transform()

    def app_installations(self):
        self._app_token_check(self)
        url = "/app/installations"
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "App",
        )
        return self.response.transform()

    def app_installtion(self, installation_id):
        self._app_token_check(self)
        url = "/app/installations/{installation_id}".format(
            installation_id=installation_id
        )
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "App",
        )
        return self.response.transform()

    def delete_app_installtion(self, installation_id):
        """Uninstalls a GitHub App on a user, organization, or business account."""
        self._app_token_check(self)
        url = "/app/installations/{installation_id}".format(
            installation_id=installation_id
        )
        self.response = Response(
            self.delete(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "App",
        )
        return self.response.transform()

    def create_app_access_token(self, installation_id, repository_ids, permissions):
        """Create a new installation token"""
        assert isinstance(repository_ids, list)
        assert isinstance(permissions, AppPermission)
        for repository_id in repository_ids:
            if not isinstance(repository_id, int):
                raise ValueError("repository_ids should contain only integers.")
        params = {
            "repository_ids": repository_ids,
            "permissions": permissions.to_dict(),
        }
        url = "/app/installations/{installation_id}/access_tokens".format(
            installation_id=installation_id
        )
        self.response = Response(
            self.post(url, params=params, **{"Accept": _app_mime_type}), "Token"
        )
        return self.response.transform()

    def org_installation(self, org):
        self._app_token_check(self)
        url = "/orgs/{org}/installation".format(org=org)
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "OrgInstallation",
        )
        return self.response.transform()

    def repo_installation(self, owner, repo):
        self._app_token_check(self)
        url = "/repos/{owner}/{repo}/installation".format(owner=owner, repo=repo)
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "RepoInstallation",
        )
        return self.response.transform()

    def user_installation(self, username):
        self._app_token_check(self)
        url = "/users/{username}/installation".format(username=username)
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": f"Bearer {self.app_token}",
                    "Accept": _app_mime_type,
                },
            ),
            "UserInstallation",
        )
        return self.response.transform()

    def create_github_app_from_manifest(self, code):
        url = "/app-manifests/{code}/conversions".format(code=code)
        self.response = Response(
            self.post(url, **{"Accept": "application/vnd.github.fury-preview+json"}),
            "App",
        )
        return self.response.transform()
