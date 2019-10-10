from allhub.response import Response
from enum import Enum


class PRState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    ALL = "all"


class PRSort(Enum):
    CREATED = "created"
    UPDATED = "updated"
    LONG_RUNNING = "long-running"
    POPULARITY = "popularity"


class PRDirection(Enum):
    ASC = "asc"
    DSC = "dsc"


class PullRequestMixin:
    def repo_pull_requests(
        self,
        owner,
        repo,
        head,
        base,
        state=PRState.OPEN,
        sort=PRSort.CREATED,
        direction=PRDirection.DSC,
    ):
        url = f"/repos/{owner}/{repo}/pulls"
        params = {
            "head": head,
            "base": base,
            "state": state.value,
            "sort": sort.value,
            "direction": direction.value,
        }
        _mime = ", ".join(
            [
                "application/vnd.github.shadow-cat-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "PullRequests"
        )
        return self.response.transform()
