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
        """
        Protected branches are not available for Free plans.
        Use Pro plan or Github Enterprise.
        :param owner:
        :param repo:
        :param branch:
        :return:
        """
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
        """
        Protected branches are not available for Free plans.
        Use Pro plan or Github Enterprise.
        :param owner:
        :param repo:
        :param branch:
        :param required_status_checks:
        :param enforce_admins:
        :param required_pull_request_reviews:
        :param restrictions:
        :return:
        """
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
        """
        Protected branches are not available for Free plans.
        Use Pro plan or Github Enterprise.
        :param owner:
        :param repo:
        :param branch:
        :return:
        """
        mime = "application/vnd.github.luke-cage-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection"
        self.response = Response(self.delete(url, **{"Accept": mime}), "")
        return self.response.status_code == 204

    def required_status_checks_of_protected_branch(self, owner, repo, branch):
        """
        Protected branches are not available for Free plans.
        Use Pro plan or Github Enterprise.
        :param owner:
        :param repo:
        :param branch:
        :return:
        """
        url = (
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        self.response = Response(self.get(url), "RequiredChecks")
        return self.response.transform()

    def update_required_status_checks_of_protected_branch(
        self, owner, repo, branch, strict, contexts
    ):
        """
        Protected branches are not available for Free plans.
        Use Pro plan or Github Enterprise.
        :param owner:
        :param repo:
        :param branch:
        :param strict:
        :param contexts:
        :return:
        """
        url = (
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        params = {"strict": strict, "contexts": contexts}
        self.response = Response(self.patch(url, params=params), "RequiredChecks")
        return self.response.transform()

    def remove_required_status_checks_of_protected_branch(self, owner, repo, branch):
        """
        Protected branches are not available for Free plans.
        Use Pro plan or Github Enterprise.
        :param owner:
        :param repo:
        :param branch:
        :return:
        """
        url = (
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204

    def required_status_checks_contexts_of_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        self.response = Response(self.get(url), "Contexts")
        return self.response.transform()

    def replace_required_status_checks_contexts_of_protected_branch(
        self, owner, repo, branch, contexts
    ):
        assert isinstance(contexts, (list, tuple))
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        params = {"contexts": list(contexts)}
        self.response = Response(self.put(url, params=params), "Contexts")
        return self.response.transform()

    def add_required_status_checks_contexts_of_protected_branch(
        self, owner, repo, branch, contexts
    ):
        assert isinstance(contexts, (list, tuple))
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        params = {"contexts": list(contexts)}
        self.response = Response(self.post(url, params=params), "Contexts")
        return self.response.transform()

    def remove_required_status_checks_contexts_of_protected_branch(
        self, owner, repo, branch
    ):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204

    def get_pr_review_enforcement_of_protected_branch(self, owner, repo, branch):
        _mime = "application/vnd.github.luke-cage-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        self.response = Response(
            self.get(url, **{"Accept": _mime}), "PRReviewEnforcement"
        )
        return self.response.transform()

    def update_pr_review_enforcement_of_protected_branch(
        self,
        owner,
        repo,
        branch,
        dismissal_restrictions,
        dismiss_stale_reviews,
        require_code_owner_reviews,
        required_approving_review_count,
    ):
        _mime = "application/vnd.github.luke-cage-preview+json"
        params = {
            "dismissal_restrictions": dismissal_restrictions,
            "dismiss_stale_reviews": dismiss_stale_reviews,
            "require_code_owner_reviews": require_code_owner_reviews,
            "required_approving_review_count": required_approving_review_count,
        }
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "PRReviewEnforcement"
        )
        return self.response.transform()

    def remove_pr_review_enforcement_of_protected_branch(self, owner, repo, branch):
        _mime = "application/vnd.github.luke-cage-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204

    def required_signatures_of_protected_branch(self, owner, repo, branch):
        _mime = "application/vnd.github.zzzax-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        self.response = Response(
            self.get(url, **{"Accept": _mime}), "RequiredSignatures"
        )
        return self.response.transform()

    def add_required_signatures_of_protected_branch(self, owner, repo, branch):
        _mime = "application/vnd.github.zzzax-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        self.response = Response(
            self.post(url, **{"Accept": _mime}), "RequiredSignatures"
        )
        return self.response.transform()

    def remove_required_signatures_of_protected_branch(self, owner, repo, branch):
        _mime = "application/vnd.github.zzzax-preview+json"
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204

    def admin_enforcement_of_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        self.response = Response(self.get(url), "AdminEnforcementOfProtectedBranch")
        return self.response.transform()

    def add_admin_enforcement_of_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        self.response = Response(self.post(url), "AdminEnforcementOfProtectedBranch")
        return self.response.transform()

    def remove_admin_enforcement_of_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204

    def restrictions_of_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        self.response = Response(self.get(url), "RestrictionsOfProtectedBranch")
        return self.response.transform()

    def remove_restrictions_of_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204

    def teams_with_access_to_protected_branch(self, owner, repo, branch):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        _mime = "application/vnd.github.hellcat-preview+json"
        self.response = Response(
            self.get(url, **{"Accept": _mime}), "RestrictionsOfProtectedBranch"
        )
        return self.response.transform()

    def replace_team_restrictions_to_protected_branch(self, owner, repo, branch, array):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        _mime = "application/vnd.github.hellcat-preview+json"
        params = {"array": array}
        self.response = Response(
            self.put(url, params=params, **{"Accept": _mime}),
            "RestrictionsOfProtectedBranch",
        )
        return self.response.transform()

    def add_team_restrictions_to_protected_branch(self, owner, repo, branch, array):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        _mime = "application/vnd.github.hellcat-preview+json"
        params = {"array": array}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}),
            "RestrictionsOfProtectedBranch",
        )
        return self.response.transform()

    def remove_team_restrictions_of_protected_branch(self, owner, repo, branch, array):
        url = f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        _mime = "application/vnd.github.hellcat-preview+json"
        params = {"array": array}
        self.response = Response(
            self.delete(url, params=params, **{"Accept": _mime}),
            "RestrictionsOfProtectedBranch",
        )
        return self.response.status_code == 204
