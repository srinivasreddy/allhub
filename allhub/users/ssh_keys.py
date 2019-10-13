from allhub.response import Response


class SSHKeysMixin:
    def list_public_ssh_keys(self, username):
        url = "/users/{username}/keys".format(username=username)
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKeys",
        )
        return self.response.transform()

    def ssh_keys(self):
        url = "/user/keys"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKeys",
        )
        return self.response.transform()

    def ssh_key(self, key_id):
        url = "/user/keys/{key_id}".format(key_id=key_id)
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKey",
        )
        return self.response.transform()

    def create_public_ssh_key(self, title, key):
        url = "/user/keys"
        self.response = Response(
            self.post(
                url,
                params=[("title", title), ("key", key)],
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKey",
        )
        return self.response.transform()

    def delete_public_ssh_key(self, key_id):
        url = "/user/keys/{key_id}".format(key_id=key_id)
        self.response = Response(
            self.delete(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        return self.response.status_code == 204
