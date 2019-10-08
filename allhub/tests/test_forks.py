from .utils import allhub


class TestForks:
    def test_create_fork(self):
        response = allhub.create_fork("srinivasreddy", "allhub")
        assert response.name == "allhub"
        assert response.owner.login == "test-github42"

    def test_forks(self):
        response = allhub.forks("srinivasreddy", "allhub")
        data = [
            fork
            for fork in response
            if fork.owner.login == "test-github42" and fork.name == "allhub"
        ]
        assert len(data) == 1
