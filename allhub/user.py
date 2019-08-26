import requests
import multiprocessing
from multiprocessing import Pool
import subprocess


def distribute_work(_url):
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
    def __init__(self, auth_token, user_name):
        self.auth_token = auth_token
        self.user_name = user_name
        # TODO: I assume the max repos per a user is 100.
        # TODO: Maybe need to revisit the assumption.
        self.clone_url = (
            f"https://api.github.com/users/{self.user_name}/repos?per_page=100"
        )

    @property
    def clone_urls(self):
        list_of_repos = requests.get(
            self.clone_url.format(user=self.user_name),
            headers={"Authorization": self.auth_token},
        ).json()
        return [repo["clone_url"] for repo in list_of_repos]

    def clone(self, urls=None):
        if urls is None:
            urls = self.clone_urls
        if not isinstance(urls, (tuple, list)):
            raise AttributeError("urls should be list or tuple")
        with Pool(processes=multiprocessing.cpu_count()) as p:
            p.map(distribute_work, urls)
