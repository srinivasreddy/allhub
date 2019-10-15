from tests.utils import allhub
from datetime import datetime, timezone


class TestTags:
    def test_get_tag(self):
        tag_sha = self._create_tag().sha
        resp = allhub.tag("python", "cpython", tag_sha)
        assert resp is not None
        assert resp.sha == tag_sha
        assert allhub.response.status_code == 200

    def _create_tag(self):
        commit = allhub.commits("test-github42", "cpython", per_page=1)[0]
        tagger = {
            "name": "Srinivas Reddy Thatiparthy",
            "email": "sr.thatiparthy@gmail.com",
            "date": str(
                datetime.now()
                .replace(microsecond=0)
                .replace(tzinfo=timezone.utc)
                .isoformat()
            ).replace("+00:00", "Z"),
        }
        response = allhub.create_tag(
            "test-github42",
            "cpython",
            tag="3.4555",
            message="This is a test tag",
            object=commit.sha,
            type="commit",
            tagger=tagger,
        )
        assert response.sha is not None
        assert response.tagger == tagger
        assert allhub.response.status_code == 201
        return response

    def test_create_tag(self):
        self._create_tag()
