from allhub.response import Response


class GistCommentsMixin:
    def gist_comments(self, gist_id, **kwargs):
        """
        The following are the MIME types supported by this method,

        application/vnd.github.VERSION.raw+json
        application/vnd.github.VERSION.text+json
        application/vnd.github.VERSION.html+json
        application/vnd.github.VERSION.full+json

        :param gist_id:
        :param kwargs:
        :return:
        """
        url = f"/gists/{gist_id}/comments"
        self.response = Response(self.get(url, **kwargs), "GistComments")
        return self.response.transform()

    def create_gist_comment(self, gist_id, body):
        url = f"/gists/{gist_id}/comments"
        params = {"body": body}
        self.response = Response(self.post(url, params=params), "GistComments")
        return self.response.transform()

    def edit_gist_comment(self, gist_id, comment_id, body):
        url = f"/gists/{gist_id}/comments/{comment_id}"
        params = {"body": body}
        self.response = Response(self.patch(url, params=params), "GistComments")
        return self.response.transform()

    def gist_comment(self, gist_id, comment_id, **kwargs):
        """
        The following are the MIME types supported by this method,

        application/vnd.github.VERSION.raw+json
        application/vnd.github.VERSION.text+json
        application/vnd.github.VERSION.html+json
        application/vnd.github.VERSION.full+json

        :param gist_id:
        :param kwargs:
        :return:
        """
        url = f"/gists/{gist_id}/comments/{comment_id}"
        self.response = Response(self.get(url, **kwargs), "GistComment")
        return self.response.transform()

    def delete_gist_comment(self, gist_id, comment_id):
        url = f"/gists/{gist_id}/comments/{comment_id}"
        self.response = Response(self.delete(url), "GistComments")
        return self.response.status_code == 204
