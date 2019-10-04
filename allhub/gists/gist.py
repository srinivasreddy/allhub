from allhub.response import Response
from allhub.util import ErrorAPICode, validate_iso8601_string
from pathlib import Path


class GistMixin:
    def user_gists(self):
        url = f"/users/{self.username}/gists"
        self.response = Response(self.get(url), "UserGists")
        return self.response.transform()

    def gists(self, since=None):
        url = "/gists"
        if since:
            validate_iso8601_string()
        params = {"since": since}
        self.response = Response(self.get(url, params=params), "Gists")
        return self.response.transform()

    def public_gists(self, since=None):
        if since:
            validate_iso8601_string()
        params = {"since": since}
        url = "/gists/public"
        self.response = Response(self.get(url, params=params), "PublicGists")
        return self.response.transform()

    def starred_gists(self, since=None):
        """
        :return: List the authenticated user's starred gists.
        """
        if since:
            validate_iso8601_string()
        params = {"since": since}
        url = "/gists/starred"
        self.response = Response(self.get(url, params=params), "StarredGists")
        return self.response.transform()

    def gist(self, gist_id):
        url = f"/gists/{gist_id}"
        self.response = Response(self.get(url), "Gist")
        return self.response.transform()

    def gist_revision(self, gist_id, sha):
        url = f"/gists/{gist_id}/{sha}"
        self.response = Response(self.get(url), "Gist")
        return self.response.transform()

    def create_gist(self, files, description, public=True):
        url = "/gists"
        files_contents = {}
        for _file in files:
            _path = Path(_file)
            files_contents[_path.name] = {"content": open(_file).read()}
        params = {"files": files_contents, "description": description, "public": public}
        self.response = Response(self.post(url, params=params), "Gist")
        return self.response.transform()

    def edit_gist(self, gist_id, files, description):
        url = f"/gists/{gist_id}"
        files_contents = {}
        for _file in files:
            _path = Path(_file)
            files_contents[_path.name] = {"content": open(_file).read()}
        params = {"files": files_contents, "description": description}
        self.response = Response(self.patch(url, params=params), "Gist")
        return self.response.transform()

    def gist_commits(self, gist_id):
        url = f"/gists/{gist_id}/commits"
        self.response = Response(self.patch(url), "GitCommits")
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
                f"The url:{url} returned status code: {code}. Maybe try after sometime?"
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
