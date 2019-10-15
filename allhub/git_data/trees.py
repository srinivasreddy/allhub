from allhub.response import Response


class TreesMixin:
    def git_tree(self, repo, owner, tree_sha):
        url = "/repos/{owner}/{repo}/git/trees/{tree_sha}".format(
            owner=owner, repo=repo, tree_sha=tree_sha
        )
        self.response = Response(self.get(url), "GitTree")
        return self.response.transform()

    def git_tree_recursively(self, repo, owner, tree_sha):
        url = "/repos/{owner}/{repo}/git/trees/{tree_sha}".format(
            owner=owner, repo=repo, tree_sha=tree_sha
        )
        self.response = Response(self.get(url, params={"recursive": 1}), "GitTree")
        return self.response.transform()

    def create_git_tree(self, repo, owner, tree, base_tree):
        assert isinstance(tree, (list, tuple))
        url = "/repos/{owner}/{repo}/git/trees".format(owner=owner, repo=repo)
        params = {"tree": list(tree), "base_tree": base_tree}
        self.response = Response(self.post(url, params=params), "GitTree")
        return self.response.transform()
