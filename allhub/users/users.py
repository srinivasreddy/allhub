from allhub.response import Response

from enum import Enum


class SubjectType(Enum):
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"
    NONE = None


class UsersMixin:
    def user(self, username):
        """
        Provides publicly available information about someone with a GitHub account.
        :param username:
        :return:
        """
        url = "/user/{username}".format(username=username)
        self.response = Response(self.get(url), "User")
        return self.response.transform()

    def auth_user(self):
        """
        Get the authenticated user
        :return:
        """
        url = "/user"
        self.response = Response(self.get(url), "User")
        return self.response.transform()

    def update_auth_user(self, **kwargs):
        params = []
        for attribute in (
            "name",
            "email",
            "blog",
            "company",
            "location",
            "hireable",
            "bio",
        ):
            if attribute in kwargs:
                params.append((attribute, kwargs.pop(attribute)))
        if params:
            url = "/user"
            self.response = Response(self.patch(url, params=params), "User")
            return self.response.transform()

    def hover_card(self, username, subject_tye=SubjectType.NONE, subject_id=None):
        if bool(subject_tye.value) != bool(subject_id):  # Python shortcut for XOR.
            raise ValueError(
                "subject_type and subject_id both should provided or both left out"
            )
        params = []
        if subject_id and subject_tye.value:
            params = [("subject_type", subject_tye.value), ("subject_id", subject_id)]
        url = "/users/{username}/hovercard".format(username=username)
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.hagar-preview+json"},
            ),
            "HoverCard",
        )
        return self.response.transform()

    def users(self, since):
        # TODO: Looks like this API is not working currently.
        # As of 19-Sep-2019.
        url = "/users"
        params = [("since", since)]
        self.response = Response(self.patch(url, params=params), "Users")
        return self.response.transform()
