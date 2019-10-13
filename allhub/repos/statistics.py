from allhub.response import Response


class StatisticsMixin:
    def contributors_list(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/stats/contributors".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "Contributors")
        return self.response.transform()

    def last_year_commit_activity(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/stats/commit_activity".format(
            owner=owner, repo=repo
        )
        self.response = Response(self.get(url, **kwargs), "Activity")
        return self.response.transform()

    def additions_deletions_per_week(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/stats/code_frequency".format(
            owner=owner, repo=repo
        )
        self.response = Response(self.get(url, **kwargs), "Activity")
        return self.response.transform()

    def weekly_commit_count(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/stats/participation".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "")
        return self.response.transform()

    def punchcard(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/stats/punchcard".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "PunchCard")
        return self.response.transform()
