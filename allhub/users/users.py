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
        url = f"/user/{username}"
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
        if subject_tye.value is None or subject_id is None:
            raise ValueError(f"subject_type and subject_id both should provided.")
        params = [("subject_type", subject_tye.value), ("subject_id", subject_id)]
        url = f"/users/{username}/hovercard"
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.hagar-preview+json"},
            ),
            "HoverCard",
        )
        return self.response.transform()

    def users(self, since=None):
        url = "/users"
        params = [("since", since)]
        self.response = Response(self.patch(url, params=params), "Users")
        return self.response.transform()