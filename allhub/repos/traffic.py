from allhub.response import Response


class TrafficMixin:
    def referrers(self, owner, repo):
        url = f"/repos/{owner}/{repo}/traffic/popular/referrers"
        self.response = Response(self.get(url), "Referrers")
        return self.response.transform()

    def paths(self, owner, repo):
        url = f"/repos/{owner}/{repo}/traffic/popular/paths"
        self.response = Response(self.get(url), "Paths")
        return self.response.transform()

    def views(self, owner, repo, per="day"):
        url = f"/repos/{owner}/{repo}/traffic/views"
        params = {"per": per}
        self.response = Response(self.get(url, params=params), "Views")
        return self.response.transform()

    def clones(self, owner, repo, per="day"):
        url = f"/repos/{owner}/{repo}/traffic/popular/paths"
        params = {"per": per}
        self.response = Response(self.get(url, params=params), "Clones")
        return self.response.transform()
