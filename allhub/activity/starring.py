from allhub.response import Response
from allhub.util import ErrorAPICode, config
from enum import Enum


class StarringDirection(Enum):
    ASC = "asc"
    DESC = "desc"


class StarringSort(Enum):
    CREATED = "created"
    UPDATED = "updated"


_mime_option = "application/vnd.github.v{version}.star+{mime}".format(
    version=config.api_version, mime=config.api_mime_type
)


class StarringMixin:
    def stargazers(self, owner, repo, starred_at=False, **kwargs):
        url = "/repos/{owner}/{repo}/stargazers".format(owner=owner, repo=repo)
        self.response = Response(
            self.get(
                url,
                params={"starred_at": starred_at},
                **{"Accept": _mime_option},
                **kwargs,
            ),
            "StarGazers",
        )
        return self.response.transform()

    def starred(
        self,
        sort=StarringSort.CREATED,
        direction=StarringDirection.DESC,
        starred_at=False,
        **kwargs,
    ):
        if sort not in StarringSort:
            raise ValueError("'sort' must be of type Sort")
        if direction not in StarringDirection:
            raise ValueError("'direction' must be of type Direction")

        url = "/user/starred"
        params = [("sort", sort.value), ("direction", direction.value)]
        if starred_at:
            kwargs.update({"Accept": _mime_option})
        self.response = Response(self.get(url, params, **kwargs), "StarRepos")
        return self.response.transform()

    def starred_by(
        self,
        username,
        sort=StarringSort.CREATED,
        direction=StarringDirection.DESC,
        starred_at=False,
        **kwargs,
    ):
        if sort not in StarringSort:
            raise ValueError("'sort' must be of type Sort")
        if direction not in StarringDirection:
            raise ValueError("'direction' must be of type Direction")

        url = "/users/{username}/starred".format(username=username)
        params = [("sort", sort.value), ("direction", direction.value)]
        if starred_at:
            kwargs.update({"Accept": _mime_option})
        self.response = Response(self.get(url, params, **kwargs), "StarRepos")
        return self.response.transform()

    def is_starred(self, owner, repo, **kwargs):
        url = "/user/starred/{owner}/{repo}".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "")
        status_code = self.response.status_code
        if status_code == 204:
            is_starred = True
        elif status_code == 404:
            is_starred = False
        else:
            raise ErrorAPICode(
                "url: {url} supposed to return 204 or 404 but returned {status_code}."
                "Maybe try after sometime?".format(url=url, status_code=status_code)
            )
        return is_starred

    def star_repo(self, owner, repo, **kwargs):
        url = "/user/starred/{owner}/{repo}".format(owner=owner, repo=repo)
        self.response = Response(self.put(url, **{"Content-Length": "0"}, **kwargs), "")
        return self.response.status_code == 204

    def unstar_repo(self, owner, repo, **kwargs):
        url = "/user/starred/{owner}/{repo}".format(owner=owner, repo=repo)
        self.response = Response(self.delete(url, **kwargs), "")
        return self.response.status_code == 204
