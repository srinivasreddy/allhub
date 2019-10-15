from allhub.response import Response


class NotificationsMixin:
    def notifications(
        self, all=False, participating=False, since=None, before=None, **kwargs
    ):
        """
        List all notifications for the current user, sorted by most recently updated.
        """
        url = "/notifications"
        params = {
            "all": all,
            "participating": participating,
            "since": since,
            "before": before,
        }
        self.response = Response(
            self.get(url, params=params, **kwargs), "Notifications"
        )
        return self.response.transform()

    def notifications_in_repo(
        self,
        owner,
        repo,
        all=False,
        participating=False,
        since=None,
        before=None,
        **kwargs,
    ):
        """
        List all notifications for the current user.
        """
        url = "/repos/{owner}/{repo}/notifications".format(owner=owner, repo=repo)
        params = {
            "all": all,
            "participating": participating,
            "since": since,
            "before": before,
        }
        self.response = Response(
            self.get(url, params=params, **kwargs), "NotificationsRepo"
        )
        return self.response.transform()

    def mark_notifications_read(self, **kwargs):
        url = "/notifications"
        params = None
        if "last_read_at" in kwargs:
            params = {"last_read_at": kwargs.pop("last_read_at")}
        self.response = Response(self.put(url, params=params, **kwargs), "")
        # Status: 205 Reset Content
        # Status: 202 Accepted
        return self.response.status_code in (205, 202)

    def mark_repo_notifications_read(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/notifications".format(owner=owner, repo=repo)
        params = {}
        if "last_read_at" in kwargs:
            params = {"last_read_at": kwargs.pop("last_read_at")}
        self.response = Response(self.put(url, params=params, **kwargs), "")
        # Status: 205 Reset Content
        # Status: 202 Accepted
        return self.response.status_code in (205, 202)

    def view_single_thread(self, thread_id, **kwargs):
        """
        View a single thread
        """
        url = "/notifications/threads/{thread_id}".format(thread_id=thread_id)
        self.response = Response(self.get(url, **kwargs), "Thread")
        return self.response.transform()

    def mark_thread_read(self, thread_id, **kwargs):
        """
        Mark thread as read.
        """
        url = "/notifications/threads/{thread_id}".format(thread_id=thread_id)
        # Status: 205 Reset Content
        self.response = Response(self.put(url, **kwargs), "")
        return self.response.status_code == 205

    def get_thread_subscription(self, thread_id, **kwargs):
        """
        Get thread subscription
        """
        url = "/notifications/threads/{thread_id}/subscription".format(
            thread_id=thread_id
        )
        self.response = Response(self.get(url, **kwargs), "ThreadSubscription")
        return self.response.transform()

    def set_thread_subscription(self, thread_id, **kwargs):
        """
        Set thread subscription
        """
        url = "/notifications/threads/{thread_id}/subscription".format(
            thread_id=thread_id
        )
        params = None
        if "ignored" in kwargs:
            params = {"ignored": kwargs.pop("ignored")}
        self.response = Response(
            self.put(url, params=params, **kwargs), "ThreadSubscription"
        )
        return self.response.transform()

    def delete_thread_subscription(self, thread_id, **kwargs):
        """
        Delete thread subscription
        """
        url = "/notifications/threads/{thread_id}/subscription".format(
            thread_id=thread_id
        )
        self.response = Response(self.delete(url, **kwargs), "")
        return self.response.status_code == 204
