from .transform import transform
from urllib import parse
import re

pattern = re.compile(r"<(?P<data>.*?)>")  # simple pattern to match <...........>

# TODO: Headers currently lives on response object, maybe should we access headers
# through response.headers.next_link, response.headers.current_page_number.


class Response:
    def __init__(self, response, class_name):
        self.response = response
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

    @property
    def current_page_number(self):
        if self.next_page_number is None and self.prev_page_number is None:
            return 1
        if self.next_page_number is None:
            return int(self.prev_page_number) + 1
        if self.prev_page_number is None:
            return int(self.next_page_number) - 1

    @property
    def next_page_number(self):
        if self.next_link() is None:
            return None
        parsed_url = parse.urlparse(self.next_link())
        parsed_data = parse.parse_qs(parsed_url.query)
        return int(parsed_data["page"][0])

    @property
    def prev_page_number(self):
        if self.prev_link() is None:
            return None
        parsed_url = parse.urlparse(self.prev_link())
        parsed_data = parse.parse_qs(parsed_url.query)
        return int(parsed_data["page"][0])

    @property
    def last_page_number(self):
        if self.last_link() is None:
            return None
        parsed_url = parse.urlparse(self.last_link())
        parsed_data = parse.parse_qs(parsed_url.query)
        return int(parsed_data["page"][0])

    @property
    def first_page_number(self):
        if self.first_link() is None:
            return None
        parsed_url = parse.urlparse(self.first_link())
        parsed_data = parse.parse_qs(parsed_url.query)
        return int(parsed_data["page"][0])

    def _extract_link(self, rel_name):
        for link in self.headers().get("Link", "").split(","):
            if rel_name in link:
                match = re.match(pattern, link.split(";")[0].strip())
                return match["data"]
        return None

    def next_link(self):
        return self._extract_link('rel="next"')

    def prev_link(self):
        return self._extract_link('rel="prev"')

    def last_link(self):
        return self._extract_link('rel="last"')

    def first_link(self):
        return self._extract_link('rel="first"')

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
