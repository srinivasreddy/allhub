from allhub.response import Response


class BlobMixin:
    def blob(self, owner, repo, file_sha):
        url = "/repos/{owner}/{repo}/git/blobs/{file_sha}".format(
            owner=owner, repo=repo, file_sha=file_sha
        )
        self.response = Response(self.get(url), "Blob")
        return self.response.transform()

    def create_blob(self, owner, repo, content, encoding="utf-8"):
        url = "/repos/{owner}/{repo}/git/blobs".format(owner=owner, repo=repo)
        params = {"content": content, "encoding": encoding}
        self.response = Response(self.post(url, params=params), "Blob")
        return self.response.transform()
