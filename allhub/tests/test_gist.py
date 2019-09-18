import os
from allhub.user import User

user = User(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)


class TestGist:
    def test_create_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
