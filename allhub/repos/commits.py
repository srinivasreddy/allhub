from allhub.response import Response


class CommitMixin:
    def commits(
        self,
        owner,
        repo,
        sha=None,
        path=None,
        author=None,
        since=None,
        until=None,
        **kwargs
    ):
        url = "/repos/{owner}/{repo}/commits".format(owner=owner, repo=repo)
        params = {}
        if sha:
            params["sha"] = sha
        if path:
            params["path"] = path
        if author:
            params["author"] = author
        if since:
            params["until"] = until
        self.response = Response(self.get(url, **kwargs), "Commits")
        return self.response.transform()

    def commit(self, owner, repo, ref):
        url = "/repos/{owner}/{repo}/commits/{ref}".format(
            owner=owner, repo=repo, ref=ref
        )
        self.response = Response(self.get(url), "Commit")
        return self.response.transform()

    def compare_commits(self, owner, repo, base, head):
        url = "/repos/{owner}/{repo}/compare/{base}...{head}".format(
            owner=owner, repo=repo, base=base, head=head
        )
        self.response = Response(self.get(url), "Compare")
        return self.response.transform()

    def branches_for_head_commit(self, owner, repo, commit_sha):
        _mime = "application/vnd.github.groot-preview+json"
        url = "/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head".format(
            owner=owner, repo=repo, commit_sha=commit_sha
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "Branches")
        return self.response.transform()

    def prs_for_commit(self, owner, repo, commit_sha):
        _mime = "application/vnd.github.groot-preview+json"
        url = "/repos/{owner}/{repo}/commits/{commit_sha}/pulls".format(
            owner=owner, repo=repo, commit_sha=commit_sha
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "PRs")
        return self.response.transform()
