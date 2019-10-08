from .utils import allhub


class TestStats:
    def test_contributors(self):
        response = allhub.contributors_list("srinivasreddy", "allhub")
        assert len(response) == 1
        assert response[0].author.login == "srinivasreddy"

    def test_last_year_commit_activity(self):
        response = allhub.last_year_commit_activity("python", "cpython")
        week1 = response[0]
        assert "total" in week1
        assert "week" in week1
        assert "days" in week1
        assert len(week1.days) == 7

    def test_additions_deletions_per_week(self):
        response = allhub.additions_deletions_per_week("python", "cpython")
        assert len(response) > 0

    def test_weekly_commit_count(self):
        response = allhub.weekly_commit_count("python", "cpython")
        assert len(response) > 0

    def test_punchcard(self):
        response = allhub.punchcard("python", "cpython")
        assert len(response) > 0
