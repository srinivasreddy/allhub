from allhub.response import Response


class ContentsMixin:
    def readme(self, owner, repo, ref="master", media_type=None):
        url = "/repos/{owner}/{repo}/readme".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, params={"ref": ref}), "Readme")
        return self.response.transform()

    def contents(self, owner, repo, path, ref="master"):
        url = "/repos/{owner}/{repo}/contents/{path}".format(
            owner=owner, repo=repo, path=path
        )
        self.response = Response(self.get(url, params={"ref": ref}), "Contents")
        return self.response.transform()

    def create_update_file(
        self, owner, repo, path, message, content, sha, branch, committer, author
    ):
        url = "/repos/{owner}/{repo}/contents/{path}".format(
            owner=owner, repo=repo, path=path
        )
        params = {
            "message": message,
            "content": content,
            "sha": sha,
            "branch": branch,
            "committer": committer,
            "author": author,
        }
        self.response = Response(self.put(url, params=params), "File")
        return self.response.transform()

    def delete_file(
        self,
        owner,
        repo,
        path,
        message,
        sha,
        committer=None,
        author=None,
        branch="master",
    ):
        url = "/repos/{owner}/{repo}/contents/{path}".format(
            owner=owner, repo=repo, path=path
        )
        params = {"message": message, "sha": sha, "branch": branch}
        if committer:
            params["committer"] = committer
        if author:
            params["author"] = author
        self.response = Response(self.delete(url, params=params), "File")
        return self.response.transform()

    def get_archive_link(self, owner, repo, archive_format, ref):
        url = "/repos/{owner}/{repo}/{archive_format}/{ref}".format(
            owner=owner, repo=repo, archive_format=archive_format, ref=ref
        )
        self.response = Response(self.get(url), "Archive")
        return self.response.transform()
