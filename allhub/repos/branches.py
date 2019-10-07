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

    def update_branch_protection(
        self,
        owner,
        repo,
        branch,
        required_status_checks,
        enforce_admins,
        required_pull_request_reviews,
        restrictions,
    ):
        mime = "application/vnd.github.luke-cage-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection"
        params = {
            "required_status_checks": required_status_checks,
            "enforce_admins": enforce_admins,
            "required_pull_request_reviews": required_pull_request_reviews,
            "restrictions": restrictions,
        }
        self.response = Response(
            self.put(url, params=params, **{"Accept": mime}), "UpdateBranchProtection"
        )
        return self.response.transform()

    def remove_branch_protection(self, owner, repo, branch):
        mime = "application/vnd.github.luke-cage-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection"
        self.response = Response(self.delete(url, **{"Accept": mime}), "")
        return self.response.status_code == 204
