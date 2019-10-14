from tests.utils import allhub


class TestGitCommit:
    def test_git_commit(self):
        sha = "63dedef48bba9d54f13b958237696505fa665796"
        response = allhub.commit("python", "cpython", sha)
        assert response.sha == sha
        assert response.commit.author.name == "Adorilson Bezerra"

    def test_create_git_commit(self):
        pass
