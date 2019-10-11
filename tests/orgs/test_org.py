from tests.utils import allhub


class TestOrg:
    def test_orgs(self):
        response = allhub.organizations()
        assert response == []

    def test_all_orgs(self):
        response = allhub.all_organizations()
        assert set(
            [
                "login",
                "id",
                "node_id",
                "url",
                "repos_url",
                "events_url",
                "hooks_url",
                "issues_url",
                "members_url",
                "public_members_url",
                "avatar_url",
                "description",
            ]
        ) == set(response[0].keys())
