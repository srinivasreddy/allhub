from allhub.response import Response


class NotificationsMixin:
    def notifications(self, **headers):
        """
        List all notifications for the current user, sorted by most recently updated.
        """
        url = "/notifications"
        self.response = Response(self.get(url, **headers), "Notifications")
        return self.response.transform()

    def notifications_in_repo(self, owner, repo, **headers):
        """
        List all notifications for the current user.
        """
        url = f"/repos/{owner}/{repo}/notifications"
        self.response = Response(self.get(url, **headers), "NotificationsRepo")
        return self.response.transform()

    def mark_notifications_read(self):
        url = "/notifications"
        self.response = Response(self.put(url), "")
        return self.response.status_code == 205
