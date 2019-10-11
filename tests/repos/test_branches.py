from allhub.tests.utils import allhub
import pytest


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

    def test_update_protected_branch(self):
        # NOTE: Protected branch feature is not available for Free plan.
        # Use pro plan or Github Enterprise.
        response = allhub.update_branch_protection(
            "test-github42", "allhub", "master", None, None, None, None
        )
        assert response is not None

    @pytest.mark.skip("Run  with pro plans")
    def test_delete_branch_protection(self):
        pass

    def test_required_checks_of_protected_branch(self):
        # NOTE: Protected branch feature is not available for Free plan.
        # Use pro plan or Github Enterprise.
        response = allhub.required_status_checks_of_protected_branch(
            "python", "cpython", "2.7"
        )
        assert response is not None
