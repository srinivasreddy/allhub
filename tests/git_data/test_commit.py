from tests.utils import allhub
from datetime import datetime, timezone


class TestGitCommit:
    def test_git_commit(self):
        sha = "63dedef48bba9d54f13b958237696505fa665796"
        response = allhub.commit("python", "cpython", sha)
        assert response.sha == sha
        assert response.commit.author.name == "Adorilson Bezerra"

    def test_create_git_commit(self):
        # TODO: This test is failing now.
        commits = allhub.commits("test-github42", "cpython", per_page=1)
        commit = commits[0]
        message = "First commit!!!"
        tree = commit.commit.tree.sha
        parents = [parent.sha for parent in commit.parents]
        author = {
            "name": "Srinivas Reddy Thatiparthy",
            "email": "sr.thatiparthy@gmail.com",
            "date": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
        }
        committer = {
            "name": "Srinivas Reddy Thatiparthy",
            "email": "sr.thatiparthy@gmail.com",
            "date": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
        }
        signature = ""

        response = allhub.create_git_commit(
            "test-github42",
            "hello-world",
            message,
            tree,
            parents,
            author,
            committer,
            signature,
        )
        assert response is not None
        assert allhub.response.status_code == 201
