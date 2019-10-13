from allhub.response import Response


class MergingMixin:
    def merge(self, owner, repo, base, head, commit_message):
        url = "/repos/{owner}/{repo}/merges".format(owner=owner, repo=repo)
        params = {"base": base, "head": head, "commit_message": commit_message}
        self.response = Response(self.post(url, params=params), "Merge")
        return self.response.transform()
