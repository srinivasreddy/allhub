from allhub.response import Response

_mime = ", ".join(
    [
        "application/vnd.github.starfox-preview+json",
        "application/vnd.github.symmetra-preview+json",
        "application/vnd.github.sailor-v-preview+json",
    ]
)


class IssueEventsMixin:
    def events_for_issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/events".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "Events")
        return self.response.transform()

    def events_for_repo(self, owner, repo):
        url = "/repos/{owner}/{repo}/issues/events".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **{"Accept": _mime}), "Events")
        return self.response.transform()

    def event(self, owner, repo, event_id):
        _local_mime = _mime + ", application/vnd.github.machine-man-preview"
        url = "/repos/{owner}/{repo}/issues/events/{event_id}".format(
            owner=owner, repo=repo, event_id=event_id
        )
        self.response = Response(self.get(url, **{"Accept": _local_mime}), "Event")
        return self.response.transform()
