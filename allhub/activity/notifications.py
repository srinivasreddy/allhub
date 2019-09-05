from allhub.response import Response


class NotificationsMixin:
    def notifications(self, **kwargs):
        """
        List all notifications for the current user, sorted by most recently updated.
        """
        url = "/notifications"
        params = [
            ("all", kwargs.pop("all", False)),
            ("participating", kwargs.pop("participating", False)),
        ]
        if "since" in kwargs:
            params.append(("since", kwargs.pop("since")))
        if "before" in kwargs:
            params.append(("before", kwargs.pop("before")))
        self.response = Response(
            self.get(url, params=params, **kwargs), "Notifications"
        )
        return self.response.transform()

    def notifications_in_repo(self, owner, repo, **kwargs):
        """
        List all notifications for the current user.
        """
        url = f"/repos/{owner}/{repo}/notifications"
        params = [
            ("all", kwargs.pop("all", False)),
            ("participating", kwargs.pop("participating", False)),
        ]
        if "since" in kwargs:
            params.append(("since", kwargs.pop("since")))
        if "before" in kwargs:
            params.append(("before", kwargs.pop("before")))
        self.response = Response(
            self.get(url, params=params, **kwargs), "NotificationsRepo"
        )
        return self.response.transform()

    def mark_notifications_read(self, **kwargs):
        url = "/notifications"
        params = None
        if "last_read_at" in kwargs:
            params = [("last_read_at", kwargs.pop("last_read_at"))]
        # Status: 205 Reset Content
        # Status: 202 Accepted
        return Response(self.put(url, params=params), "").status_code in (205, 202)

    def mark_repo_notifications_read(self, owner, repo, **kwargs):
        url = f"/repos/{owner}/{repo}/notifications"
        params = None
        if "last_read_at" in kwargs:
            params = [("last_read_at", kwargs.pop("last_read_at"))]
        # Status: 205 Reset Content
        # Status: 202 Accepted
        return Response(self.put(url, params=params), "").status_code in (205, 202)

    def view_single_thread(self, thread_id, **kwargs):
        """
        View a single thread
        """
        url = f"/notifications/threads/{thread_id}"
        self.response = Response(self.get(url, **kwargs), "Thread")
        return self.response.transform()

    def mark_thread_read(self, thread_id, **kwargs):
        """
        Mark thread as read.
        """
        url = f"/notifications/threads/{thread_id}"
        # Status: 205 Reset Content
        return Response(self.put(url), "").status_code == 205

    def get_thread_subscription(self, thread_id, **kwargs):
        """
        Get thread subscription
        """
        url = f"/notifications/threads/{thread_id}/subscription"
        self.response = Response(self.get(url, **kwargs), "ThreadSubscription")
        return self.response.transform()

    def set_thread_subscription(self, thread_id, **kwargs):
        """
        Set thread subscription
        """
        url = f"/notifications/threads/{thread_id}/subscription"
        params = None
        if "ignored" in kwargs:
            params = [("ignored", kwargs.pop("ignored"))]
        self.response = Response(
            self.put(url, params=params, **kwargs), "ThreadSubscription"
        )
        return self.response.transform()

    def delete_thread_subscription(self, thread_id, **kwargs):
        """
        Delete thread subscription
        """
        url = f"/notifications/threads/{thread_id}/subscription"
        # Status code 204:  No Content
        return Response(self.delete(url, **kwargs), "").status_code == 204
