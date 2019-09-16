from enum import Enum
from allhub.response import Response


class IssueType(Enum):
    Raw = "application/vnd.github.VERSION.raw+json"
    Text = "application/vnd.github.VERSION.text+json"
    Html = "application/vnd.github.VERSION.html+json"
    Full = "application/vnd.github.VERSION.full+json"


class LockReason(Enum):
    OffTopic = "off - topic"
    TooHeated = "too heated"
    Resolved = "resolved"
    Spam = "spam"


class Filter(Enum):
    Assigned = "assigned"
    Created = "created"
    Mentioned = "mentioned"
    Subscribed = "subscribed"
    All = "all"


class State(Enum):
    Open = "open"
    Closed = "closed"
    All = "all"


class Sort(Enum):
    Created = "created"
    Updated = "updated"
    Comments = "comments"


class Direction(Enum):
    Ascending = "asc"
    Descending = "desc"


IssueCustomMediaType = "application/vnd.github.symmetra-preview+json"


class IssueMixin:
    def assigned_issues(
        self,
        filter=Filter.Assigned,
        state=State.Open,
        labels="",
        sort=Sort.Created,
        direction=Direction.Descending,
        since="",
    ):
        url = "/issues"
        params = [
            ("filter", filter.value),
            ("state", state.value),
            ("labels", labels),
            ("sort", sort.value),
            ("direction", direction.value),
            ("since", since),
        ]
        self.response = Response(
            self.get(url, params=params, **{"Accept": IssueCustomMediaType}), "Issues"
        )
        return self.response.transform()

    def user_issues(
        self,
        filter=Filter.Assigned,
        state=State.Open,
        labels="",
        sort=Sort.Created,
        direction=Direction.Descending,
        since="",
    ):
        url = "/user/issues"
        params = [
            ("filter", filter.value),
            ("state", state.value),
            ("labels", labels),
            ("sort", sort.value),
            ("direction", direction.value),
            ("since", since),
        ]
        self.response = Response(
            self.get(url, params=params, **{"Accept": IssueCustomMediaType}), "Issues"
        )
        return self.response.transform()

    def org_user_issues(
        self,
        org,
        filter=Filter.Assigned,
        state=State.Open,
        labels="",
        sort=Sort.Created,
        direction=Direction.Descending,
        since="",
    ):
        url = f"/org/{org}/issues"
        params = [
            ("filter", filter.value),
            ("state", state.value),
            ("labels", labels),
            ("sort", sort.value),
            ("direction", direction.value),
            ("since", since),
        ]
        self.response = Response(
            self.get(url, params=params, **{"Accept": IssueCustomMediaType}), "Issues"
        )
        return self.response.transform()

    def issue(self, owner, repo, issue_number):
        url = f"/repos/{owner}/{repo}/issues/{issue_number}"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.squirrel-girl-preview"},
                # The above Accept header gives us the reactions API.
            ),
            "Issue",
        )
        return self.response.transform()

    def edit_issue(
        self,
        owner,
        repo,
        issue_number,
        title,
        body,
        state,
        milestone,
        labels,
        assignees,
    ):
        """
        :param owner: repo owner
        :param repo : repo name
        :param issue_number: Issue number
        :param title: The title of the issue.
        :param body: The contents of the issue.
        :param state: State of the issue. Either open or closed.
        :param milestone: The number of the milestone to associate this issue with or null to remove current.
        NOTE: Only users with push access can set the milestone for issues.
        :param labels:  Pass one or more Labels to replace the set of Labels on this Issue.
        Send an empty array ([]) to clear all Labels from the Issue.
        :param assignees: Pass one or more user logins to replace the set of assignees on this Issue.
        Send an empty array ([]) to clear all assignees from the Issue.
        :return:
        """
        url = f"/repos/{owner}/{repo}/issues/{issue_number}"
        self.response = Response(
            self.patch(
                url,
                json=[
                    ("title", title),
                    ("body", body),
                    ("assignees", list(assignees)),
                    ("milestone", milestone),
                    ("state", state),
                    ("labels", list(labels)),
                ],
                **{"Accept": "application/vnd.github.symmetra-preview+json"},
            ),
            "Issue",
        )
        return self.response.transform()

    def lock_issue(self, owner, repo, issue_number, lock_reason=None):
        if lock_reason and not isinstance(lock_reason, LockReason):
            raise ValueError(
                "You should use LockReason instance for lock_reason variable."
            )
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/lock"
        custom_headers = {}
        if lock_reason is None:
            custom_headers["Content-Length"] = "0"
        custom_headers.update(
            {"Accept": "application/vnd.github.sailor-v-preview+json"}
        )
        self.response = Response(
            self.put(
                url,
                json=[("locked", True), ("active_lock_reason", lock_reason.value)]
                ** custom_headers,
            ),
            "",
        )
        return self.response.status_code == 204

    def unlock_issue(self, owner, repo, issue_number):
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/lock"
        self.response = Response(
            self.delete(url, **{"Accept": IssueCustomMediaType}), ""
        )
        return self.response.status_code == 204