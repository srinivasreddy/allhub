from allhub.response import Response


class DeployKeysMixin:
    def deploy_keys(self, owner, repo):
        url = "/repos/{owner}/{repo}/keys".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "DeployKeys")
        return self.response.transform()

    def deploy_key(self, owner, repo, key_id):
        url = "/repos/{owner}/{repo}/keys/{key_id}".format(
            owner=owner, repo=repo, key_id=key_id
        )
        self.response = Response(self.get(url), "DeployKey")
        return self.response.transform()

    def add_deploy_key(self, owner, repo, title, key, read_only):
        url = "/repos/{owner}/{repo}/keys/".format(owner=owner, repo=repo)
        params = {"title": title, "key": key, "read_only": read_only}
        self.response = Response(self.post(url, params=params), "DeployKey")
        return self.response.transform()

    def remove_deploy_key(self, owner, repo, key_id):
        url = "/repos/{owner}/{repo}/keys/{key_id}".format(
            owner=owner, repo=repo, key_id=key_id
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
