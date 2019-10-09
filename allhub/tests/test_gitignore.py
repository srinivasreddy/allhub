from .utils import allhub


class TestGitIgnore:
    def test_gitignore_templates(self):
        # TODO: Not sure `git_ignore_templates` is working anymore?
        response = allhub.git_ignore_templates()
        assert response is not None
        single_response = allhub.git_ignore_template("C")
        assert "name" in single_response
        assert single_response["name"] == "C"
