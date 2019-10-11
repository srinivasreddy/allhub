from tests.utils import allhub


class TestRateLimit:
    def test_rate_limit(self):
        response = allhub.rate_limit()
        assert response.resources.core.limit == 5000
