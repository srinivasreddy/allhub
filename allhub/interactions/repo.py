from allhub.response import Response
from .util import InteractionLimit

_mime = "application/vnd.github.sombra-preview"


class RepoMixin:
    def repo_interaction_limits(self, owner, repo):
        url = "/repos/{owner}/{repo}/interaction-limits".format(owner=owner, repo=repo)
        self.response = Response(
            self.get(url, **{"Accept": _mime}), "RepoInteractionLimits"
        )
        return self.response.transform()

    def add_repo_interaction_limits(self, owner, repo, limit):
        assert isinstance(limit, InteractionLimit)
        url = "/repos/{owner}/{repo}/interaction-limits".format(owner=owner, repo=repo)
        self.response = Response(
            self.put(url, params={"limit": limit.value}, **{"Accept": _mime}),
            "RepoInteractionLimits",
        )
        return self.response.transform()

    def remove_repo_interaction_limits(self, owner, repo):
        url = "/repos/{owner}/{repo}/interaction-limits".format(owner=owner, repo=repo)
        self.response = Response(self.put(url), "")
        return self.response.status_code == 204
