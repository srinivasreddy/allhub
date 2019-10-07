from allhub.response import Response


class BranchMixin:
    def branches(self, owner, repo, protected=None):
        url = f"/repos/{owner}/{repo}/branches"
        params = {}
        if protected:
            params = {"protected": protected}
        self.response = Response(self.get(url, params=params), "Branches")
        return self.response.transform()

    def branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}"
        self.response = Response(self.get(url), "Branch")
        return self.response.transform()

    def protected_branch(self, owner, repo, branch):
        mime = "application/vnd.github.luke-cage-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection"
        self.response = Response(self.get(url, **{"Accept": mime}), "BranchProtection")
        return self.response.transform()
