from tests.utils import allhub


class TestOrg:
    def test_orgs(self):
        response = allhub.organizations()
        assert response == []

    def test_user_orgs(self):
        response = allhub.user_organizations("serhiy-storchaka")
        assert response[0].login == "python"

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
        counter = 10
        for resp in allhub.iterator(allhub.all_organizations):
            print(allhub.page)
            if counter == allhub.page:
                break
        else:
            assert False, "There are no 10 page ogs"
