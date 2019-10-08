from allhub.response import Response

_mime = "application/vnd.github.scarlet-witch-preview+json"


class CodeOfConductMixin:
    def codes_of_conduct(self):
        url = "/codes_of_conduct"
        self.response = Response(self.get(url, **{"Accept": _mime}), "COCs")
        return self.response.transform()

    def code_of_conduct(self, key):
        url = f"/codes_of_conduct/{key}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "COC")
        return self.response.transform()

    def repo_code_of_conduct(self, owner, repo):
        url = f"/repos/{owner}/{repo}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "RepoCOC")
        return self.response.transform()

    def contents_of_repo_code_of_conduct(self, owner, repo):
        url = f"/repos/{owner}/{repo}/community/code_of_conduct"
        self.response = Response(self.get(url, **{"Accept": _mime}), "RepoCOC")
        return self.response.transform()
