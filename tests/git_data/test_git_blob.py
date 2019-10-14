from tests.utils import allhub


class TestGitBlob:
    def test_get_blob(self):
        blob = "02f523c42d355f27b70b709b0723898d5f2cb721"
        response = allhub.blob("python", "cpython", blob)
        assert response.encoding == "base64"
        assert (
            response.url
            == "https://api.github.com/repos/python/cpython/git/blobs/{blob}".format(
                blob=blob
            )
        )

    def test_create_blob(self):
        response = allhub.create_blob(
            "test-github42", "hello-world", "Hello world!! This is srinivas reddy"
        )
        assert allhub.response.status_code == 201
        assert response.sha is not None
