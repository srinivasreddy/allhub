from allhub.response import Response


class FeedsMixin:
    """
    GitHub provides several timeline resources in Atom format. The Feeds API lists all
    the feeds available to the authenticated user:

    https://developer.github.com/v3/activity/feeds/

    Timeline: The GitHub global public timeline
    User: The public timeline for any user, using URI template
    Current user public: The public timeline for the authenticated user
    Current user: The private timeline for the authenticated user
    Current user actor: The private timeline for activity created by the authenticated user
    Current user organizations: The private timeline for the organizations the authenticated user is a member of.
    Security advisories: A collection of public announcements that provide information about
    security-related vulnerabilities in software on GitHub.
    """

    def feeds(self, **kwargs):
        """
        List all the feeds in a JSON response - it is a dictionary.
        """
        url = "/feeds"
        self.response = Response(self.get_basic(url, **kwargs), "Feeds")
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

    def current_user_public_feed(self):
        """
        The public timeline for the authenticated user
        """
        url = self.feeds().current_user_public_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    def current_user_feed(self):
        """
        The private timeline for the authenticated user
        """
        url = self.feeds().current_user_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    def current_user_actor_feed(self):
        """
        The private timeline for activity created by the authenticated user
        """
        url = self.feeds().current_user_actor_url
        self.response = Response(self.get_basic(url, Accept="application/atom+xml"), "")
        return self.response.content()

    #  TODO: current_user_organization_url and current_user_organization_urls should be implemented.
