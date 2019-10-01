from allhub.response import Response

_app_mime_type = "application/vnd.github.machine-man-preview+json"


class InstallationMixin:
    def installation_repos(self):
        if self.app_token is None:
            raise ValueError(
                f"You need to supply app_token to {self.__class__.__name__}(.....)."
                f"In order to obtain app_token see the documentation on how to generate JWT"
            )
        url = "/installation/repositories"
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
