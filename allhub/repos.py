import requests
import multiprocessing
from multiprocessing import Pool
import subprocess


def distribute_work(_url):
    command = f"git clone {_url}"
    subprocess.call(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )


class Repos:
    def __init__(self, auth_token, user_name, per_page=None):
        self.auth_token = auth_token
        self.user_name = user_name
        self.per_page = per_page
        self.clone_url = "https://api.github.com/users/{user}/repos"
        if self.per_page:
            self.clone_url = self.clone_url + "?per_page={per_page}"

    def clone(self):
        list_of_repos = requests.get(
            self.clone_url.format(
                self.clone_url, user=self.user_name, per_page=self.per_page
            ),
            headers={"Authorization": self.auth_token},
        ).json()
        urls = [repo["clone_url"] for repo in list_of_repos]
        with Pool(processes=multiprocessing.cpu_count()) as p:
            p.map(distribute_work, urls)
