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
        head=None,
        base=None,
        state=PRState.OPEN,
        sort=PRSort.CREATED,
        direction=PRDirection.DSC,
        **kwargs,
    ):
        url = "/repos/{owner}/{repo}/pulls".format(owner=owner, repo=repo)
        params = {
            "state": state.value,
            "sort": sort.value,
            "direction": direction.value,
        }
        if head:
            params["head"] = head
        if base:
            params["base"] = base
        _mime = ", ".join(
            [
                "application/vnd.github.shadow-cat-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}, **kwargs), "PullRequests"
        )
        return self.response.transform()

    def repo_pull_request(self, owner, repo, pull_number):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        _mime = ", ".join(
            [
                "application/vnd.github.shadow-cat-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "PullRequest")
        return self.response.transform()

    def create_pull_request(
        self,
        owner,
        repo,
        title,
        head,
        base,
        body=None,
        maintainer_can_modify=None,
        draft=None,
    ):
        url = "/repos/{owner}/{repo}/pulls".format(owner=owner, repo=repo)
        _mime = ", ".join(
            [
                "application/vnd.github.shadow-cat-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        params = {"title": title, "head": head, "base": base}
        if body:
            params["body"] = body
        if maintainer_can_modify:
            params["maintainer_can_modify"] = maintainer_can_modify
        if draft:
            params["draft"] = draft
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "PullRequest"
        )
        return self.response.transform()

    def update_pull_request_branch(self, owner, repo, pull_number, expected_head_sha):
        _mime = "application/vnd.github.lydian-preview+json"
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/update-branch".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(
            self.put(
                url,
                params={"expected_head_sha": expected_head_sha},
                **{"Accept": _mime},
            ),
            "PullRequest",
        )
        return self.response.transform()

    def update_pull_request(
        self, owner, repo, pull_number, title, body, state, base, maintainer_can_modify
    ):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        _mime = ", ".join(
            [
                "application/vnd.github.shadow-cat-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        params = {
            "title": title,
            "base": base,
            "body": body,
            "state": state,
            "maintainer_can_modify": maintainer_can_modify,
        }
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "PullRequest"
        )
        return self.response.transform()

    def commits_in_pull_request(self, owner, repo, pull_number):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/commits".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(self.get(url), "Commits")
        return self.response.transform()

    def files_in_pull_request(self, owner, repo, pull_number):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/files".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(self.get(url), "Files")
        return self.response.transform()

    def is_pull_request_has_been_merged(self, owner, repo, pull_number):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/merge".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(self.get(url), "")
        return self.response.status_code == 204

    def merge_pull_request(
        self, owner, repo, pull_number, commit_title, commit_message, sha, merge_method
    ):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/merge".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        params = {
            "commit_title": commit_title,
            "commit_message": commit_message,
            "sha": sha,
            "merge_method": merge_method,
        }
        self.response = Response(self.post(url, params=params), "MergePR")
        return self.response.transform()
