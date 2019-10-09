from .utils import allhub


class TestLicense:
    def test_licenses(self):
        response = allhub.licenses()
        licenses = [resp.key for resp in response]
        assert set(
            [
                "agpl-3.0",
                "apache-2.0",
                "bsd-2-clause",
                "bsd-3-clause",
                "epl-2.0",
                "gpl-2.0",
                "gpl-3.0",
                "lgpl-2.1",
                "lgpl-3.0",
                "mit",
                "mpl-2.0",
                "unlicense",
            ]
        ).issubset(set(licenses))

    def test_license(self):
        response = allhub.license("mit")
        assert response["key"] == "mit"

    def test_repo_license(self):
        response = allhub.license_contents("python", "cpython")
        assert response.license.key == "other"
