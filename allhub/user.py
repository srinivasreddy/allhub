from .transform import transform


class UserMixin:
    def list_blocked_users(self):
        url = f"/user/blocks"
        return transform("BlockedUsers", self.get_basic(url))

    def endpoints(self):
        return transform("Endpoints", self.get(""))
