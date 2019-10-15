from tests.utils import allhub


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
