from allhub.response import Response
from allhub.util import ErrorAPICode, config
from enum import Enum


class Direction(Enum):
    ASC = "asc"
    DESC = "desc"


class Sort(Enum):
    CREATED = "created"
    UPDATED = "updated"


class StarringMixin:
    def stargazers(self, owner, repo, starred_at=False):
        url = f"/repos/{owner}/{repo}/stargazers"
        kwargs = {}
        if starred_at:
            kwargs = {
                "Accept": f"application/vnd.github.v{config.api_version}.star+{config.api_mime_type}"
            }
        self.response = Response(self.get(url, **kwargs), "StarGazers")
        return self.response.transform()

    def starred(
        self, sort=Sort.CREATED, direction=Direction.DESC, starred_at=False, **kwargs
    ):
        if sort not in Sort:
            raise ValueError("'sort' must be of type Sort")
        if direction not in Direction:
            raise ValueError("'direction' must be of type Direction")

        url = "/user/starred"
        params = [("sort", sort.value), ("direction", direction.value)]
        if starred_at:
            kwargs.update(
                {
                    "Accept": f"application/vnd.github.v{config.api_version}.star+{config.api_mime_type}"
                }
            )
        self.response = Response(self.get(url, params, **kwargs), "StarRepos")
        return self.response.transform()

    def starred_by(
        self,
        username,
        sort=Sort.CREATED,
        direction=Direction.DESC,
        starred_at=False,
        **kwargs,
    ):
        if sort not in Sort:
            raise ValueError("'sort' must be of type Sort")
        if direction not in Direction:
            raise ValueError("'direction' must be of type Direction")

        url = f"/users/{username}/starred"
        params = [("sort", sort.value), ("direction", direction.value)]
        if starred_at:
            kwargs.update(
                {
                    "Accept": f"application/vnd.github.v{config.api_version}.star+{config.api_mime_type}"
                }
            )
        self.response = Response(self.get(url, params, **kwargs), "StarRepos")
        return self.response.transform()

    def is_starred(self, owner, repo):
        url = f"/user/starred/{owner}/{repo}"
        self.response = Response(self.get(url), "")
        status_code = self.response.status_code
        if status_code == 204:
            is_starred = True
        elif status_code == 404:
            is_starred = False
        else:
            raise ErrorAPICode(
                f"url: {url} supposed to return 204 or 404 but returned {status_code}."
                f"Maybe try after sometime?"
            )
        return is_starred

    def star_repo(self, owner, repo):
        url = f"/user/starred/{owner}/{repo}"
        self.response = Response(self.put(url, **{"Content-Length": "0"}), "")
        return self.response.status_code == 204

    def unstar_repo(self, owner, repo):
        url = f"/user/starred/{owner}/{repo}"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
