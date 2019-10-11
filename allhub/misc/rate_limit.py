from allhub.response import Response


class RateLimitMixin:
    def rate_limit(self, **kwargs):
        url = "/rate_limit"
        self.response = Response(self.get(url, **kwargs), "RateLimit")
        return self.response.transform()
