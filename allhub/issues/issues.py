from enum import Enum
from allhub.response import Response


class IssueType(Enum):
    RAW = "application/vnd.github.VERSION.raw+json"
    TEXT = "application/vnd.github.VERSION.text+json"
    HTML = "application/vnd.github.VERSION.html+json"
    FULL = "application/vnd.github.VERSION.full+json"


class IssueLockReason(Enum):
    OFFTOPIC = "off - topic"
    TOOHEATED = "too heated"
    RESOLVED = "resolved"
    SPAM = "spam"


class IssueFilter(Enum):
    ASSIGNED = "assigned"
    CREATED = "created"
    MENTIONED = "mentioned"
    SUBSCRIBED = "subscribed"
    ALL = "all"


class IssueState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    ALL = "all"


class IssueSort(Enum):
    CREATED = "created"
    UPDATED = "updated"
    COMMENTS = "comments"


class IssueDirection(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


IssueCustomMediaType = "application/vnd.github.symmetra-preview+json"


class IssueMixin:
    def all_assigned_issues(
        self,
        filter=IssueFilter.ASSIGNED,
        state=IssueState.OPEN,
        labels="",
        sort=IssueSort.CREATED,
        direction=IssueDirection.DESCENDING,
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
        filter=IssueFilter.ASSIGNED,
        state=IssueState.OPEN,
        labels="",
        sort=IssueSort.CREATED,
        direction=IssueDirection.DESCENDING,
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
        filter=IssueFilter.ASSIGNED,
        state=IssueState.OPEN,
        labels="",
        sort=IssueSort.CREATED,
        direction=IssueDirection.DESCENDING,
        since="",
    ):
        url = "/org/{org}/issues".format(org=org)
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

    def repo_issues(
        self,
        owner,
        repo,
        milestone="*",
        state=IssueState.OPEN,
        assignee="*",
        creator=None,
        mentioned=None,
        labels=None,
        sort=IssueSort.CREATED,
        direction=IssueDirection.DESCENDING,
        since=None,
    ):
        url = "/repos/{owner}/{repo}/issues".format(owner=owner, repo=repo)
        params = [
            ("milestone", milestone),
            ("state", state.value),
            ("assignee", assignee),
            ("sort", sort.value),
            ("direction", direction.value),
        ]
        if creator:
            params.append(("creator", creator))
        if mentioned:
            params.append(("mentioned", mentioned))
        if labels:
            params.append(("labels", labels))
        if since:
            params.append(("since", since))
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.symmetra-preview+json"},
            ),
            "Issues",
        )
        return self.response.transform()

    def issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.squirrel-girl-preview"},
                # The above Accept header gives us the reactions API.
            ),
            "Issue",
        )
        return self.response.transform()

    def create_issue(
        self,
        owner,
        repo,
        title,
        body=None,
        assignee=None,
        milestone=None,
        labels=None,
        assignees=None,
    ):
        params = {"title": title}
        if body:
            params["body"] = body
        if assignee:
            params["assignee"] = assignee
        if milestone:
            params["milestone"] = milestone
        if assignee:
            params["assignee"] = assignee
        if assignees:
            params["assignees"] = assignees
        url = "/repos/{owner}/{repo}/issues".format(owner=owner, repo=repo)
        self.response = Response(
            self.post(
                url,
                params=params,
                **{"Accept": "application/vnd.github.symmetra-preview+json"},
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
        url = "/repos/{owner}/{repo}/issues/{issue_number}".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(
            self.patch(
                url,
                params=[
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
        if lock_reason and not isinstance(lock_reason, IssueLockReason):
            raise ValueError(
                "You should use LockReason instance for lock_reason variable."
            )
        url = "/repos/{owner}/{repo}/issues/{issue_number}/lock".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        custom_headers = {}
        if lock_reason is None:
            custom_headers["Content-Length"] = "0"
        custom_headers.update(
            {"Accept": "application/vnd.github.sailor-v-preview+json"}
        )
        self.response = Response(
            self.put(
                url,
                params=[("locked", True), ("active_lock_reason", lock_reason.value)]
                ** custom_headers,
            ),
            "",
        )
        return self.response.status_code == 204

    def unlock_issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/lock".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(
            self.delete(url, **{"Accept": IssueCustomMediaType}), ""
        )
        return self.response.status_code == 204
