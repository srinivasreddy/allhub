import os
from .utils import allhub


class TestFeeds:
    def test_feeds(self):
        feeds = allhub.feeds()
        assert len(feeds) > 0

    def test_security_advisory_feed(self):
        feed = allhub.security_advisory_feed()
        assert len(feed) > 0

    def test_timeline_feed(self):
        feed = allhub.timeline_feed()
        assert len(feed) > 0

    def test_user_feed(self):
        feed = allhub.user_feed(os.environ.get("USERNAME"))
        assert len(feed) > 0

    def test_current_user_public_feed(self):
        feed = allhub.current_user_public_feed()
        assert len(feed) > 0

    def test_current_user_feed(self):
        feed = allhub.current_user_feed()
        assert len(feed) > 0

    def test_current_user_actor_feed(self):
        feed = allhub.current_user_actor_feed()
        assert len(feed) > 0
