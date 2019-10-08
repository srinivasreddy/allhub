from .utils import allhub


class TestForks:
    def test_create_fork(self):
        response = allhub.create_fork("srinivasreddy", "allhub")
        assert response.name == "allhub"
        assert response.owner.login == "test-github42"

    def test_forks(self):
        response = allhub.create_fork("python", "cpython")
        for response in allhub.iterator(allhub.forks, "python", "cpython"):
            data = [
                fork
                for fork in response
                if fork.owner.login == "test-github42" and fork.name == "cpython"
            ]
            if data:
                assert len(data) == 1
                break
        else:
            assert False, 'The repo "python/cpython" should have been forked.'
