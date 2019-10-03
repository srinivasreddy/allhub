from allhub import AllHub
import os

user = AllHub(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)


class TestWatching:
    @staticmethod
    def helper(_list, class_name, attr):
        assert len(_list) > 0
        assert _list[0].__class__.__name__ == class_name
        assert getattr(_list[0], attr) is not None
        assert _list[0][attr] is not None

    def test_list_watchers(self):
        watchers = user.list_watchers("python", "cpython")
        TestWatching.helper(watchers, "Watcher", "login")

    def test_repos_watched_by(self):
        repos = user.repos_watched_by("srinivasreddy")
        TestWatching.helper(repos, "WatchedRepo", "default_branch")

    def test_repos_watched(self):
        repos = user.repos_watched()
        TestWatching.helper(repos, "WatchedRepo", "default_branch")

    def test_set_subscription(self):
        subscription = user.set_subscription("python", "cpython")
        subscription.subscribed is True
        subscription["subscribed"] is True
        subscription.ignored is False
        subscription["ignored"] is False

    def test_repo_subscription(self):
        subscription = user.repo_subscription("python", "cpython")
        subscription.subscribed is True
        subscription["subscribed"] is True
        subscription.ignored is False
        subscription["ignored"] is False

    def test_delete_subscription(self):
        assert user.delete_subscription("python", "cpython") is True
        # Second assertion is redundant but it is a testimony for
        # API's Idempotency.
        assert user.delete_subscription("python", "cpython") is True
