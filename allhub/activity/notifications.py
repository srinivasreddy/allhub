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
        self.response = Response(self.put(url, params=params), "")
        # Status: 205 Reset Content
        # Status: 202 Accepted
        return self.response.status_code == 205 or self.response.status_code == 202
