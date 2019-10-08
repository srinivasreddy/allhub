from tempfile import NamedTemporaryFile
from .utils import allhub


named_file = NamedTemporaryFile(delete=False)
named_file.write(b"Hello world!!!")
named_file.close()


class TestGist:
    def test_create_gist(self):
        gist = allhub.create_gist([named_file.name], "Create a gist", public=True)
        assert allhub.response.status_code == 201
        assert gist.owner.login == allhub.username
        assert allhub.delete_gist(gist.id)

    def test_edit_gist(self):
        gist = allhub.create_gist([named_file.name], "Create a gist", public=False)
        assert allhub.response.status_code == 201
        assert gist.owner.login == allhub.username
        edited_gist = allhub.edit_gist(
            gist.id, [named_file.name], "Modified the Created gist"
        )
        assert allhub.response.status_code == 200
        assert edited_gist.owner.login == allhub.username
        new_gist = allhub.gist(edited_gist.id)
        assert new_gist.description == "Modified the Created gist"
        assert allhub.delete_gist(gist.id)

    def test_delete_gist(self):
        gist = allhub.create_gist([named_file.name], "Create a gist", public=True)
        assert allhub.response.status_code == 201
        assert gist.owner.login == allhub.username
        assert allhub.delete_gist(gist.id)

    def test_is_gist_starred(self):
        gist = allhub.create_gist([named_file.name], "Create a gist", public=True)
        assert allhub.response.status_code == 201
        assert gist.owner.login == allhub.username
        assert allhub.is_gist_starred(gist.id)
        assert allhub.delete_gist(gist.id)

    def test_gist_unstarred(self):
        gist = allhub.create_gist([named_file.name], "Create a gist", public=True)
        assert allhub.response.status_code == 201
        assert gist.owner.login == allhub.username
        assert allhub.is_gist_starred(gist.id)
        assert allhub.unstar_gist(gist.id)

    def test_gist_starred(self):
        gist = allhub.create_gist([named_file.name], "Create a gist", public=True)
        assert allhub.response.status_code == 201
        assert gist.owner.login == allhub.username
        assert allhub.is_gist_starred(gist.id)
        assert allhub.unstar_gist(gist.id)
        assert allhub.star_gist(gist.id)
        assert allhub.delete_gist(gist.id)

    def test_gists(self):
        allhub.create_gist([named_file.name], "Create a gist", public=True)
        gists = allhub.gists()
        for gist in gists:
            assert allhub.delete_gist(gist.id)

    def test_starred_gists(self):
        for gist in allhub.starred_gists():
            assert allhub.unstar_gist(gist.id)
        gists = allhub.public_gists()
        for gist in gists:
            assert allhub.star_gist(gist.id)
        starred_gists = allhub.starred_gists()
        assert len(starred_gists) == len(gists)
        for gist in gists:
            assert allhub.unstar_gist(gist.id)

    def test_gist_forks(self):
        forks = allhub.gist_forks("9620683")
        assert len(forks) > 0

    def test_fork_gist(self):
        fork = allhub.fork_gist("9620683")
        gist = allhub.gist(fork.id)
        assert allhub.delete_gist(fork.id)
        gist = allhub.gist(fork.id)
        assert gist.message == "Not Found"
        assert allhub.response.status_code == 404

    def test_gist_revision(self):
        description = "Create a gist"
        modified_description = "Modified the created gist"
        gist = allhub.create_gist([named_file.name], description, public=True)
        edited_gist = allhub.edit_gist(gist.id, [named_file.name], modified_description)
        gist = allhub.gist_revision(edited_gist.id, edited_gist.history[1].version)
        assert gist.description == modified_description
        gist = allhub.gist_revision(edited_gist.id, edited_gist.history[0].version)
        # TODO: Shouldn't i get the starting description.
        assert gist.description == modified_description
        gist = allhub.gist(edited_gist.id)
        assert gist.description == modified_description
        assert allhub.delete_gist(gist.id)

    def test_gist_commits(self):
        description = "Create a gist"
        modified_description = "Modified the created gist"
        gist = allhub.create_gist([named_file.name], description, public=True)
        edited_gist = allhub.edit_gist(gist.id, [named_file.name], modified_description)
        assert len(allhub.gist_commits(edited_gist.id)) == 2
        assert allhub.delete_gist(edited_gist.id)

    def test_gist_create_comment(self):
        description = "Create a gist"
        comment = "this is the first comment."
        edited_comment = "This is the edited comment"
        gist = allhub.create_gist([named_file.name], description, public=True)
        comment_obj = allhub.create_gist_comment(gist.id, comment)
        assert allhub.response.status_code == 201
        assert comment_obj.body == comment
        comment_obj = allhub.gist_comment(gist.id, comment_obj.id)
        assert comment_obj.body == comment
        comment_obj = allhub.edit_gist_comment(gist.id, comment_obj.id, edited_comment)
        comment_obj = allhub.gist_comment(gist.id, comment_obj.id)
        assert comment_obj.body == edited_comment
        assert allhub.delete_gist_comment(gist.id, comment_obj.id)
