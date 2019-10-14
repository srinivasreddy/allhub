from tests.utils import allhub


class TestReferences:
    def test_get_git_reference(self):
        response = allhub.git_reference("python", "cpython", "heads/master")
        assert response.ref == "refs/heads/master"
        assert response.object.sha is not None
        assert response.object.type == "commit"
        response = allhub.git_reference("python", "cpython", "heads/2.7")
        assert response.ref == "refs/heads/2.7"
        assert response.object.sha is not None
        assert response.object.type == "commit"

    def test_get_git_matching_references(self):
        responses = allhub.matching_git_references("python", "cpython", "heads/3.6")
        response = responses[0]
        assert response.ref == "refs/heads/3.6"
        assert response.object.sha is not None
        assert response.object.type == "commit"
