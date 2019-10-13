from allhub.response import Response

_mime = "application/vnd.github.black-panther-preview+json"


class CommunityMixin:
    def community_profile_metrics(self, owner, repo):
        url = "/repos/{owner}/{repo}/community/profile".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **{"Accept": _mime}), "CommunityProfile")
        return self.response.transform()
