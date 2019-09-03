from .transform import transform


class GistMixin:
    def gist_comments(self, gist_id):
        url = f"users/gists/{gist_id}/comments"
        return transform("GistComments", self.get(url))

    def gist_comment(self, gist_id, comment_id):
        url = f"users/gists/{gist_id}/comments/{comment_id}"
        return transform("GistComment", self.get(url))

    def list_user_gists(self):
        url = f"users/{self.user_name}/gists"
        return transform("UserGists", self.get(url))

    def list_public_gists(self):
        url = "users/gists/public"
        return transform("PublicGists", self.get(url))

    def list_starred_gists(self):
        url = f"users/gists/public"
        return transform("StarredGists", self.get(url))

    def gist(self, gist_id):
        url = f"users/gists/{gist_id}"
        return transform("UserGist", self.get(url))
