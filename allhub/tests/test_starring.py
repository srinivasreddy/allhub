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

    def test_starred(self):
        pass

    def test_starred_by(self):
        pass

    def test_is_starred(self):
        pass

    def test_star_repo(self):
        pass

    def test_unstar_repo(self):
        pass
