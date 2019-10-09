from allhub.response import Response


class CommitMixin:
    def commit(self, owner, repo, commit_sha):
        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"
        self.response = Response(self.get(url), "Commit")
        return self.response.transform()

    def create_commit(
        self, owner, repo, message, tree, parents, author, committer, signature
    ):
        url = f"/repos/{owner}/{repo}/git/commits"
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
