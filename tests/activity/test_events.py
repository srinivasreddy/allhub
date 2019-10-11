import os
from tests.utils import allhub


class TestEvents:
    @staticmethod
    def helper(events, class_name):
        assert len(events) > 0
        assert events[0].__class__.__name__ == class_name
        assert events[0].created_at is not None
        assert events[0]["created_at"] is not None

    def test_public_events(self):
        events = allhub.public_events()
        TestEvents.helper(events, "PublicEvent")

    def test_repo_events(self):
        events = allhub.repo_events("python", "cpython")
        TestEvents.helper(events, "RepoEvent")

    def test_issue_events(self):
        events = allhub.issue_events("python", "cpython")
        TestEvents.helper(events, "IssueEvent")

    def test_public_events_network_repos(self):
        events = allhub.public_events_network_repos("python", "cpython")
        TestEvents.helper(events, "NetworkRepoPublicEvent")

    def test_public_events_orgs(self):
        events = allhub.public_events_orgs("python")
        TestEvents.helper(events, "OrgPublicEvent")

    def test_user_received_events(self):
        events = allhub.user_received_events(os.environ.get("USERNAME"))
        # TODO: Need to do something to receive the user to receive events.
        assert len(events) == 0

    def test_user_received_public_events(self):
        events = allhub.user_received_public_events(os.environ.get("USERNAME"))
        # TODO: Need to do something to receive the user to receive events.
        assert len(events) == 0

    def test_events_by_user(self):
        events = allhub.events_by_user(os.environ.get("USERNAME"))
        TestEvents.helper(events, "UserEvent")

    def test_public_events_by_user(self):
        events = allhub.public_events_by_user(os.environ.get("USERNAME"))
        # TODO: Need to do something to receive the user to receive events.
        assert len(events) == 0

    def test_events_for_org(self):
        events = allhub.events_for_org(os.environ.get("USERNAME"), "python")
        TestEvents.helper(events, "UserReceivedEvent")
