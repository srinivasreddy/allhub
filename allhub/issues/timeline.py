from allhub.response import Response


class TimelineMixin:
    def list_events_for_issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/timeline".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        _mime = ", ".join(
            [
                "application/vnd.github.mockingbird-preview",
                "application/vnd.github.starfox-preview+json",
            ]
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "EventsForIssue")
        return self.response.transform()
