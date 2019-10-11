from allhub.response import Response


class EmojiMixin:
    def emojis(self, **kwargs):
        url = "/emojis"
        self.response = Response(self.get(url, **kwargs), "Emoji")
        return self.response.transform()
