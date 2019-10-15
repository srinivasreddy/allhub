from tests.utils import allhub


class TestTrees:
    def test_get_tree(self):
        commit = allhub.commits("test-github42", "cpython", per_page=1)[0]
        tree_sha = commit.commit.tree.sha
        response = allhub.git_tree("test-github42", "cpython", tree_sha)
        assert response is not None

    def test_get_tree_recursively(self):
        pass

    def test_create_tree(self):
        commit = allhub.commits("test-github42", "cpython", per_page=1)[0]
        base_tree = commit.commit.tree.sha
        tree = [
            {"path": "aclocal.m4", "mode": "100644", "type": "blob", "sha": commit.sha}
        ]
        response = allhub.create_git_tree("test-github42", "cpython", tree, base_tree)
        assert response is not None
