from .transform import transform


class UserMixin:
    def list_blocked_users(self):
        url = f"https://api.github.com/user/blocks"
        return transform(
            "BlockedUsers",
            self.get_partial(
                url,
                headers={
                    "Accept": "application/vnd.github.giant-sentry-fist-preview+json"
                },
            ).json(),
        )
