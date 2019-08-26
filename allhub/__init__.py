from .github import *
import os

auth_token = os.environ.get("AUTH_TOKEN")
user_name = os.environ.get("USER_NAME")
per_page = os.environ.get("PER_PAGE")
clone = Clone(auth_token, user_name, per_page)
