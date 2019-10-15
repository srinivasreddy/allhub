from tests.utils import allhub
from datetime import datetime, timezone


class TestGitCommit:
    def test_git_commit(self):
        sha = "63dedef48bba9d54f13b958237696505fa665796"
        response = allhub.commit("python", "cpython", sha)
        assert response.sha == sha
        assert response.commit.author.name == "Adorilson Bezerra"

    def test_create_git_commit(self):
        commits = allhub.commits("test-github42", "cpython", per_page=1)
        commit = commits[0]
        message = "First commit!!!"
        tree = commit.commit.tree.sha
        parents = [commit.sha]
        author = {
            "name": "Srinivas Reddy Thatiparthy",
            "email": "sr.thatiparthy@gmail.com",
            "date": datetime.utcnow()
            .replace(tzinfo=timezone.utc)
            .replace(microsecond=0)
            .isoformat(),
        }
        committer = {
            "name": "Srinivas Reddy Thatiparthy",
            "email": "sr.thatiparthy@gmail.com",
            "date": datetime.utcnow()
            .replace(tzinfo=timezone.utc)
            .replace(microsecond=0)
            .isoformat(),
        }
        signature = ""

        response = allhub.create_git_commit(
            "test-github42",
            "cpython",
            message,
            tree,
            parents,
            author,
            committer,
            signature,
        )
        assert allhub.response.status_code == 201
        assert response.sha is not None
        assert response.committer.name == committer["name"]
        assert response.committer.email == committer["email"]
        assert response.committer.date.replace("Z", "+00:00") == committer["date"]
        assert response.author.name == author["name"]
        assert response.author.email == author["email"]
        assert response.author.date.replace("Z", "+00:00") == author["date"]
        assert response.message == message
        assert (
            len([parent for parent in response.parents if parent.sha == commit.sha])
            == 1
        )
