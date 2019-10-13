from allhub.response import Response
from allhub.util import ErrorAPICode


class FollowersMixin:
    def list_followers(self, username):
        url = "/users/{username}/followers".format(username=username)
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Followers",
        )
        return self.response.transform()

    def followers(self):
        url = "/users/followers"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Followers",
        )
        return self.response.transform()

    def user_following(self, username):
        url = "/users/{username}/following".format(username=username)
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Following",
        )
        return self.response.transform()

    def following(self):
        url = "/users/following"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Following",
        )
        return self.response.transform()

    def is_following(self, username):
        url = "/users/following/{username}".format(username=username)
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

    def user_is_following(self, username, target_user):
        url = "/users/{username}/following/{target_user}".format(
            username=username, target_user=target_user
        )
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

    def follow(self, username):
        url = "/user/following/{username}".format(username=username)
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
                "API has returned an Unexpected response code - {status_code}."
                "It should either be 204 or 404.".format(
                    status_code=self.response.status_code
                )
            )

    def unfollow(self, username):
        url = "/user/following/{username}".format(username=username)
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
