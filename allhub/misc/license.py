from allhub.response import Response


class LicenseMixin:
    def licenses(self, **kwargs):
        url = "/licenses"
        self.response = Response(self.get(url, **kwargs), "Licenses")
        return self.response.transform()

    def license(self, license_name, **kwargs):
        url = "/licenses/{license_name}".format(license_name=license_name)
        self.response = Response(self.get(url, **kwargs), "License")
        return self.response.transform()

    def license_contents(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/license".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "LicenseContent")
        return self.response.transform()
