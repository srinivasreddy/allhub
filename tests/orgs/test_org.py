from tests.utils import allhub


class TestOrg:
    def test_orgs(self):
        response = allhub.organizations()
        assert len(response) == 1

    def test_user_org(self):
        response = allhub.get_organization("test-github43")
        response.login == "test-github43"

    def test_user_orgs(self):
        response = allhub.user_organizations("srinivasreddy")
        assert len(response) == 1

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
        num_pages = 4
        for index, resp in enumerate(
            allhub.iterator(allhub.all_organizations, num_pages=num_pages), start=1
        ):
            pass
        assert num_pages == index
