from allhub.response import Response
from enum import Enum


class Sort(Enum):
    NEWEST = "newest"
    OLDEST = "oldest"
    STARGAZERS = "stargazers"


class ForkMixin:
    def forks(self, owner, repo, sort=Sort.NEWEST, **kwargs):
        url = f"/repos/{owner}/{repo}/forks"
        self.response = Response(
            self.get(url, params=[("sort", sort.value)], **kwargs), "Forks"
        )
        return self.response.transform()

    def create_fork(self, owner, repo, organization=None, **kwargs):
        url = f"/repos/{owner}/{repo}/forks"
        params = {}
        if organization:
            params["organization"] = organization
        self.response = Response(self.post(url, params=params, **kwargs), "Fork")
        assert self.response.status_code == 202
        return self.response.transform()
