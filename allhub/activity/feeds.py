from allhub.response import Response


class FeedsMixin:
    def feeds(self):
        """
        List all the feeds in a JSON response.Though we use plural here response
        is a dictionary not list.
        """
        url = "/feeds"
        self.response = Response(self.get(url), "Feeds")
        return self.response.transform()

    def security_advisory_feed(self):
        url = self.feeds()["security_advisories_url"]
        self.response = Response(
            self.get(url, Accept="application/atom+xml"), "SecurityAdvFeed"
        )
        return self.response.content()

    def timeline_feed(self):
        url = self.feeds()._links.timeline.href
        self.response = Response(
            self.get(url, Accept="application/atom+xml"), "TimelineFeed"
        )
        return self.response.content()

    def user_feed(self, username):
        url = self.feeds()._links.user.href.format(user=username)
        self.response = Response(
            self.get(url, Accept="application/atom+xml"), "UserFeed"
        )
        return self.response.content()

    def current_user_feed(self):
        """
        This is feed is gives only public data.
        :return:
        """
        url = self.feeds()._links.current_user_public.href
        self.response = Response(
            self.get(url, Accept="application/atom+xml"), "CurrentUserFeed"
        )
        return self.response.content()
