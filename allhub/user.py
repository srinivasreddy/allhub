from .transform import transform


class UserMixin:
    def list_blocked_users(self):
        url = "https://api.github.com/user/blocks"
        return transform("BlockedUsers", self.get_basic(url))
