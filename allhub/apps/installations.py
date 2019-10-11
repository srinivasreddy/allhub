from allhub.response import Response

_mime = ", ".join(
    [
        "application/vnd.github.machine-man-preview+json",
        "application/vnd.github.mercy-preview+json",
    ]
)


class InstallationMixin:
    def github_app_installation_repos(self):
        self._app_token_check()
        url = "/installation/repositories"
        self.response = Response(
            self.get(
                url, **{"Authorization": f"Bearer {self.app_token}", "Accept": _mime}
            ),
            "Apps",
        )
        return self.response.transform()

    def github_app_installations_for_user(self):
        """
        Lists installations of your GitHub App that the authenticated user has explicit permission
        (:read, :write, or :admin) to access.
        :return:
        """
        self._app_token_check()
        _mime = "application/vnd.github.machine-man-preview+json"
        url = "/user/installations"
        self.response = Response(
            self.get(
                url, **{"Authorization": f"Bearer {self.app_token}", "Accept": _mime}
            ),
            "Apps",
        )
        return self.response.transform()

    def repos_accessible_to_user_for_installation(self, installation_id):
        self._app_token_check()
        url = f"/user/installations/{installation_id}/repositories"
        self.response = Response(
            self.get(
                url, **{"Authorization": f"Bearer {self.app_token}", "Accept": _mime}
            ),
            "Repositories",
        )
        return self.response.transform()

    def add_repo_to_app_installation(self, installation_id, repository_id):
        self._app_token_check()
        _mime = "application/vnd.github.machine-man-preview+json"
        url = f"/user/installations/{installation_id}/repositories/{repository_id}"
        self.response = Response(
            self.put(
                url, **{"Authorization": f"Bearer {self.app_token}", "Accept": _mime}
            ),
            "",
        )
        return self.response.status_code == 204

    def remove_repo_from_app_installation(self, installation_id, repository_id):
        self._app_token_check()
        _mime = "application/vnd.github.machine-man-preview+json"
        url = f"/user/installations/{installation_id}/repositories/{repository_id}"
        self.response = Response(
            self.delete(
                url, **{"Authorization": f"Bearer {self.app_token}", "Accept": _mime}
            ),
            "",
        )
        return self.response.status_code == 204

    def create_content_attachment(self, content_reference_id, title, body):
        url = f"/content_references/{content_reference_id}/attachments"
        self._app_token_check()
        _mime = "application/vnd.github.corsair-preview+json"
        self.response = Response(
            self.post(
                url,
                params={"title": title, "body": body},
                **{"Authorization": f"Bearer {self.app_token}", "Accept": _mime},
            ),
            "",
        )
        return self.response.transform()
