from allhub.user import User
import os

user = User(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    True,
    os.environ.get("PASSWORD"),
)


class TestFeeds:
    def test_feeds(self):
        feeds = user.feeds()
        assert len(feeds) > 0

    def test_security_advisory_feed(self):
        feed = user.security_advisory_feed()
        assert len(feed) > 0

    def test_timeline_feed(self):
        feed = user.timeline_feed()
        assert len(feed) > 0

    def test_user_feed(self):
        feed = user.user_feed(os.environ.get("USERNAME"))
        assert len(feed) > 0

    def test_current_user_public_feed(self):
        feed = user.current_user_public_feed()
        assert len(feed) > 0

    def test_current_user_feed(self):
        feed = user.current_user_feed()
        assert len(feed) > 0

    def test_current_user_actor_feed(self):
        feed = user.current_user_actor_feed()
        assert len(feed) > 0
