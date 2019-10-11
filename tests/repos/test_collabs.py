from tests.utils import allhub
from allhub.repos import CollabPermission


class TestCollaborator:
    def test_repo_collaborators(self):
        response = allhub.repo_collaborators("test-github42", "cpython")
        assert len(response) == 1
        assert response[0].login == "test-github42"

    def test_is_collaborator(self):
        assert allhub.is_collaborator("test-github42", "cpython", "test-github42")
        assert (
            allhub.is_collaborator("test-github42", "cpython", "test-github41") is False
        )

    def test_user_permission(self):
        response = allhub.user_permission("test-github42", "cpython", "test-github42")
        assert response.permission == "admin"
        assert response.user.login == "test-github42"

    def test_add_user_as_collaborator(self):
        response = allhub.add_user_as_collaborator(
            "test-github42", "cpython", "srinivasreddy"
        )
        assert response.permissions == "write"
        response = allhub.add_user_as_collaborator(
            "test-github42",
            "cpython",
            "srinivasreddy42",
            permission=CollabPermission.ADMIN,
        )
        assert response.permissions == "write"

    def test_remove_user_as_collaborator(self):
        assert allhub.remove_user_as_collaborator(
            "test-github42", "cpython", "srinivasreddy"
        )

        assert allhub.remove_user_as_collaborator(
            "test-github42", "cpython", "srinivasreddy42"
        )
