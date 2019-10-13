from allhub.response import Response
from allhub.util import ErrorAPICode


class BlockMixin:
    def list_blocked_users(self, **kwargs):
        url = "/user/blocks"
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
        url = "/user/blocks/{username}".format(username=username)
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
                "API has returned an Unexpected response code - {status_code}."
                "It should either be 204 or 404.".format(
                    status_code=self.response.status_code
                )
            )

    def block(self, username):
        """
        Block a user
        """
        url = "/user/blocks/{username}".format(username=username)
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
                "API has returned an Unexpected response code - {status_code}."
                "It should either be 204 or 404.".format(
                    status_code=self.response.status_code
                )
            )

    def unblock(self, username):
        """
        Unblock a user
        """
        url = "/user/blocks/{username}".format(username=username)
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
                "API has returned an Unexpected response code - {status_code}."
                "It should either be 204 or 404.".format(
                    status_code=self.response.status_code
                )
            )
