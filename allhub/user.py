import requests
from .transform import transform
import os


class UserMixin:
    def list_blocked_users(self):
        url = f"https://api.github.com/user/blocks"
        return transform(
            "BlockedUsers",
            requests.get(
                url,
                headers={
                    "User-Agent": os.environ.get("APP_NAME", self.user_name),
                    "Authorization": f"token {self.auth_token}",
                    "Accept": "application/vnd.github.giant-sentry-fist-preview+json",
                },
            ).json(),
        )
