from allhub.response import Response


class SSHKeysMixin:
    def list_public_keys(self, username):
        url = f"/users/{username}/keys"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKeys",
        )
        return self.response.transform()

    def public_keys(self):
        url = f"/users/keys"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKeys",
        )
        return self.response.transform()

    def public_key(self, key_id):
        url = f"/user/keys/{key_id}"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKey",
        )
        return self.response.transform()

    def create_public_key(self, title, key):
        url = "/user/keys"
        self.response = Response(
            self.post(
                url,
                json=[("title", title), ("key", key)]
                ** {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKey",
        )
        return self.response.transform()

    def delete_public_key(self, key_id):
        url = f"/user/keys/{key_id}"
        self.response = Response(
            self.delete(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        return self.response.status_code == 204