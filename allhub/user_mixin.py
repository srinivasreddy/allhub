from .response import Response


class UserMixin:
    def list_blocked_users(self):
        url = f"/user/blocks"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "BlockedUsers",
        )
        return self.response.transform()

    def endpoints(self):
        self.response = Response(self.get(""), "Endpoints")
        return self.response.transform()

    def blocked(self, username):
        """
        Check whether you've blocked a user
        """
        url = f"/user/blocks/{username}"
        self.response = Response(self.get(url), "")
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            return None

    def block(self, username):
        """
        Block a user
        """
        url = f"/user/blocks/{username}"
        self.response = Response(self.put(url), "")
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            return None

    def unblock(self, username):
        """
        Unblock a user
        """
        url = f"/user/blocks/{username}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            return None
