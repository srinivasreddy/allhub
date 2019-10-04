import os
from urllib.parse import urljoin
import requests
from allhub.activity import ActivityMixin
from allhub.orgs import OrganizationMixin
from allhub.gists import GistMixin
from allhub.oauth import OAuthMixin
from allhub.users import UsersMixin
from allhub.util import MimeType, ConflictCheck, config
from allhub.repos import RepositoryMixin
from allhub.search import SearchMixin
from allhub.projects import ProjectsMixin
from allhub.apps import AppMixin

"""
The usage pattern is like this,
```
from allhub import AllHub
all_hub = AllHub('username', 'oauth_token')
all_hub.gist_comments('gist_id')
```
For some API, like OAuth - please see oauth.py file, permits only basic authentication, in that case,
you need to set the password environment variable.

export PASSWORD="mypassword"

If you are using this library as part of a third party Github app, you need to set the environment
variable APP_NAME as well in order for the github to correctly log/diagnose the API requests.

export APP_NAME="Grandeur"

"""


class AllHub(
    GistMixin,
    OAuthMixin,
    ActivityMixin,
    UsersMixin,
    RepositoryMixin,
    SearchMixin,
    ProjectsMixin,
    AppMixin,
    OrganizationMixin,
    metaclass=ConflictCheck,
):
    def __init__(
        self, username, auth_token, transform_resp, app_token=None, password=None
    ):
        self.username = username
        self.auth_token = auth_token
        self.app_token = app_token
        self.page = 1
        self.per_page = 30  # respect the default per_page given by Github API.
        self.transform_resp = transform_resp
        self.host = "https://api.github.com"
        self.password = password
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

    def get(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        if params is None:
            params = {"per_page": self.per_page, "page": self.page}
        else:
            params = dict(params)
            params.update({"per_page": self.per_page, "page": self.page})

        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{config.api_version}+{config.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.get(full_url, headers=headers, params=params)
        if raise_for_status:
            response.raise_for_status()
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response

    def get_basic(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        if params is None:
            params = {"per_page": self.per_page, "page": self.page}
        else:
            params = dict(params)
            params.update({"per_page": self.per_page, "page": self.page})
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Accept": f"application/vnd.github.v{config.api_version}+{config.api_mime_type}",
        }
        password = kwargs.pop("password", None)
        headers.update(**kwargs)
        response = requests.get(
            full_url,
            headers=headers,
            auth=(self.user_name, password or self.password or os.environ["PASSWORD"]),
            params=params,
        )
        if raise_for_status:
            response.raise_for_status()
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"])
        # For response codes 2xx,4xx,5xx
        # Just return the response
        return response

    def put(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        if params is not None:
            params = dict(params)
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{config.api_version}+{config.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.put(full_url, headers=headers, params=params)
        if raise_for_status:
            response.raise_for_status()
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.get(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response

    def post(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        if params is not None:
            params = dict(params)
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{config.api_version}+{config.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.post(full_url, headers=headers, json=params)
        if raise_for_status:
            response.raise_for_status()
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.post(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response

    def patch(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        if params is not None:
            params = dict(params)
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{config.api_version}+{config.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.patch(full_url, headers=headers, json=params)
        if raise_for_status:
            response.raise_for_status()
        # Permanent URL redirection - 301
        # Temporary URL redirection - 302, 307
        if response.status_code in (301, 302, 307):
            return self.post(response.headers["Location"], **kwargs)

        # for response codes 2xx,4xx,5xx
        # just return the response
        return response

    def delete(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        if params is not None:
            params = dict(params)
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("APP_NAME", self.user_name),
            "Authorization": f"token {self.auth_token}",
            "Accept": f"application/vnd.github.v{config.api_version}+{config.api_mime_type}",
        }
        headers.update(**kwargs)
        response = requests.delete(full_url, headers=headers, json=params)
        if raise_for_status:
            response.raise_for_status()
        return response
