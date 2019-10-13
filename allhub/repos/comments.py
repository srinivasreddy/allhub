from allhub.response import Response


class CommentsMixin:
    def repo_comments(self, owner, repo):
        _mime = "application/vnd.github.squirrel-girl-preview"
        url = "/repos/{owner}/{repo}/comments".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **{"Accept": _mime}), "Comments")
        return self.response.transform()

    def commit_comments(self, owner, repo, commit_sha):
        _mime = "application/vnd.github.squirrel-girl-preview"
        url = "/repos/{owner}/{repo}/commits/{commit_sha}/comments".format(
            owner=owner, repo=repo, commit_sha=commit_sha
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "Comment")
        return self.response.transform()

    def create_commit_comment(
        self, owner, repo, commit_sha, body, path, position, line=None
    ):
        url = "/repos/{owner}/{repo}/commits/{commit_sha}/comments".format(
            owner=owner, repo=repo, commit_sha=commit_sha
        )
        params = {"body": body, "path": path, "position": position, "line": line}
        self.response = Response(self.post(url, params=params), "Comment")
        return self.response.transform()

    def single_commit_comment(self, owner, repo, comment_id):
        _mime = "application/vnd.github.squirrel-girl-preview"
        url = "/repos/{owner}/{repo}/comments/{comment_id}".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "Comment")
        return self.response.transform()

    def update_commit_comment(self, owner, repo, comment_id, body):
        _mime = "application/vnd.github.squirrel-girl-preview"
        url = "/repos/{owner}/{repo}/comments/{comment_id}".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        self.response = Response(self.patch(url, **{"Accept": _mime}), "Comment")
        return self.response.transform()

    def delete_commit_comment(self, owner, repo, comment_id):
        url = "/repos/{owner}/{repo}/comments/{comment_id}".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
