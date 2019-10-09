from allhub.response import Response


class AssigneesMixin:
    def available_assignees(self, owner, repo):
        url = f"/repos/{owner}/{repo}/assignees"
        self.response = Response(self.get(url), "Assignees")
        return self.response.transform()

    def check_assignee(self, owner, repo, username):
        url = f"/repos/{owner}/{repo}/assignees/{username}"
        self.response = Response(self.get(url), "Assignee")
        return self.response.status_code == 204

    def add_assignee_to_issue(self, owner, repo, issue_number):
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        self.response = Response(self.post(url), "Assignee")
        return self.response.transform()

    def remove_assignees_from_issue(self, owner, repo, issue_number, assignees):
        assert isinstance(assignees, (list, tuple))
        _mime = "application/vnd.github.symmetra-preview+json"
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        self.response = Response(
            self.delete(url, params={"assignees": assignees}, **{"Accept": _mime}),
            "Assignee",
        )
        return self.response.transform()
