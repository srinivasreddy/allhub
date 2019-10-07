from allhub.response import Response

# TODO: Downloads API is deprecated.
# Write a deprecation warning.


class DownloadMixin:
    def downloads(self, owner, repo):
        url = f"/repos/{owner}/{repo}/downloads"
        self.response = Response(self.get(url), "Downloads")
        return self.response.transform()

    def download(self, owner, repo, download_id):
        url = f"/repos/{owner}/{repo}/downloads/{download_id}"
        self.response = Response(self.get(url), "Downloads")
        return self.response.transform()

    def delete_download(self, owner, repo, download_id):
        url = f"/repos/{owner}/{repo}/downloads/{download_id}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"delete_download(.....) returned:{self.response.status_code}, instead it should return 204."
        )
