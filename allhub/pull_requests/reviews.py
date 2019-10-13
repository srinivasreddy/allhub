from allhub.response import Response


class ReviewsMixin:
    def reviews_on_pull_request(self, owner, repo, pull_number):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(self.get(url), "PRReviews")
        return self.response.transform()

    def review_on_pull_request(self, owner, repo, pull_number, review_id):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}".format(
            owner=owner, repo=repo, pull_number=pull_number, review_id=review_id
        )
        self.response = Response(self.get(url), "PRReview")
        return self.response.transform()

    def delete_pending_review(self, owner, repo, pull_number, review_id):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}".format(
            owner=owner, repo=repo, pull_number=pull_number, review_id=review_id
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204

    def comments_for_pull_request_review(self, owner, repo, pull_number, review_id):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments".format(
            owner=owner, repo=repo, pull_number=pull_number, review_id=review_id
        )
        self.response = Response(self.get(url), "Comments")
        return self.response.transform()

    def create_pull_request_review(
        self, owner, repo, pull_number, commit_id, body, event, comments
    ):
        params = {
            "commit_id": commit_id,
            "body": body,
            "event": event,
            "comments": comments,
        }
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews".format(
            owner=owner, repo=repo, pull_number=pull_number
        )
        self.response = Response(self.post(url, params=params), "PRReview")
        return self.response.transform()

    def update_pull_request_review(self, owner, repo, pull_number, review_id, body):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}".format(
            owner=owner, repo=repo, pull_number=pull_number, review_id=review_id
        )
        self.response = Response(self.put(url, params={"body": body}), "PRReview")
        return self.response.transform()

    def submit_pull_request_review(
        self, owner, repo, pull_number, review_id, body, event
    ):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events".format(
            owner=owner, repo=repo, pull_number=pull_number, review_id=review_id
        )
        params = {"body": body, "event": event}
        self.response = Response(self.post(url, params=params), "PRReview")
        return self.response.transform()

    def dismiss_pull_request_review(self, owner, repo, pull_number, review_id, message):
        url = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals".format(
            owner=owner, repo=repo, pull_number=pull_number, review_id=review_id
        )

        params = {"message": message}
        self.response = Response(self.put(url, params=params), "PRReview")
        return self.response.transform()
