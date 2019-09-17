from allhub.repos import Response


class GistCommentsMixin:
    def gist_comments(self, gist_id):
        url = f"/users/gists/{gist_id}/comments"
        self.response = Response(self.get(url), "GistComments")
        return self.response.transform()

    def gist_comment(self, gist_id, comment_id):
        url = f"/users/gists/{gist_id}/comments/{comment_id}"
        self.response = Response(self.get(url), "GistComment")
        return self.response.transform()
