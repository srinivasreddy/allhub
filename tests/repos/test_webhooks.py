from tests.utils import allhub


class TestWebHooks:
    def test_repo_hooks(self):
        response = allhub.repo_hooks("python", "cpython")
        # TODO: is not done yet.
        assert response is not None
