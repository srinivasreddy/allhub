from allhub.tests.utils import allhub


class TestMeta:
    def test_meta(self):
        response = allhub.meta()
        # NOTE: This response includes Values are mostly None
        # Needs to know the reason.
        assert "verifiable_password_authentication" in response
        assert "hooks" in response
        assert "api" in response
        assert "web" in response
