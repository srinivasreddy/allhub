from .response import Response


class GistMixin:
    def gist_comments(self, gist_id):
        url = f"/users/gists/{gist_id}/comments"
        self.response = Response(self.get(url), "GistComments")
        return self.response.transform()

    def gist_comment(self, gist_id, comment_id):
        url = f"/users/gists/{gist_id}/comments/{comment_id}"
        self.response = Response(self.get(url), "GistComment")
        return self.response.transform()

    def list_user_gists(self):
        url = f"/users/{self.user_name}/gists"
        self.response = Response(self.get(url), "UserGists")
        return self.response.transform()

    def list_public_gists(self):
        url = "/users/gists/public"
        self.response = Response(self.get(url), "PublicGists")
        return self.response.transform()

    def list_starred_gists(self):
        url = "/users/gists/public"
        self.response = Response(self.get(url), "StarredGists")
        return self.response.transform()

    def gist(self, gist_id):
        url = f"/users/gists/{gist_id}"
        self.response = Response(self.get(url), "UserGist")
        return self.response.transform()
