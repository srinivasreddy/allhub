import requests
import multiprocessing
from multiprocessing import Process, Pool
import os


url = "https://api.github.com/users/{user}/repos?per_page={per_page}"
auth_token = os.environ.get("AUTH_TOKEN")
cpu_count = multiprocessing.cpu_count()


class Clone:
    def __init__(self, auth_token, user_name, per_page):
        self.auth_token = auth_token
        self.user_name = user_name
        self.per_page = per_page

    def _distribute_work(self, url):
        pass

    def clone(self):
        list_of_repos = requests.get(
            url.format(url, user=self.user_name, per_page=self.per_page),
            headers={"Authorization": self.auth_token},
        ).json()
        urls = [repo["clone_url"] for repo in list_of_repos]
        with Pool(processes=multiprocessing.cpu_count()) as p:
            p.map(self._distribute_work, urls)
