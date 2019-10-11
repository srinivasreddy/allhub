import pytest
from tests.utils import allhub


@pytest.fixture(scope="module")
def setup_teardown():
    assert allhub.unblock("srinivasreddy42")
    yield


class TestBlocking:
    def test_block_user(self, setup_teardown):
        assert allhub.block("srinivasreddy42")
        assert allhub.unblock("srinivasreddy42")
        assert allhub.blocked("srinivasreddy42") is False

    def test_list_blocked_users(self, setup_teardown):
        assert allhub.block("srinivasreddy42")
        blocked_users = allhub.list_blocked_users()
        assert len(blocked_users) == 1
        assert blocked_users[0].login == "srinivasreddy42"
        assert allhub.unblock("srinivasreddy42")
        assert allhub.blocked("srinivasreddy42") is False
