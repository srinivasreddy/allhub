import os
from allhub.user import User

user = User(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)


class TestGist:
    def delete_gist(self, gist_id):
        assert user.delete_gist(gist_id) is True

    def test_create_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        self.delete_gist(gist.id)

    def test_edit_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=False)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        edited_gist = user.edit_gist(
            gist.id, ["test_watching.py"], "Modified the Created gist"
        )
        assert user.response.status_code == 200
        assert edited_gist.owner.login == user.user_name
        self.delete_gist(edited_gist.id)

    def test_delete_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.delete_gist(gist.id) is True

    def test_is_gist_starred(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id) is True
        assert user.delete_gist(gist.id) is True

    def test_gist_unstarred(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id) is True
        assert user.unstar_gist(gist.id) is True

    def test_gist_starred(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id) is True
        assert user.unstar_gist(gist.id) is True
        assert user.star_gist(gist.id) is True
        assert user.delete_gist(gist.id) is True
