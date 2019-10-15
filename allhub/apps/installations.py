from allhub.response import Response

_mime = ", ".join(
    [
        "application/vnd.github.machine-man-preview+json",
        "application/vnd.github.mercy-preview+json",
    ]
)


class InstallationMixin:
    def github_app_installation_repos(self, **kwargs):
        self._check_app_token()
        url = "/installation/repositories"
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _mime,
                },
                **kwargs
            ),
            "Apps",
        )
        return self.response.transform()

    def github_app_installations_for_user(self, **kwargs):
        """
        Lists installations of your GitHub App that the authenticated user has explicit permission
        (:read, :write, or :admin) to access.
        :return:
        """
        self._check_app_token()
        _mime = "application/vnd.github.machine-man-preview+json"
        url = "/user/installations"
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _mime,
                },
                **kwargs
            ),
            "Apps",
        )
        return self.response.transform()

    def repos_accessible_to_user_for_installation(self, installation_id, **kwargs):
        self._check_app_token()
        url = "/user/installations/{installation_id}/repositories".format(
            installation_id=installation_id
        )
        self.response = Response(
            self.get(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _mime,
                },
                **kwargs
            ),
            "Repositories",
        )
        return self.response.transform()

    def add_repo_to_app_installation(self, installation_id, repository_id, **kwargs):
        self._check_app_token()
        _mime = "application/vnd.github.machine-man-preview+json"
        url = "/user/installations/{installation_id}/repositories/{repository_id}".format(
            installation_id=installation_id, repository_id=repository_id
        )
        self.response = Response(
            self.put(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _mime,
                },
                **kwargs
            ),
            "",
        )
        return self.response.status_code == 204

    def remove_repo_from_app_installation(
        self, installation_id, repository_id, **kwargs
    ):
        self._check_app_token()
        _mime = "application/vnd.github.machine-man-preview+json"
        url = "/user/installations/{installation_id}/repositories/{repository_id}".format(
            installation_id=installation_id, repository_id=repository_id
        )
        self.response = Response(
            self.delete(
                url,
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _mime,
                },
                **kwargs
            ),
            "",
        )
        return self.response.status_code == 204

    def create_content_attachment(self, content_reference_id, title, body, **kwargs):
        url = "/content_references/{content_reference_id}/attachments".format(
            content_reference_id=content_reference_id
        )
        self._check_app_token()
        _mime = "application/vnd.github.corsair-preview+json"
        self.response = Response(
            self.post(
                url,
                params={"title": title, "body": body},
                **{
                    "Authorization": "Bearer {app_token}".format(
                        app_token=self.app_token
                    ),
                    "Accept": _mime,
                },
                **kwargs
            ),
            "",
        )
        return self.response.transform()
