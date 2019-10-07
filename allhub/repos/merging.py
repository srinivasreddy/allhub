from allhub.response import Response


class MergingMixin:
    def merge(self, owner, repo, base, head, commit_message):
        url = f"/repos/{owner}/{repo}/merges"
        params = {"base": base, "head": head, "commit_message": commit_message}
        self.response = Response(self.post(url, params=params), "Merge")
        return self.response.transform()
