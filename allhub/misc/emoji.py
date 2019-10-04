from allhub.response import Response


class EmojiMixin:
    def emojis(self):
        url = "/emojis"
        self.response = Response(self.get(url), "Emoji")
        return self.response.transform()
