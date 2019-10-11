from allhub.response import Response
from allhub.util import ErrorAPICode


class BlockMixin:
    def list_blocked_users(self, **kwargs):
        url = f"/user/blocks"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
                **kwargs,
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
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            raise ErrorAPICode(
                f"API has returned an Unexpected response code - {self.response.status_code}."
                f"It should either be 204 or 404."
            )

    def block(self, username):
        """
        Block a user
        """
        url = f"/user/blocks/{username}"
        self.response = Response(
            self.put(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            raise ErrorAPICode(
                f"API has returned an Unexpected response code - {self.response.status_code}."
                f"It should either be 204 or 404."
            )

    def unblock(self, username):
        """
        Unblock a user
        """
        url = f"/user/blocks/{username}"
        self.response = Response(
            self.delete(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            raise ErrorAPICode(
                f"API has returned an Unexpected response code - {self.response.status_code}."
                f"It should either be 204 or 404."
            )
