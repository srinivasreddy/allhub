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
