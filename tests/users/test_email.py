import pytest
from .utils import allhub


@pytest.fixture(scope="module")
def cleanup():
    allhub.delete_email(["reddy@gmail.com"])
    yield
    allhub.toggle_email_visibility("sr.thatiparthy@gmail.com", "public")


class TestEmail:
    def test_list_email(self, cleanup):
        assert len(allhub.list_email()) > 1

    def test_add_email(self, cleanup):
        email_length = len(allhub.list_email())
        allhub.add_email(["reddy@gmail.com"])
        assert len(allhub.list_email()) == email_length + 1

    def test_toggle_email_visibility(self, cleanup):
        allhub.add_email(["reddy@gmail.com"])
        visibility = [
            email
            for email in allhub.list_email()
            if email.email == "sr.thatiparthy@gmail.com"
        ][0].visibility
        data = allhub.toggle_email_visibility("sr.thatiparthy@gmail.com", "public")[0]
        assert data.visibility != visibility
        data = allhub.toggle_email_visibility("sr.thatiparthy@gmail.com", "public")[0]
        assert data.visibility == visibility
