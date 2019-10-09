from allhub.tests.utils import allhub


class TestWebHooks:
    def test_repo_hooks(self):
        response = allhub.repo_hooks("python", "cpython")
        assert response is not None
