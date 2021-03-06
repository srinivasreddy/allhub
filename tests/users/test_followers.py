import os
import pytest
from tests.utils import allhub


@pytest.fixture(scope="module")
def cleanup():
    assert allhub.unfollow("srinivasreddy")
    yield


class TestFollowers:
    def test_list_followers(self):
        assert len(allhub.list_followers("srinivasreddy")) > 1

    def test_follow_unfollow(self, cleanup):
        assert (
            allhub.user_is_following(os.environ.get("GH_USERNAME"), "srinivasreddy")
            is False
        )
        assert allhub.follow("srinivasreddy")
        assert allhub.user_is_following(os.environ.get("GH_USERNAME"), "srinivasreddy")
        assert allhub.unfollow("srinivasreddy")
        assert (
            allhub.user_is_following(os.environ.get("GH_USERNAME"), "srinivasreddy")
            is False
        )
        assert len(allhub.user_following("srinivasreddy")) > 1
        assert len(allhub.following()) > 1
        assert len(allhub.followers()) > 1
