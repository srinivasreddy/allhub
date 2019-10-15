from tests.utils import allhub


class TestTags:
    def test_get_tag(self):
        resp = allhub.tag("python", "cpython", "3.4")
        print(resp)

    def test_create_tag(self):
        pass
