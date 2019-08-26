from requests import get

url = "https://api.github.com/users/{user}/repos?per_page={per_page}"

class Clone:
    def __init__(self, auth_token, user_name, per_page):
        self.auth_token = auth_token
        self.user_name = user_name
        self.per_page = per_page

    def clone(self):
