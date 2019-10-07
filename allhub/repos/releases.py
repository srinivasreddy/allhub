from allhub.response import Response


class ReleaseMixin:
    def releases(self, owner, repo):
        url = f"/repos/{owner}/{repo}/releases"
        self.response = Response(self.get(url), "Releases")
        return self.response.transform()

    def release(self, owner, repo, release_id):
        url = f"/repos/{owner}/{repo}/releases/{release_id}"
        self.response = Response(self.get(url), "Release")
        return self.response.transform()

    def latest_release(self, owner, repo):
        url = f"/repos/{owner}/{repo}/releases/latest"
        self.response = Response(self.get(url), "Release")
        return self.response.transform()

    def latest_release_by_tag_name(self, owner, repo, tag):
        url = f"/repos/{owner}/{repo}/releases/tags/{tag}"
        self.response = Response(self.get(url), "Release")
        return self.response.transform()

    def create_release(
        self,
        owner,
        repo,
        tag_name,
        target_commitish,
        name,
        body,
        draft=False,
        prerelease=False,
    ):
        params = {
            "tag_name": tag_name,
            "target_commitish": target_commitish,
            "name": name,
            "body": body,
            "draft": draft,
            "prerelease": prerelease,
        }
        url = f"/repos/{owner}/{repo}/releases"
        self.response = Response(self.post(url, params=params), "Release")
        return self.response.transform()

    def edit_release(
        self,
        owner,
        repo,
        release_id,
        tag_name,
        target_commitish,
        name,
        body,
        draft=False,
        prerelease=False,
    ):
        params = {
            "tag_name": tag_name,
            "target_commitish": target_commitish,
            "name": name,
            "body": body,
            "draft": draft,
            "prerelease": prerelease,
        }
        url = f"/repos/{owner}/{repo}/releases/{release_id}"
        self.response = Response(self.patch(url, params=params), "Release")
        return self.response.transform()

    def delete_release(self, owner, repo, release_id):
        url = f"/repos/{owner}/{repo}/releases/{release_id}"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204

    def release_assets(self, owner, repo, release_id):
        url = f"/repos/{owner}/{repo}/releases/{release_id}/assets"
        self.response = Response(self.get(url), "ReleaseAssets")
        return self.response.transform()

    # TODO: https://developer.github.com/v3/repos/releases/#upload-a-release-asset

    def release_asset(self, owner, repo, asset_id):
        url = f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        self.response = Response(self.get(url), "ReleaseAsset")
        return self.response.transform()

    def edit_release_asset(self, owner, repo, asset_id, name, label):
        params = {"name": name, "label": label}
        url = f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        self.response = Response(self.patch(url, params=params), "ReleaseAsset")
        return self.response.transform()

    def delete_release_asset(self, owner, repo, asset_id):
        url = f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
