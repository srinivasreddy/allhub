from allhub.response import Response


class MetaMixin:
    def meta(self):
        url = "/meta"
        self.response = Response(self.get(url), "Meta")
        return self.response.transform()
