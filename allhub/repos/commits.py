from allhub.response import Response


class CommitMixin:
    def commits(
        self, owner, repo, sha=None, path=None, author=None, since=None, until=None
    ):
        url = f"/repos/{owner}/{repo}/commits"
        params = {}
        if sha:
            params["sha"] = sha
        if path:
            params["path"] = path
        if author:
            params["author"] = author
        if since:
            params["until"] = until
        self.response = Response(self.get(url), "Commits")
        return self.response.transform()

    def commit(self, owner, repo, ref):
        url = f"/repos/{owner}/{repo}/commits/{ref}"
        self.response = Response(self.get(url), "Commit")
        return self.response.transform()

    def compare_commits(self, owner, repo, base, head):
        url = f"/repos/{owner}/{repo}/compare/{base}...{head}"
        self.response = Response(self.get(url), "Compare")
        return self.response.transform()

    def branches_for_head_commit(self, owner, repo, commit_sha):
        _mime = "application/vnd.github.groot-preview+json"
        url = f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Branches")
        return self.response.transform()

    def prs_for_commit(self, owner, repo, commit_sha):
        _mime = "application/vnd.github.groot-preview+json"
        url = f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls"
        self.response = Response(self.get(url, **{"Accept": _mime}), "PRs")
        return self.response.transform()
