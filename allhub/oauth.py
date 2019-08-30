from .transform import transform


class OAuth:
    def grants(self):
        url = "https://api.github.com/applications/grants"
        return transform("AppGrants", self.get_partial(url).json())
