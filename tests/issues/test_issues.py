from tests.utils import allhub
from allhub.issues import IssueState


class TestIssues:
    def test_all_assigned_issues(self):
        response = allhub.all_assigned_issues()
        assert response == []

    def test_repo_issues(self):
        response = allhub.repo_issues("ipython", "ipython")
        resp = response[0]
        assert 0 < len(response) <= 30
        assert resp.created_at is not None
        assert resp.url is not None

    def test_repo_issues_with_page(self):
        response = allhub.repo_issues(
            "ipython", "ipython", state=IssueState.ALL, page=4
        )
        resp = response[0]
        assert 0 < len(response) <= 30
        assert resp.created_at is not None
        assert resp.url is not None
        assert allhub.page == 4
        assert allhub.response.next_page_number == 5
        print(allhub.response.headers()["Link"])
