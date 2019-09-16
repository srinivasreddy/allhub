from allhub.response import Response

from enum import Enum


class Visibility(Enum):
    ALL = "all"
    PUBLIC = "public"
    PRIVATE = "private"


class Sort(Enum):
    CREATED = "created"
    UPDATED = "updated"
    PUSHED = "pushed"
    FULLNAME = "full_name"


class Type(Enum):
    ALL = "all"
    OWNER = "owner"
    PUBLIC = "public"
    PRIVATE = "private"
    MEMBER = "member"


class Affiliation(Enum):
    OWNER = "owner"
    COLLABORATOR = "collaborator"
    ORGANIZATION_MEMBER = "organization_member"


class Direction(Enum):
    ASC = "asc"
    DESC = "desc"


_affiliation = f"{Affiliation.OWNER.value},{Affiliation.COLLABORATOR.value},{Affiliation.ORGANIZATION_MEMBER.value}"


class ReposMixin:
    def repos(self, **kwargs):
        """
        Lists repositories that the authenticated user has explicit permission
        (:read, :write, or :admin) to access.

        The authenticated user has explicit permission to access repositories they own,
        repositories where they are a collaborator, and repositories that they can access
        through an organization membership.
        """
        params = []
        if "visibility" in kwargs:
            visibility = kwargs.pop("visibility")
            if not isinstance(visibility, Visibility):
                raise ValueError(f"'{visibility}' should be instance Visibility")
            if visibility not in Visibility:
                raise ValueError(
                    f"'{visibility}' should either be 'ALL','PUBLIC', or 'PRIVATE'"
                )
            params.append(("visibility", visibility.value))
        if "affiliation" in kwargs:
            affiliation = kwargs.pop("affiliation")
            for aff in affiliation.split(","):
                if aff not in ("owner", "collaborator", "organization_member"):
                    raise ValueError(
                        f"'{aff}' should either be 'owner', 'collaborator', or 'organization_member'"
                    )
            params.append(("affiliation", affiliation))
        if "type" in kwargs and ("visibility" in kwargs or "affiliation" in kwargs):
            raise AttributeError(
                "If you specify visibility or affiliation, you cannot specify type."
            )
        if "type" in kwargs:
            type = kwargs.pop("type")
            if not isinstance(type, Type):
                raise ValueError(f"'{type}' should be instance of Type")
            if type not in Type:
                raise ValueError(
                    f"'{type}' should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'"
                )
            params.append(("type", type.value))
        if "sort" in kwargs:
            sort = kwargs.pop("sort")
            if not isinstance(sort, Sort):
                raise ValueError(f"{sort} should be instance of Sort")
            if sort not in Sort:
                raise ValueError(
                    f"'{sort}' should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'"
                )
            params.append(("sort", sort.value))
        if "direction" in kwargs:
            direction = kwargs.pop("direction")
            if not isinstance(direction, Direction):
                raise ValueError(f"'{direction}' is not an instance of Direction")
            if direction not in Direction:
                raise ValueError(f"'{direction}' should either be 'ASC', or 'DESC'")
            params.append(("direction", direction.value))
        url = "/user/repos"
        self.response = Response(self.get_basic(url, params=params), "Repos")
        return self.response.transform()

    def user_repos(self, username, **kwargs):
        params = []
        if "type" in kwargs:
            type = kwargs.pop("type")
            if not isinstance(type, Type):
                raise ValueError(f"'{type}' should be instance of Type")
            if type not in Type:
                raise ValueError(
                    f"'{type}' should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'"
                )
            params.append(("type", type.value))
        if "sort" in kwargs:
            sort = kwargs.pop("sort")
            if not isinstance(sort, Sort):
                raise ValueError(f"{sort} should be instance of Sort")
            if sort not in Sort:
                raise ValueError(
                    f"'{sort}' should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'"
                )
            params.append(("sort", sort.value))
        if "direction" in kwargs:
            direction = kwargs.pop("direction")
            if not isinstance(direction, Direction):
                raise ValueError(f"'{direction}' is not an instance of Direction")
            if direction not in Direction:
                raise ValueError(f"'{direction}' should either be 'ASC', or 'DESC'")
            params.append(("direction", direction.value))
        url = f"/users/{username}/repos"
        self.response = Response(self.get_basic(url, params=params), "Repos")
        return self.response.transform()

    def org_repos(self, org, **kwargs):
        params = []
        if "type" in kwargs:
            type = kwargs.pop("type")
            if not isinstance(type, Type):
                raise ValueError(f"'{type}' should be instance of Type")
            if type not in Type:
                raise ValueError(
                    f"'{type}' should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'"
                )
            params.append(("type", type.value))
        if "sort" in kwargs:
            sort = kwargs.pop("sort")
            if not isinstance(sort, Sort):
                raise ValueError(f"{sort} should be instance of Sort")
            if sort not in Sort:
                raise ValueError(
                    f"'{sort}' should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'"
                )
            params.append(("sort", sort.value))
        if "direction" in kwargs:
            direction = kwargs.pop("direction")
            if not isinstance(direction, Direction):
                raise ValueError(f"'{direction}' is not an instance of Direction")
            if direction not in Direction:
                raise ValueError(f"'{direction}' should either be 'ASC', or 'DESC'")
            params.append(("direction", direction.value))
        url = f"/users/{org}/repos"
        self.response = Response(self.get_basic(url, params=params), "Repos")
        return self.response.transform()

    def all_repos(self, **kwargs):
        url = "/repositories"
        params = []
        if "since" in kwargs:
            since = kwargs.pop("since")
            params.append(("since", since))
        self.response = Response(self.get_basic(url, params=params), "Repos")
        return self.response.transform()