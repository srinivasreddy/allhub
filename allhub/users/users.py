from allhub.response import Response


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

    def hover_card(self, username):
        url = f"/users/{username}/hovercard"
        self.response = Response(self.get(url), "HoverCard")
        return self.response.transform()
