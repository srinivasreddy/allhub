from allhub.response import Response

_mime = "application/vnd.github.scarlet-witch-preview+json"


class CodeOfConductMixin:
    def codes_of_conduct(self, **kwargs):
        url = "/codes_of_conduct"
        self.response = Response(self.get(url, **{"Accept": _mime}, **kwargs), "COCs")
        return self.response.transform()

    def code_of_conduct(self, key, **kwargs):
        url = "/codes_of_conduct/{key}".format(key=key)
        self.response = Response(self.get(url, **{"Accept": _mime}, **kwargs), "COC")
        return self.response.transform()

    def repo_code_of_conduct(self, owner, repo):
        url = "/repos/{owner}/{repo}".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **{"Accept": _mime}), "RepoCOC")
        return self.response.transform()

    def contents_of_repo_code_of_conduct(self, owner, repo):
        url = "/repos/{owner}/{repo}/community/code_of_conduct".format(
            owner=owner, repo=repo
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "RepoCOC")
        return self.response.transform()
