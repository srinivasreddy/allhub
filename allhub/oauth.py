from .transform import transform


class OAuthMixin:
    """
    OAuth permissions API Mixin.
    """

    def grants(self, mime_type=None):
        url = f"{self.host}applications/grants"
        return transform("AppGrants", self.get_basic(url, mime_type))
