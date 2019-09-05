from urllib.parse import urljoin
import os
from functools import partial
import requests
from allhub.gist import GistMixin
from allhub.user_mixin import UserMixin
from allhub.oauth import OAuthMixin
from allhub.util import MimeType
from allhub.activity import ActivityMixin

"""
The usage pattern is like this,
```
from allhub import User
user = User('username', 'oauth_token')
user.gist_comments('gist_id')
```
For some API, like OAuth - please see oauth.py file, permit only basic authentication, in that case,
you need to set the password environment variable.

export PASSWORD="mypassword"

If you are using this library as part of a third party Github app, you need to set the environment
variable APP_NAME as well in order for the github to correctly log/diagnose the API requests.

export APP_NAME="Grandeur"

"""


class User(GistMixin, UserMixin, OAuthMixin, ActivityMixin):
    def __init__(self, user_name, auth_token, transform_resp, password=None):
        self.user_name = user_name
        self.auth_token = auth_token
        self.per_page = 100
        self.api_version = 3
        self.api_mime_type = "json"
        self.transform_resp = transform_resp
        self.host = "https://api.github.com"
        self.password = password
        self.clone_url = urljoin(
            self.host, f"/users/{self.user_name}/repos?per_page={self.per_page}"
        )
        self.post_partial = partial(
            requests.post,
            headers={
                "User-Agent": os.environ.get("APP_NAME", self.user_name),
                "Authorization": f"token {self.auth_token}",
                "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
            },
        )
        self.response = None

    @classmethod
    def build(
        cls,
        user_name,
        auth_token,
        api_version=3,
        api_mime_type=MimeType.Json,
        per_page=100,
        password=None,
        transform_resp=True,
    ):
        obj = cls(user_name, auth_token, transform_resp, password)
        obj.per_page = per_page
        obj.api_version = api_version
        obj.api_mime_type = api_mime_type
        return obj

    def get(self, url, *args, **kwargs):
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.get(full_url, headers=headers)
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response

    def get_basic(self, url, *args, **kwargs):
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
        }
        password = kwargs.pop("password", None)
        headers.update(**kwargs)
        response = requests.get(
            full_url,
            headers=headers,
            auth=(self.user_name, password or self.password or os.environ["PASSWORD"]),
        )
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"])
        # For response codes 2xx,4xx,5xx
        # Just return the response
        return response

    def put(self, url, *args, **kwargs):
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.put(full_url, headers=headers)
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response

    def post(self, url, *args, **kwargs):
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{self.api_version}+{self.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.put(full_url, headers=headers)
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response
