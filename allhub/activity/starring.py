from allhub.response import Response
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
                "Accept": f"application/vnd.github.v{self.api_version}.star+{self.api_mime_type}"
            }
        self.response = Response(self.get(url, **kwargs), "StarGazers")
        return self.response.transform()

    def starred(
        self, sort=Sort.CREATED, direction=Direction.DESC, starred_at=False, **kwargs
    ):
        url = "/user/starred"
        params = [("sort", sort.value), ("direction", direction.value)]
        if starred_at:
            kwargs.update(
                {
                    "Accept": f"application/vnd.github.v{self.api_version}.star+{self.api_mime_type}"
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
        url = f"/users/{username}/starred"
        params = [("sort", sort.value), ("direction", direction.value)]
        if starred_at:
            kwargs.update(
                {
                    "Accept": f"application/vnd.github.v{self.api_version}.star+{self.api_mime_type}"
                }
            )
        self.response = Response(self.get(url, params, **kwargs), "StarRepos")
        return self.response.transform()

    def is_starred(self, owner, repo):
        url = f"/user/starred/{owner}/{repo}"
        status_code = Response(self.get(url), "").status_code
        if status_code == 204:
            is_starred = True
        elif status_code == 404:
            is_starred = False
        else:
            # TODO: Currently i am giving it a False, not sure what to do.
            is_starred = False
        return is_starred

    def star_repo(self, owner, repo):
        url = f"/user/starred/{owner}/{repo}"
        return Response(self.put(url, **{"Content-Length": "0"}), "").status_code == 204

    def unstar_repo(self, owner, repo):
        url = f"/user/starred/{owner}/{repo}"
        return Response(self.delete(url), "").status_code == 204
