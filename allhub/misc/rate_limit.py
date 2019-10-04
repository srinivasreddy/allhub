from allhub.response import Response


class RateLimitMixin:
    def rate_limit(self):
        url = "/rate_limit"
        self.response = Response(self.get(url), "RateLimit")
        return self.response.transform()
