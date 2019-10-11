import pytest
from tests.utils import allhub


class TestNotifications:
    @staticmethod
    def helper(notifications, class_name):
        assert len(notifications) > 0
        assert notifications[0].__class__.__name__ == class_name
        assert notifications[0].created_at is not None
        assert notifications[0]["created_at"] is not None

    def test_notifications(self):
        notifications = allhub.notifications(all=True)
        # TODO: Revisit this test case.
        # create notification events by other means and check for notifications.
        assert len(notifications) == 0

    def test_notifications_in_repo(self):
        notifications = allhub.notifications_in_repo("python", "cpython")
        # TODO: Revisit this test case.
        # create notification events by other means and check for notifications.
        assert len(notifications) == 0

    def test_mark_notifications_as_read(self):
        assert allhub.mark_notifications_read() is True
        # TODO: Create notifications and mark all as read.
        # TODO: Delete notifications and mark all as read.

    def test_mark_repo_notifications_as_read(self):
        assert allhub.mark_repo_notifications_read("python", "cpython") is True
        # TODO: Create notifications and mark all as read.
        # TODO: Delete notifications and mark all as read.

    @pytest.mark.skip()
    def test_view_single_thread(self):
        thread = allhub.view_single_thread("532")
        assert TestNotifications.helper(thread, "Thread")

    @pytest.mark.skip()
    def test_mark_single_thread(self):
        assert allhub.mark_thread_read("532") is True

    @pytest.mark.skip()
    def test_get_thread_subscription(self):
        thread = allhub.get_thread_subscription("532")
        assert TestNotifications.helper(thread, "ThreadSubscription")

    @pytest.mark.skip()
    def test_set_thread_subscription(self):
        assert allhub.set_thread_subscription("532") is True

    @pytest.mark.skip()
    def test_delete_thread_subscription(self):
        assert allhub.delete_thread_subscription("532") is True
