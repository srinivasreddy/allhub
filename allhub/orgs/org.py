from allhub.response import Response
from enum import Enum


class Permission(Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    NONE = None


class OrgMixin:
    def organizations(self):
        """List your organizations"""
        url = "/user/orgs"
        self.response = Response(self.get(url), "Organizations")
        return self.response.transform()

    def all_organizations(self, since=None):
        """List all organizations"""
        url = "/organizations"
        self.response = Response(self.get(url), "Organizations")
        return self.response.transform()

    def user_organizations(self, username):
        """
        This method only lists public memberships, regardless of authentication.
        If you need to fetch all of the organization memberships (public and private)
        for the authenticated user, use the `def organizations()` API instead.
        """
        url = f"/users/{username}/orgs"
        self.response = Response(self.get(url), "Organizations")
        return self.response.transform()

    def get_organization(self, org):
        url = f"/orgs/{org}"
        self.response = Response(
            self.get(url, **{"Accept": "application/vnd.github.surtur-preview+json"}),
            "Organization",
        )
        return self.response.transform()

    def edit_organization(
        self,
        org,
        billing_email=None,
        company=None,
        email=None,
        location=None,
        name=None,
        description=None,
        has_organization_projects=None,
        default_repository_permission=None,
        members_can_create_repositories=None,
        members_allowed_repository_creation_type=None,
    ):
        url = f"/orgs/{org}"
        params = {}
        if billing_email:
            params["billing_email"] = billing_email
        if company:
            params["company"] = company
        if email:
            params["email"] = email
        if location:
            params["location"] = location
        if name:
            params["name"] = name
        if description:
            params["description"] = description
        if has_organization_projects:
            params["has_organization_projects"] = has_organization_projects
        if default_repository_permission:
            params["default_repository_permission"] = default_repository_permission
        if members_can_create_repositories:
            params["members_can_create_repositories"] = members_can_create_repositories
        if members_allowed_repository_creation_type:
            params[
                "members_allowed_repository_creation_type"
            ] = members_allowed_repository_creation_type

        self.response = Response(
            self.patch(
                url,
                params=params,
                **{"Accept": "application/vnd.github.surtur-preview+json"},
            ),
            "Organization",
        )
        return self.response.transform()
