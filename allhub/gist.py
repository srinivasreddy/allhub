class GistMixin:
    def gist_comments(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments"
        return self.get_partial(url).json()

    def gist_comment(self, gist_id, comment_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments/{comment_id}"
        return self.get_partial(url).json()

    def list_user_gists(self):
        url = f"https://api.github.com/users/{self.user_name}/gists"
        return self.get_partial(url).json()

    def list_public_gists(self):
        url = f"https://api.github.com/users/gists/public"
        return self.get_partial(url).json()

    def list_starred_gists(self):
        url = f"https://api.github.com/users/gists/public"
        return self.get_partial(url).json()

    def gist(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}"
        return self.get_partial(url).json()
