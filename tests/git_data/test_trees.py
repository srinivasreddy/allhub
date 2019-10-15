from tests.utils import allhub


class TestTrees:
    def test_get_tree(self):
        response = allhub.git_tree("python", "cpython", "3.8")
        assert response is not None

    def test_get_tree_recursively(self):
        pass

    def test_create_tree(self):
        pass
