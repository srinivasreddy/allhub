from allhub.user import User
import os

user = User(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)


class TestStarring:
    @staticmethod
    def helper(_list, class_name):
        assert len(_list) > 0
        assert _list[0].__class__.__name__ == class_name
        assert _list[0].login is not None
        assert _list[0]["login"] is not None

    def test_stargazers(self):
        stars = user.stargazers("python", "cpython")
        TestStarring.helper(stars, "StarGazer")
        # pass starred_at=True
        stars = user.stargazers("python", "cpython", starred_at=True)
        assert stars[0].starred_at is not None
        assert stars[0].user.login is not None
        assert stars[0]["user"]["login"] is not None

    def test_starred(self):
        stars = user.starred()
        stars[0].owner.login is not None
        stars[0]["owner"]["login"] is not None
        stars = user.starred(starred_at=True)
        assert stars[0].starred_at is not None
        assert stars[0].repo.owner.login is not None
        assert stars[0]["repo"]["owner"]["login"] is not None

    def test_starred_by(self):
        stars = user.starred_by("srinivasreddy")
        stars[0].owner.login is not None
        stars[0]["owner"]["login"] is not None
        stars = user.starred_by("srinivasreddy", starred_at=True)
        assert stars[0].starred_at is not None
        assert stars[0].repo.owner.login is not None
        assert stars[0]["repo"]["owner"]["login"] is not None

    def test_is_starred(self):
        assert user.is_starred("python", "cpython") is False

    def test_star_repo(self):
        assert user.star_repo("python", "cpython") is True

    def test_unstar_repo(self):
        assert user.unstar_repo("python", "cpython") is True
