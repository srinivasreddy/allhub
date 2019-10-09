from .transform import transform


class Response:
    def __init__(self, response, class_name):
        self.response = response
        # TODO: Add plural and singular class names for list of results.
        self.class_name = class_name

    def headers(self):
        return self.response.headers

    def json(self):
        return self.response.json()

    def oauth_scopes(self):
        """
        Return available scopes for oauth token.
        """
        return self.headers()["X-OAuth-Scopes"]

    def next_link(self):
        for link in self.headers().get("Link", "").split(","):
            if 'rel="next"' in link:
                return link.split(";")[0]
        return None

    def prev_link(self):
        for link in self.headers().get("Link", "").split(","):
            if 'rel="prev"' in link:
                return link.split(";")[0]
        return None

    def last_link(self):
        for link in self.headers().get("Link", "").split(","):
            if 'rel="last"' in link:
                return link.split(";")[0]
        return None

    def first_link(self):
        for link in self.headers().get("Link", "").split(","):
            if 'rel="first"' in link:
                return link.split(";")[0]
        return None

    @property
    def status_code(self):
        return self.response.status_code

    def transform(self):
        if "text/html" in self.headers().get("Content-Type"):
            return str(self.content())
        return transform(self.class_name, self.json())

    def content(self):
        return self.response.content

    @property
    def rate_limit(self):
        """
        The maximum number of requests you're permitted to make per hour.
        """
        interval = self.headers().get("X-RateLimit-Limit")
        return interval and int(interval) or None

    @property
    def rate_limit_remaining(self):
        """
        The number of requests remaining in the current rate limit window.
        """
        interval = self.headers().get("X-RateLimit-Remaining")
        return interval and int(interval) or None

    @property
    def rate_limit_reset(self):
        """
        The time at which the current rate limit window resets in UTC epoch seconds.
        https://en.wikipedia.org/wiki/Unix_time
        """
        # TODO: to be done
        pass

    @property
    def poll_interval(self):
        # All responses may not contain X-Poll-Interval headers.
        interval = self.headers().get("X-Poll-Interval")
        return interval and int(interval) or None

    @property
    def etag(self):
        """
        ETag header helps by determining the result set changed between time.
        :return:
        """
        return self.headers().get("ETag")

    @property
    def last_modified(self):
        """
        Last-Modified header helps in fetching the result set changed between time.
        """
        return self.headers().get("Last-Modified")
