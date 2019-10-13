from allhub.response import Response
from enum import Enum


class IssueSort(Enum):
    CREATED = "created"
    UPDATED = "updated"


class IssueDirection(Enum):
    ASC = "asc"
    DSC = "DSC"


class CommentsMixin:
    def comments_on_issue(self, owner, repo, issue_number, since=None):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/comments".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        params = {}
        if since:
            params["since"] = since
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.squirrel-girl-preview"},
            ),
            "Comments",
        )
        return self.response.transform()

    def comments_in_repo(
        self, owner, repo, sort=IssueSort.CREATED, direction=None, since=None
    ):
        url = "/repos/{owner}/{repo}/issues/comments".format(owner=owner, repo=repo)
        params = {"sort": sort.value}
        if direction:
            params["direction"] = direction
        if since:
            params["since"] = since

        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.squirrel-girl-preview"},
            ),
            "Comments",
        )
        return self.response.transform()

    def issue_comment(self, owner, repo, comment_id):
        url = "/repos/{owner}/{repo}/issues/comments/{comment_id}".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        self.response = Response(
            self.get(url, **{"Accept": "application/vnd.github.machine-man-preview"}),
            "Comment",
        )
        return self.response.transform()

    def create_issue_comment(self, owner, repo, issue_number, body):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/comments".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(
            self.post(
                url,
                params={"body": body},
                **{"Accept": "application/vnd.github.machine-man-preview"},
            ),
            "Comment",
        )
        return self.response.transform()

    def edit_issue_comment(self, owner, repo, comment_id, body):
        url = "/repos/{owner}/{repo}/issues/comments/{comment_id}".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        self.response = Response(
            self.patch(
                url,
                params={"body": body},
                **{"Accept": "application/vnd.github.machine-man-preview"},
            ),
            "Comment",
        )
        return self.response.transform()

    def delete_issue_comment(self, owner, repo, comment_id):
        url = "/repos/{owner}/{repo}/issues/comments/{comment_id}".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
