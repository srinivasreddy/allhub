import multiprocessing
import subprocess
import sys
from distutils.spawn import find_executable
from multiprocessing import Pool

import requests


def check_git_installed():
    # TODO: move to utils.
    git_location = find_executable("git")
    if git_location is None:
        sys.stderr.write(
            "git is not installed. " "Please install git for your operating system.\n"
        )
        sys.exit(-1)


def shell_git_clone(_url):
    # TODO: How to recover from the network failure, existing repos??
    command = f"git clone {_url}"
    subprocess.call(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )


class User:
    def __init__(self, user_name, auth_token):
        self.user_name = user_name
        self.auth_token = auth_token
        # TODO: I assume the max repos per a user is 100.
        # TODO: Maybe need to revisit the assumption.
        self.clone_url = (
            f"https://api.github.com/users/{self.user_name}/repos?per_page=100"
        )

    @property
    def clone_urls(self):
        check_git_installed()  # TODO: Move this call to decorator.
        list_of_repos = requests.get(
            self.clone_url.format(user=self.user_name),
            headers={"Authorization": self.auth_token},
        ).json()
        return [repo["clone_url"] for repo in list_of_repos]

    def _build_clone_url(self, repo_name):
        return f"https://github.com/{self.user_name}/{repo_name}.git"

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
                f"repo_name should be string, instead got {type(repo_name)}"
            )
        clone_url = self._build_clone_url(repo_name)
        shell_git_clone(clone_url)
