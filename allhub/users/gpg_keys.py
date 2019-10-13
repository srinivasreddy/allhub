from allhub.response import Response


class GPGKeysMixin:
    def list_gpg_keys(self, username):
        url = "/users/{username}/gpg_keys".format(username=username)
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "GPGKeys",
        )
        return self.response.transform()

    def gpg_keys(self):
        url = "/users/gpg_keys"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "GPGKeys",
        )
        return self.response.transform()

    def gpg_key(self, gpg_key_id):
        url = "/user/gpg_keys/{gpg_key_id}".format(gpg_key_id=gpg_key_id)
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "GPGKey",
        )
        return self.response.transform()

    def create_public_gpg_key(self, armored_public_key):
        url = "/user/gpg_keys"
        self.response = Response(
            self.post(
                url,
                json=[("armored_public_key", armored_public_key)]
                ** {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "SSHKey",
        )
        return self.response.transform()

    def delete_public_gpg_key(self, gpg_key_id):
        url = "/user/gpg_keys/{gpg_key_id}".format(gpg_key_id=gpg_key_id)
        self.response = Response(
            self.delete(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        return self.response.status_code == 204
