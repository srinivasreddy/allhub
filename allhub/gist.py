from .transform import transform


class GistMixin:
    def gist_comments(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments"
        return transform("GistComments", self.get_partial(url).json())

    def gist_comment(self, gist_id, comment_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments/{comment_id}"
        return transform("GistComment", self.get_partial(url).json())

    def list_user_gists(self):
        url = f"https://api.github.com/users/{self.user_name}/gists"
        return transform("UserGists", self.get_partial(url).json())

    def list_public_gists(self):
        url = f"https://api.github.com/users/gists/public"
        return transform("PublicGists", self.get_partial(url).json())

    def list_starred_gists(self):
        url = f"https://api.github.com/users/gists/public"
        return transform("StarredGists", self.get_partial(url).json())

    def gist(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}"
        return transform("Gist", self.get_partial(url).json())
