from allhub.response import Response


class PagesSiteMixin:
    def pages_site_info(self, owner, repo):
        url = "/repos/{owner}/{repo}/pages".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "PagesInfo")
        return self.response.transform()

    def enable_pages_site(self, owner, repo, source_branch, source_path):
        params = {"source": {"branch": source_branch, "path": source_path}}
        url = "/repos/{owner}/{repo}/pages".format(owner=owner, repo=repo)
        self.response = Response(
            self.post(
                url,
                params=params,
                **{"Accept": "application/vnd.github.switcheroo-preview+json"},
            ),
            "PagesInfo",
        )
        return self.response.transform()

    def disable_pages_site(self, owner, repo):
        url = "/repos/{owner}/{repo}/pages".format(owner=owner, repo=repo)
        self.response = Response(
            self.delete(
                url, **{"Accept": "application/vnd.github.switcheroo-preview+json"}
            ),
            "",
        )
        return self.response.status_code == 204

    def update_pages_site(self, owner, repo, cname, source):
        params = {"cname": cname, "source": source}
        url = "/repos/{owner}/{repo}/pages".format(owner=owner, repo=repo)
        self.response = Response(
            self.put(
                url,
                params=params,
                **{"Accept": "application/vnd.github.switcheroo-preview+json"},
            ),
            "PagesInfo",
        )
        return self.response.status_code == 204

    def request_pages_build(self, owner, repo):
        url = "/repos/{owner}/{repo}/pages/builds".format(owner=owner, repo=repo)
        self.response = Response(self.post(url), "PagesInfo")
        return self.response.transform()

    def pages_build(self, owner, repo):
        url = "/repos/{owner}/{repo}/pages/builds".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "PagesInfo")
        return self.response.transform()

    def latest_pages_build(self, owner, repo):
        url = "/repos/{owner}/{repo}/pages/builds/latest".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "PagesInfo")
        return self.response.transform()

    def get_pages_build(self, owner, repo, build_id):
        url = "/repos/{owner}/{repo}/pages/builds/{build_id}".format(
            owner=owner, repo=repo, build_id=build_id
        )
        self.response = Response(self.get(url), "PagesInfo")
        return self.response.transform()
