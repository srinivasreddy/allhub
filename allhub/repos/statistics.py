from allhub.response import Response


class StatisticsMixin:
    def contributors_list(self, owner, repo):
        url = f"/repos/{owner}/{repo}/stats/contributors"
        self.response = Response(self.get(url), "Contributors")
        return self.response.transform()

    def last_year_commit_activity(self, owner, repo):
        url = f"/repos/{owner}/{repo}/stats/commit_activity"
        self.response = Response(self.get(url), "Activity")
        return self.response.transform()

    def additions_deletions_per_week(self, owner, repo):
        url = f"/repos/{owner}/{repo}/stats/code_frequency"
        self.response = Response(self.get(url), "Activity")
        return self.response.transform()

    def weekly_commit_count(self, owner, repo):
        url = f"/repos/{owner}/{repo}/stats/participation"
        self.response = Response(self.get(url), "")
        return self.response.transform()

    def punchcard(self, owner, repo):
        url = f"/repos/{owner}/{repo}/stats/punchcard"
        self.response = Response(self.get(url), "PunchCard")
        return self.response.transform()
