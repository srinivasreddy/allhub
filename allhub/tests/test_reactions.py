from .utils import allhub
from allhub.reactions import ReactionType


class TestReactions:
    def test_reactions_for_issue(self):
        reactions = allhub.reactions_for_issue(
            "rust-lang", "rust", 65196, ReactionType.NONE
        )
        assert reactions[0].content == "+1"
