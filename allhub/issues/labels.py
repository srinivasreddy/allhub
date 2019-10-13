from allhub.response import Response

accept_header = {"Accept": "application/vnd.github.symmetra-preview+json"}


class IssueLabelsMixin:
    def labels_for_repo(self, owner, repo):
        url = "/repos/{owner}/{repo}/labels".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **accept_header), "Labels")
        return self.response.transform()

    def label_for_repo(self, owner, repo, label_name):
        url = "/repos/{owner}/{repo}/labels/{label_name}".format(
            owner=owner, repo=repo, label_name=label_name
        )
        self.response = Response(self.get(url, **accept_header), "Label")
        return self.response.transform()

    def create_label(self, owner, repo, name, color, description):
        url = "/repos/{owner}/{repo}/labels".format(owner=owner, repo=repo)
        params = {"name": name, "color": color, "description": description}
        self.response = Response(
            self.post(url, params=params, **accept_header), "Label"
        )
        return self.response.transform()

    def update_label(self, owner, repo, name, new_name, color, description):
        url = "/repos/{owner}/{repo}/labels/{name}".format(
            owner=owner, repo=repo, name=name
        )
        params = {"new_name": new_name, "color": color, "description": description}
        self.response = Response(
            self.patch(url, params=params, **accept_header), "Label"
        )
        return self.response.transform()

    def delete_label(self, owner, repo, name):
        url = "/repos/{owner}/{repo}/labels/{name}".format(
            owner=owner, repo=repo, name=name
        )
        self.response = Response(self.delete(url, **accept_header), "Label")
        return self.response.status_code == 204

    def labels_on_issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/labels".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(self.get(url, **accept_header), "Labels")
        return self.response.transform()

    def add_labels_to_issue(self, owner, repo, issue_number, labels):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/labels".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        params = {"labels": labels}
        self.response = Response(
            self.post(url, params=params, **accept_header), "Labels"
        )
        return self.response.transform()

    def remove_label_from_issue(self, owner, repo, issue_number, name):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(self.delete(url, **accept_header), "Labels")
        return self.response.transform()

    def replace_labels_to_issue(self, owner, repo, issue_number, labels):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/labels".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        params = {"labels": labels}
        self.response = Response(
            self.put(url, params=params, **accept_header), "Labels"
        )
        return self.response.transform()

    def remove_labels_from_issue(self, owner, repo, issue_number):
        url = "/repos/{owner}/{repo}/issues/{issue_number}/labels".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        self.response = Response(self.delete(url, **accept_header), "")
        return self.response.status_code == 204

    def labels_for_every_issue_in_milestone(self, owner, repo, milestone_number):
        url = "/repos/{owner}/{repo}/milestones/{milestone_number}/labels".format(
            owner=owner, repo=repo, milestone_number=milestone_number
        )
        self.response = Response(self.get(url, **accept_header), "Labels")
        return self.response.transform()
