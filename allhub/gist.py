class Gist:
    def gist_comments(self, gist_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments"
        return self.partial(url).json()

    def gist_comment(self, gist_id, comment_id):
        url = f"https://api.github.com/users/gists/{gist_id}/comments/{comment_id}"
        return self.partial(url).json()
