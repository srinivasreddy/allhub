import requests
from .transform import transform


class UserMixin:
    def list_blocked_users(self):
        url = f"https://api.github.com/user/blocks"
        return transform(
            "BlockedUsers",
            requests.get(
                url,
                headers={
                    "User-Agent": "srinivasreddy",
                    "Authorization": f"token {self.auth_token}",
                    # TODO: the current version is v3, may be we need to configure
                    "Accept": "application/vnd.github.giant-sentry-fist-preview+json",
                },
            ).json(),
        )
