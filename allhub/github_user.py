import os

from functools import partial
import requests
from .gist import GistMixin
from .user import UserMixin
from .oauth import OAuthMixin

"""
The usage pattern is like this,
```
from allhub import User
user = User('username', 'oauth_token')
user.gist_comments("gist_id")
```
For some API like oauth permit only Basic authentication, in that case you need
to set PASSWORD environment variable as well,

export PASSWORD="mypassword"

If you are using this library as part of a third party github app, you need to set the environment
variable APP_NAME as well in order for the github to correctly log/diagnose the API requests.

export APP_NAME="Grandeur"

"""


class User(GistMixin, UserMixin, OAuthMixin):
    def __init__(self, user_name, auth_token=None, password=None):
        self.user_name = user_name
        self.auth_token = auth_token
        self.per_page = 100
        self.api_version = 3
        self.api_mime_type = "json"
        self.clone_url = f"https://api.github.com/users/{self.user_name}/repos?per_page={self.per_page}"
        self.get = partial(
            requests.get,
            headers={
                "User-Agent": os.environ.get("APP_NAME", self.user_name),
                "Authorization": f"token {self.auth_token}",
                "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
            },
        )
        self.get_basic = partial(
            requests.get,
            headers={
                "User-Agent": os.environ.get("APP_NAME", self.user_name),
                "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
            },
            auth=(self.user_name, os.environ["PASSWORD"]),
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
