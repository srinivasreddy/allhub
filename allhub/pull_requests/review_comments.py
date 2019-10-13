from allhub.response import Response
from enum import Enum


class PRCommentsSort(Enum):
    CREATED = "created"
    UPDATED = "updated"


class PRCommentsDirection(Enum):
    ASC = "asc"
    DSC = "dsc"


class ReviewCommentsMixin:
    def comments_on_pull_request(
        self,
        owner,
        repo,
        pull_number,
        sort=PRCommentsSort.CREATED,
        direction=None,
        since=None,
    ):
        _mime = ", ".join(
            [
                "application/vnd.github.comfort-fade-preview+json",
                "application/vnd.github.squirrel-girl-preview",
            ]
        )
        params = {"sort": sort.value}
        if direction:
            params["direction"] = direction
        if since:
            params["since"] = since

        url = "/repos/{owner}/{repo}/pulls/{pull_number}/comments".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "PRComments"
        )
        return self.response.transform()

    def review_comments_in_repo(
        self, owner, repo, sort=PRCommentsSort.CREATED, direction=None, since=None
    ):
        _mime = ", ".join(
            [
                "application/vnd.github.comfort-fade-preview+json",
                "application/vnd.github.squirrel-girl-preview",
            ]
        )
        params = {"sort": sort.value}
        if direction:
            params["direction"] = direction
        if since:
            params["since"] = since
        url = "/repos/{owner}/{repo}/pulls/comments".format(owner=owner, repo=repo)
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "PRComments"
        )
        return self.response.transform()

    def comment_on_pull_request(self, owner, repo, pull_number, comment_id):
        _mime = ", ".join(
            [
                "application/vnd.github.comfort-fade-preview+json",
                "application/vnd.github.squirrel-girl-preview",
            ]
        )
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}".format(
            owner=owner, repo=repo, pull_number=pull_number, comment_id=comment_id
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "PRComments")
        return self.response.transform()

    def create_comment_on_pull_request(
        self,
        owner,
        repo,
        pull_number,
        body,
        commit_id,
        path,
        position,
        side,
        line,
        start_line,
        start_side,
    ):
        _mime = ", ".join(
            [
                "application/vnd.github.comfort-fade-preview+json",
                "application/vnd.github.squirrel-girl-preview",
            ]
        )
        params = {
            "body": body,
            "commit_id": commit_id,
            "path": path,
            "position": position,
            "side": side,
            "line": line,
            "start_line": start_line,
            "start_side": start_side,
        }
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/comments".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "PRComment"
        )
        return self.response.transform()

    def create_comment_reply_on_pull_request(
        self, owner, repo, pull_number, comment_id, body
    ):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies".format(
            owner=owner, repo=repo, pull_number=pull_number, comment_id=comment_id
        )
        self.response = Response(self.post(url, params={"body": body}), "PRComment")
        return self.response.transform()

    def edit_comment_on_pull_request(self, owner, repo, pull_number, comment_id, body):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}".format(
            owner=owner, repo=repo, pull_number=pull_number, comment_id=comment_id
        )
        self.response = Response(
            self.patch(
                url,
                params={"body": body},
                **{"Accept": "application/vnd.github.comfort-fade-preview+json"},
            ),
            "PRComment",
        )
        return self.response.transform()

    def delete_comment_on_pull_request(self, owner, repo, pull_number, comment_id):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}".format(
            owner=owner, repo=repo, pull_number=pull_number, comment_id=comment_id
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
