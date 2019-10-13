from allhub.response import Response


class CommitMixin:
    def git_commit(self, owner, repo, commit_sha):
        url = "/repos/{owner}/{repo}/git/commits/{commit_sha}".format(
            owner=owner, repo=repo, commit_sha=commit_sha
        )
        self.response = Response(self.get(url), "Commit")
        return self.response.transform()

    def create_git_commit(
        self, owner, repo, message, tree, parents, author, committer, signature
    ):
        url = "/repos/{owner}/{repo}/git/commits".format(owner=owner, repo=repo)
        params = {
            "message": message,
            "tree": tree,
            "parents": parents,
            "author": author,
            "committer": committer,
            "signature": signature,
        }
        self.response = Response(self.post(url, params=params), "Commit")
        return self.response.transform()
