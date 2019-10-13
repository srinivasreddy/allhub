from allhub.response import Response


class TagsMixin:
    def tag(self, owner, repo, tag_sha):
        url = "/repos/{owner}/{repo}/git/tags/{tag_sha}".format(
            owner=owner, repo=repo, tag_sha=tag_sha
        )
        self.response = Response(self.get(url), "Tag")
        return self.response.transform()

    def create_tag(self, owner, repo, tag, message, object, type, tagger):
        url = "/repos/{owner}/{repo}/git/tags".format(owner=owner, repo=repo)
        params = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
            "tagger": tagger,
        }
        self.response = Response(self.post(url, params=params), "Tag")
        return self.response.transform()
