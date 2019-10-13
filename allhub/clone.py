import multiprocessing
from multiprocessing import Pool

import requests

from .util import check_git_installed, shell_git_clone


class CloneMixin:
    @property
    def clone_urls(self):
        check_git_installed()  # TODO: Move this call to decorator.
        list_of_repos = requests.get(
            self.clone_url.format(user=self.username),
            headers={
                "Authorization": "token {auth_token}".format(auth_token=self.auth_token)
            },
        ).json()
        return [repo["clone_url"] for repo in list_of_repos]

    def _build_clone_url(self, repo_name):
        return "https://github.com/{username}/{repo_name}.git".format(
            username=self.username, repo_name=repo_name
        )

    def clone_repos(self, urls=None):
        check_git_installed()
        if urls is None:
            urls = self.clone_urls
        if not isinstance(urls, (tuple, list)):
            raise AttributeError("urls should be list or tuple")
        with Pool(processes=multiprocessing.cpu_count()) as p:
            p.map(shell_git_clone, urls)

    def clone_repo(self, repo_name):
        check_git_installed()
        if not isinstance(repo_name, str):
            raise AttributeError(
                "repo_name should be string, instead got {name}".format(
                    name=type(repo_name)
                )
            )
        clone_url = self._build_clone_url(repo_name)
        shell_git_clone(clone_url)
