from allhub.response import Response


class AssigneesMixin:
    def available_assignees(self, owner, repo):
        url = "/repos/{owner}/{repo}/assignees".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "Assignees")
        return self.response.transform()

    def check_assignee(self, owner, repo, username):
        url = "/repos/{owner}/{repo}/assignees/{username}".format(
            owner=owner, repo=repo, username=username
        )
        self.response = Response(self.get(url), "Assignee")
        return self.response.status_code == 204

    def add_assignee_to_issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/assignees".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(self.post(url), "Assignee")
        return self.response.transform()

    def remove_assignees_from_issue(self, owner, repo, issue_number, assignees):
        assert isinstance(assignees, (list, tuple))
        _mime = "application/vnd.github.symmetra-preview+json"
        url = "/repos/{owner}/{repo}/issues/{issue_number}/assignees".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(
            self.delete(url, params={"assignees": assignees}, **{"Accept": _mime}),
            "Assignee",
        )
        return self.response.transform()
