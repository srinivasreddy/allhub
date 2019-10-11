from allhub.response import Response


class LicenseMixin:
    def licenses(self, **kwargs):
        url = "/licenses"
        self.response = Response(self.get(url), "Licenses")
        return self.response.transform()

    def license(self, license_name, **kwargs):
        url = f"/licenses/{license_name}"
        self.response = Response(self.get(url), "License")
        return self.response.transform()

    def license_contents(self, owner, repo):
        url = f"/repos/{owner}/{repo}/license"
        self.response = Response(self.get(url), "LicenseContent")
        return self.response.transform()
