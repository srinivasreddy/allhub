from allhub.response import Response


class MarkDownMixin:
    def render_markdown(self, text, mode="markdown", content=None, **kwargs):
        url = "/markdown"
        params = {"text": text, "mode": mode, "content": content}
        self.response = Response(self.post(url, params=params, **kwargs), "Markdown")
        return self.response.transform()

    def render_markdown_raw_mode(self, text, **kwargs):
        url = "/markdown/raw"
        params = {"text": text}
        self.response = Response(
            self.post(url, params=params, **{"Content-Type": "text/plain"}, **kwargs),
            "MarkdownRaw",
        )
        return self.response.transform()
