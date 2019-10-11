from .utils import allhub


class TestStarring:
    @staticmethod
    def helper(_list, class_name):
        assert len(_list) > 0
        assert _list[0].__class__.__name__ == class_name
        assert _list[0].login is not None
        assert _list[0]["login"] is not None

    def test_stargazers(self):
        stars = allhub.stargazers("python", "cpython")
        TestStarring.helper(stars, "StarGazer")
        # pass starred_at=True
        stars = allhub.stargazers("python", "cpython", starred_at=True)
        assert stars[0].starred_at is not None
        assert stars[0].user.login is not None
        assert stars[0]["user"]["login"] is not None

    def test_starred(self):
        stars = allhub.starred()
        stars[0].owner.login is not None
        stars[0]["owner"]["login"] is not None
        stars = allhub.starred(starred_at=True)
        assert stars[0].starred_at is not None
        assert stars[0].repo.owner.login is not None
        assert stars[0]["repo"]["owner"]["login"] is not None

    def test_starred_by(self):
        stars = allhub.starred_by("srinivasreddy")
        stars[0].owner.login is not None
        stars[0]["owner"]["login"] is not None
        stars = allhub.starred_by("srinivasreddy", starred_at=True)
        assert stars[0].starred_at is not None
        assert stars[0].repo.owner.login is not None
        assert stars[0]["repo"]["owner"]["login"] is not None

    def test_is_starred(self):
        assert allhub.is_starred("python", "cpython") is False

    def test_star_repo(self):
        assert allhub.star_repo("python", "cpython") is True

    def test_is_starred_true(self):
        assert allhub.is_starred("python", "cpython") is True

    def test_unstar_repo(self):
        assert allhub.unstar_repo("python", "cpython") is True
