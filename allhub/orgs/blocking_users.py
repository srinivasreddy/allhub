from allhub.response import Response

_mime_type = "application/vnd.github.giant-sentry-fist-preview+json"


class BlockingMixin:
    def blocked_users(self, org):
        url = "/orgs/{org}/blocks".format(org=org)
        self.response = Response(self.get(url, **{"Accept": _mime_type}), "Users")
        return self.response.transform()

    def blocked_from_org(self, org, username):
        """
        Check whether a user is blocked from an organization
        :param org:
        :param username:
        :return:
        """
        url = "/orgs/{org}/blocks/{username}".format(org=org, username=username)
        self.response = Response(self.get(url, **{"Accept": _mime_type}), "User")
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            raise ValueError(
                "blocked_from_org(....) returned status code : {status_code} it should either be 204 or 404".format(
                    status_code=self.response.status_code
                )
            )

    def block_user_from_org(self, org, username):
        """
        Block a user.

        :param org:
        :param username:
        :return:
        """
        url = "/orgs/{org}/blocks/{username}".format(org=org, username=username)
        self.response = Response(self.put(url, **{"Accept": _mime_type}), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "block_user_from_org(....) returned status code : {status_code}, instead of 204".format(
                status_code=self.response.status_code
            )
        )

    def unblock_user_from_org(self, org, username):
        """
        Unblock a user
        :param org:
        :param username:
        :return:
        """
        url = "/orgs/{org}/blocks/{username}".format(org=org, username=username)
        self.response = Response(self.delete(url, **{"Accept": _mime_type}), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "unblock_user_from_org(....) returned status code : {status_code}, instead of 204".format(
                status_code=self.response.status_code
            )
        )
