from allhub.tests.utils import allhub


class TestEmoji:
    def test_emojis(self):
        response = allhub.emojis()
        assert response is not None
        assert "+1" in response
        assert "-1" in response
        assert "wheel_of_dharma" in response
        assert "shit" in response
