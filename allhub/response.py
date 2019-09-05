from .transform import transform


class Response:
    def __init__(self, response, class_name, transform_resp=True):
        self.response = response
        self.class_name = class_name
        self.transform_resp = transform_resp

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
    def status_code(self):
        return self.response.status_code

    def transform(self):
        if self.transform_resp:
            return transform(self.class_name, self.json())
        else:
            return self.json()

    def content(self):
        return self.response.content

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
