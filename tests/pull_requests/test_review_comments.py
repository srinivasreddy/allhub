from tests.utils import allhub


class TestPRReviewComments:
    def test_comments_on_pull_request(self):
        response = allhub.comments_on_pull_request("python", "cpython", 9916)
        assert response[0].diff_hunk is not None
