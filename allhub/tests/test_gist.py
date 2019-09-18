import os
from allhub.user import User
from tempfile import NamedTemporaryFile

user = User(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)

named_file = NamedTemporaryFile(delete=False)
named_file.write(b"Hello world!!!")
named_file.close()


class TestGist:
    @staticmethod
    def delete_gist(gist_id):
        assert user.delete_gist(gist_id)

    def test_create_gist(self):
        gist = user.create_gist([named_file.name], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        TestGist.delete_gist(gist.id)

    def test_edit_gist(self):
        gist = user.create_gist([named_file.name], "Create a gist", public=False)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        edited_gist = user.edit_gist(
            gist.id, [named_file.name], "Modified the Created gist"
        )
        assert user.response.status_code == 200
        assert edited_gist.owner.login == user.user_name
        new_gist = user.gist(edited_gist.id)
        assert new_gist.description == "Modified the Created gist"
        TestGist.delete_gist(edited_gist.id)

    def test_delete_gist(self):
        gist = user.create_gist([named_file.name], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.delete_gist(gist.id)

    def test_is_gist_starred(self):
        gist = user.create_gist([named_file.name], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id)
        assert user.delete_gist(gist.id)

    def test_gist_unstarred(self):
        gist = user.create_gist([named_file.name], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id)
        assert user.unstar_gist(gist.id)

    def test_gist_starred(self):
        gist = user.create_gist([named_file.name], "Create a gist", public=True)
        assert user.response.status_code == 201
        assert gist.owner.login == user.user_name
        assert user.is_gist_starred(gist.id)
        assert user.unstar_gist(gist.id)
        assert user.star_gist(gist.id)
        assert user.delete_gist(gist.id)

    def test_gists(self):
        user.create_gist([named_file.name], "Create a gist", public=True)
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

    def test_gist_forks(self):
        forks = user.gist_forks("9620683")
        assert len(forks) > 0

    def test_fork_gist(self):
        fork = user.fork_gist("9620683")
        gist = user.gist(fork.id)
        assert user.delete_gist(fork.id)
        gist = user.gist(fork.id)
        assert gist.message == "Not Found"
        assert user.response.status_code == 404

    def test_gist_revision(self):
        description = "Create a gist"
        modified_description = "Modified the created gist"
        gist = user.create_gist([named_file.name], description, public=True)
        edited_gist = user.edit_gist(gist.id, [named_file.name], modified_description)
        gist = user.gist_revision(edited_gist.id, edited_gist.history[1].version)
        assert gist.description == modified_description
        assert (
            user.gist_revision(
                edited_gist.id, edited_gist.history[0].version
            ).description
            == modified_description
        )
