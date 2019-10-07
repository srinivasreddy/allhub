from allhub.response import Response

_mime = "application/vnd.github.black-panther-preview+json"


class CommunityMixin:
    def community_profile_metrics(self, owner, repo):
        url = f"/repos/{owner}/{repo}/community/profile"
        self.response = Response(self.get(url, **{"Accept": _mime}), "CommunityProfile")
        return self.response.transform()
