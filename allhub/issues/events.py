from allhub.response import Response


class IssueEventsMixin:
    def events_for_issue(self, owner, repo, issue_number):
        _mime = ", ".join(
            [
                "application/vnd.github.starfox-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/events"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Events")
        return self.response.transform()

    def events_for_repo(self, owner, repo):
        _mime = ", ".join(
            [
                "application/vnd.github.starfox-preview+json",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        url = f"/repos/{owner}/{repo}/issues/events"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Events")
        return self.response.transform()

    def event(self, owner, repo, event_id):
        _mime = ", ".join(
            [
                "application/vnd.github.starfox-preview+json",
                "application/vnd.github.machine-man-preview",
                "application/vnd.github.symmetra-preview+json",
                "application/vnd.github.sailor-v-preview+json",
            ]
        )
        url = f"/repos/{owner}/{repo}/issues/events/{event_id}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Event")
        return self.response.transform()
