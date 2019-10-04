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
        url = f"/repos/{owner}/{repo}/import"
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
        url = f"/repos/{owner}/{repo}/import"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Import")
        return self.response.transform()

    def update_import(self, owner, repo, vcs_username, vcs_password):
        url = f"/repos/{owner}/{repo}/import"
        params = {"vcs_username": vcs_username, "vcs_password": vcs_password}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "Import"
        )
        return self.response.transform()

    def import_commit_authors(self, owner, repo, since=None):
        url = f"/repos/{owner}/{repo}/import/authors"
        params = {}
        if since:
            params["since"] = since
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "Authors"
        )
        return self.response.transform()

    def map_commit_author(self, owner, repo, author_id, email, name):
        url = f"/repos/{owner}/{repo}/import/authors/{author_id}"
        params = {"email": email, "name": name}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "Author"
        )
        return self.response.transform()

    def set_git_lfs_preference(self, owner, repo, use_lfs):
        url = f"/repos/{owner}/{repo}/import/lfs"
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
        url = f"/repos/{owner}/{repo}/import/large_files"
        self.response = Response(self.get(url, **{"Accept": _mime}), "Author")
        return self.response.transform()

    def cancel_import(self, owner, repo):
        url = f"/repos/{owner}/{repo}/import"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "Author")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"cancel_import(.....) returned {self.response.status_code}, instead it should return 204."
        )
