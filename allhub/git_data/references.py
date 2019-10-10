from allhub.response import Response


class ReferencesMixin:
    def git_reference(self, owner, repo, ref):
        url = f"/repos/{owner}/{repo}/git/ref/{ref}"
        self.response = Response(self.get(url), "Reference")
        return self.response.transform()

    def matching_git_references(self, owner, repo, ref):
        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"
        self.response = Response(self.get(url), "References")
        return self.response.transform()

    def create_git_reference(self, owner, repo, ref, sha):
        url = f"/repos/{owner}/{repo}/git/refs"
        params = {"ref": ref, "sha": sha}
        self.response = Response(self.post(url, params=params), "Reference")
        return self.response.transform()

    def update_git_reference(self, owner, repo, ref, sha, force=False):
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"
        params = {"sha": sha, "force": force}
        self.response = Response(self.patch(url, params=params), "Reference")
        return self.response.transform()

    def delete_git_reference(self, owner, repo, ref):
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
