from allhub.response import Response


class FeedsMixin:
    def feeds(self):
        """
        List all the feeds in a JSON response.Though we use plural noun here response
        is a dictionary, not list.
        """
        url = "/feeds"
        self.response = Response(self.get_basic(url), "Feeds")
        return self.response.transform()

    def security_advisory_feed(self):
        """
        A collection of public announcements that provide information about
        security-related vulnerabilities in software on GitHub.
        """
        url = self.feeds().security_advisories_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    def timeline_feed(self):
        """
        The GitHub global public timeline
        """
        url = self.feeds().timeline_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    def user_feed(self, username):
        """
        The public timeline for any user.
        """
        url = self.feeds().user_url.format(user=username)
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    def current_user_feed(self):
        """
        The public timeline for the authenticated user
        """
        url = self.feeds().current_user_public_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    def current_user_private_feed(self):
        """
        The private timeline for the authenticated user
        """
        url = self.feeds().current_user_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()
