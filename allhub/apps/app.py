from allhub.response import Response

_app_mime_type = "application/vnd.github.machine-man-preview+json"


class AppMixin:
    def app(self, app_slug):
        url = f"/apps/{app_slug}"
        self.response = Response(self.get(url, **{"Accept": _app_mime_type}), "App")
        return self.response.transform()

    def auth_app(self):
        if self.app_token is None:
            raise ValueError(
                f"You need to supply app_token to {self.__class__.__name__}()."
                f"In order to obtain app_token see the documentation on how to generate JWT"
            )
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
        if self.app_token is None:
            raise ValueError(
                f"You need to supply app_token to {self.__class__.__name__}()."
                f"In order to obtain app_token see the documentation on how to generate JWT"
            )
        url = f"/app/installations"
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
        if self.app_token is None:
            raise ValueError(
                f"You need to supply app_token to {self.__class__.__name__}()."
                f"In order to obtain app_token see the documentation on how to generate JWT"
            )
        url = f"/app/installations/{installation_id}"
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
        if self.app_token is None:
            raise ValueError(
                f"You need to supply app_token to {self.__class__.__name__}()."
                f"In order to obtain app_token, invoke the method `create_app_access_token(....)` "
            )
        url = f"/app/installations/{installation_id}"
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
        assert isinstance(repository_ids, (list, tuple))
        for repository_id in repository_ids:
            if not isinstance(repository_id, int):
                raise ValueError("repository_ids should contain only integers.")

        url = f"/app/installations/{installation_id}/access_tokens"

        self.response = Response(self.post(url, **{"Accept": _app_mime_type}), "Token")
        return self.response.transform()
