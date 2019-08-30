import os

from functools import partial
import requests
from .gist import GistMixin
from .user import UserMixin
from .oauth import OAuth


class User(GistMixin, UserMixin, OAuth):
    def __init__(self, user_name, auth_token=None, password=None):
        self.user_name = user_name
        self.auth_token = auth_token
        self.per_page = 100
        self.api_version = 3
        self.api_mime_type = "json"
        # TODO: I assume the max repos per a user is 100.
        # TODO: Maybe need to revisit the assumption.
        self.clone_url = f"https://api.github.com/users/{self.user_name}/repos?per_page={self.per_page}"
        self.get_partial = partial(
            requests.get,
            headers={
                "User-Agent": os.environ.get("APP_NAME", self.user_name),
                "Authorization": f"token {self.auth_token}",
                # TODO: the current version is v3, may be we need to configure
                "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
            },
        )
        self.post_partial = partial(
            requests.post,
            headers={
                "User-Agent": os.environ.get("APP_NAME", self.user_name),
                "Authorization": f"token {self.auth_token}",
                # TODO: the current version is v3, may be we need to configure
                "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
            },
        )
