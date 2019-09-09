from allhub.response import Response
from allhub.util import ErrorAPICode


class FollowersMixin:
    def list_followers(self, username):
        url = f"/users/{username}/followers"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Followers",
        )
        return self.response.transform()

    def followers(self):
        url = f"/users/followers"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Followers",
        )
        return self.response.transform()

    def user_following(self, username):
        url = f"/users/{username}/following"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Following",
        )
        return self.response.transform()

    def following(self):
        url = f"/users/following"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Following",
        )
        return self.response.transform()

    def is_following(self, username):
        url = f"/users/following/{username}"
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

    def user_is_following(self, username, target_user):
        url = f"/users/{username}/following/{target_user}"
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

    def follow(self, username):
        url = f"/user/following/{username}"
        self.response = Response(
            self.put(
                url,
                **{
                    "Accept": "application/vnd.github.giant-sentry-fist-preview+json",
                    "Content-Length": "0",
                },
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

    def unfollow(self, username):
        url = f"/user/following/{username}"
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
