from tests.utils import allhub


class TestCOC:
    def test_codes_of_conduct(self):
        response = allhub.codes_of_conduct()
        assert len(response) > 0

    def test_code_of_conduct(self):
        response = allhub.code_of_conduct("contributor_covenant")
        assert "contributor_covenant" in response.values()
        assert len(response) > 0

    def test_repo_code_of_conduct(self):
        response = allhub.repo_code_of_conduct("django", "django")
        assert response.code_of_conduct is not None
        assert len(response) > 0

    def test_contents_of_repo_code_of_conduct(self):
        response = allhub.contents_of_repo_code_of_conduct("rust-lang", "rust")
        assert "key" in response
        assert "name" in response
        assert "html_url" in response
        assert "url" in response
        assert "body" in response
        assert len(response) > 0
