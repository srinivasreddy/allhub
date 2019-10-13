from allhub.response import Response


class ReviewRequestsMixin:
    def pr_review_requests(self, owner, repo, pull_number):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(self.get(url), "ReviewRequests")
        return self.response.transform()

    def create_pr_review_request(
        self, owner, repo, pull_number, reviewers, team_reviewers
    ):
        _mime = "application/vnd.github.symmetra-preview+json"
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        params = {"reviewers": reviewers, "team_reviewers": team_reviewers}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "ReviewRequest"
        )
        return self.response.transform()

    def delete_pr_review_requests(
        self, owner, repo, pull_number, reviewers, team_reviewers
    ):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        params = {"reviewers": reviewers, "team_reviwers": team_reviewers}
        self.response = Response(self.delete(url, params=params), "")
        return self.response.status_code == 204
