import os
from allhub.user import User

user = User(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)


class TestGist:
    @staticmethod
    def delete_gist(gist_id):
        assert user.delete_gist(gist_id)

    def test_create_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        TestGist.delete_gist(gist.id)

    def test_edit_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=False)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        edited_gist = user.edit_gist(
            gist.id, ["test_watching.py"], "Modified the Created gist"
        )
        assert user.response.status_code == 200
        assert edited_gist.owner.login == user.user_name
        TestGist.delete_gist(edited_gist.id)

    def test_delete_gist(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.delete_gist(gist.id)

    def test_is_gist_starred(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id)
        assert user.delete_gist(gist.id)

    def test_gist_unstarred(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id)
        assert user.unstar_gist(gist.id)

    def test_gist_starred(self):
        gist = user.create_gist(["test_watching.py"], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id)
        assert user.unstar_gist(gist.id)
        assert user.star_gist(gist.id)
        assert user.delete_gist(gist.id)

    def test_gists(self):
        user.create_gist(["test_watching.py"], "Create a gist", public=True)
        gists = user.gists()
        for gist in gists:
            assert user.delete_gist(gist.id)

    def test_starred_gists(self):
        for gist in user.starred_gists():
            assert user.unstar_gist(gist.id)
        gists = user.public_gists()
        for gist in gists:
            assert user.star_gist(gist.id)
        starred_gists = user.starred_gists()
        assert len(starred_gists) == len(gists)
        for gist in gists:
            assert user.unstar_gist(gist.id)
