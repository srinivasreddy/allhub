from allhub.response import Response


class FeedsMixin:
    def feeds(self):
        """
        List all the feeds in a JSON response.
        """
        url = "/feeds"
        self.response = Response(self.get(url), "Feeds")
        return self.response.transform()

    def security_advisory_feed(self):
        url = self.feeds()["security-advisories"]
        self.response = Response(
            self.get(url, Accept="application/atom+xml"), "SecurityAdvFeed"
        )
        return self.response.content()
