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
from allhub.reactions import ReactionMixin
from allhub.search import SearchMixin
from allhub.projects import ProjectsMixin
from allhub.misc import MiscellaneousMixin
from allhub.migrations import MigrationMixin
from allhub.iterator import Iterator
from allhub.interactions import InteractionLimitsMixin
from allhub.issues import IssuesMixin
from allhub.apps import AppsMixin
from allhub.git_data import GitDataMixin
from allhub.teams import TeamsMixin
from allhub.pull_requests import PullRequestsMixin

from allhub.checks import ChecksMixin

"""
The usage pattern,
```
from allhub import AllHub
all_hub = AllHub('username', 'oauth_token')
all_hub.gist_comments('gist_id')
```
For some API, like OAuth - please see oauth.py file, permits only basic authentication, in that case,
you need to set the password environment variable.

export GH_PASSWORD="mypassword"

If you are using this library as part of a third party Github app, you need to set the environment
variable APP_NAME as well in order for the github to correctly log/diagnose the API requests.

export GH_APP_NAME="Grandeur"

"""


class AllHub(
    GitDataMixin,
    PullRequestsMixin,
    TeamsMixin,
    AppsMixin,
    ChecksMixin,
    GistMixin,
    OAuthMixin,
    ActivityMixin,
    UsersMixin,
    RepositoryMixin,
    ReactionMixin,
    SearchMixin,
    ProjectsMixin,
    OrganizationMixin,
    MiscellaneousMixin,
    MigrationMixin,
    InteractionLimitsMixin,
    IssuesMixin,
    metaclass=ConflictCheck,
):
    def __init__(self, username, auth_token, app_token=None, password=None):
        if username is None:
            raise ValueError("username cannot be None.")
        if auth_token is None:
            raise ValueError("auth_token cannot be None.")
        self.username = username
        self.auth_token = auth_token
        self.app_token = app_token
        self._page = 1
        self._per_page = 30  # respect the default per_page given by Github API.
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
    ):
        obj = cls(user_name, auth_token, password)
        obj.per_page = per_page
        obj.api_version = api_version
        obj.api_mime_type = api_mime_type
        return obj

    def get(self, url, params=None, *args, **kwargs):
        raise_for_status = kwargs.pop("raise_for_status", False)
        kwargs.pop(
            "num_pages", None
        )  # throw away num_pages keyword argument which is meant for an iterator
        params = params and dict(params) or {}
        params.update(
            {"per_page": kwargs.pop("per_page", 30), "page": kwargs.pop("page", 1)}
        )
        self.page = params["page"]
        self.per_page = params["per_page"]
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("GH_APP_NAME", self.username),
            "Authorization": "token {auth_token}".format(auth_token=self.auth_token),
            "Accept": "application/vnd.github.v{version}+{mime}".format(
                version=config.api_version, mime=config.api_mime_type
            ),
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
        kwargs.pop(
            "num_pages", None
        )  # throw away num_pages keyword argument which is meant for an iterator
        params = params and dict(params) or {}
        params.update({"per_page": self.per_page, "page": self.page})
        self.page = params["page"]
        self.per_page = params["per_page"]
        full_url = urljoin(self.host, url)
        headers = {
            "User-Agent": os.environ.get("GH_APP_NAME", self.username),
            "Accept": "application/vnd.github.v{version}+{mime}".format(
                version=config.api_version, mime=config.api_mime_type
            ),
        }
        password = kwargs.pop("password", None)
        headers.update(**kwargs)
        response = requests.get(
            full_url,
            headers=headers,
            auth=(self.username, password or self.password or os.environ["PASSWORD"]),
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
            "User-Agent": os.environ.get("GH_APP_NAME", self.username),
            "Authorization": "token {auth_token}".format(auth_token=self.auth_token),
            "Accept": "application/vnd.github.v{version}+{mime}".format(
                version=config.api_version, mime=config.api_mime_type
            ),
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
            "User-Agent": os.environ.get("APP_NAME", self.username),
            "Authorization": "token {auth_token}".format(auth_token=self.auth_token),
            "Accept": "application/vnd.github.v{version}+{mime}".format(
                version=config.api_version, mime=config.api_mime_type
            ),
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
            "User-Agent": os.environ.get("APP_NAME", self.username),
            "Authorization": "token {auth_token}".format(auth_token=self.auth_token),
            "Accept": "application/vnd.github.v{version}+{mime}".format(
                version=config.api_version, mime=config.api_mime_type
            ),
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
            "User-Agent": os.environ.get("APP_NAME", self.username),
            "Authorization": "token {auth_token}".format(auth_token=self.auth_token),
            "Accept": "application/vnd.github.v{version}+{mime}".format(
                version=config.api_version, mime=config.api_mime_type
            ),
        }
        headers.update(**kwargs)
        response = requests.delete(full_url, headers=headers, json=params)
        if raise_for_status:
            response.raise_for_status()
        return response

    @property
    def per_page(self):
        return self._per_page

    def _check_app_token(self):
        if self.app_token is None:
            raise ValueError(
                "You need to supply app_token to {name}(.....)."
                "In order to obtain app_token see the documentation on how to generate JWT".format(
                    name=self.__class__.__name__
                )
            )

    @property
    def api_version(self):
        return "v3"

    @property
    def page(self):
        return self._page

    @per_page.setter
    def per_page(self, value):
        self._per_page = value

    @page.setter
    def page(self, value):
        self._page = value

    def iterator(self, function, *args, **kwargs):
        page = kwargs.pop("page", None) or self.page
        per_page = kwargs.pop("per_page", None) or self.per_page
        return Iterator(self, function, per_page, page, *args, **kwargs)
