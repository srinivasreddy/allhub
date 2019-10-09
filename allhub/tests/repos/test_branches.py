from allhub.tests.utils import allhub


class TestBranches:
    def test_branches(self):
        response = allhub.branches("python", "cpython")
        two_seven_branch = [
            resp for resp in response if resp.name in ("2.7", "3.5", "3.6", "master")
        ]
        assert len(two_seven_branch) == 4

    def test_branch(self):
        response = allhub.branch("python", "cpython", "2.7")
        assert response.name == "2.7"
        assert response.protected

    def test_protected_branch(self):
        # NOTE: Protected branch feature is not available for Free plan.
        # Use pro plan or Github Enterprise.
        response = allhub.protected_branch("test-github42", "allhub", "master")
        assert response.message == "Branch not protected"
