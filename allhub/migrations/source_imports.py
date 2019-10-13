from allhub.response import Response

from enum import Enum

_mime = "application/vnd.github.barred-rock-preview"


class SourceControlType(Enum):
    SUBVERSION = "subversion"
    GIT = "git"
    MERCURIAL = "mercurial"
    TFVC = "tfvc"  # Team Foundation Version Control
    NONE = None


class SourceImportMixin:
    def start_source_import(
        self,
        owner,
        repo,
        vcs_url,
        vcs_username,
        vcs_password,
        tfvc_project=None,
        vcs=SourceControlType.NONE,
    ):
        url = "/repos/{owner}/{repo}/import".format(owner=owner, repo=repo)
        params = {
            "vcs": vcs.value,
            "vcs_url": vcs_url,
            "vcs_username": vcs_username,
            "vcs_password": vcs_password,
        }
        if vcs == SourceControlType.TFVC:
            params.update({"tfvc_project": tfvc_project})
        self.response = Response(
            self.put(url, params=params, **{"Accept": _mime}), "Import"
        )
        return self.response.transform()

    def import_progress(self, owner, repo):
        url = "/repos/{owner}/{repo}/import".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **{"Accept": _mime}), "Import")
        return self.response.transform()

    def update_import(self, owner, repo, vcs_username, vcs_password):
        url = "/repos/{owner}/{repo}/import".format(owner=owner, repo=repo)
        params = {"vcs_username": vcs_username, "vcs_password": vcs_password}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "Import"
        )
        return self.response.transform()

    def import_commit_authors(self, owner, repo, since=None):
        url = "/repos/{owner}/{repo}/import/authors".format(owner=owner, repo=repo)
        params = {}
        if since:
            params["since"] = since
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "Authors"
        )
        return self.response.transform()

    def map_commit_author(self, owner, repo, author_id, email, name):
        url = "/repos/{owner}/{repo}/import/authors/{author_id}".format(
            owner=owner, repo=repo, author_id=author_id
        )
        params = {"email": email, "name": name}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "Author"
        )
        return self.response.transform()

    def set_git_lfs_preference(self, owner, repo, use_lfs):
        url = "/repos/{owner}/{repo}/import/lfs".format(owner=owner, repo=repo)
        params = {"use_lfs": use_lfs}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "Author"
        )
        return self.response.transform()

    def get_large_files(self, owner, repo):
        """
        List files larger than 100MB found during the import
        :param owner:
        :param repo:
        :return:
        """
        url = "/repos/{owner}/{repo}/import/large_files".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **{"Accept": _mime}), "Author")
        return self.response.transform()

    def cancel_import(self, owner, repo):
        url = "/repos/{owner}/{repo}/import".format(owner=owner, repo=repo)
        self.response = Response(self.delete(url, **{"Accept": _mime}), "Author")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "cancel_import(.....) returned {status_code}, instead it should return 204.".format(
                status_code=self.response.status_code
            )
        )
