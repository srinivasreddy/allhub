from allhub.response import Response


class TagsMixin:
    def tag(self, owner, repo, tag_sha):
        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"
        self.response = Response(self.get(url), "Tag")
        return self.response.transform()

    def create_tag(self, owner, repo, tag, message, object, type, tagger):
        url = f"/repos/{owner}/{repo}/git/tags"
        params = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
            "tagger": tagger,
        }
        self.response = Response(self.post(url, params=params), "Tag")
        return self.response.transform()
