from tests.utils import allhub


class TestMarkdown:
    def test_render_markdown(self):
        response = allhub.render_markdown(
            "Hello world github/linguist#1 **cool**, and #1!", "gfm"
        )
        assert "Hello world" in response

    def test_render_markdown_raw_mode(self):
        response = allhub.render_markdown_raw_mode(
            "Hello world github/linguist#1 **cool**, and #1!"
        )
        assert "Hello world" in response
