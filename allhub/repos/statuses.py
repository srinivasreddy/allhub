from allhub.response import Response


class StatusMixin:
    def create_status(self, owner, repo, sha, state, target_url, description, context):
        url = "/repos/{owner}/{repo}/statuses/{sha}".format(
            owner=owner, repo=repo, sha=sha
        )
        params = {
            "state": state,
            "target_url": target_url,
            "description": description,
            "context": context,
        }
        self.response = Response(self.post(url, params=params), "Status")
        return self.response.transform()

    def statuses_for_ref(self, owner, repo, ref):
        url = "/repos/{owner}/{repo}/commits/{ref}/statuses".format(
            owner=owner, repo=repo, ref=ref
        )
        self.response = Response(self.get(url), "Statuses")
        return self.response.transform()

    def combined_status_for_ref(self, owner, repo, ref):
        url = "/repos/{owner}/{repo}/commits/{ref}/status".format(
            owner=owner, repo=repo, ref=ref
        )
        self.response = Response(self.get(url), "CombinedStatus")
        return self.response.transform()
