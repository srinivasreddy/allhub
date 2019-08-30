from .transform import transform


class GistMixin:
    def gist_comments(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments"
        return transform("GistComments", self.get(url))

    def gist_comment(self, gist_id, comment_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments/{comment_id}"
        return transform("GistComment", self.get(url))

    def list_user_gists(self):
        url = f"https://api.github.com/users/{self.user_name}/gists"
        return transform("UserGists", self.get(url))

    def list_public_gists(self):
        url = "https://api.github.com/users/gists/public"
        return transform("PublicGists", self.get(url))

    def list_starred_gists(self):
        url = f"https://api.github.com/users/gists/public"
        return transform("StarredGists", self.get(url))

    def gist(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}"
        return transform("Gist", self.get(url))
