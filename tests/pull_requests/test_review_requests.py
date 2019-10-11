from tests.utils import allhub


class TestPRReviewRequests:
    def test_pr_review_requests(self):
        response = allhub.reviews_on_pull_request("python", "cpython", 10564)
        assert response[0].user.login == "terryjreedy"
        assert response[0].state == "CHANGES_REQUESTED"

    def test_create_pr_review_requests(self):
        pass

    def test_delete_pr_review_requests(self):
        pass
