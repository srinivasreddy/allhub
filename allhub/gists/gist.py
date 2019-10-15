from allhub.response import Response
from allhub.util import ErrorAPICode, validate_iso8601_string
from pathlib import Path


class GistMixin:
    def user_gists(self, **kwargs):
        url = "/users/{username}/gists".format(username=self.username)
        self.response = Response(self.get(url, **kwargs), "UserGists")
        return self.response.transform()

    def gists(self, since=None, **kwargs):
        url = "/gists"
        if since:
            validate_iso8601_string()
        params = {"since": since}
        self.response = Response(self.get(url, params=params, **kwargs), "Gists")
        return self.response.transform()

    def public_gists(self, since=None, **kwargs):
        if since:
            validate_iso8601_string()
        params = {"since": since}
        url = "/gists/public"
        self.response = Response(self.get(url, params=params, **kwargs), "PublicGists")
        return self.response.transform()

    def starred_gists(self, since=None, **kwargs):
        """
        :return: List the authenticated user's starred gists.
        """
        if since:
            validate_iso8601_string()
        params = {"since": since}
        url = "/gists/starred"
        self.response = Response(self.get(url, params=params, **kwargs), "StarredGists")
        return self.response.transform()

    def gist(self, gist_id, **kwargs):
        url = "/gists/{gist_id}".format(gist_id=gist_id)
        self.response = Response(self.get(url, **kwargs), "Gist")
        return self.response.transform()

    def gist_revision(self, gist_id, sha):
        url = "/gists/{gist_id}/{sha}".format(gist_id=gist_id, sha=sha)
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
        url = "/gists/{gist_id}".format(gist_id=gist_id)
        files_contents = {}
        for _file in files:
            _path = Path(_file)
            files_contents[_path.name] = {"content": open(_file).read()}
        params = {"files": files_contents, "description": description}
        self.response = Response(self.patch(url, params=params), "Gist")
        return self.response.transform()

    def gist_commits(self, gist_id, **kwargs):
        url = "/gists/{gist_id}/commits".format(gist_id=gist_id)
        self.response = Response(self.get(url, **kwargs), "GitCommits")
        return self.response.transform()

    def star_gist(self, gist_id):
        url = "/gists/{gist_id}/star".format(gist_id=gist_id)
        return Response(self.put(url, **{"Content-Length": "0"}), "").status_code == 204

    def unstar_gist(self, gist_id):
        url = "/gists/{gist_id}/star".format(gist_id=gist_id)
        return Response(self.delete(url), "").status_code == 204

    def is_gist_starred(self, gist_id):
        url = "/gists/{gist_id}/star".format(gist_id=gist_id)
        code = Response(self.get(url), "").status_code
        if code == 204:
            return True
        elif code == 404:
            return False
        else:
            raise ErrorAPICode(
                "The url:{url} returned status code: {code}. Maybe try after sometime?".format(
                    url=url, code=code
                )
            )

    def fork_gist(self, gist_id):
        url = "/gists/{gist_id}/forks".format(gist_id=gist_id)
        self.response = Response(self.post(url), "GistFork")
        return self.response.transform()

    def gist_forks(self, gist_id, **kwargs):
        url = "/gists/{gist_id}/forks".format(gist_id=gist_id)
        self.response = Response(self.get(url, **kwargs), "GistForks")
        return self.response.transform()

    def delete_gist(self, gist_id):
        url = "/gists/{gist_id}".format(gist_id=gist_id)
        return Response(self.delete(url), "").status_code == 204
