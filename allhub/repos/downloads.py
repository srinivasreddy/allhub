from allhub.response import Response

# TODO: Downloads API is deprecated.
# Write a deprecation warning.


class DownloadMixin:
    def downloads(self, owner, repo):
        url = "/repos/{owner}/{repo}/downloads".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "Downloads")
        return self.response.transform()

    def download(self, owner, repo, download_id):
        url = "/repos/{owner}/{repo}/downloads/{download_id}".format(
            owner=owner, repo=repo, download_id=download_id
        )
        self.response = Response(self.get(url), "Downloads")
        return self.response.transform()

    def delete_download(self, owner, repo, download_id):
        url = "/repos/{owner}/{repo}/downloads/{download_id}".format(
            owner=owner, repo=repo, download_id=download_id
        )
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "delete_download(.....) returned:{status_code}, instead it should return 204.".format(
                status_code=self.response.status_code
            )
        )
