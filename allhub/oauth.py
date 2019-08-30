from .transform import transform


class OAuthMixin:
    """ """

    def grants(self):
        url = "https://api.github.com/applications/grants"
        return transform("AppGrants", self.get_basic(url).json())
