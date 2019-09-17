from allhub.response import Response
from allhub.util import ErrorAPICode


class GistMixin:
    def user_gists(self):
        url = f"/users/{self.user_name}/gists"
        self.response = Response(self.get(url), "UserGists")
        return self.response.transform()

    def public_gists(self, since=None):
        url = "/gists/public"
        self.response = Response(self.get(url), "PublicGists")
        return self.response.transform()

    def list_starred_gists(self):
        url = "/gists/starred"
        self.response = Response(self.get(url), "StarredGists")
        return self.response.transform()

    def gist(self, gist_id):
        url = f"/users/gists/{gist_id}"
        self.response = Response(self.get(url), "UserGist")
        return self.response.transform()

    def star_gist(self, gist_id):
        url = f"/gists/{gist_id}/star"
        return Response(self.put(url, **{"Content-Length": "0"}), "").status_code == 204

    def unstar_gist(self, gist_id):
        url = f"/gists/{gist_id}/star"
        return Response(self.delete(url), "").status_code == 204

    def is_gist_starred(self, gist_id):
        url = f"/gists/{gist_id}/star"
        code = Response(self.delete(url), "").status_code
        if code == 204:
            return True
        elif code == 404:
            return False
        else:
            raise ErrorAPICode(
                f"The url:{url} returned status code: {code}. May be try after sometime?"
            )

    def fork_gist(self, gist_id):
        url = f"/gists/{gist_id}/forks"
        self.response = Response(self.post(url), "GistFork")
        return self.response.transform()

    def gist_forks(self, gist_id):
        url = f"/gists/{gist_id}/forks"
        self.response = Response(self.get(url), "GistForks")
        return self.response.transform()

    def delete_gist(self, gist_id):
        url = f"/gists/{gist_id}"
        return Response(self.delete(url), "").status_code == 204
