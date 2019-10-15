from allhub.response import Response
from .permission import AppPermission

_app_mime_type = "application/vnd.github.machine-man-preview+json"


class AppMixin:
    def app(self, app_slug, **kwargs):
        """Get a single GitHub App"""
        url = "/apps/{app_slug}".format(app_slug=app_slug)
        self.response = Response(
            self.get(url, **{"Accept": _app_mime_type}, **kwargs), "App"
        )
        return self.response.transform()

    def auth_app(self, **kwargs):
        """Get the authenticated GitHub App"""
        self._check_app_token(self)
        url = "/app"
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "App",
        )
        return self.response.transform()

    def app_installations(self, **kwargs):
        self._check_app_token(self)
        url = "/app/installations"
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "App",
        )
        return self.response.transform()

    def app_installtion(self, installation_id, **kwargs):
        self._check_app_token(self)
        url = "/app/installations/{installation_id}".format(
            installation_id=installation_id
        )
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "App",
        )
        return self.response.transform()

    def delete_app_installtion(self, installation_id, **kwargs):
        """Uninstalls a GitHub App on a user, organization, or business account."""
        self._check_app_token(self)
        url = "/app/installations/{installation_id}".format(
            installation_id=installation_id
        )
        self.response = Response(
            self.delete(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "App",
        )
        return self.response.transform()

    def create_app_access_token(
        self, installation_id, repository_ids, permissions, **kwargs
    ):
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
            self.post(url, params=params, **{"Accept": _app_mime_type}, **kwargs),
            "Token",
        )
        return self.response.transform()

    def org_installation(self, org, **kwargs):
        self._check_app_token(self)
        url = "/orgs/{org}/installation".format(org=org)
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "OrgInstallation",
        )
        return self.response.transform()

    def repo_installation(self, owner, repo, **kwargs):
        self._check_app_token(self)
        url = "/repos/{owner}/{repo}/installation".format(owner=owner, repo=repo)
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "RepoInstallation",
        )
        return self.response.transform()

    def user_installation(self, username, **kwargs):
        self._check_app_token(self)
        url = "/users/{username}/installation".format(username=username)
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _app_mime_type,
                },
                **kwargs
            ),
            "UserInstallation",
        )
        return self.response.transform()

    def create_github_app_from_manifest(self, code, **kwargs):
        url = "/app-manifests/{code}/conversions".format(code=code)
        self.response = Response(
            self.post(
                url, **{"Accept": "application/vnd.github.fury-preview+json"}, **kwargs
            ),
            "App",
        )
        return self.response.transform()
