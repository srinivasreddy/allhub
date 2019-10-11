from allhub.response import Response


class MetaMixin:
    def meta(self, **kwargs):
        url = "/meta"
        self.response = Response(self.get(url, **kwargs), "Meta")
        return self.response.transform()
